"""Configuration, constants, and enums."""

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict


class Severity(Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    INFO = "Info"


class OutputFormat(Enum):
    MARKDOWN = "markdown"
    JSON = "json"
    CSV = "csv"
    EXCEL = "excel"


class ReportView(Enum):
    PACKAGE = "package"
    HOST = "host"
    BOTH = "both"


@dataclass
class Config:
    # Rate limiting
    MAX_RETRIES: int = 5
    BACKOFF_INCREMENT: int = 30

    # Request delays
    REQUEST_DELAY: float = 0.5

    # Directories
    OUTPUT_DIR: str = "output"

    # API constraints
    MAX_TIME_RANGE_DAYS: int = 7
    PAGE_SIZE: int = 5000

    # Priority scoring weights
    SCORE_EXPLOIT_PUBLIC: float = 2.0
    SCORE_EXPLOIT_WORMIFIED: float = 1.0

    # CVSS defaults by severity (when NVD score unavailable)
    CVSS_DEFAULTS: Dict[str, float] = field(default_factory=lambda: {
        "Critical": 9.5,
        "High": 7.5,
        "Medium": 5.0,
        "Low": 2.5,
        "Info": 0.0,
    })

    # Excel formatting
    EXCEL_HEADER_COLOR: str = "366092"
    EXCEL_HEADER_TEXT_COLOR: str = "FFFFFF"
    EXCEL_LINK_COLOR: str = "0000FF"
    EXCEL_MAX_COLUMN_WIDTH: int = 50


CONFIG = Config()

RATE_LIMIT_PATTERNS = [
    r"HTTP.*429",
    r"status.*429",
    r"429.*Too Many",
    r"rate limit exceeded",
    r"rate\.limit\.exceeded",
    r"too many requests",
]

SEVERITY_ORDER = {"Critical": 1, "High": 2, "Medium": 3, "Low": 4, "Info": 5}
