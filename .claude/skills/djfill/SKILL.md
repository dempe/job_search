---
name: djfill
description: Fill out a job application form in Chrome from an existing note in `Job Applications/`, using the note's answers and `_meta/profile.yaml`. Fills every field it can, skips file uploads, and never submits. Takes the application note's name (e.g. `Coinbase`).
argument-hint: <application-note-name>
---

# Fill a Job Application Form

Open the job posting for one application note and fill in the form from data the vault already holds: the note's answers, `_meta/profile.yaml`, and `../resume/resume.yaml`. The form is left filled but unsent, for the user to check and submit.

Invoking this skill is the user's authorization to enter their personal data into that one form. It is not authorization to submit it.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

Follow the steps below in order. A step that says STOP ends the run.

## Constraints

- The assistant MUST NOT click Submit, Apply, or any control that sends the application.
- The assistant MUST NOT upload files or click file-attachment controls (Attach, Choose file, drag-and-drop targets). File inputs are reported for the user to handle.
- The assistant MUST NOT create an account, enter a password or payment details, or attempt a CAPTCHA.
- The assistant MUST only fill the page at the note's `listing` URL, and pages that posting navigates to as part of the same application.
- The assistant MUST NOT modify any file. This skill only reads the vault and writes into the browser.
- The assistant MUST NOT invoke another skill. This skill is run by the user, on its own.
- The assistant MUST NOT commit or push anything to git.

## Output

- The assistant MUST NOT narrate while working.
- The assistant MUST end with the report in Step 7. The user needs to know what was filled and what was skipped before they submit.
- A run that stops early MUST say why in one line.

## Step 1: Inputs

- The argument is `{Application}`, an application note's name without `.md`. Resolve it to the real filename in `Job Applications/` (`ls`), matching case-insensitively, and use that file's casing.
- If no argument was provided, the assistant MUST STOP and ask for it.
- If no matching note exists, the assistant MUST STOP with one line naming the missing file.
- Read the note. Take `{listing}` from its frontmatter. If `listing` is blank, the assistant MUST STOP and ask for the URL.
- Read `_meta/profile.yaml` and `../resume/resume.yaml`.
- A `# TODO` value in `profile.yaml` counts as missing: the field it feeds is skipped and reported, never guessed.

## Step 2: Collect the written answers

For each question in the note (a `>` blockquote):

- If a fenced code block follows it, the answer is that block's contents.
- If a link line follows it (e.g. `[[Why Company X#Coinbase|Why Company X]]`), read that note in `Answers/` and take the code block under the named `##` heading.
- An empty code block means the question is unanswered. Record it for the report and move on.

Answers MUST be entered verbatim. The assistant MUST NOT reword, shorten, or improve them on the way into the form.

## Step 3: Open the posting

- Call `tabs_context_mcp` first, to see what tabs exist.
- Open a new tab with `tabs_create_mcp` and `navigate` to `{listing}`. The assistant MUST NOT reuse an existing tab unless the user asks.
- If the page fails to load, or the extension lacks permission for the site, the assistant MUST STOP and say so. Site permissions are granted by the user in the extension.
- If the posting requires signing in or creating an account before the form appears, the assistant MUST STOP and say so.

## Step 4: Read the form

- Read the form with `read_page` using `filter: "interactive"`, which keeps the output small and lists each field's reference, type, and, for dropdowns, the options actually offered.
- Use `find` for a single field when that is cheaper than reading the page again.
- If the form spans multiple steps or pages, handle one step at a time: read, fill, then continue only if moving on doesn't submit anything.

## Step 5: Match fields to values

Build a field-to-value mapping before typing anything:

| Form field | Source |
| --- | --- |
| First/last/preferred name, email, phone, city, state, postal code, country | `profile.identity` |
| LinkedIn, website, GitHub | `profile.links` |
| Employment history rows | `profile.employment`, in order |
| Education rows | `profile.education` |
| Written questions (cover letter, "why us", exercises) | the answers from Step 2, matched on question text |
| Dropdowns and radio groups | the closest option the form actually offers to the matching value in `profile.standard_answers` |
| Résumé, cover letter attachment, any file input | skipped; reported in Step 7 |

Rules:

- The assistant MUST choose only from the options the form presents. If nothing matches closely, skip the field and report it.
- The assistant MUST NOT infer an answer from the resume when `profile.yaml` has a `# TODO` for it.
- A question in the form that the note doesn't answer MUST be left blank and reported. The assistant MUST NOT compose a new answer here; drafting belongs to `danswers`.
- `previously_employed_here` in `profile.yaml` is a default. If the vault shows a previous application or employment at this company that contradicts it, skip the field and report it.

## Step 6: Fill

- Set each mapped field with `form_input`, using the refs from Step 4.
- The assistant MUST NOT trigger native dialogs: no clicking file inputs, and no buttons that open an alert or confirm.
- If a field won't take a value after two attempts, skip it and report it rather than retrying further.
- After filling, re-read the form (`read_page`, interactive) once and check the values landed, particularly dropdowns, which often reset.

## Step 7: Report and stop

Leave the tab open. Report, briefly:

1. The application note and the URL that was filled.
2. Fields filled, grouped (contact, employment, education, written answers, dropdowns).
3. Fields skipped, each with its reason: a `# TODO` in `profile.yaml`, an unanswered question in the note, no matching dropdown option, or a file input.
4. Anything the user must do before submitting: attach the résumé and any other file, answer the skipped fields, then review and submit.

Then STOP.

## Troubleshooting

- **Stale refs.** Refs come from the last `read_page`. If a fill fails oddly or the page re-renders, read the page again to get fresh refs.
- **Dropdowns that won't stick.** Try the option's exact visible text, then its value. If neither holds after two attempts, skip and report.
- **Dynamic fields.** Some forms add rows (e.g. "Add another" for employment) only after the previous row is filled. Fill a row, re-read, then continue.
- **Loops.** If three attempts at the same field or page fail, the assistant MUST stop and ask the user how to proceed, rather than continuing to retry.
