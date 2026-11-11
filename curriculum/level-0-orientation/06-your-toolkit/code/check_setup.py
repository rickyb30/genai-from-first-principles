"""Check that your computer is ready to run every example in this catalog.

It checks three things, without using the network:
  1. Python is version 3.11 or newer.
  2. NumPy is installed (used from Level 1 onwards).
  3. matplotlib is installed (used for plots and diagrams).
It also finds the catalog's shared/ folder, which later lessons import from.

Run:  python check_setup.py

Expected output:
    [ok] Python 3.11 or newer
    [ok] NumPy installed
    [ok] matplotlib installed
    [ok] catalog's shared/ folder found
    Everything is ready.
"""

import importlib.util
import sys
from pathlib import Path


def has_package(name: str) -> bool:
    """True if `name` can be imported. find_spec looks without actually importing it."""
    return importlib.util.find_spec(name) is not None


def find_repo_root() -> Path | None:
    """Walk up from this file until we find the folder that contains shared/."""
    for folder in Path(__file__).resolve().parents:
        if (folder / "shared").is_dir():
            return folder
    return None


def main() -> None:
    checks = {
        "Python 3.11 or newer": sys.version_info >= (3, 11),
        "NumPy installed": has_package("numpy"),
        "matplotlib installed": has_package("matplotlib"),
        "catalog's shared/ folder found": find_repo_root() is not None,
    }
    for name, ok in checks.items():
        print(f"[{'ok' if ok else 'MISSING'}] {name}")
    if all(checks.values()):
        print("Everything is ready.")
    else:
        print("Something is missing: see 'Common pitfalls' in the lesson.")


if __name__ == "__main__":
    main()
