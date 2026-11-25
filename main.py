#!/usr/bin/env python3
"""Emit the contest entry line into entry.txt.

This is the entry for make.fun's "One Line, One Laugh". The joke is a
single fixed sentence: a fridge whose light clicks on at 2 a.m. like an
interrogation lamp whenever the cheese is approached. The humour sits
entirely inside that one image, so the program's only job is to deliver
the line unchanged - no randomness, no clock, no network access.
"""
import os
from pathlib import Path

JOKE = (
    "My fridge has started turning its light on at 2 a.m. like an "
    "interrogation lamp every time I reach for the cheese."
)
PAYLOAD = JOKE + "\n"
LIMIT = 200


def check_line(text: str) -> None:
    """Guard the contest rules before writing anything.

    The entry must be one non-empty line of at most LIMIT characters;
    anything else is rejected here instead of reaching the output file.
    """
    body = text.rstrip("\n")
    if len(body) == 0 or len(body) > LIMIT:
        raise ValueError("line length outside the allowed range")
    if not body.strip():
        raise ValueError("line must contain visible characters")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must fit on a single line")


def target_file() -> Path:
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.txt"


def run() -> None:
    check_line(PAYLOAD)
    target_file().write_bytes(PAYLOAD.encode("utf-8"))


if __name__ == "__main__":
    run()
