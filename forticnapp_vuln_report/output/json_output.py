"""JSON report renderer."""

import datetime
import json
from typing import List, Optional

from ..config import ReportView, SEVERITY_ORDER
from ..models import HostGroup, PackageGroup, ScoredVuln


def render_json(
    vulns: List[ScoredVuln],
    pkg_groups: List[PackageGroup],
    host_groups: List[HostGroup],
    view: ReportView,
    limit: Optional[int],
    min_severity: str,
) -> str:
    """Render report as JSON string."""
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()

    total_cves = len(set(v.vuln_id for v in vulns))
    total_packages = len(set((v.pkg_name, v.pkg_namespace) for v in vulns))
    total_hosts = len(set(v.machine_id for v in vulns))

    output = {
        "metadata": {
            "generated": now,
            "min_severity": min_severity,
            "fixable_only": True,
            "total_entries": len(vulns),
        },
        "summary": {
            "unique_cves": total_cves,
            "vulnerable_packages": total_packages,
            "affected_hosts": total_hosts,
            "critical_count": sum(1 for v in vulns if v.severity == "Critical"),
            "high_count": sum(1 for v in vulns if v.severity == "High"),
        },
    }

    if view in (ReportView.PACKAGE, ReportView.BOTH):
        display_pkgs = pkg_groups[:limit] if limit else pkg_groups
        output["by_package"] = [
            {
                "package": g.pkg_name,
                "namespace": g.pkg_namespace,
                "fixed_version": g.fixed_version,
                "cve_ids": sorted(g.cve_ids),
                "severities": sorted(g.severities, key=lambda s: SEVERITY_ORDER.get(s, 99)),
                "max_cvss": g.max_cvss,
                "host_count": len(g.hosts),
                "aggregate_score": g.aggregate_score,
                "hosts": g.hosts,
            }
            for g in display_pkgs
        ]

    if view in (ReportView.HOST, ReportView.BOTH):
        display_hosts = host_groups[:limit] if limit else host_groups
        output["by_host"] = [
            {
                "hostname": h.hostname,
                "instance_id": h.instance_id,
                "machine_id": h.machine_id,
                "vm_provider": h.vm_provider,
                "collector_type": h.collector_type,
                "host_risk_score": h.host_risk_score,
                "unique_cves": h.unique_cves,
                "unique_packages": h.unique_packages,
                "max_priority": h.max_priority,
                "top_vulns": [
                    {
                        "vuln_id": v.vuln_id,
                        "severity": v.severity,
                        "cvss": v.cvss_score,
                        "package": v.pkg_name,
                        "version_installed": v.pkg_version_installed,
                        "fixed_version": v.fixed_version,
                        "priority_score": v.priority_score,
                    }
                    for v in h.vulns[:20]
                ],
            }
            for h in display_hosts
        ]

    return json.dumps(output, indent=2)
