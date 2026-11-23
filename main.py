#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters or fewer.

Writes the robot vacuum's excuse for missing a spot to /output/entry.txt.
"""

LINE = "My lidar classified that dust bunny as a protected species, so I filed it under 'do not disturb' and will be billing you for the paperwork."

def main() -> None:
    import os

    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
