# FortiCNAPP vulnerability report generator

A CLI tool that queries the FortiCNAPP (Lacework) host vulnerability API and generates prioritised reports. It pulls fixable, active vulnerabilities, scores them by severity and exploit availability, then groups the results by package or host so you can see what to patch first.

## What it does

- Fetches host vulnerabilities from the FortiCNAPP API (last 7 days)
- Filters to fixable, active CVEs at Critical or High severity
- Deduplicates entries across overlapping scan results
- Scores each finding using CVSS + exploit risk factors
- Groups by package (what to update) or by host (what to patch)
- Outputs as Markdown, JSON, CSV, or Excel

## Prerequisites

- **Python 3.9+**
- **Lacework CLI** installed and on your PATH — see <a href="INSTALL-LACEWORK-CLI.md">installation guide</a>
- **FortiCNAPP API key** — see the <a href="INSTALL-LACEWORK-CLI.md#get-a-lacework-api-key">API key section</a> of the installation guide

### Optional

For Excel output, install openpyxl:

```bash
pip install -r requirements.txt
```

## Setup

1. Clone the repo:

```bash
git clone https://github.com/andrewbearsley/forticnapp-vuln-reporting.git
cd forticnapp-vuln-reporting
```

2. Copy the example credentials file and fill in your API key details:

```bash
cp api-key/lw-api-key.json.example api-key/mykey.json
```

Edit `api-key/mykey.json` with your account name, key ID, and secret. See the <a href="INSTALL-LACEWORK-CLI.md#get-a-lacework-api-key">installation guide</a> for how to generate these. The `subAccount` field is optional (only needed for org-level accounts).

JSON files in `api-key/` are gitignored — only the `.example` template is committed.

3. (Optional) Install Excel dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic (Critical severity, Markdown to stdout)

```bash
python3 -m forticnapp_vuln_report api-key/mykey.json
```

Or via the wrapper script:

```bash
python3 scripts/forticnapp_vuln_report.py api-key/mykey.json
```

### Include High severity

```bash
python3 -m forticnapp_vuln_report api-key/mykey.json -s high
```

### JSON output (pipe to jq for quick summary)

```bash
python3 -m forticnapp_vuln_report api-key/mykey.json -f json | jq .summary
```

### CSV to file

```bash
python3 -m forticnapp_vuln_report api-key/mykey.json -f csv -o output/vulns.csv
```

### Excel report

```bash
python3 -m forticnapp_vuln_report api-key/mykey.json -f excel -o output/vulns.xlsx
```

### Both package and host views, top 10

```bash
python3 -m forticnapp_vuln_report api-key/mykey.json --view both --limit 10
```

### Verbose logging

```bash
python3 -m forticnapp_vuln_report api-key/mykey.json -v
```

## CLI reference

```
python3 -m forticnapp_vuln_report <api-key-path> [options]
```

| Option | Description | Default |
|--------|-------------|---------|
| `-s, --severity {critical,high}` | Minimum severity to include | `critical` |
| `-f, --format {markdown,json,csv,excel}` | Output format | `markdown` |
| `-o, --output PATH` | Output file (stdout if omitted) | stdout |
| `--view {package,host,both}` | Report grouping | `package` |
| `--limit N` | Top N entries per view | all |
| `-v, --verbose` | Verbose logging to stderr | off |
| `--no-color` | Disable coloured terminal output | off |

## Output formats

**Markdown**: Summary stats, ranked package table, per-package host breakdown. Good for pasting into tickets or docs.

**JSON**: Structured data with `metadata`, `summary`, `by_package`, and `by_host` sections. Pipe into other tools or dashboards.

**CSV**: One row per (CVE, package, host), sorted by priority score. Opens directly in any spreadsheet app.

**Excel**: Four sheets (Summary, By Package, By Host, Detail) with styled headers, auto-column widths, auto-filters, and CVE hyperlinks.

## Priority scoring

Each vulnerability entry gets a score based on:

| Factor | Points |
|--------|--------|
| Base CVSS (from NVD CVSSv3, or cveRiskScore, or severity default) | 0–10 |
| Known public exploit | +2 |
| Wormified exploit | +1 |

**Score range:** 0–13.

For the package view, the aggregate score adds `log2(host_count)` to the maximum host score, so packages affecting many machines sort higher.

## Project structure

```
forticnapp-vuln-reporting/
├── forticnapp_vuln_report/        # Main package
│   ├── __init__.py
│   ├── __main__.py                # CLI entry point
│   ├── config.py                  # Configuration, enums, constants
│   ├── logger.py                  # Terminal output / logging
│   ├── auth.py                    # API key loading, CLI auth
│   ├── api.py                     # API calls, pagination, rate limiting
│   ├── models.py                  # Data classes (ScoredVuln, PackageGroup, HostGroup)
│   ├── scoring.py                 # CVSS scoring, deduplication
│   ├── grouping.py                # Package and host grouping
│   └── output/                    # Output renderers
│       ├── __init__.py
│       ├── markdown.py
│       ├── json_output.py
│       ├── csv_output.py
│       └── excel.py
├── scripts/
│   └── forticnapp_vuln_report.py  # Wrapper script
├── api-key/                       # API credentials (gitignored)
├── output/                        # Generated reports (gitignored)
├── requirements.txt               # openpyxl for Excel output
└── .gitignore
```

Each module handles one concern. You can swap out a renderer or change the scoring formula without touching the rest.

## API details

The tool uses the <a href="https://docs.fortinet.com/document/forticnapp/latest/api-reference" target="_blank">FortiCNAPP v2 API</a> endpoint:

```
POST /api/v2/Vulnerabilities/Hosts/search
```

Constraints:
- Maximum 7-day time window per request
- 5,000 entries per page (auto-paginated)
- Rate limited (429 responses handled with incremental backoff)

All API calls go through the Lacework CLI binary (`lacework api post/get`) with `--nocache` to avoid stale results.

## Extending

Some ideas if you want to build on this:

- **Container vulnerabilities**: the API has a matching `/api/v2/Vulnerabilities/Containers/search` endpoint with a similar response shape
- **Additional scoring factors**: the raw API returns `packageStatus` (ACTIVE/INACTIVE), `lw_InternetExposure` (Public/Private), and `package_active` fields that could feed into the priority score
- **Scheduled reports**: wrap the CLI call in a cron job or Lambda and ship output to S3/Slack
- **Trend tracking**: store JSON outputs over time and diff to see new/resolved vulnerabilities
