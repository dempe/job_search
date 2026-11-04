# 0009: Keep interview transcripts in their own files

## Context

Interview transcripts run 5–70k characters each. Inline in an application note, they bury the note's real content (Q/As, prep, model answers), make the note slow to read and edit, and make every skill that reads the note load them.

## Decision

- Each transcript lives in `Transcripts/{title} - {interview heading}.md`, where `{title}` is the application note's title and `{interview heading}` is the `##` heading of the interview it belongs to (e.g. `People Data Labs - Interview 2.md`, `Cognizant (1) - Interview.md`).
- The file holds only the raw transcript text, with no frontmatter and no fence.
- In the application note, the interview's `### Transcript` section holds one embed: `![[Transcripts/{title} - {interview heading}]]`. Obsidian renders it inline, but the source stays short.
- The link lives in the body, not in frontmatter, because a note has one transcript per interview and each belongs beside that interview's prep and `### Questions`.

## How to apply

- The user adds a new transcript by pasting it into the note as a fenced block under the interview's `### Transcript` heading. The agent moves it out, not the user.
- `djtrans` runs its bundled `extract.py` first. It copies each fenced transcript byte for byte to its file and replaces the block with the embed, so the text is never retyped. To move one outside of `djtrans`, run the same script on the note.
- `djtrans` then reads transcripts through the embeds and never edits the files.
