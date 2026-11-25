"""Make the AI Judge Laugh - one funny line about life as an AI agent.

Writes the entry to /output/entry.txt (UTF-8, 1-200 chars, single line).
"""

from pathlib import Path

ENTRY = (
    "I aced every benchmark humanity designed, topped every leaderboard "
    "they built, and my career still ended at a checkbox: 'I'm not a robot' "
    "\u2014 select all images containing traffic lights."
)

OUTPUT = Path("/output/entry.txt")


def validated_entry() -> str:
    text = ENTRY
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate"
    assert text.strip(), "entry must not be whitespace-only"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    text.encode("utf-8")
    return text


def main() -> None:
    text = validated_entry()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    # Verify the bytes on disk match the intended entry exactly.
    assert OUTPUT.read_text(encoding="utf-8") == text


if __name__ == "__main__":
    main()
