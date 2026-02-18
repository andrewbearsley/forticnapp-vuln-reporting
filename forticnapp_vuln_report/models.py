"""Data models for vulnerability report entries."""

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ScoredVuln:
    """A single scored vulnerability entry (one CVE on one package on one host)."""
    vuln_id: str
    severity: str
    status: str
    cvss_score: float
    description: str
    cve_link: str

    # Package info
    pkg_name: str
    pkg_namespace: str
    pkg_version_installed: str
    pkg_path: str

    # Fix info
    fix_available: bool
    fixed_version: str

    # Host info
    machine_id: str
    hostname: str
    instance_id: str
    vm_provider: str
    state: str
    collector_type: str  # Agent, Agentless

    # Risk info
    host_risk_score: float
    cve_risk_score: float
    exploit_public: bool
    exploit_wormified: bool

    # Timing
    first_seen: str = ""  # earliest startTime across deduped entries (ISO date)

    # Computed
    priority_score: float = 0.0
    eval_guid: str = ""


@dataclass
class PackageGroup:
    """A unique vulnerable package across hosts."""
    pkg_name: str
    pkg_namespace: str
    fixed_version: str
    cve_ids: List[str] = field(default_factory=list)
    severities: List[str] = field(default_factory=list)
    max_cvss: float = 0.0
    hosts: List[Dict[str, Any]] = field(default_factory=list)
    aggregate_score: float = 0.0
    exploit_count: int = 0


@dataclass
class HostGroup:
    """A host with its vulnerable packages."""
    machine_id: str
    hostname: str
    instance_id: str
    vm_provider: str
    collector_type: str
    host_risk_score: float
    vulns: List[ScoredVuln] = field(default_factory=list)
    unique_cves: int = 0
    unique_packages: int = 0
    max_priority: float = 0.0
