"""Move inline interview transcripts out of an interview or application note.

Each `### Transcript` section holding a fenced block is written byte for byte to
`Transcripts/`, and the block is replaced with an embed of that file. In an
interview note (`Interviews/{name}.md`) the file is `Transcripts/{name}.md`; in an
application note it's `Transcripts/{note title} - {interview heading}.md`.
Sections that already embed a file are left alone.

Usage: python3 -I extract.py "Interviews/{note}.md"
"""

import pathlib
import re
import sys

BLOCK = re.compile(r"### Transcript\n\n```\n(.*?)\n```\n", re.S)


def main(note_path):
    note = pathlib.Path(note_path)
    transcripts = note.parent.parent / "Transcripts"
    text = note.read_text(encoding="utf-8")
    new_text = text
    for m in reversed(list(BLOCK.finditer(text))):
        body = m.group(1)
        if note.parent.name == "Interviews":
            name = label = note.stem
        else:
            parents = re.findall(r"^## (.+)$", text[: m.start()], re.M)
            if not parents:
                print(f"skipped: transcript at offset {m.start()} has no ## parent heading")
                continue
            label = parents[-1]
            name = f"{note.stem} - {label}"
        target = transcripts / f"{name}.md"
        content = body + "\n"
        if target.exists() and target.read_text(encoding="utf-8") != content:
            print(f"skipped: {target} already exists with different content")
            continue
        transcripts.mkdir(exist_ok=True)
        target.write_text(content, encoding="utf-8")
        new_text = new_text[: m.start()] + f"### Transcript\n\n![[Transcripts/{name}]]\n" + new_text[m.end():]
        print(f"moved: {label} -> {target}")
    if new_text != text:
        note.write_text(new_text, encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1])
