#!/usr/bin/env python3
"""One Line of Earned Pride - make.fun entry.

Writes a single line of text (1 to 240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene - a small person
doing something hard, a long effort finally landing.
"""

import os
import sys

LINE = (
    "At seventy-one, Ibu Sari read her grandson's letter aloud for the "
    "first time, slowly, every word her own, and the whole kitchen "
    "listened."
)


def main() -> int:
    line = LINE.strip()
    if not line or len(line) > 240 or "\n" in line or "\r" in line:
        print("entry line is not a single line of 1-240 characters",
              file=sys.stderr)
        return 1
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as handle:
        handle.write(line)
    print("wrote %d characters to %s" % (len(line), out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
