---
name: djspeakers
description: Label who is speaking in an application's raw interview transcripts. Writes `transcript-speakers.md` beside each `transcript.md`, with one `**Me:**` or `**{Interviewer}:**` paragraph per turn, cut from the raw text by a bundled script so no word is retyped. Use before grading (djtrans does), or when the user wants a transcript split by speaker. Takes the application note's name (e.g. `Rivora`), and optionally an interview number.
argument-hint: <application-note-name> [interview-number]
---

# Label Transcript Speakers

The user records interviews with Apple Voice Memos, whose transcripts have no speaker labels: just text, broken into chunks at pauses, not at speaker changes. This skill decides who said what and writes a speaker-labelled copy beside the raw transcript (ADR 0012). The raw `transcript.md` stays as it is.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

## Constraints

- The assistant MUST NOT modify any `transcript.md` or interview note.
- The only file it writes is `transcript-speakers.md`, and only through the bundled `label.py`. It MUST NOT write or edit that file any other way, so the transcript's words are never retyped.
- The Bash tool MUST be used only for `ls`, `test -e`, and `label.py`.

## Step 1: Input

- The argument is `{Application}`, an application note's name, plus an optional interview number `{n}`. Resolve the application to its folder in `Applications/` (`ls`), matching case-insensitively. If no argument was given, STOP and ask for it. If no folder matches, STOP with one line saying so.
- The transcripts are `Applications/{Application}/Interviews/{n}/transcript.md`. With `{n}`, take only that one; otherwise every interview that has one.
- Skip, and report, any transcript that already has a `transcript-speakers.md` beside it. To redo one, the user deletes that file first.
- If there's nothing left to do, STOP with one line saying so.

## Step 2: Gather context

For each transcript, read:

- the interview note `{n}.md` beside it: its frontmatter (`company`, `interviewers`) and any prep notes
- the whole `transcript.md`

The user is Chris. Knowing his background (`_meta/profile.yaml`, `Answers/`) helps tell his answers from the interviewer's pitch about their company.

## Step 3: Choose the labels

- The user's label is `Me`.
- One interviewer: their first name if `interviewers` names exactly one person or the transcript makes it clear (e.g. "my name is Rob"), otherwise `Interviewer`.
- Several interviewers: each one's first name where known, otherwise `Interviewer 1`, `Interviewer 2`… in order of first speaking.
- Labels are fixed for the whole transcript.

## Step 4: Decide the turns

Read the whole transcript in order and work out where the speaker changes. Speaker changes often fall mid-chunk and mid-line, so ignore the chunk breaks. Cues:

- The interviewer asks the questions, explains the company and role, and runs the agenda. Chris answers, talks about his own work (DataRank, SimplyMeasured, Octimine, Athena Math, Dekstech, his company), and asks his own questions near the end.
- Being addressed by name: "Chris" is said to Chris, not by him.
- A question followed by "Yeah, so…" or "Um, so…" is usually the other person answering.
- Short backchannels ("Okay.", "Yeah.", "Mm-hmm.", "Right.", "Cool.") are usually the listener reacting. Give one its own turn only when it's clearly the other person; if unsure, leave it inside the surrounding turn, where it does less harm than a wrong label.
- When a stretch is genuinely unclear, label it the way that best fits the conversation's flow, and count it as an uncertain call for the report.

## Step 5: Write the anchors and run the script

An anchor is one line per turn: `{Label}: {the turn's first words}`.

- Copy the first words exactly as they appear in the transcript: same spelling, punctuation and filler. Whitespace doesn't matter.
- Use at least three or four words, or the whole turn if it's shorter. Use more when the opening is common ("Yeah. So…").
- The first anchor is the transcript's first words.
- Anchors are in transcript order. Consecutive anchors with the same label are merged into one turn.

Run, with the anchors in a quoted heredoc:

```bash
python3 -I .claude/skills/djspeakers/label.py "Applications/{Application}/Interviews/{n}/transcript.md" "Applications/{Application}/Interviews/{n}/transcript-speakers.md" <<'ANCHORS'
Interviewer: Hi, Chris.
Me: Hi. Can you hear
...
ANCHORS
```

- On success it prints `wrote: … (N turns: …)`. By construction the turns, joined, equal the raw transcript.
- On `error: line N: …`, fix that anchor (not found: copy the words exactly; ambiguous: add words so it's unique before the next anchor) and run it again with all the anchors. After three failed runs for one transcript, STOP that transcript and report the error.

## Step 6: Report and stop

One line per transcript: the file written, its turn counts, and how many uncertain calls there were, naming the two or three most important ones briefly (e.g. `"It's a lot more difficult than it looks" -- Me or Rob?`). One line for each transcript skipped and why. Then STOP.
