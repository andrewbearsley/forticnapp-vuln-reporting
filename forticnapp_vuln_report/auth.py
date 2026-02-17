"""Authentication and Lacework CLI configuration."""

import json
import os
import shutil
import subprocess
import sys
from typing import Dict

from .config import OutputFormat
from .logger import Logger

try:
    import openpyxl  # noqa: F401
    HAS_OPENPYXL = True
except ImportError:
    HAS_OPENPYXL = False


def check_required_tools(output_format: OutputFormat) -> None:
    """Verify required external tools are available."""
    if not shutil.which("lacework"):
        Logger.error("lacework CLI is not installed. Please install it first.")
        Logger.error("See: https://docs.fortinet.com/document/forticnapp/latest/cli-reference")
        sys.exit(1)

    if output_format == OutputFormat.EXCEL and not HAS_OPENPYXL:
        Logger.error("openpyxl is required for Excel output. Install: pip3 install openpyxl")
        sys.exit(1)


def load_api_key(api_key_path: str) -> Dict:
    """Load and validate API key from JSON file."""
    if not os.path.exists(api_key_path):
        Logger.error(f"API key file not found: {api_key_path}")
        sys.exit(1)

    with open(api_key_path, "r") as f:
        api_key = json.load(f)

    required_fields = ["keyId", "secret", "account"]
    missing = [fld for fld in required_fields if not api_key.get(fld)]
    if missing:
        Logger.error(f"Invalid API key file. Missing fields: {', '.join(missing)}")
        sys.exit(1)

    return api_key


def configure_lacework(api_key: Dict) -> Dict[str, str]:
    """Configure Lacework CLI environment variables and test connection."""
    Logger.verbose(f"Configuring Lacework CLI for account: {api_key['account']}")

    env = os.environ.copy()
    env["LW_ACCOUNT"] = api_key["account"]
    env["LW_API_KEY"] = api_key["keyId"]
    env["LW_API_SECRET"] = api_key["secret"]

    if api_key.get("subAccount"):
        env["LW_SUBACCOUNT"] = api_key["subAccount"]
        Logger.verbose(f"Using sub-account: {api_key['subAccount']}")

    Logger.verbose("Testing Lacework CLI connection...")
    result = subprocess.run(
        ["lacework", "configure", "list"],
        capture_output=True,
        text=True,
        env=env,
    )

    if result.returncode != 0:
        Logger.error("Failed to configure Lacework CLI. Check your API key.")
        Logger.verbose(f"Output: {result.stdout + result.stderr}")
        sys.exit(1)

    Logger.info(f"Connected to account: {api_key['account']}")
    return env
