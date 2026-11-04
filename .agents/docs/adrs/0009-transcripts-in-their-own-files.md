# 0009: Keep interview transcripts in their own files

## Context

Interview transcripts run 5–70k characters each. Inline in an application note, they bury the note's real content (Q/As, prep, model answers), make the note slow to read and edit, and make every skill that reads the note load them.

## Decision

- Each transcript lives in `Transcripts/{title} - {interview heading}.md`, where `{title}` is the application note's title and `{interview heading}` is the `##` heading of the interview it belongs to (e.g. `People Data Labs - Interview 2.md`, `Cognizant (1) - Interview.md`).
- The file holds only the raw transcript text, with no frontmatter and no fence.
- In the application note, the interview's `### Transcript` section holds one embed: `![[Transcripts/{title} - {interview heading}]]`. Obsidian renders it inline, but the source stays short.
- The link lives in the body, not in frontmatter, because a note has one transcript per interview and each belongs beside that interview's prep and `### Questions`.

## How to apply

- To add a transcript for a new interview: save the text to `Transcripts/{title} - Interview {n}.md`, then put the embed under that interview's `### Transcript` heading.
- `djtrans` reads transcripts through these embeds and never edits them.
