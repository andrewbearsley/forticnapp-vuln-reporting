"""Markdown report renderer."""

import datetime
from typing import List, Optional

from ..config import ReportView, SEVERITY_ORDER
from ..models import HostGroup, PackageGroup, ScoredVuln


def render_markdown(
    vulns: List[ScoredVuln],
    pkg_groups: List[PackageGroup],
    host_groups: List[HostGroup],
    view: ReportView,
    limit: Optional[int],
    min_severity: str,
) -> str:
    """Render report as markdown text."""
    lines: List[str] = []
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    lines.append("# FortiCNAPP Host Vulnerability Report")
    lines.append("")
    lines.append(f"**Generated:** {now}")
    lines.append(f"**Minimum severity:** {min_severity}")
    lines.append("**Fixable only:** Yes")
    lines.append("")

    total_cves = len(set(v.vuln_id for v in vulns))
    total_packages = len(set((v.pkg_name, v.pkg_namespace) for v in vulns))
    total_hosts = len(set(v.machine_id for v in vulns))
    critical_count = sum(1 for v in vulns if v.severity == "Critical")
    high_count = sum(1 for v in vulns if v.severity == "High")

    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| Unique CVEs | {total_cves} |")
    lines.append(f"| Vulnerable packages | {total_packages} |")
    lines.append(f"| Affected hosts | {total_hosts} |")
    lines.append(f"| Critical findings | {critical_count} |")
    lines.append(f"| High findings | {high_count} |")
    lines.append("")

    if total_cves == 0:
        lines.append("No fixable vulnerabilities found matching the criteria.")
        return "\n".join(lines)

    if view in (ReportView.PACKAGE, ReportView.BOTH):
        _render_package_view(lines, pkg_groups, limit)

    if view in (ReportView.HOST, ReportView.BOTH):
        _render_host_view(lines, host_groups, limit)

    return "\n".join(lines)


def _render_package_view(
    lines: List[str],
    pkg_groups: List[PackageGroup],
    limit: Optional[int],
) -> None:
    """Render the package-focused view."""
    display = pkg_groups[:limit] if limit else pkg_groups
    count_str = str(len(display))
    if limit and limit < len(pkg_groups):
        count_str += f" of {len(pkg_groups)}"

    lines.append(f"## Top Packages to Remediate ({count_str})")
    lines.append("")
    lines.append("| # | Package | Namespace | Fix Version | CVEs | Hosts | Score |")
    lines.append("|---|---------|-----------|-------------|------|-------|-------|")

    for i, g in enumerate(display, 1):
        cve_str = ", ".join(sorted(g.cve_ids)[:3])
        if len(g.cve_ids) > 3:
            cve_str += f" (+{len(g.cve_ids) - 3})"
        lines.append(
            f"| {i} | {g.pkg_name} | {g.pkg_namespace} | {g.fixed_version} "
            f"| {cve_str} | {len(g.hosts)} | {g.aggregate_score} |"
        )

    lines.append("")

    # Per-package detail
    for i, g in enumerate(display, 1):
        sev_str = ", ".join(sorted(g.severities, key=lambda s: SEVERITY_ORDER.get(s, 99)))
        lines.append(f"### {i}. {g.pkg_name} ({g.pkg_namespace})")
        lines.append("")
        lines.append(f"- **Fix version:** {g.fixed_version}")
        lines.append(f"- **Severities:** {sev_str}")
        lines.append(f"- **Max CVSS:** {g.max_cvss}")
        lines.append(f"- **CVEs:** {', '.join(sorted(g.cve_ids))}")
        lines.append(f"- **Affected hosts:** {len(g.hosts)}")
        lines.append("")

        lines.append("| Hostname | Instance | Version | Score |")
        lines.append("|----------|----------|---------|-------|")
        for h in sorted(g.hosts, key=lambda x: x["priority_score"], reverse=True):
            lines.append(
                f"| {h['hostname']} | {h['instance_id']} "
                f"| {h['version_installed']} | {h['priority_score']} |"
            )
        lines.append("")


def _render_host_view(
    lines: List[str],
    host_groups: List[HostGroup],
    limit: Optional[int],
) -> None:
    """Render the host-focused view."""
    display = host_groups[:limit] if limit else host_groups
    count_str = str(len(display))
    if limit and limit < len(host_groups):
        count_str += f" of {len(host_groups)}"

    lines.append(f"## Hosts by Risk ({count_str})")
    lines.append("")
    lines.append("| # | Hostname | Instance | CVEs | Packages | Risk Score | Max Priority |")
    lines.append("|---|----------|----------|------|----------|------------|--------------|")

    for i, h in enumerate(display, 1):
        lines.append(
            f"| {i} | {h.hostname} | {h.instance_id} "
            f"| {h.unique_cves} | {h.unique_packages} "
            f"| {h.host_risk_score} | {h.max_priority} |"
        )

    lines.append("")
