"""Grouping functions for packages and hosts."""

import math
from typing import Dict, List

from .models import HostGroup, PackageGroup, ScoredVuln


def group_by_package(vulns: List[ScoredVuln]) -> List[PackageGroup]:
    """Group vulns by (pkg_name, pkg_namespace, fixed_version).

    Aggregate score = max(host_priority) + log2(host_count), rewarding
    packages that affect many hosts.
    """
    groups: Dict[str, PackageGroup] = {}

    for v in vulns:
        key_str = f"{v.pkg_name}|{v.pkg_namespace}|{v.fixed_version}"

        if key_str not in groups:
            groups[key_str] = PackageGroup(
                pkg_name=v.pkg_name,
                pkg_namespace=v.pkg_namespace,
                fixed_version=v.fixed_version,
            )

        g = groups[key_str]

        if v.vuln_id not in g.cve_ids:
            g.cve_ids.append(v.vuln_id)
        if v.severity not in g.severities:
            g.severities.append(v.severity)
        if v.cvss_score > g.max_cvss:
            g.max_cvss = v.cvss_score

        # Track host (dedupe within group)
        host_entry = {
            "machine_id": v.machine_id,
            "hostname": v.hostname,
            "instance_id": v.instance_id,
            "priority_score": v.priority_score,
            "collector_type": v.collector_type,
            "version_installed": v.pkg_version_installed,
        }
        if not any(h["machine_id"] == v.machine_id for h in g.hosts):
            g.hosts.append(host_entry)

        if v.exploit_public or v.exploit_wormified:
            g.exploit_count = max(g.exploit_count, 1)

    # Compute aggregate scores
    for g in groups.values():
        max_host_priority = max((h["priority_score"] for h in g.hosts), default=0)
        host_count = len(g.hosts)
        g.aggregate_score = round(
            max_host_priority + (math.log2(host_count) if host_count > 1 else 0), 2
        )

    return sorted(groups.values(), key=lambda g: g.aggregate_score, reverse=True)


def group_by_host(vulns: List[ScoredVuln]) -> List[HostGroup]:
    """Group vulns by host, sorted by max priority descending."""
    groups: Dict[str, HostGroup] = {}

    for v in vulns:
        if v.machine_id not in groups:
            groups[v.machine_id] = HostGroup(
                machine_id=v.machine_id,
                hostname=v.hostname,
                instance_id=v.instance_id,
                vm_provider=v.vm_provider,
                collector_type=v.collector_type,
                host_risk_score=v.host_risk_score,
            )

        groups[v.machine_id].vulns.append(v)

    for g in groups.values():
        g.unique_cves = len(set(v.vuln_id for v in g.vulns))
        g.unique_packages = len(set((v.pkg_name, v.pkg_namespace) for v in g.vulns))
        g.max_priority = max((v.priority_score for v in g.vulns), default=0)
        g.vulns.sort(key=lambda v: v.priority_score, reverse=True)

    return sorted(groups.values(), key=lambda g: g.max_priority, reverse=True)
