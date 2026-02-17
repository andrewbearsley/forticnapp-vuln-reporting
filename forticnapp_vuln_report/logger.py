"""Logging and terminal output utilities."""

import sys


class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[0;34m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    NC = "\033[0m"

    _enabled = True

    @classmethod
    def disable(cls):
        cls.RED = cls.GREEN = cls.YELLOW = cls.BLUE = ""
        cls.BOLD = cls.DIM = cls.NC = ""
        cls._enabled = False


class Logger:
    _verbose = False

    @classmethod
    def set_verbose(cls, enabled: bool):
        cls._verbose = enabled

    @staticmethod
    def info(msg: str) -> None:
        print(f"{Colors.GREEN}[INFO]{Colors.NC} {msg}", file=sys.stderr)

    @staticmethod
    def warning(msg: str) -> None:
        print(f"{Colors.YELLOW}[WARNING]{Colors.NC} {msg}", file=sys.stderr)

    @staticmethod
    def error(msg: str) -> None:
        print(f"{Colors.RED}[ERROR]{Colors.NC} {msg}", file=sys.stderr)

    @classmethod
    def verbose(cls, msg: str) -> None:
        if cls._verbose:
            print(f"{Colors.DIM}[VERBOSE]{Colors.NC} {msg}", file=sys.stderr)
