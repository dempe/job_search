"""Attach a new interview transcript to an interview note.

The source file (normally ./transcript.txt) is copied byte for byte to
`transcript.md` beside the interview note, the note gets a `## Transcript`
section embedding that file, and the source is deleted. Nothing is changed if
the interview already has a transcript.

Usage: python3 -I extract.py "Applications/{title}/Interviews/{n}/{n}.md" transcript.txt
"""

import pathlib
import re
import shutil
import sys

FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
EMPTY_SECTION = re.compile(r"\n*## Transcript\n\s*(?=## |\Z)")


def attach(note_path, source_path):
    note, source = pathlib.Path(note_path), pathlib.Path(source_path)
    target = note.parent / "transcript.md"
    if not source.is_file():
        raise ValueError(f"{source} not found")
    if target.exists():
        raise ValueError(f"{target} already exists")
    text = note.read_text(encoding="utf-8")
    front = FRONTMATTER.match(text)
    head, body = (text[: front.end()], text[front.end():]) if front else ("", text)
    body = EMPTY_SECTION.sub("\n", body, count=1)
    if re.search(r"^## Transcript$", body, re.M):
        raise ValueError(f"{note} already has a transcript section")

    vault_path = pathlib.Path(*note.parent.parts[note.parent.parts.index("Applications"):])
    section = f"## Transcript\n\n![[{vault_path.as_posix()}/transcript]]\n"
    rest = body.lstrip("\n")
    shutil.copyfile(source, target)
    note.write_text(head + "\n" + section + ("\n" + rest if rest else ""), encoding="utf-8")
    source.unlink()


def main(note_path, source_path):
    try:
        attach(note_path, source_path)
    except ValueError as e:
        print(f"error: {e}")
        sys.exit(1)
    print(f"moved: {source_path} -> {pathlib.Path(note_path).parent / 'transcript.md'}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
