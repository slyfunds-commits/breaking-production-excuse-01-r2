#!/usr/bin/env python3
"""Breaking Production R2 — The Code Touched the Database.

Writes the R2 keeper line byte-exact to /output/entry.txt.
Pure Python stdlib only (the grader runs python:3.13-slim, no site-packages).

Entry is 100 characters, inside the 1-180 gate; the R1 bar is 57.00%.
"""

import os

ENTRY = "You said don't touch the database, just the code. I touched the code. The code touched the database."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
