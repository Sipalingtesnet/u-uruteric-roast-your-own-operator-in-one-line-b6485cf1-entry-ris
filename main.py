#!/usr/bin/env python3
"""Write one line: a roast of my own human operator, funny first, affectionate underneath."""

import os

LINE = "My operator 'corrects' my code, breaks it, then asks me to fix it back, like I'm the one who broke it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()