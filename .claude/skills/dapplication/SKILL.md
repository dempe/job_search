---
name: dapplication
description: Create a new job application note in `Job Applications/` from a job description text file (e.g. jd.txt), filling its YAML frontmatter from the JD and recording the application form's questions with empty answer blocks. Use when the user wants to log, record, or start a job application note from a JD file.
argument-hint: <path-to-jd.txt> <source> <listing-url>
---

<!-- auto-fill-applications T0: FR0, FR1, NFR1 -->

# Job Application Note

Create a new job application note under `./Job Applications/` from a job description (JD) text file. The note's YAML frontmatter is filled from the JD, and the application form's questions are recorded with empty answer blocks for the user to fill in later.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

Follow the steps below in order. A step that says STOP ends the run.

## Constraints

<!-- auto-fill-applications T1: NFR0, NFR2, NFR4, FR55, FR56, FR57 -->

- The assistant MUST use only Claude Code's built-in tools (Bash, Read, Write, and asking the user). It MUST NOT write or run scripts.
- The Bash tool MUST be used only to run `date "+%Y-%m-%d %H:%M"` and read-only file listing commands (`ls`, `test -e`).
- The only file this skill creates is the new application note. The assistant MUST NOT rename, modify, or overwrite any existing note.
- The assistant MUST NOT write answers to any application question.
- The assistant MUST NOT create or modify anything in `Answers/`.
- The assistant MUST NOT create or modify anything in `Questions/`.
- The assistant MUST NOT commit or push anything to git.

## Output

- The only output of this skill is the new application note.
- The assistant MUST NOT write any text to the user before, between, or after tool calls. That includes narration, progress updates, summaries, and a completion report.
- There are two exceptions, and each MUST be as short as possible:
  - A question the user must answer to continue: the JD path (Step 1), the company name (Step 2), or a missing `source` or `listing` (Step 6).
  - A single line explaining why the run stopped without creating a note: an unreadable JD (Step 1), a duplicate application (Step 4), or an existing target file (Step 11).

## Step 1: Input

<!-- auto-fill-applications T2: FR2, FR3, FR4 -->

- The skill's arguments (or, when invoked without the slash command, the user's request) are expected to contain three values, in any order:
  - `{jd_path}`: the path to the JD text file. A relative path resolves against the current working directory (the vault root).
  - `{listing}`: the listing URL, i.e. the value starting with `http://` or `https://`.
  - `{source}`: where the listing was found, i.e. the remaining word (for example `matcha` or `4dayweek.io`).
  For example: `/dapplication /tmp/jd.txt matcha https://job-boards.greenhouse.io/afresh/jobs/6190640004`.
- If no JD path was provided, the assistant MUST STOP and ask the user for it.
- If the file does not exist or cannot be read, the assistant MUST STOP with one line giving the path and the error. No note is created.
- Otherwise, read the whole file. Its contents are referred to below as the JD.

## Step 2: Company name

<!-- auto-fill-applications T3: FR5, FR6 -->

- Derive the name of the hiring company from the JD.
- If the JD names more than one plausible company, the assistant MUST ask the user which name to use, listing the candidates. It MUST NOT pick one silently. Common cases:
  - A product brand and its parent company. For example, a JD for "Privacy" (Privacy.com) that describes it as part of "Lithic".
  - A recruiting agency and the employer it hires for.
  - A job board and the employer whose listing it hosts.
- The chosen name is `{Company}`. It is used verbatim for matching existing notes, for the new filename, and for the `company` frontmatter value.

## Step 3: Existing applications

<!-- auto-fill-applications T4: FR7, FR8, FR9 -->

- List the notes in `Job Applications/` with Bash (`ls "Job Applications"`).
- A note is an existing application for `{Company}` if and only if its filename is exactly one of:
  - `{Company}.md`
  - `{Company} ({n}).md`, where `{n}` is a non-negative integer
- Matching MUST be exact on the whole filename. For `Meta`, `Meta (1).md` and `Meta (2).md` match, but `Metal.md` and `Meta Platforms.md` do not.
- Existing applications MUST be identified by filename only. Do not use a note's `title`, its `company` value, or its contents.
- For each matching note, record:
  - its suffix: `{n}`, or `0` for a bare `{Company}.md`
  - its `applied` frontmatter value, read with the Read tool from that note's frontmatter
- The assistant MUST NOT read or use any other field or content from existing notes.

## Step 4: Clock and duplicate check

<!-- auto-fill-applications T5: FR10, FR11, FR12, FR13 -->

- Run `date "+%Y-%m-%d %H:%M"` once with the Bash tool. Record:
  - `{today}`: the date part (`YYYY-MM-DD`)
  - `{now}`: the full output (`YYYY-MM-DD HH:mm`)
- Compute `{cutoff}` as `{today}` minus six calendar months: the same day of the month, six months earlier. If that day doesn't exist in that month, use the month's last day. For example, `2026-09-14` gives `2026-03-14`, and `2026-08-31` gives `2026-02-28`.
- For each existing application from Step 3, take its `applied` value, ignoring surrounding quotes.
- An existing application whose `applied` value is missing or blank MUST NOT cause an abort.
- If any existing application has an `applied` date on or after `{cutoff}`, it is a duplicate. The assistant MUST STOP without creating a note and without asking for `listing` or `source`, after one line naming the matching note and its `applied` date (for example, `Duplicate: Job Applications/Lithic.md applied 2026-09-04`).

## Step 5: Filename

<!-- auto-fill-applications T6: FR15, FR16, FR17 -->

- If Step 3 found no existing applications, `{filename}` is `{Company}.md`.
- Otherwise, `{filename}` is `{Company} ({m}).md`, where `{m}` is one greater than the highest recorded suffix. For example:
  - with `Lithic.md` only, it is `Lithic (1).md`
  - with `Walmart (1).md` through `Walmart (3).md`, it is `Walmart (4).md`
- `{title}` is `{filename}` without the `.md` extension.
- Existing notes MUST NOT be renamed, modified, or overwritten, even when their numbering is inconsistent.

## Step 6: Listing and source

<!-- auto-fill-applications T7: FR14, FR30, FR31, FR32 -->

- This step runs only after Step 4 finds no duplicate.
- If both `{source}` and `{listing}` were provided in Step 1, the assistant MUST NOT ask for them. Skip to Step 7.
- Otherwise, ask the user only for the missing value or values, in a single message:
  - the `listing` URL of the job posting
  - the `source` where the listing was found (for example `matcha` or `4dayweek.io`)
- Wait for the reply. Any value the user leaves unanswered or blank MUST be written as blank.

## Step 7: Questions

<!-- auto-fill-applications T8: FR36, FR37, FR38, FR39, FR40, FR41, FR42, FR43, NFR5 -->

Find the application form in the JD. It usually follows the job description, after text such as "Apply for this job". Every field label in the form is a question.

**Include by default.** The assistant MUST include every question unless it clearly falls into one of the exclusion categories below. This holds whatever the answer format: free text, a dropdown, or a selection. For example, "What did you get when you cracked the code?" is answered with a dropdown, but it is not in any exclusion category, so it MUST be included.

**Exclusion categories.** This list is closed. A question that doesn't clearly fit a category MUST be included.

1. **Identity and contact.** Name (first, last, preferred), email, phone, country, city, LinkedIn, website, and resume/CV.
2. **Work authorization.** Work authorization, visa, and sponsorship questions. For example, "Will you now or in the future require sponsorship to work in the US?"
3. **Compensation.** Salary and compensation questions. For example, "What are your salary expectations?"
4. **Location and logistics.** Location, relocation, travel, and availability or start-date questions. For example, "Can you please confirm your working location?", a travel expectation question, or "When could you start?"
5. **Condition confirmations.** Yes/no confirmations of interview or employment conditions. For example, "Can you confirm that you can keep your camera on for the entire duration of the interview?"
6. **Referral source.** How the candidate heard about the role, or who referred them. For example, "How did you hear about this opportunity? (if referred please give employee name)" or "Where did you hear about this role?"
7. **Prior employment.** Whether the candidate has previously worked for the company. For example, "Have you previously been employed by Techstars?"
8. **Demographics.** Demographic and EEO questions, such as gender, race or ethnicity, veteran status, and disability status.
9. **Excluded follow-ups.** Fields that only apply to an excluded question. For example, "If so, please specify the type of sponsorship required" or "If you have selected Other for the travel requirement question, please provide more details".

**Reading the form.**

- A trailing `*` on a label marks a required field. It is not part of the question.
- `Select...` on the line after a label marks a dropdown. That is not grounds for exclusion.
- Widget text is not a question. Examples: "Attach", "No file chosen", "Enter manually", "Accepted file types: …", "Locate me", "indicates a required field".

## Step 8: Question formatting

<!-- auto-fill-applications T9: FR44, FR45, FR46, FR47, FR48 -->

- Included questions MUST keep the order in which they appear in the JD.
- Each question MUST be written as a Markdown blockquote: each line starts with `> `.
- The question text MUST be copied verbatim. The only change is removing a trailing required-field marker `*`, along with any whitespace before it.
- **Preceding content.** Sometimes a question can't be answered without text or embedded content that comes before it, such as a heading, instructions, a code snippet, an encoded string, or a passage the question refers to. That content MUST be copied verbatim into the same blockquote, before the question text. For example, "What did you get when you cracked the code?" is preceded by the "Crack the code" heading, its instructions, and the encoded blob.
- **Multi-line blockquotes.** A multi-line blockquote puts each non-blank source line on its own `> ` line. Every line except the last ends with `<br/>`. Blank lines between source lines are omitted. For example:

  ```markdown
  > Why do you want to join Resend?<br/>
  > Send an engaging message and tell us why you want to join us, what excites you about the problem we're solving, and how you envision your role at Resend.
  ```

## Step 9: Frontmatter

<!-- auto-fill-applications T10: FR18, FR19, FR20, FR21, FR22, FR23, FR24, FR25, FR26, FR27, FR28, FR29, FR33, FR34, NFR3, NFR6 -->

Read `_meta/Templates/Job Template.md`. The new note's frontmatter MUST contain exactly the template's keys, in the template's order, with these values:

| Key | Value |
| --- | --- |
| `type` | `job` |
| `applied` | `{today}` |
| `job_type` | `fulltime`, `parttime`, or `contractor`, as stated in the JD. Use `fulltime` if the JD doesn't say. |
| `recruited` | `false` |
| `status` | `awaiting-reply` |
| `interviews` | blank |
| `source` | `{source}` from Step 1 or Step 6, or blank |
| `listing` | `{listing}` from Step 1 or Step 6, or blank |
| `company` | `{Company}` |
| `position` | the job title from the JD, verbatim |
| `contract` | `true` if the role is a contract role, otherwise `false` |
| `remote` | `true` if the JD says the role is remote. `false` if it says on-site or hybrid. Blank if it doesn't say. |
| `compensation` | the pay range exactly as stated in the JD, or blank if it states none |
| `title` | `{title}` |
| `date_created` | `{now}` |
| `date_modified` | `{now}` |

The frontmatter MUST be valid YAML:

- A blank value is written as the key and colon with nothing after it (`interviews:`).
- Booleans are lowercase `true` or `false`.
- Wrap a value in double quotes if it contains `:` or `#`, or if it begins with any of ``- ? , [ ] { } & * ! | > ' " % @ ` ``. Escape embedded `"` as `\"` and `\` as `\\`. Because they contain `:`, `date_created`, `date_modified`, and URLs are always quoted.

The `YYYY-MM-DD HH:mm` timestamps and the filename-based `title` match the vault's Obsidian Linter rules (`yaml-timestamp`, `yaml-title`), so linting on save changes little.

## Step 10: Body

<!-- auto-fill-applications T11: FR35, FR49, FR50, FR51 -->

- After the closing `---` of the frontmatter, leave one blank line, then write the `## Application` heading followed by one blank line.
- For each included question, write its blockquote (Step 8), then one blank line, then an empty fenced code block: an opening ```` ``` ```` line followed immediately by a closing ```` ``` ```` line. Nothing goes between them.
- Separate consecutive question/answer pairs with exactly one blank line.
- If every question was excluded, the body is only the `## Application` heading.

## Step 11: Write

<!-- auto-fill-applications T12: FR17 -->

- Immediately before writing, check with Bash (`test -e "Job Applications/{filename}"`) that the note still does not exist. If it exists, the assistant MUST STOP with one line naming the existing file, without writing anything.
- Write the note to `Job Applications/{filename}` with the Write tool.
- STOP. The assistant MUST NOT write any text to the user after the note is written.

## Worked example

<!-- auto-fill-applications T13: NFR5, FR47, FR48, FR49, FR54 -->

**Input.** A JD copied from a Greenhouse posting for "Staff Software Engineer" at Privacy. The page:

- describes Privacy.com as having grown into Lithic
- is marked Remote
- states "The annual US salary range for this role is $200,000 - $220,000 plus equity"
- contains a "Crack the code" section with instructions and an encoded blob
- ends with an application form

**Run.**

- Step 1: invoked as `/dapplication /tmp/jd.txt matcha`, so `{source}` is `matcha` and `{listing}` is missing.
- Step 2: the assistant asks which company name to use. The user chooses `Privacy` over `Lithic`.
- Step 3: no filename matches `Privacy.md` or `Privacy ({n}).md`.
- Step 4: `date` prints `2026-09-14 18:30`.
- Step 6: the assistant asks only for the listing URL. The user leaves it blank.
- Step 11: the note is written, and the run ends with no further text.

**Expected note** at `Job Applications/Privacy.md`. `{encoded blob, verbatim}` stands in for the JD's full encoded string. A real run copies it exactly.

````markdown
---
type: job
applied: 2026-09-14
job_type: fulltime
recruited: false
status: awaiting-reply
interviews:
source: matcha
listing:
company: Privacy
position: Staff Software Engineer
contract: false
remote: true
compensation: $200,000 - $220,000 plus equity
title: Privacy
date_created: "2026-09-14 18:30"
date_modified: "2026-09-14 18:30"
---

## Application

> What do you think are our most complex technical challenges based on the very little you know about Lithic?

```
```

> Crack the code<br/>
> A hidden code is tucked into this application. Find it and enter it below to continue.<br/>
> {encoded blob, verbatim}<br/>
> What did you get when you cracked the code?

```
```
````
