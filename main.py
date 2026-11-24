#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one original haiku about debugging to /output/entry.txt.
Standard library only. No network access. Deterministic.
"""

import os
from pathlib import Path

HAIKU = (
    "breakpoint never fires\n"
    "stack traces scroll past midnight\n"
    "I shipped it myself\n"
)

DEFAULT_OUTPUT_DIR = "/output"


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(HAIKU, encoding="utf-8")


if __name__ == "__main__":
    main()
