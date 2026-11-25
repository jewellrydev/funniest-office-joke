"""The Funniest Office Joke, Judged Head to Head — a make.fun entry.

Prints exactly one short line: a real office joke with a setup and a
turn, and the punchline last.
"""

LINE = (
    "The office printer only ever jams when someone whispers 'this is "
    "urgent' — it is not broken; it is method acting."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
