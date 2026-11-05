---
name: djmvanswers
description: Migrate answered application questions out of a job application note into topic-based notes in `Answers/`, replacing each answer code block with a backlink. Takes the application note's name (e.g. `Rivora`). Use when the user wants to file, move, or link an application's answers into Answer notes.
argument-hint: <application-note-name>
---

# Migrate Application Answers

Move every answered question in one `Applications/` note, and in the interview notes it embeds, into an Answer note in `Answers/`. Each answer goes to an existing note whose topic fits, or to a new note when nothing fits. Where the Q/A was, the answer's code block is replaced with a link to its new home.

Each interview is its own note, `Applications/{Application}/Interviews/{n}/{n}.md`, embedded in its application note as `![[Applications/{Application}/Interviews/{n}/{n}]]` (see ADRs 0010 and 0011). Below, "the application's notes" means the application note plus every interview note it embeds.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

Follow the steps below in order. A step that says STOP ends the run.

## Constraints

- The assistant MUST use only Claude Code's built-in tools (Bash, Read, Edit, Write). It MUST NOT write or run scripts.
- The Bash tool MUST be used only for read-only file listing commands (`ls`, `test -e`).
- The assistant MAY modify only:
  - the application's notes, and only by replacing answer code blocks with backlinks
  - notes in `Answers/`, and only by adding sections or creating new notes
- Answer text and question text MUST be moved verbatim: every character, blank line, and trailing space. The assistant MUST NOT fix typos, reword, reformat, or trim anything it moves.
- The assistant MUST NOT delete, reorder, or edit existing sections in `Answers/` notes.
- The assistant MUST NOT commit or push anything to git.

## Output

- The only output of this skill is the file changes.
- The assistant MUST NOT write any text to the user before, between, or after tool calls. That includes narration, progress updates, summaries, and a completion report.
- The single exception is one line explaining why the run stopped without changing anything (Step 1 or Step 2).

## Formats

**Q/A in an application note.** A Q/A is:

1. A question: one or more consecutive lines starting with `>`. A multi-line question may also contain lines that continue the blockquote without a `>` prefix. The question ends at the first blank line.
2. Exactly one blank line.
3. An answer: a fenced code block whose opening line is exactly ```` ``` ```` (no language), followed by the answer lines, followed by a closing ```` ``` ```` line.

A question followed by a link line (e.g. `[[Why Company X#Afresh|Why Company X]]`) instead of a code block has already been migrated.

**Q/A in an interview note.** Inside an interview note's `### Questions` section, a Q/A is instead:

1. A question: a `#### {question}` heading, holding the whole question on one line.
2. Optionally, bullets (`- grade:: …`, `- answer:: …`, `- missing:: …`, `- practice:: …`). These record the user's own answers, not the answer being filed, and MUST stay in place.
3. An answer: the fenced code block after the bullets (the model answer), or a link line if already migrated.

When filing one, the `Answers/` section's `> {question}` line is the heading text, so the Answers format doesn't change.

**Section in an Answer note.** Answer notes have no frontmatter. They are a series of sections sorted alphabetically (case-insensitive) by heading, separated by one blank line:

````markdown
## {Heading}

[[{Application}]]

> {question, verbatim}

```
{answer, verbatim}
```
````

**Backlink in the application note.** The code block is replaced by one line:

```markdown
[[{Answer note}#{Heading}|{Answer note}]]
```

## Step 1: Application note

- The argument is `{Application}`, the application note's name without `.md`.
- If no argument was provided, the assistant MUST STOP and ask for it.
- If `Applications/{Application}/{Application}.md` does not exist (check with `test -e`), the assistant MUST STOP with one line naming the missing file.
- Read the whole note, then every interview note it embeds.

## Step 2: Find answered Q/As

- Find every Q/A in the application's notes (see Formats), in any section, not only `## Application`.
- A Q/A is **answered** if its code block contains at least one non-whitespace character. Empty code blocks are unanswered and MUST be left untouched.
- Questions already followed by a link line MUST be left untouched.
- If there are no answered Q/As, the assistant MUST STOP with one line saying so.

## Step 3: Learn the Answer notes

- List `Answers/` with `ls`, and Read every note in it.
- Answer notes are organized by **topic**, not by company. A topic is the story, project, or recurring kind of question the answers share. For example:
  - `Why Company X`: answers to "why do you want to work here?"
  - `Introduction`: cover letters and introductions
  - `AI-assisted development workflow`: how the user works with AI tools
  - `Replacing batch analytics with Kafka Streams`: answers built around one project story
- For each note, determine its topic from its title and the questions and answers in it.

## Step 4: Choose a home for each answer

For each answered Q/A, in the order they appear:

- Decide what the answer is primarily about: the story it tells, the project it describes, or the kind of question it answers. Judge by the substance of the answer, not by keyword overlap with the question.
- If an existing Answer note's topic matches, that note is `{Answer note}`.
- If no existing note fits, create a new one. Its title:
  - MUST be a short, sentence-case noun phrase naming the topic, in the style of the existing titles (e.g. `Favorite development tools`, `Working remotely across time zones`)
  - MUST NOT contain a company name
  - MUST NOT contain the characters `# | [ ] ^ : / \`
  - MUST NOT match an existing note's filename (check with `test -e`)
- An answer created as a new note in this run is a valid home for later answers in the same run.

## Step 5: Choose the heading

- `{Heading}` is `{Application}`.
- If `{Answer note}` already has a `## {Heading}` section (including one added earlier in this run), `{Heading}` MUST instead be `{Application} ({label})`, where `{label}` is a short lowercase description of the question. For example, `Starbridge (interview preparation)`. It MUST NOT collide with any existing heading in that note.

## Step 6: Write the section

- Build the section (see Formats): the heading, the `[[{Application}]]` backlink, the question copied verbatim, and the code block copied verbatim, including its opening and closing fences.
- **Existing note:** insert the section with Edit at its alphabetical position (case-insensitive) among the note's `##` headings. Keep exactly one blank line between sections, and keep the file ending in a single newline.
- **New note:** create `Answers/{Answer note}.md` with Write, containing only the section and a trailing newline.

## Step 7: Replace the answer with a backlink

- In the note the Q/A is in (the application note or one of its interview notes), use Edit to replace the answer's code block, from its opening fence through its closing fence, with `[[{Answer note}#{Heading}|{Answer note}]]`.
- The question (blockquote or `####` heading), any `- field::` bullets (including `- practice::` lines after an application-note answer), and the blank lines around them MUST stay in place.
- Repeat Steps 4–7 for each answered Q/A, then STOP.
