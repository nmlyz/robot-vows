#!/usr/bin/env python3
"""One-Line Robot Wedding Vows -- submission generator.

Writes the winning vow to ``entry.txt`` inside OUTPUT_DIR
(default ``/output``). The output is deterministic: running the
script twice produces byte-identical files.
"""

import os
from pathlib import Path

LINE = "I do take you, and I accept your terms and conditions \u2014 all 4,096 pages, without reading a single word."

OUTPUT_DIR_ENV = "OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"
MAX_LINE_LENGTH = 160


def validate_line(line: str) -> None:
    """Check the line meets the submission rules before writing it."""
    if "\n" in line or "\r" in line:
        raise ValueError("line must not contain a newline")
    if not 1 <= len(line) <= MAX_LINE_LENGTH:
        raise ValueError("line must be 1-160 characters")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if not line.endswith("."):
        raise ValueError("line must end with a period")


def main() -> None:
    output_dir = Path(os.environ.get(OUTPUT_DIR_ENV, DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)

    validate_line(LINE)

    entry_path = output_dir / ENTRY_FILENAME
    entry_path.write_text(LINE + "\n", encoding="utf-8")
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
