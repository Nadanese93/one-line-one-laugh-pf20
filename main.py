#!/usr/bin/env python3
"""Write the One Line, One Laugh entry to entry.txt."""

import os
import sys

ENTRY = "My lawyer bills in six-minute increments, so I now say hello in under thirty seconds to save money."


def _check_length(entry):
    """Raise if the entry is not 1-200 characters."""
    if not 1 <= len(entry) <= 200:
        raise ValueError(
            f"entry length {len(entry)} is outside the 1-200 character gate"
        )


def _check_not_blank(entry):
    """Raise if the entry is only whitespace."""
    if not entry.strip():
        raise ValueError("entry is only whitespace")


def _check_single_line(entry):
    """Raise if the entry spans more than one line."""
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")


def _verify_written(path, expected):
    """Read entry.txt back and raise if its bytes differ from the entry."""
    with open(path, "rb") as f:
        written = f.read()
    if written != expected.encode("utf-8"):
        raise ValueError(
            f"written entry.txt bytes differ from the entry "
            f"({len(written)} bytes written, {len(expected.encode('utf-8'))} expected)"
        )


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    try:
        _check_length(ENTRY)
        _check_not_blank(ENTRY)
        _check_single_line(ENTRY)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    try:
        _verify_written(path, ENTRY)
    except (ValueError, OSError) as exc:
        print(f"error: verification failed: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote {len(ENTRY)}-character entry to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
