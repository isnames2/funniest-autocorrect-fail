"""Funniest Autocorrect Fail — make.fun entry.

Writes one line: the funniest autocorrect fail, under 140 characters.
Pure Python standard library; deterministic output.
"""

import os

LINE = (
    "I texted my boss 'sorry, I'm running late' — autocorrect sent "
    "'sorry, I'm running naked.' My 9 a.m. meeting is going to be awkward."
)


def main() -> None:
    # Gate: the entry must be a single line of 1 to 140 characters.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
