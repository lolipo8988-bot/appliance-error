"""Funniest honest appliance error for make.fun.

The program writes exactly one line to entry.txt and nothing else.
The line is a fridge reporting its own death in a flat, put-upon
voice: the compressor has failed, so the fridge reclassifies itself
as a $900 cupboard with a light in it, and the milk is already lost.
No title, no preamble, and no explanation of the joke in the output.
"""

import os

LINE = "ERROR: Compressor failed. I am now a $900 cupboard with a light in it. The milk did not make it."


def write_entry() -> str:
    """Write the line to the output directory and return its path."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return target


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
