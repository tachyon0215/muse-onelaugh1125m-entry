#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "One Line, One Laugh".
Candidates compared: a procrastination self-help book still in its
delivery box (a familiar joke shape), a dentist-and-floss confession
(needs its setup explained), and the selected fridge line: a fresh,
instantly pictured image - the fridge light snapping on at 2 a.m. like
an interrogation lamp over the cheese - whose laugh arrives inside the
line, reads cleanly in one pass, and is easy to repeat to someone else.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "My fridge has started turning its light on at 2 a.m. like an interrogation lamp every time I reach for the cheese."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
