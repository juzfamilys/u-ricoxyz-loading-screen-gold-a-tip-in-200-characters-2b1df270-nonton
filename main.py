#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one sharp, funny loading-screen tip for stressed developers and
AI coding agents to /output/entry.txt.

Pure Python standard library only.
"""

import os

TIP = (
    "Tip: your agent isn't stuck. It's rewriting the same function "
    "for the fourth time \u2014 this time with confidence. Let it cook."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Assert the gate: 1-200 chars, a single non-blank line."""
    assert isinstance(text, str)
    assert text.strip(), "entry must not be empty or only whitespace"
    assert "\n" not in text.rstrip("\n"), "entry must be a single line"
    assert "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
    )


def main() -> None:
    validate(TIP)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)
    print(f"Wrote /output/entry.txt ({len(TIP)} characters)")
    print(TIP)


if __name__ == "__main__":
    main()
