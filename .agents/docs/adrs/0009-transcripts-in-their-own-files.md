# 0009: Keep interview transcripts in their own files

## Context

Interview transcripts run 5–70k characters each. Inline in an application note, they bury the note's real content (Q/As, prep, model answers), make the note slow to read and edit, and make every skill that reads the note load them.

## Decision

- Each transcript lives in its own file, `transcript.md`, beside its interview note: `Applications/{title}/Interviews/{n}/transcript.md` (ADRs 0010 and 0011).
- The file holds only the raw transcript text, with no frontmatter and no fence.
- In the interview note, the `### Transcript` section holds one embed: `![[Applications/{title}/Interviews/{n}/transcript-processed]]`, the speaker-labelled copy (ADR 0012), or `…/transcript` until that exists. Obsidian renders it inline, but the source stays short.
- The link lives in the body, not in frontmatter, so the transcript sits beside that interview's prep and `### Questions`.

## How to apply

- The user adds a new transcript by pasting it into the interview note as a fenced block under `### Transcript`. The agent moves it out, not the user.
- `djtrans` runs its bundled `extract.py` first. It copies each fenced transcript byte for byte to `transcript.md` and replaces the block with the embed, so the text is never retyped. To move one outside of `djtrans`, run the same script on the note.
- The raw `transcript.md` is never edited. `djspeakers` writes the speaker-labelled `transcript-processed.md` beside it and switches the embed to it (ADR 0012). Skills read the processed copy.
