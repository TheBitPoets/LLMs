#!/usr/bin/env python3
"""Export only student files into a NEW directory (never overwrite work)."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    if args.destination.exists():
        parser.error("destination already exists; choose a new directory")
    shutil.copytree(ROOT / "starter", args.destination,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    print(f"Student workspace: {args.destination.resolve()}")
    print("Baseline deliberately incomplete: several acceptance tests should fail.")


if __name__ == "__main__":
    main()
