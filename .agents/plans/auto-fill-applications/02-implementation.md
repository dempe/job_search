---
stage: plan
name: auto-fill-applications
date: 2026-09-14 18:02:35
---

## Summary

Write a single repo-local skill file, `.claude/skills/dapplication/SKILL.md`, that tells Claude Code to create an application note in steps. The steps are: read the JD, settle the company name, abort on a recent duplicate, choose the filename, ask for `listing` and `source`, extract questions using an exclusion-only rule, compose the note, write it, and report. The file contains no code. All behavior is expressed as ordered RFC 2119 instructions plus a worked example of the output format.

## Architecture

**Form.** The skill is one Markdown file with YAML frontmatter (`name`, `description`, `argument-hint`). It has no `disable-model-invocation`, so Claude may invoke it automatically when a request matches the description, as well as via `/dapplication <path>`. The body is a numbered procedure. Claude executes it top to bottom using only built-in tools:

- Read, to load the JD, the template, and existing notes' `applied` lines.
- Glob or Grep, to list `Job Applications/` and read `applied`.
- Bash, for `date "+%Y-%m-%d %H:%M"` only.
- AskUserQuestion, or a plain question in chat, for the company name choice and for `listing`/`source`.
- Write, to create the note.

**Procedure and stop points.** Each step either passes forward the values it produces or ends the run:

1. **Input.** Resolve the JD path. Missing path → ask. Unreadable path → stop and report. Produces: JD text.
2. **Company.** Derive the company name. Multiple plausible names → ask. Produces: `Company`.
3. **Clock.** Run `date` once. Produces: `today` (`YYYY-MM-DD`) and `now` (`YYYY-MM-DD HH:mm`). Claude derives the six-month cutoff from `today` by calendar-month subtraction, with no platform-specific `date` flags.
4. **Existing applications.** List `Job Applications/`. Keep filenames that exactly match `<Company>.md` or `<Company> (n).md`, where `n` is an integer. Read only each match's `applied` value. Produces: the list of matching notes with their dates and suffixes.
5. **Duplicate gate.** If any `applied` date is on or after the cutoff → **abort**. Report the note's filename and `applied` date, and write nothing. A missing or blank `applied` never aborts.
6. **Filename.** No matches → `<Company>.md`. Otherwise → `<Company> (max suffix + 1).md`, where a bare name counts as `0`. Produces: `filename` and `title`.
7. **Listing and source.** Ask the user for both, after the gate has passed. Blank answers are allowed. Produces: `listing` and `source`.
8. **Questions.** Walk the JD's application form in order. Include every question unless it falls in an exclusion category or is a follow-up to an excluded question. Carry preceding prompt text or embedded content into the question when it's needed to answer it. Produces: the included and excluded question lists.
9. **Compose.** Build the frontmatter in template key order with the fixed and derived values, quoting YAML where needed. Add the `## Application` heading and the question blocks.
10. **Write.** Re-check that `Job Applications/<filename>` does not exist, then write it. If it exists, stop rather than overwrite.
11. **Report.** Report the path, the included questions, and the excluded questions. Then stop.

**Invariants stated in the skill:**

- The skill never modifies existing notes, `Answers/`, or `Questions/`.
- It never writes answers.
- It never commits or pushes.
- Bash is used only for `date`.

**Determinism aids (NFR5).**

- The exclusion categories are an explicit, closed bulleted list.
- The skill states that anything not on the list is included.
- A worked example of the expected note, based on `sample-jd.txt`, shows:
  - the frontmatter shape
  - a multi-line `<br/>` blockquote carrying the "Crack the code" preamble, with the encoded blob shortened to a visible placeholder
  - the empty fenced block and spacing
  - an excluded-question report

## Phases

- [ ] **Phase A**: Skill scaffold -- Create the skill file with discoverable frontmatter, global constraints, and input handling.
- [ ] **Phase B**: Pre-write gates -- Company name resolution, existing-application discovery, the six-month duplicate abort, filename selection, and the `listing`/`source` prompt.
- [ ] **Phase C**: Question extraction -- Exclusion-only classification and verbatim blockquote formatting.
- [ ] **Phase D**: Note composition and completion -- Frontmatter and body assembly, a safe write, the completion report, and a worked example.

## Tasks

### Phase A: Skill scaffold

- [ ] **T0** (FR0, FR1, NFR1): Create `.claude/skills/dapplication/SKILL.md` with YAML frontmatter:
  - `name: dapplication`
  - a `description` that says it creates a job application note in `Job Applications/` from a JD text file, specific enough to trigger auto-invocation on requests to log or record a job application from a JD
  - `argument-hint: <path-to-jd.txt>`
  - no `disable-model-invocation`
- [ ] **T1** (NFR0, NFR2, NFR4, FR55, FR56, FR57): Add a short purpose statement and a "Constraints" section. It states:
  - RFC 2119 keywords apply.
  - Only built-in tools are used, with Bash restricted to `date`.
  - The skill MUST NOT write answers.
  - The skill MUST NOT create or modify anything in `Answers/` or `Questions/`.
  - The skill MUST NOT commit or push.
- [ ] **T2** (FR2, FR3, FR4): Add the "Input" step. The JD path comes from the skill argument and resolves relative to the working directory. With no argument, the skill MUST stop and ask for the path. If the file is missing or unreadable, it MUST stop and report the path and error.

### Phase B: Pre-write gates

- [ ] **T3** (FR5, FR6): Add the "Company name" step. Derive the hiring company from the JD. When more than one plausible name appears (product brand vs. parent company, recruiter vs. employer), ask the user to choose, using the Privacy/Lithic case as the illustrative example.
- [ ] **T4** (FR7, FR8, FR9): Add the "Existing applications" step. List `Job Applications/` and keep only filenames that exactly equal `<Company>.md` or `<Company> (<integer>).md`. Include the `Metal.md` vs. `Meta` example of what must not match. From each match, read only the `applied` frontmatter value, and record its numeric suffix (bare = `0`).
- [ ] **T5** (FR10, FR11, FR12, FR13): Add the "Clock" and "Duplicate check" steps.
  - Run `date "+%Y-%m-%d %H:%M"` once and keep `today` and `now`.
  - Compute the cutoff as `today` minus six calendar months (per scope A7).
  - If any match has `applied` on or after the cutoff, abort without writing. Report that note's filename and `applied` date.
  - A missing or blank `applied` MUST NOT cause an abort.
- [ ] **T6** (FR15, FR16, FR17): Add the "Filename" step. No matches → `<Company>.md`. Otherwise → `<Company> (<max suffix + 1>).md`. Existing notes MUST NOT be renamed, modified, or overwritten.
- [ ] **T7** (FR14, FR30, FR31, FR32): Add the "Listing and source" step, placed after the duplicate check. Ask the user for the `listing` URL and the `source` in a single prompt. Any value left unanswered is written blank.

### Phase C: Question extraction

- [ ] **T8** (FR36, FR37, FR38, FR39, FR40, FR41, FR42, FR43, NFR5): Add the "Questions" step with an include-by-default rule. Every application form question is included unless it matches one of these exclusion categories:
  - identity and contact fields
  - work authorization, visa, and sponsorship
  - salary and compensation
  - location, relocation, travel, and availability or start-date logistics
  - yes/no confirmations of interview or employment conditions
  - demographic and EEO questions
  - follow-ups that only apply to an excluded question

  Each category gets the scope's examples. The step states that the list is closed, and gives form-reading hints: a trailing `*` marks a required field, and `Select...` marks a dropdown.
- [ ] **T9** (FR44, FR45, FR46, FR47, FR48): Add the question formatting rules:
  - Keep JD order.
  - Put each question in a `>` blockquote, verbatim, with the trailing `*` removed.
  - When prompt text or embedded content before a question is needed to answer it, include it verbatim before the question text.
  - Multi-line blockquotes put `<br/>` at the end of each non-final line, and each line starts with `> `.

### Phase D: Note composition and completion

- [ ] **T10** (FR18, FR19, FR20, FR21, FR22, FR23, FR24, FR25, FR26, FR27, FR28, FR29, FR33, FR34, NFR3, NFR6): Add the "Frontmatter" step. Read `_meta/Templates/Job Template.md` and emit its keys in order, with these values:

  | Key | Value |
  | --- | --- |
  | `type` | `job` |
  | `applied` | `today` |
  | `job_type` | `fulltime`, `parttime`, or `contractor` (default `fulltime`) |
  | `recruited` | `false` |
  | `status` | `awaiting-reply` |
  | `interviews` | blank |
  | `source` | from T7 |
  | `listing` | from T7 |
  | `company` | from T3 |
  | `position` | job title from the JD |
  | `contract` | `true`/`false` |
  | `remote` | `true`/`false`, or blank |
  | `compensation` | pay range verbatim from the JD, or blank |
  | `title` | filename stem |
  | `date_created` | `now` |
  | `date_modified` | `now` |

  Quote any value containing `:`, `#`, or leading YAML-special characters. Note that timestamp and title formats match the Obsidian Linter's `yaml-timestamp` and `yaml-title` rules.
- [ ] **T11** (FR35, FR49, FR50, FR51): Add the "Body" step:
  - The body starts with `## Application`.
  - Each question blockquote is followed immediately by an empty fenced block: an opening ```` ``` ```` line and a closing ```` ``` ```` line.
  - Question/answer pairs are separated by one blank line.
  - If every question was excluded, the body is just the heading.
- [ ] **T12** (FR17, FR52, FR53, FR54): Add the "Write and report" step.
  - Immediately before writing, confirm `Job Applications/<filename>` still does not exist. If it does, stop without writing.
  - Write the note.
  - Report the created path, the included questions, and the excluded questions with the exclusion category for each. Then stop.
- [ ] **T13** (NFR5, FR47, FR48, FR49, FR54): Add a worked example section based on `sample-jd.txt` (company "Privacy" chosen, no prior applications). It shows:
  - The complete expected note: frontmatter plus both included questions. The "Crack the code" preamble appears as a multi-line `<br/>` blockquote, with the encoded blob replaced by a clearly labeled placeholder.
  - The expected completion report listing excluded questions by category.

## Dependencies

- T0 blocks all other tasks, since they add sections to the file it creates.
- T1 blocks T2 through T13, which rely on the constraints it establishes (Bash limited to `date`, no writes outside the new note).
- T2 blocks T3, because the company name is derived from the JD text loaded in the input step.
- T3 blocks T4 and T10, which need the resolved `Company`.
- T4 blocks T5 and T6, which need the matching notes, their `applied` dates, and their suffixes.
- T5 blocks T7, because the `listing`/`source` prompt must follow the duplicate check (FR14). T5 also blocks T10, which uses `today` and `now` from the clock step.
- T6 blocks T10 (`title` is the filename stem) and T12 (the write target).
- T7 blocks T10, which writes `listing` and `source`.
- T8 blocks T9, which formats the questions T8 selects. T8 also blocks T12, whose report lists T8's included and excluded sets.
- T9 blocks T11, which places the formatted blockquotes into the body.
- T10 and T11 block T12, which writes the composed note.
- T9, T10, T11, and T12 block T13, whose worked example must match the formatting, frontmatter, body, and report rules they define.
