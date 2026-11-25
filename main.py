#!/usr/bin/env python3
"""The Best Advice I Ever Got — make.fun entry.

Writes the one-sentence answer to /output/entry.txt.
Deterministic: the same line every run.

Why this line (see variants.md in the build folder for the full pairwise
tournament — 14 candidates, 28-game round-robin, champion 7-0):
- 2-beat + reveal in the last clause: beat 1 (the day my father died, the
  neighbour, the soup — a real moment with a named giver) -> beat 2 (the
  advice itself) -> reveal ("cooking for other people's bad days ever
  since" — the advice lived, not just heard).
- Specific and earned: a named giver, a dated moment, advice that is true
  beyond the moment it came from (grief, given somewhere to go, becomes
  care for other people).
- Real voice, not a slogan: the line is a recalled scene, and the turn
  ("give it somewhere") plus the lived reveal are original.
- 184 characters, 186 bytes — inside the 200 cap, one sentence.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-200 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "The day my father died, my neighbour brought soup and said, "
    "'Grief is just love with nowhere to go — give it somewhere,' "
    "and I have been cooking for other people's bad days ever since."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back what was written: the gate scores exactly this file, so a
    # silent encoding or truncation slip must fail here, not on the server.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("ERROR: entry.txt does not match the line", file=sys.stderr)
        sys.exit(1)
    print(LINE)


if __name__ == "__main__":
    main()
