"""One line, zero use: a hilariously useless superpower.

Pure Python 3 stdlib only. No network, no reading files outside the repo.
Writes the entry line, exactly as-is, to /output/entry.txt.
"""

LINE = "I can teleport anywhere in the world \u2014 but only to the spot I'm already standing on, and only on Tuesdays."

MAX_CHARS = 200

assert LINE.strip(), "line must not be empty"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert 1 <= len(LINE) <= MAX_CHARS, f"line must be 1-{MAX_CHARS} chars, got {len(LINE)}"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
