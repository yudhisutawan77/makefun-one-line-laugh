#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry.

Writes a single funny line (one sentence, at most 200 characters)
The joke's shape, per the judge's brief:
- Everyday truth: everyone buys focus gear to escape distraction.
- Surprise at the end: the distraction was never the noise outside,
  it was the thinker inside — a turn that still makes sense.
- Economy: one sentence, no word explains the joke.
"""

import os
import sys


def main() -> int:
    line = (
        "I bought noise-cancelling headphones to focus, and now I can hear "
        "my own thoughts \u2014 turns out they were the distraction all along."
    )

    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space.
    if not (1 <= len(line) <= 200):
        print(f"line is {len(line)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not line.strip():
        print("line is only white space", file=sys.stderr)
        return 1

    out_dir = os.environ.get("ENTRY_OUT") or os.environ.get(
        "ENTRY_OUT_DIR", "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
