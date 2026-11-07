---
name: djinterview
description: Add a new interview to a job application. Creates the next `Applications/{Application}/Interviews/{n}/{n}.md` note, adds its date to the application's `interviews` frontmatter, and embeds it under a new `## Interview {n}` heading, then runs `djtrans` on it to file and grade `./transcript.txt` if there is one. Takes the application note's name and the interview's date/time (e.g. `People Data Labs 2026-11-10 14:00 - 15:00`).
argument-hint: <application-note-name> <date/time>
---

# New Interview Note

Each interview is its own note, `Applications/{Application}/Interviews/{n}/{n}.md`, embedded in its application note. Create the note for one new interview, wire it into its application, then hand off to `djtrans`, which takes the transcript from `./transcript.txt` if the interview has already happened.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

Follow the steps below in order. A step that says STOP ends the run.

## Constraints

- The assistant MUST use only Claude Code's built-in tools (Bash, Read, Edit, Write, and Skill for `djtrans` in Step 5). It MUST NOT write or run scripts.
- The Bash tool MUST be used only to run `date "+%Y-%m-%d %H:%M"`, read-only commands (`ls`, `test -e`), and `mkdir -p` for the new interview's folder.
- The assistant creates exactly one file, the new interview note (`djtrans` then adds the transcript). In the application note it MAY only add one `interviews` list item and one `## Interview {n}` section. Everything else MUST stay byte-for-byte unchanged.
- The assistant MUST NOT commit or push anything to git.

## Output

- The assistant MUST NOT narrate while working.
- After Step 4, it writes one line naming the new interview note, plus one line listing any field it left blank because the user didn't give it (`interviewers`). Then `djtrans`'s output rules apply.
- A run that stops early MUST say why in one line.

## Step 1: Input

- The arguments are `{Application}`, an application note's name without `.md`, and `{date}`, the interview's date and time as the user wrote it. The user MAY also say who the interviewer is.
- Resolve `{Application}` to an application folder in `Applications/` (`ls`), matching case-insensitively, and use that folder's casing. The note is `Applications/{Application}/{Application}.md`.
- If the application or the date is missing, the assistant MUST STOP and ask for it.
- If no matching note exists, the assistant MUST STOP with one line naming the missing file.
- Normalize `{date}` to the vault's format: `YYYY-MM-DD HH:mm`, or `YYYY-MM-DD HH:mm - HH:mm` when an end time is given, in 24-hour time. If the user gave a relative date ("next Tuesday"), resolve it against `date "+%Y-%m-%d %H:%M"`.
- Read the whole note.

## Step 2: Round number

- `{n}` is one more than the highest numbered folder in `Applications/{Application}/Interviews/` (`ls`), or `1` if there are none.
- If `Applications/{Application}/Interviews/{n}/{n}.md` already exists (`test -e`), the assistant MUST STOP with one line naming it.

## Step 3: Create the interview note

- Read `_meta/Templates/Interview Template.md`. The new note's frontmatter MUST contain exactly the template's keys, in its order:

| Key | Value |
| --- | --- |
| `type` | `interview` |
| `application` | `"[[Applications/{Application}/{Application}]]"` |
| `company` | the application note's `company` value, verbatim |
| `round` | `{n}` |
| `date` | `{date}` |
| `interviewers` | the interviewer's name(s) if the user gave them; otherwise blank |
| `outcome` | `pending` |
| `title` | `{n}` |
| `date_created` | `"{now}"` from `date "+%Y-%m-%d %H:%M"` |
| `date_modified` | the same as `date_created` |

- The body is empty. `djtrans` adds the transcript (Step 5); prep and notes are added by hand.
- Create the folder with `mkdir -p "Applications/{Application}/Interviews/{n}"`, then write the note to `Applications/{Application}/Interviews/{n}/{n}.md`.

## Step 4: Wire it into the application

- Append `{date}` as a new item at the end of the application's `interviews` list, matching the existing items' indentation. If `interviews:` is blank, add the list under it with two-space indentation (`  - {date}`).
- Add this section after the application's last `## Interview {m}` section, or at the end of the note if it has none:

```markdown
## Interview {n}

![[Applications/{Application}/Interviews/{n}/{n}]]
```

- Keep exactly one blank line between sections and the file ending in a single newline.

## Step 5: Transcript and grading

- Write the lines described in Output.
- If `./transcript.txt` doesn't exist (`test -e`), the interview hasn't happened yet: STOP.
- Otherwise, invoke the `djtrans` skill with the Skill tool, with `{Application} {n}` as its arguments. From this point, follow `djtrans`'s instructions, including its output rules.
