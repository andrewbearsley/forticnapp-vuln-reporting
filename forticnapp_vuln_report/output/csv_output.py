"""CSV report renderer."""

import csv
import io
from typing import List

from ..models import ScoredVuln

CSV_HEADERS = [
    "Priority", "CVE", "Severity", "CVSS", "Package", "Namespace",
    "Version Installed", "Fixed Version",
    "Hostname", "Instance ID",
    "Exploit Public", "Exploit Wormified", "VM Provider", "Collector Type",
    "CVE Link",
]


def render_csv(vulns: List[ScoredVuln]) -> str:
    """Render flat CSV, one row per (CVE, package, host), sorted by priority."""
    sorted_vulns = sorted(vulns, key=lambda v: v.priority_score, reverse=True)

    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(CSV_HEADERS)

    for v in sorted_vulns:
        writer.writerow([
            v.priority_score,
            v.vuln_id,
            v.severity,
            v.cvss_score,
            v.pkg_name,
            v.pkg_namespace,
            v.pkg_version_installed,
            v.fixed_version,
            v.hostname,
            v.instance_id,
            "Yes" if v.exploit_public else "No",
            "Yes" if v.exploit_wormified else "No",
            v.vm_provider,
            v.collector_type,
            v.cve_link,
        ])

    return buf.getvalue()
