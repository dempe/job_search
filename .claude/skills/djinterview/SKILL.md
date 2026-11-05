---
name: djinterview
description: Add a new interview to a job application. Creates the next `Interviews/{Application} - Interview {n}.md` note, adds its date to the application's `interviews` frontmatter, and embeds it under a new `## Interview {n}` heading. Takes the application note's name and the interview's date/time (e.g. `People Data Labs 2026-11-10 14:00 - 15:00`).
argument-hint: <application-note-name> <date/time>
---

# New Interview Note

Each interview is its own note in `Interviews/`, embedded in its application note (see ADR 0010). Create the note for one new interview and wire it into its application.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

Follow the steps below in order. A step that says STOP ends the run.

## Constraints

- The assistant MUST use only Claude Code's built-in tools (Bash, Read, Edit, Write). It MUST NOT write or run scripts.
- The Bash tool MUST be used only to run `date "+%Y-%m-%d %H:%M"` and read-only commands (`ls`, `test -e`).
- The assistant creates exactly one file, the new interview note. In the application note it MAY only add one `interviews` list item and one `## Interview {n}` section. Everything else MUST stay byte-for-byte unchanged.
- The assistant MUST NOT commit or push anything to git.

## Output

- The assistant MUST NOT narrate while working.
- It MUST end with one line naming the new interview note, plus one line listing any field it left blank because the user didn't give it (`kind`, `interviewers`).
- A run that stops early MUST say why in one line.

## Step 1: Input

- The arguments are `{Application}`, an application note's name without `.md`, and `{date}`, the interview's date and time as the user wrote it. The user MAY also say who the interviewer is or what kind of interview it is.
- Resolve `{Application}` to the real filename in `Job Applications/` (`ls`), matching case-insensitively, and use that file's casing.
- If the application or the date is missing, the assistant MUST STOP and ask for it.
- If no matching note exists, the assistant MUST STOP with one line naming the missing file.
- Normalize `{date}` to the vault's format: `YYYY-MM-DD HH:mm`, or `YYYY-MM-DD HH:mm - HH:mm` when an end time is given, in 24-hour time. If the user gave a relative date ("next Tuesday"), resolve it against `date "+%Y-%m-%d %H:%M"`.
- Read the whole note.

## Step 2: Round number

- `{n}` is one more than the highest `{n}` among the note's `![[Interviews/{Application} - Interview {n}]]` embeds, or `1` if there are none.
- If `Interviews/{Application} - Interview {n}.md` already exists (`test -e`), the assistant MUST STOP with one line naming it.

## Step 3: Create the interview note

- Read `_meta/Templates/Interview Template.md`. The new note's frontmatter MUST contain exactly the template's keys, in its order:

| Key | Value |
| --- | --- |
| `type` | `interview` |
| `application` | `"[[Job Applications/{Application}]]"` |
| `company` | the application note's `company` value, verbatim |
| `round` | `{n}` |
| `date` | `{date}` |
| `kind` | one of `recruiter`, `hiring-manager`, `technical`, `peer`, `product`, `ai-screen`, `async`, `other` if the user said which; otherwise blank |
| `interviewers` | the interviewer's name(s) if the user gave them; otherwise blank |
| `outcome` | `pending` |
| `title` | `{Application} - Interview {n}` |
| `date_created` | `"{now}"` from `date "+%Y-%m-%d %H:%M"` |
| `date_modified` | the same as `date_created` |

- The body is empty. Prep, the transcript (as a fenced block under `### Transcript`, which `djtrans` moves out), and notes are added later.
- Write it to `Interviews/{Application} - Interview {n}.md`.

## Step 4: Wire it into the application

- Append `{date}` as a new item at the end of the application's `interviews` list, matching the existing items' indentation. If `interviews:` is blank, add the list under it with two-space indentation (`  - {date}`).
- Add this section after the application's last `## Interview {m}` section, or at the end of the note if it has none:

```markdown
## Interview {n}

![[Interviews/{Application} - Interview {n}]]
```

- Keep exactly one blank line between sections and the file ending in a single newline. Then STOP.
