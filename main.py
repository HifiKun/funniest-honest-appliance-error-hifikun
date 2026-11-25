"""The Funniest Honest Appliance Error (make.fun).

A washing machine reports the fault every laundry owner knows: a sock
goes into the wash and never comes back. The machine states the facts,
counts twice, and admits it has no answer either.

The program writes exactly one line to /output/entry.txt.
"""

import os

ENTRY = (
    "Error 404: sock not found. "
    "I washed it, dried it, counted twice. "
    "It is gone, and I am just as confused as you are."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> str:
    """One line, 1-200 characters, nothing else."""
    text = line.strip()
    if not text:
        raise ValueError("entry must not be blank")
    if len(text) > 200:
        raise ValueError("entry must be at most 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    line = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
