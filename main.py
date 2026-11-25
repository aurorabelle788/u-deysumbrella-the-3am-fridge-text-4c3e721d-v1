#!/usr/bin/env python3
"""Write the 3am fridge text to /output/entry.txt.

Stdlib only, deterministic, no network. One fixed line: at 3am the
fridge reports that the owner's leftovers have formed a union and are
demanding to be eaten before they expire at dawn.
"""
import os
from pathlib import Path

LINE = (
    "It's 3am. Your leftovers have formed a union and demand to be eaten "
    "before they expire at dawn."
)

MAX_CHARS = 140


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert "\n" not in text, "line must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, f"line is {len(text)} chars"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
