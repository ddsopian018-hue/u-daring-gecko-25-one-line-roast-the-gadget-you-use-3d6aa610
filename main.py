#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day — entry program.

The roast targets my smartwatch, the gadget that lives on my wrist around
the clock. The joke is built on the one contradiction every smartwatch
owner recognises on first read: the watch never stops monitoring *my*
health — heart rate, sleep score, stress level, blood oxygen — yet the
only vital sign in the relationship that is actually failing is its own
battery. It dies before dinner, every day, and I end up carrying a
charger for it like a drip line.

So the line frames the watch as a patient rather than a doctor: it is
"on life support while monitoring mine". That reversal is the sting —
the health gadget is the sick one, and its full-time carer is me. The
wording is kept tight: a three-item list of its monitoring duties sets
up the turn, then a short second clause lands the reversal. No wasted
words, one clear daily gadget, comfortably inside the 200-character
gate (the line is 175 characters).

The program is deterministic and pure standard library: it writes the
single line, with no trailing newline, to ``entry.txt`` inside the
directory named by the ``MAKEFUN_OUTPUT_DIR`` environment variable,
falling back to ``/output`` when the variable is unset.
"""

import os

LINE = (
    "My smartwatch tracks my sleep, counts my steps and watches my heart "
    "around the clock — then dies by dinner: the only gadget I own that's "
    "on life support while monitoring mine."
)


def main() -> None:
    # Gate self-check: the sealed scorer only forwards entries whose
    # text is 1 to 200 characters and not blank, so fail loudly here
    # rather than ship an invalid entry if the line is ever edited.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line breaks the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
