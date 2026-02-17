#!/usr/bin/env python3
"""Wrapper script — delegates to the forticnapp_vuln_report package.

Usage: python3 scripts/forticnapp_vuln_report.py <api-key-path> [options]

Equivalent to: python -m forticnapp_vuln_report <api-key-path> [options]
"""

import os
import sys

# Add project root to path so the package can be imported without installing
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from forticnapp_vuln_report.__main__ import main

if __name__ == "__main__":
    main()
