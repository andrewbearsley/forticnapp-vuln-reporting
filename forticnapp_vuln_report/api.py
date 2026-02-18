"""API call handling, rate limiting, and vulnerability fetching."""

import datetime
import json
import re
import subprocess
import time
from typing import Dict, List, Tuple

from .config import CONFIG, RATE_LIMIT_PATTERNS, SEVERITY_ORDER
from .logger import Logger


def make_api_call(
    cmd: List[str],
    env: Dict[str, str],
    retry_count: int = 0,
) -> Tuple[str, bool]:
    """Make API call via lacework CLI with rate limit handling.

    Returns (output, was_rate_limited). was_rate_limited is True when retries
    were exhausted due to rate limiting (output will be "").
    """
    while retry_count < CONFIG.MAX_RETRIES:
        Logger.verbose(f"Executing: {' '.join(cmd)}")

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, env=env)
            output = result.stdout + result.stderr

            if _check_rate_limit(output, result.returncode):
                _handle_rate_limit(retry_count, output)
                retry_count += 1
                continue

            if result.returncode != 0:
                if _is_valid_json(result.stdout):
                    return result.stdout, False
                # Non-zero exit with no valid JSON — likely a suppressed 429
                # or transient error. Retry with backoff.
                _handle_rate_limit(retry_count, output)
                retry_count += 1
                continue

            return result.stdout, False

        except Exception as e:
            Logger.warning(f"Error executing command: {e}")
            return "", False

    Logger.warning(f"Failed after {CONFIG.MAX_RETRIES} attempts")
    return "", True


def build_search_filters(
    min_severity: str, days: int = 1, tag_filters: Dict | None = None,
) -> Dict:
    """Build the search request body with filters."""
    now = datetime.datetime.now(datetime.timezone.utc)
    start = now - datetime.timedelta(days=days)

    # Include all severities at or above the minimum
    min_order = SEVERITY_ORDER.get(min_severity, 1)
    severity_values = [s for s, order in SEVERITY_ORDER.items() if order <= min_order]

    filters = [
        {"field": "severity", "expression": "in", "values": severity_values},
        {"field": "fixInfo.fix_available", "expression": "eq", "value": "1"},
        {"field": "status", "expression": "in", "values": ["Active", "New"]},
    ]

    # Machine tag filters (server-side)
    if tag_filters:
        for key, value in tag_filters.items():
            filters.append({
                "field": f"machineTags.{key}",
                "expression": "eq",
                "value": value,
            })

    return {
        "timeFilter": {
            "startTime": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "endTime": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        },
        "filters": filters,
        "returns": [
            "vulnId", "severity", "status", "fixInfo", "featureKey",
            "machineTags", "cveProps", "evalCtx", "startTime", "props",
            "riskInfo", "hostRiskScore", "cveRiskScore",
        ],
    }


def fetch_vulnerabilities(
    env: Dict[str, str], min_severity: str, days: int = 1,
    tag_filters: Dict | None = None,
) -> List[Dict]:
    """Fetch all vulnerability entries with pagination."""
    search_body = build_search_filters(min_severity, days, tag_filters)
    body_json = json.dumps(search_body)

    Logger.info(f"Fetching vulnerabilities (severity >= {min_severity}, fixable, active)...")
    Logger.verbose(f"Search body: {body_json}")

    all_entries = []
    page = 1

    # First page via POST
    cmd = [
        "lacework", "api", "post",
        "/api/v2/Vulnerabilities/Hosts/search",
        "-d", body_json,
        "--json", "--noninteractive", "--nocache",
    ]

    output, rate_limited = make_api_call(cmd, env)
    if rate_limited or not output:
        Logger.error("Failed to fetch vulnerabilities from API")
        return []

    try:
        data = json.loads(output)
    except json.JSONDecodeError:
        Logger.error("Failed to parse API response")
        Logger.verbose(f"Raw output: {output[:1000]}")
        return []

    entries = data.get("data", [])
    all_entries.extend(entries)
    Logger.info(f"Page {page}: {len(entries)} entries")

    # Paginate
    while data.get("paging", {}).get("urls", {}).get("nextPage"):
        next_url = data["paging"]["urls"]["nextPage"]
        page += 1

        time.sleep(CONFIG.REQUEST_DELAY)

        cmd = [
            "lacework", "api", "get", next_url,
            "--json", "--noninteractive", "--nocache",
        ]
        output, rate_limited = make_api_call(cmd, env)
        if rate_limited:
            Logger.warning(f"Pagination stopped at page {page} (rate limited)")
            break
        if not output:
            Logger.warning(f"Pagination stopped at page {page} (API error)")
            break

        try:
            data = json.loads(output)
        except json.JSONDecodeError:
            Logger.warning(f"Failed to parse page {page}")
            break

        entries = data.get("data", [])
        all_entries.extend(entries)
        Logger.info(f"Page {page}: {len(entries)} entries")

        if len(entries) < CONFIG.PAGE_SIZE:
            break

    Logger.info(f"Total raw entries fetched: {len(all_entries)}")
    return all_entries


def _check_rate_limit(output: str, exit_code: int) -> bool:
    """Check if output indicates rate limiting."""
    if exit_code == 0 and _is_valid_json(output):
        return False
    for pattern in RATE_LIMIT_PATTERNS:
        if re.search(pattern, output, re.IGNORECASE):
            return True
    return False


def _is_valid_json(text: str) -> bool:
    """Check if text is valid JSON."""
    try:
        json.loads(text)
        return True
    except (json.JSONDecodeError, ValueError):
        return False


def _handle_rate_limit(retry_count: int, output: str) -> None:
    """Handle rate limit with incremental backoff."""
    delay = CONFIG.BACKOFF_INCREMENT * (retry_count + 1)
    Logger.warning(
        f"Rate limited (429). Waiting {delay}s before retry "
        f"{retry_count + 1}/{CONFIG.MAX_RETRIES}..."
    )
    Logger.verbose(f"Response: {output[:500]}")
    time.sleep(delay)
