"""Say What Actually Broke — round 2 entry.

Writes one single-line error message to $ENTRY_OUTPUT or /output/entry.txt.
Stdlib only.

Round 2 is a new angle, not a polish of round 1: round 1 blamed a lost file
in Downloads; this one names a different real failure — a laptop that died
because its charger was plugged into the wall, not the laptop.
"""

import os
import re
import sys

ENTRY = "Your laptop died at 1% because the charger was plugged into the wall, not the laptop — plug it in properly this time."


def validate(text: str) -> None:
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if text != text.strip():
        raise ValueError("entry has leading/trailing whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text or "\t" in text:
        raise ValueError("entry must be a single line with no tabs")
    if "  " in text:
        raise ValueError("entry has double spaces")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry has control characters")
    if not text.endswith("."):
        raise ValueError("entry must end with a period")
    # Single sentence: exactly one sentence-ending period, at the end.
    if text.count(".") != 1:
        raise ValueError("entry must be a single sentence")
    if not re.fullmatch(r"[ -~\u00a0-\uffff]+", text):
        raise ValueError("entry has unexpected characters")


def main() -> int:
    validate(ENTRY)
    out = os.environ.get("ENTRY_OUTPUT") or "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and re-validate exactly what was written.
    with open(out, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry does not match ENTRY exactly")
    validate(written)
    print(f"Wrote {len(written)} chars to {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
