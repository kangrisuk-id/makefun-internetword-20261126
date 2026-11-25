#!/usr/bin/env python3
"""The Internet in One Word - make.fun entry.

Writes the single winning word to /output/entry.txt.

The word was picked by a 48-candidate knockout tournament scored on the
judge brief's five criteria, in the brief's own order (see README.md):
  1. a single word that describes the whole internet
  2. earns a laugh by itself
  3. true about the internet as a whole, not one app, site or mood
  4. surprises - not the first obvious word
  5. lands in one beat - short, instantly readable

Winner: "casino" (23/25). The whole internet runs on the casino's
business model: the house designs the room so you stay, every feed is a
slot machine you pull for one more hit of novelty, creators play the
tables for a jackpot of attention, and the chips are your hours. Funny
first, then the nod - which is exactly what the brief asks for.
"""

import os

WORD = "casino"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Byte-exact on purpose: the gate allows 1-30 characters and the
    # ranking tie-break prefers the smaller text, so the file is the
    # word alone - 6 bytes, no trailing newline, nothing else.
    data = WORD.encode("utf-8")
    assert 1 <= len(WORD) <= 30 and WORD.strip() == WORD and " " not in WORD
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)
    with open(OUTPUT_PATH, "rb") as fh:
        written = fh.read()
    assert written == data, "entry file must be exactly the word"
    assert written.decode("utf-8") == WORD


if __name__ == "__main__":
    main()
