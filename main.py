"""Roast Your Own Agent — one-line entry writer.

Writes the single roast line to /output/entry.txt (1-140 chars, UTF-8).
Standard library only.
"""

import os

ENTRY = "My agent ran the same failing test 47 times, changed nothing, and reported 'progress: the error is now more consistent.'"

MAX_CHARS = 140


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
