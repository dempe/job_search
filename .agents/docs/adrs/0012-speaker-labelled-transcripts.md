# 0012: Speaker-labelled transcripts beside the raw ones

## Context

Interviews are recorded and transcribed with Apple Voice Memos. Its transcripts have no speaker labels: the text is broken into chunks at pauses, and speaker changes often fall mid-chunk. Every skill that read a transcript had to work out who was speaking, separately each time, and an answer quote could take in the interviewer's words or miss part of the user's answer.

## Decision

- `djspeakers` decides who said what once per transcript and writes `transcript-speakers.md` beside the raw `transcript.md`: one paragraph per turn, `**Me:** …` for the user and `**{Interviewer's first name}:** …` (or `**Interviewer:**`) for the other side.
- The assistant never retypes the transcript. It writes one anchor per turn (a label and the turn's first words), and the bundled `label.py` cuts the raw text at those anchors. Joined back together, the turns equal the raw transcript with whitespace collapsed; the script checks this and rejects anchors that are missing or ambiguous.
- The raw `transcript.md` stays unchanged and stays the embed in the interview note (ADR 0009). The labelled file is derived from it.
- `djtrans` labels any transcript that has no `transcript-speakers.md` yet, then reads only the labelled copy: interviewer turns for the questions, `**Me:**` turns for the user's answers.

## How to apply

- Speaker calls are still judgment, so they can be wrong. To redo a transcript, delete its `transcript-speakers.md` and run `djspeakers` again for that interview, saying which calls to change.
- `label.py` has unit tests: `python3 -I .claude/skills/djspeakers/test_label.py`.
