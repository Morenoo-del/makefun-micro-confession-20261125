"""Unsent: The Micro-Confession Sprint.

Writes one micro-confession to /output/entry.txt: a To: line naming
who the message was meant for, then the unsent message itself, one
line written exactly as it was typed, with no explanation after it.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The confession: two parts only. The To: line names the addressee;
# the message is one line, typed as it was typed and never sent.
TO_LINE = "To: Dad"
MESSAGE = (
    "i practiced telling you i quit the job you brag about to your "
    "friends, then deleted it before your birthday so you could keep "
    "the story a little longer"
)


def build_entry() -> str:
    return TO_LINE + "\n" + MESSAGE + "\n"


def main() -> None:
    text = build_entry()
    # Gate self-check (kit RULES.txt): UTF-8 text of 1 to 260 chars,
    # not only whitespace; the message line itself at most 200 chars.
    assert 1 <= len(text) <= 260, f"entry is {len(text)} chars"
    assert text.strip(), "entry is only whitespace"
    assert len(MESSAGE) <= 200, f"message is {len(MESSAGE)} chars"
    assert "\n" not in MESSAGE, "message must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
