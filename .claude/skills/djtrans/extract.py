"""Move inline interview transcripts out of an application note.

Each `### Transcript` section holding a fenced block is written byte for byte to
`Transcripts/{note title} - {interview heading}.md`, and the block is replaced
with an embed of that file. Sections that already embed a file are left alone.

Usage: python3 -I extract.py "Job Applications/{note}.md"
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
        parents = re.findall(r"^## (.+)$", text[: m.start()], re.M)
        if not parents:
            print(f"skipped: transcript at offset {m.start()} has no ## parent heading")
            continue
        name = f"{note.stem} - {parents[-1]}"
        target = transcripts / f"{name}.md"
        content = body + "\n"
        if target.exists() and target.read_text(encoding="utf-8") != content:
            print(f"skipped: {target} already exists with different content")
            continue
        transcripts.mkdir(exist_ok=True)
        target.write_text(content, encoding="utf-8")
        new_text = new_text[: m.start()] + f"### Transcript\n\n![[Transcripts/{name}]]\n" + new_text[m.end():]
        print(f"moved: {parents[-1]} -> {target}")
    if new_text != text:
        note.write_text(new_text, encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1])
