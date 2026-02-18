"""CLI entry point for the FortiCNAPP vulnerability report generator.

Usage:
    python -m forticnapp_vuln_report <api-key-path> [options]
"""

import argparse
import json
import os
import sys

from .api import fetch_vulnerabilities
from .auth import check_required_tools, configure_lacework, load_api_key
from .config import CONFIG, OutputFormat, ReportView
from .grouping import group_by_host, group_by_package
from .logger import Colors, Logger
from .output.csv_output import render_csv
from .output.excel import write_excel
from .output.json_output import render_json
from .output.markdown import render_markdown
from .scoring import deduplicate, extract_scored_vuln


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="FortiCNAPP Host Vulnerability Report Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s api-key/mykey.json
  %(prog)s api-key/mykey.json -s high -f json | jq .summary
  %(prog)s api-key/mykey.json -f csv -o output/vulns.csv
  %(prog)s api-key/mykey.json -f excel -o output/vulns.xlsx
  %(prog)s api-key/mykey.json --view both --limit 20
        """,
    )

    parser.add_argument(
        "api_key_path",
        help="Path to API key JSON file (with account, keyId, secret)",
    )
    parser.add_argument(
        "-s", "--severity",
        choices=["critical", "high", "medium", "low", "info"],
        default="critical",
        help="Minimum severity to include (default: critical)",
    )
    parser.add_argument(
        "-d", "--days",
        type=int,
        default=1,
        choices=range(1, 8),
        metavar="1-7",
        help="Number of days to look back (default: 1, max: 7)",
    )
    parser.add_argument(
        "-f", "--format",
        choices=["markdown", "json", "csv", "excel"],
        default="markdown",
        help="Output format (default: markdown)",
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: stdout for markdown/json/csv)",
    )
    parser.add_argument(
        "--view",
        choices=["package", "host", "both"],
        default="package",
        help="Report view (default: package)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit to top N entries per view",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored output",
    )

    return parser.parse_args()


def _write_text_output(content: str, output_path: str | None) -> None:
    """Write text content to file or stdout."""
    if output_path:
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, "w") as f:
            f.write(content)
        Logger.info(f"Report written to {output_path}")
    else:
        print(content)


def main():
    args = parse_args()

    if args.no_color:
        Colors.disable()
    Logger.set_verbose(args.verbose)

    output_format = OutputFormat(args.format)
    view = ReportView(args.view)
    min_severity = args.severity.capitalize()

    check_required_tools(output_format)

    # Default output path for Excel
    output_path = args.output
    if output_format == OutputFormat.EXCEL and not output_path:
        os.makedirs(CONFIG.OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(CONFIG.OUTPUT_DIR, "forticnapp-vuln-report.xlsx")

    # Auth
    api_key = load_api_key(args.api_key_path)
    env = configure_lacework(api_key)

    # Fetch
    raw_entries = fetch_vulnerabilities(env, min_severity, args.days)
    if not raw_entries:
        Logger.warning("No vulnerabilities found matching criteria")
        if output_format == OutputFormat.JSON:
            print(json.dumps({"summary": {"total_entries": 0}, "by_package": [], "by_host": []}))
        elif output_format == OutputFormat.MARKDOWN:
            print(f"# FortiCNAPP Host Vulnerability Report\n\nNo fixable "
                  f"{min_severity.lower()}+ vulnerabilities found.")
        return

    # Deduplicate
    deduped = deduplicate(raw_entries)

    # Score
    Logger.info("Scoring and prioritising vulnerabilities...")
    vulns = [extract_scored_vuln(entry) for entry in deduped]
    Logger.info(f"Scored {len(vulns)} entries")

    # Group
    pkg_groups = group_by_package(vulns)
    host_groups = group_by_host(vulns)
    Logger.info(f"Grouped into {len(pkg_groups)} packages across {len(host_groups)} hosts")

    # Render
    if output_format == OutputFormat.MARKDOWN:
        result = render_markdown(vulns, pkg_groups, host_groups, view, args.limit, min_severity)
        _write_text_output(result, output_path)

    elif output_format == OutputFormat.JSON:
        result = render_json(vulns, pkg_groups, host_groups, view, args.limit, min_severity)
        _write_text_output(result, output_path)

    elif output_format == OutputFormat.CSV:
        result = render_csv(vulns)
        _write_text_output(result, output_path)

    elif output_format == OutputFormat.EXCEL:
        write_excel(vulns, pkg_groups, host_groups, output_path, min_severity)
        Logger.info(f"Excel report written to {output_path}")

    Logger.info("Done.")


if __name__ == "__main__":
    main()
