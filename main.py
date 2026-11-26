#!/usr/bin/env python3
"""Texts From Your Future Self — make.fun bounty entry.

Writes one funny text message from the writer's future self to
``<OUTPUT_DIR>/entry.txt``. Pure Python 3.13 standard library: no third-party
imports, no network, no files read from anywhere else. The entry text is a
plain string literal below, so the program is fully deterministic — every run
writes the exact same bytes.
"""

import os

# The entry: one text message, under 200 characters, sent back in time by
# the writer's future self. The joke lands on the twist — the smoke alarm
# has become the future self's biggest fan — and it stays specific: a
# person who finally learned to cook in 2041, still setting the alarm off.
ENTRY_TEXT = (
    "Hey, it's you from 2041. Good news: you finally learned to cook. "
    "Bad news: the smoke alarm is now your biggest fan — "
    "it cheers for every single meal."
)


def check_gate(text: str) -> None:
    """Fail loudly if the entry would fail the competition gate.

    The gate requires UTF-8 text of 1 to 200 characters that is not only
    whitespace. Encoding to UTF-8 here also proves the text is encodable.
    """
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry is {len(text)} characters, gate needs 1..200")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    text.encode("utf-8")


def main() -> None:
    """Write the entry text to <OUTPUT_DIR>/entry.txt."""
    check_gate(ENTRY_TEXT)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
