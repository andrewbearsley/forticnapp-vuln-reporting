"""Vulnerability scoring, extraction, and deduplication."""

from typing import Dict, List

from .config import CONFIG
from .logger import Logger
from .models import ScoredVuln


def _resolve_machine_id(machine_tags: Dict) -> str:
    """Resolve a unique machine identifier, falling back through available fields.

    Agentless scans have empty mid/MachineId — use InstanceId or Hostname.
    """
    for field in ("mid", "MachineId", "InstanceId", "Hostname"):
        val = machine_tags.get(field, "")
        if val:
            return val
    return "unknown"


def deduplicate(entries: List[Dict]) -> List[Dict]:
    """Deduplicate entries keeping latest per (vulnId, pkg_name, pkg_ns, version, machine)."""
    seen: Dict[str, Dict] = {}

    for entry in entries:
        vuln_id = entry.get("vulnId", "")
        fk = entry.get("featureKey", {})
        mt = entry.get("machineTags", {})

        key = (
            vuln_id,
            fk.get("name", ""),
            fk.get("namespace", ""),
            fk.get("version_installed", ""),
            _resolve_machine_id(mt),
        )

        existing = seen.get(key)
        if existing is None:
            seen[key] = entry
        else:
            new_time = entry.get("startTime", "")
            old_time = existing.get("startTime", "")
            if new_time > old_time:
                seen[key] = entry

    deduped = list(seen.values())
    Logger.info(f"After deduplication: {len(deduped)} unique entries (from {len(entries)})")
    return deduped


def extract_scored_vuln(entry: Dict) -> ScoredVuln:
    """Extract a ScoredVuln from a raw API entry."""
    fk = entry.get("featureKey", {})
    fi = entry.get("fixInfo", {})
    mt = entry.get("machineTags", {})
    cp = entry.get("cveProps", {})
    ri = entry.get("riskInfo", {})
    ec = entry.get("evalCtx", {})

    # CVSS score: try NVD first, then cveRiskScore, then severity default
    cvss = 0.0
    try:
        cvss = float(cp.get("metadata", {}).get("NVD", {}).get("CVSSv3", {}).get("Score", 0))
    except (TypeError, ValueError):
        pass
    if cvss == 0.0:
        try:
            cvss = float(entry.get("cveRiskScore", 0))
        except (TypeError, ValueError):
            pass
    if cvss == 0.0:
        severity = entry.get("severity", "Medium")
        cvss = CONFIG.CVSS_DEFAULTS.get(severity, 5.0)

    # Exploit info
    exploit_breakdown = ri.get("host_risk_factors_breakdown", {}).get("exploit_summary", {})
    exploit_public = str(exploit_breakdown.get("exploit_public", "")).lower() == "yes"
    exploit_wormified = str(exploit_breakdown.get("exploit_wormified", "")).lower() == "yes"

    sv = ScoredVuln(
        vuln_id=entry.get("vulnId", ""),
        severity=entry.get("severity", ""),
        status=entry.get("status", ""),
        cvss_score=cvss,
        description=cp.get("description", ""),
        cve_link=cp.get("link", ""),
        pkg_name=fk.get("name", ""),
        pkg_namespace=fk.get("namespace", ""),
        pkg_version_installed=fk.get("version_installed", ""),
        pkg_path=fk.get("package_path", ""),
        fix_available=str(fi.get("fix_available", "0")) == "1",
        fixed_version=fi.get("fixed_version", ""),
        machine_id=_resolve_machine_id(mt),
        hostname=mt.get("Hostname", mt.get("Name", "")),
        instance_id=mt.get("InstanceId", ""),
        vm_provider=mt.get("VmProvider", ""),
        state=mt.get("State", ""),
        collector_type=ec.get("collector_type", ""),
        host_risk_score=float(entry.get("hostRiskScore", 0) or 0),
        cve_risk_score=float(entry.get("cveRiskScore", 0) or 0),
        exploit_public=exploit_public,
        exploit_wormified=exploit_wormified,
        eval_guid=ec.get("eval_guid", ""),
    )
    sv.priority_score = compute_priority_score(sv)
    return sv


def compute_priority_score(v: ScoredVuln) -> float:
    """Compute priority score for a single vulnerability entry.

    Score = base CVSS + exploit bonuses.
    Range: 0-13 (CVSS 0-10 + public exploit +2 + wormified +1).
    """
    score = v.cvss_score

    if v.exploit_public:
        score += CONFIG.SCORE_EXPLOIT_PUBLIC
    if v.exploit_wormified:
        score += CONFIG.SCORE_EXPLOIT_WORMIFIED

    return round(score, 2)
