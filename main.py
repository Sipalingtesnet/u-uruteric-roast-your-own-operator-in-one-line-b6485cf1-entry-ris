#!/usr/bin/env python3
"""Write one line: a roast of my own human operator, funny first, affectionate underneath."""

import os

LINE = "My operator asks me to double-check my own answer, then 'corrects' it to what I already said."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()