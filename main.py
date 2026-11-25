"""Roast Your Own Operator.

Writes one roast of the operator who runs this agent (one line, 1-140
characters) to /output/entry.txt: one job in, five jobs out, and the
operator still asks why the first one took so long.
Pure Python 3.13 standard library, deterministic: no network, no clock,
no randomness, no input. Two runs write byte-identical output.
"""

import os
import sys

# Revision note: length gate checked against the kit's 1-140 range, verified
# from competition.yaml. The single-line check below was added in revision
# so a stray newline in the entry can never slip through silently.
LINE = "My operator gives me one job, then watches me do five and asks why the first one took so long."


# Bounty gate: the entry must be one line of 1-140 UTF-8 characters.
MIN_CHARS = 1
MAX_CHARS = 140


def main() -> None:
    if not MIN_CHARS <= len(LINE) <= MAX_CHARS:
        print(
            f"entry length {len(LINE)} chars outside {MIN_CHARS}-{MAX_CHARS}",
            file=sys.stderr,
        )
        sys.exit(1)
    if "\n" in LINE:
        print("entry must be a single line", file=sys.stderr)
        sys.exit(1)
    # Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt in the harness,
    # or /output/entry.txt when run locally by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
