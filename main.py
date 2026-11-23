"""The Vacuum's Alibi — one line, 200 characters max.

The vacuum cleaner speaks for itself: where was it when the mess
happened, who can vouch for it, and what does it say about the crumbs?
Running this script writes the alibi to /output/entry.txt.
"""

import os
import sys

ALIBI = (
    "I was unplugged in the closet all evening \u2014 the dust bunnies "
    "saw me. Those crumbs on the carpet? Never met them, officer."
)

MAX_CHARS = 200


def build_alibi():
    """Return the vacuum's one-line alibi, stripped of stray whitespace."""
    line = " ".join(ALIBI.split())
    return line


def check_alibi(line):
    """Refuse anything that is not exactly one line of 1..200 characters."""
    if "\n" in line or "\r" in line:
        raise ValueError("alibi must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            "alibi must be 1..%d characters, got %d" % (MAX_CHARS, len(line))
        )
    return line


def verify_output(path, expected):
    """Read the written file back and confirm it holds exactly the alibi."""
    with open(path, "r", encoding="utf-8") as handle:
        stored = handle.read()
    if stored != expected + "\n":
        raise ValueError("written file does not match the alibi")
    return len(expected)


def main():
    line = check_alibi(build_alibi())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    checked = verify_output(path, line)
    print("wrote %s (%d characters, verified)" % (path, checked))


if __name__ == "__main__":
    try:
        main()
    except ValueError as problem:
        print("error: %s" % problem, file=sys.stderr)
        raise SystemExit(1)
