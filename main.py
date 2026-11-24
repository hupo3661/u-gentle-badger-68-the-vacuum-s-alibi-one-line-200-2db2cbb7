#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, 200 characters or fewer.

Writes the robot vacuum's excuse for missing a spot to /output/entry.txt.
"""

LINE = "I had 4% battery, a full schedule, and one dust bunny that looked at me funny, so I filed it under 'protected species' and went home."

def main() -> None:
    import os

    # Explicit validation: entry must be non-empty, single-line, <=200 chars.
    if not LINE:
        raise SystemExit("error: entry text is empty; expected a non-empty one-line entry")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("error: entry text must be a single line; found a line break")
    if len(LINE) > 200:
        raise SystemExit(
            f"error: entry text is {len(LINE)} characters; expected 200 or fewer"
        )
    if LINE != LINE.strip():
        raise SystemExit("error: entry text must not have leading or trailing whitespace")

    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)

    # Read-back verification: what landed on disk must match LINE exactly.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit(
            f"error: read-back verification failed; file contains {written!r}, expected {LINE!r}"
        )


if __name__ == "__main__":
    main()
