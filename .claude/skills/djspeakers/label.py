"""Split a raw interview transcript into speaker-labelled turns.

The raw transcript (Apple Voice Memos) has no speaker labels. The assistant
decides who said what and writes one anchor per turn, on stdin:

    Interviewer: Hi, Chris.
    Me: Hi. Can you
    Interviewer: So tell me about

Each anchor is a speaker label and the turn's first words, copied exactly. The
script finds each anchor in order and cuts the raw text there, so the
transcript's words are never retyped: joined back together, the turns equal
the raw transcript (whitespace collapsed). Consecutive turns by the same
speaker are merged.

The output is `transcript-processed.md` beside the raw transcript. The
interview note's `## Transcript` embed is then pointed at it, so the note
shows the labelled transcript; the raw `transcript.md` is never changed.

Usage: python3 -I label.py <transcript.md> <transcript-processed.md> < anchors.txt
"""

import pathlib
import re
import sys

LINE = re.compile(r"^([^:\n]{1,40}):\s+(\S.*)$")


def squash(text):
    return " ".join(text.split())


def label(raw, anchors):
    text = squash(raw)
    parsed = []
    for n, line in enumerate(anchors.splitlines(), 1):
        if not line.strip():
            continue
        m = LINE.match(line.strip())
        if not m:
            raise ValueError(f"line {n}: expected 'Label: words', got {line.strip()[:60]!r}")
        parsed.append((n, m[1].strip(), squash(m[2])))
    if not parsed:
        raise ValueError("no anchors given")

    positions = []
    for i, (n, _, words) in enumerate(parsed):
        start = positions[-1] + 1 if positions else 0
        at = text.find(words, start)
        if i == 0 and at != 0:
            raise ValueError(f"line {n}: the first anchor must match the start of the transcript")
        if at == -1:
            raise ValueError(f"line {n}: {words[:60]!r} not found after the previous anchor")
        positions.append(at)

    for i, (n, _, words) in enumerate(parsed):
        end = positions[i + 1] if i + 1 < len(positions) else len(text)
        again = text.find(words, positions[i] + 1)
        if again != -1 and again < end:
            raise ValueError(f"line {n}: {words[:60]!r} is ambiguous (it appears again before the next anchor); use more words")

    turns = []
    for i, (_, speaker, _) in enumerate(parsed):
        end = positions[i + 1] if i + 1 < len(positions) else len(text)
        chunk = text[positions[i]:end].strip()
        if turns and turns[-1][0] == speaker:
            turns[-1] = (speaker, f"{turns[-1][1]} {chunk}")
        else:
            turns.append((speaker, chunk))

    if " ".join(t for _, t in turns) != text:
        raise ValueError("internal error: turns don't rejoin to the transcript")
    return turns


def render(turns):
    return "\n\n".join(f"**{speaker}:** {text}" for speaker, text in turns) + "\n"


def switch_embed(note, folder):
    """Point the note's embed of {folder}/transcript at {folder}/transcript-processed."""
    return note.replace(f"![[{folder}/transcript]]", f"![[{folder}/transcript-processed]]")


def main(transcript, out):
    raw = pathlib.Path(transcript).read_text(encoding="utf-8")
    try:
        turns = label(raw, sys.stdin.read())
    except ValueError as e:
        print(f"error: {e}")
        sys.exit(1)
    out = pathlib.Path(out)
    out.write_text(render(turns), encoding="utf-8")
    note = out.parent / f"{out.parent.name}.md"
    if note.exists() and "Applications" in out.parent.parts:
        folder = pathlib.Path(*out.parent.parts[out.parent.parts.index("Applications"):]).as_posix()
        text = note.read_text(encoding="utf-8")
        switched = switch_embed(text, folder)
        if switched != text:
            note.write_text(switched, encoding="utf-8")
            print(f"embedded: {note} now embeds {folder}/transcript-processed")
    counts = {}
    for speaker, _ in turns:
        counts[speaker] = counts.get(speaker, 0) + 1
    print(f"wrote: {out} ({len(turns)} turns: " + ", ".join(f"{s} {c}" for s, c in counts.items()) + ")")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__.strip().splitlines()[-1])
        sys.exit(2)
    main(sys.argv[1], sys.argv[2])
