#!/usr/bin/env python3
"""Write the 3 AM hotfix commit message to /output/entry.txt.

One line, no trailing newline, well under the 180-character gate.
"""

import os

ENTRY = "revert: the 3 AM deploy that paged me mid-dream; prod is back, my trust in main is not"


def main() -> None:
    line = ENTRY.strip()
    if not 1 <= len(line) <= 179:
        raise ValueError(f"entry must be 1-179 chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
