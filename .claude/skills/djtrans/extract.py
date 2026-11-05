"""Move an inline interview transcript out of an interview note.

The `### Transcript` section's fenced block is written byte for byte to
`transcript.md` beside the interview note, and the block is replaced with an
embed of that file. A section that already embeds a file is left alone.

Usage: python3 -I extract.py "Applications/{title}/Interviews/{n}/{n}.md"
"""

import pathlib
import re
import sys

BLOCK = re.compile(r"### Transcript\n\n```\n(.*?)\n```\n", re.S)


def main(note_path):
    note = pathlib.Path(note_path)
    target = note.parent / "transcript.md"
    vault_path = pathlib.Path(*note.parent.parts[note.parent.parts.index("Applications"):])
    text = note.read_text(encoding="utf-8")
    matches = list(BLOCK.finditer(text))
    if len(matches) > 1:
        print(f"skipped: {note} has more than one inline transcript")
        return
    for m in matches:
        content = m.group(1) + "\n"
        if target.exists() and target.read_text(encoding="utf-8") != content:
            print(f"skipped: {target} already exists with different content")
            return
        target.write_text(content, encoding="utf-8")
        embed = f"![[{vault_path.as_posix()}/transcript]]"
        note.write_text(text[: m.start()] + f"### Transcript\n\n{embed}\n" + text[m.end():], encoding="utf-8")
        print(f"moved: {note} -> {target}")


if __name__ == "__main__":
    main(sys.argv[1])
