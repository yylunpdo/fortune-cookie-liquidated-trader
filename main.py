#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun entry 168.

Writes a single fortune-cookie line for a crypto trader who has just
been liquidated to /output/entry.txt (UTF-8, 1-160 characters, at most
20 words). Pure standard library; deterministic output.
"""

import os

FORTUNE = (
    "You lost everything at 3am except your sense of humour "
    "\u2014 the cookie says that was the real leverage."
)


def main():
    # Gate check, mirroring the sealed scorer: UTF-8 text of 1-160
    # characters, not only whitespace, at most 20 words, one line.
    assert 1 <= len(FORTUNE) <= 160, "fortune outside 1-160 chars"
    assert FORTUNE.strip(), "fortune is only whitespace"
    assert len(FORTUNE.split()) <= 20, "fortune over 20 words"
    assert "\n" not in FORTUNE, "fortune must be one line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
