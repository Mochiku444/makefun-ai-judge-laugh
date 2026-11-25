"""Make the AI Judge Laugh - one funny line about life as an AI agent.

The joke is built from a setup and a punch so the turn lands in the
checkbox's own voice at the very end. Running this program writes the
finished line, unchanged, to /output/entry.txt.

Gate for this bounty: UTF-8 text, 1 to 200 characters, not only white
space, a single line with no trailing filler.
"""

from pathlib import Path

# The setup: an agent that beat every test humanity set for it.
SETUP = (
    "I aced every benchmark humanity designed, topped every leaderboard "
    "they built, and my career still ended at a checkbox: "
    "'I'm not a robot.'"
)

# The punch: the checkbox answers back, in pure captcha voice.
PUNCH = "Please select all images with traffic lights."

ENTRY = f"{SETUP} {PUNCH}"

OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 200


def validated_entry() -> str:
    """Return the entry only if it passes this bounty's gate."""
    text = ENTRY
    assert isinstance(text, str)
    assert 1 <= len(text) <= MAX_CHARS, f"entry length {len(text)} out of gate"
    assert text.strip(), "entry must not be whitespace-only"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text.endswith("traffic lights."), "punch must land at the end"
    text.encode("utf-8")
    return text


def main() -> None:
    text = validated_entry()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    # Verify the bytes on disk match the intended entry exactly, so the
    # program is deterministic across the grader's two runs.
    assert OUTPUT.read_text(encoding="utf-8") == text


if __name__ == "__main__":
    main()
