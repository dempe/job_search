# 0010: Each interview is its own note

## Context

Interviews lived as `## Interview N` sections inside application notes. That left nowhere to record facts about an interview (what kind it was, who ran it, how it went), so an interview-centric view could only repeat the application's `interviews` dates. The dates and sections didn't reliably line up either: some notes had more dates than sections, some had more sections than dates, and older notes used ad hoc headings.

## Decision

- Each interview is a note at `Applications/{title}/Interviews/{n}/{n}.md`, in its application's folder (ADR 0011). Its frontmatter follows `_meta/Templates/Interview Template.md`:
  - `type: interview`
  - `application`: a link to the application note
  - `company`, `round`, `date`: `date` uses the same string format as the application's `interviews` list
  - `interviewers`
  - `outcome`: one of `pending`, `advanced`, `rejected`, `declined`, `ghosted`, `offer`
- Its body holds everything about that interview: prep, the `### Transcript` embed (ADR 0009), `### Questions` model answers, `### Review`, and retros.
- `### Review` grades each question's real answer against its model answer as Dataview list items, `- [grade:: right|partial|missed] [question:: …]`, with `You said:` and `Missing:` lines. `djtrans` writes it, and `Interviews.md` aggregates the grades into a Missed and Partial list and a per-interview scorecard.
- The application note keeps a `## Interview {n}` heading for each round, holding only `![[Applications/{title}/Interviews/{n}/{n}]]`. The full application still reads top to bottom in Obsidian.
- The interview's transcript is `transcript.md` beside it (ADR 0009).
- `Interviews.md`, at the vault root, is the interview-centric view. It's a set of Dataview queries over `Applications/` for `type: interview`.

## Known duplication

The interview date is stored twice: in the interview note's `date` and in the application's `interviews` list, which `_MOC Jobs` still reads. `djinterview` writes both. Making the interview note the single source and pointing `_MOC Jobs` at the interview notes is a planned follow-up.

## How to apply

- To add an interview, run `djinterview {Application} {date/time}`. Don't add `## Interview` sections to application notes by hand.
- Interview prep, transcripts, and retros go in the interview note, not in the application note.
- Skills that read an application's Q/As (`djanswers`, `djmvanswers`, `djtrans`) also read the interview notes it embeds. `djq` picks from both application and interview notes.
- When an interview's outcome becomes known, update its `outcome`. Set it to `advanced` when a later round is scheduled.
- The `interviewers` and `outcome` values on interviews migrated on 2026-11-04 were inferred from their content. A blank field means the content didn't say.
