---
stage: scope
name: auto-fill-applications
date: 2026-09-14 17:51:46
---

## Summary

Create a reusable Claude Code skill, `dapplication`, that takes a job description text file (`jd.txt`) and creates a new job application note under `Job Applications/`. The skill fills the note's YAML frontmatter from the JD and adds every application question that isn't in an excluded category, each with an empty answer block. It aborts if an application for the same company was made within the last six months. The deliverable is the skill's Markdown file only. No scripts or other code.

## Requirements

### Functional

**Skill packaging**

- FR0: The deliverable MUST be a Claude Code skill named `dapplication`.
- FR1: The skill MUST be located at `.claude/skills/dapplication/SKILL.md` in this repository.
- FR2: The skill MUST accept the path to a JD text file as its argument.
- FR3: If no JD path is provided, the skill MUST stop and ask the user for one.
- FR4: If the JD path does not exist or is unreadable, the skill MUST stop and report the problem to the user.

**Company name**

- FR5: The skill MUST derive the company name from the JD.
- FR6: If the JD names more than one plausible company (e.g. a product brand and its parent company, such as "Privacy" and "Lithic" in `sample-jd.txt`), the skill MUST ask the user which name to use.

**Existing applications**

- FR7: The skill MUST identify existing applications for the company solely by note filename in `Job Applications/`: `<Company>.md` or `<Company> (n).md`.
- FR8: Filename matching MUST be exact on the company name, so that e.g. `Metal.md` does not count as a note for `Meta`.
- FR9: The only field the skill reads from an existing application note MUST be its `applied` frontmatter date.
- FR10: If any existing application for the company has an `applied` date within the six months before the current date, the skill MUST abort without creating a note.
- FR11: An existing application whose `applied` date is missing or blank MUST NOT cause an abort.
- FR12: When aborting, the skill MUST report the matching note's filename to the user.
- FR13: When aborting, the skill MUST report the matching note's `applied` date to the user.
- FR14: The existing-application check MUST run before the skill asks the user for `listing` or `source`.

**Filename**

- FR15: If no existing application for the company exists, the new note's filename MUST be `<Company>.md`.
- FR16: If existing applications for the company exist, the new note's filename MUST be `<Company> (m).md`, where `m` is one greater than the highest existing suffix. A bare `<Company>.md` counts as suffix `0`.
- FR17: The skill MUST NOT rename, modify, or overwrite any existing note.

**Frontmatter**

- FR18: The new note's frontmatter MUST contain the keys from `_meta/Templates/Job Template.md`, in the template's order.
- FR19: `type` MUST be `job`.
- FR20: `company` MUST be the company name chosen under FR5/FR6.
- FR21: `position` MUST be the job title from the JD.
- FR22: `remote` MUST be `true` or `false` when the JD states the work arrangement, and blank otherwise.
- FR23: `job_type` MUST be one of `fulltime`, `parttime`, or `contractor` as derived from the JD, defaulting to `fulltime` when the JD doesn't say.
- FR24: `contract` MUST be `true` when the role is a contract role, and `false` otherwise.
- FR25: `compensation` MUST contain the pay range as stated in the JD, and be blank if the JD states none.
- FR26: `applied` MUST be the current date in `YYYY-MM-DD` format.
- FR27: `status` MUST be `awaiting-reply`.
- FR28: `recruited` MUST be `false`.
- FR29: `interviews` MUST be blank.
- FR30: Before writing the note, the skill MUST ask the user for the `listing` URL.
- FR31: Before writing the note, the skill MUST ask the user for the `source`.
- FR32: If the user leaves `listing` or `source` unanswered, that field MUST be left blank.
- FR33: `title` MUST equal the filename without the `.md` extension.
- FR34: `date_created` and `date_modified` MUST be the current local time in `YYYY-MM-DD HH:mm` format.

**Body and questions**

- FR35: The note body MUST begin with a `## Application` heading, matching the template.
- FR36: The skill MUST include every application question from the JD that is not excluded by FR37–FR43.
- FR37: Identity and contact fields (name, email, phone, country, city, LinkedIn, website, resume) MUST be excluded.
- FR38: Work authorization, visa, and sponsorship questions MUST be excluded.
- FR39: Salary and compensation questions MUST be excluded.
- FR40: Location, relocation, travel, and availability or start-date logistics questions MUST be excluded.
- FR41: Yes/no confirmations of interview or employment conditions (e.g. "Can you confirm that you can keep your camera on for the entire duration of the interview?") MUST be excluded.
- FR42: Demographic and EEO questions MUST be excluded.
- FR43: Follow-up fields that only apply to an excluded question (e.g. "If so, please specify the type of sponsorship required") MUST be excluded.
- FR44: Questions MUST appear in the note in the same order as in the JD.
- FR45: Each question MUST be written as a Markdown blockquote (`> question`).
- FR46: Question text MUST be preserved verbatim, except that a trailing required-field marker (`*`) MUST be removed.
- FR47: When a question depends on preceding prompt text or embedded content to be answerable (e.g. the "Crack the code" instructions and encoded blob in `sample-jd.txt`), that content MUST be included verbatim in the question's blockquote, before the question text.
- FR48: A multi-line question (e.g. a prompt followed by helper text) MUST put every line in the blockquote, joining lines with `<br/>` at the end of each non-final line. This matches existing notes such as `Job Applications/Resend.md`.
- FR49: Each question MUST be followed by an empty fenced code block (a ```` ``` ```` line immediately followed by a closing ```` ``` ```` line).
- FR50: Question/answer pairs MUST be separated from each other by one blank line.
- FR51: If every question is excluded, the note MUST still be created with only the frontmatter and the `## Application` heading.

**Completion**

- FR52: After writing the note, the skill MUST report the created note's path to the user.
- FR53: After writing the note, the skill MUST list the included questions for the user.
- FR54: After writing the note, the skill MUST list the excluded questions for the user, so misclassifications can be reviewed.
- FR55: The skill MUST NOT write answers to any question.
- FR56: The skill MUST NOT create or modify notes in `Answers/`.
- FR57: The skill MUST NOT create or modify notes in `Questions/`.

### Non-Functional

- NFR0: The skill MUST be a single Markdown instruction file. It MUST NOT depend on scripts, binaries, or packages beyond Claude Code's built-in tools.
- NFR1: The skill file MUST include YAML frontmatter with `name` and `description`, so Claude Code can discover it and it can be invoked as `/dapplication <path>`.
- NFR2: The skill's instructions SHOULD use RFC 2119 terminology, consistent with the existing `d*` skills (e.g. `dscope`).
- NFR3: Frontmatter values the skill writes MUST be valid YAML. Values containing `:` or leading special characters MUST be quoted.
- NFR4: The skill MUST NOT commit or push changes to git.
- NFR5: The skill SHOULD state the exclusion categories (FR37–FR43) explicitly enough that repeated runs on the same JD produce the same question set.
- NFR6: Generated notes SHOULD be stable under the vault's Obsidian Linter configuration, so that linting on save makes minimal changes. Relevant rules: `yaml-title` from filename, and `yaml-timestamp` with format `YYYY-MM-DD HH:mm`.

## Context

**Repository.** `/Users/cld/workspace/job_search` is an Obsidian vault tracked in git. It has no existing `.claude/` directory. Relevant top-level folders:

- `Job Applications/`: about 200 application notes, one per application.
- `Answers/`: answer notes created by a recent reorganization. Each has one `## <Application>` section per use, containing `Source: [[<Application>]]`, the `> question`, and the answer in a fenced code block.
- `Questions/`: question notes with `aliases` and backlink lists to applications. Out of scope for this skill.
- `_meta/Templates/Job Template.md`: the application note template. Its frontmatter keys, in order: `type, applied, job_type, recruited, status, interviews, source, listing, company, position, contract, remote, compensation, title, date_created, date_modified`. The body is `## Application`.

**Existing application note conventions.**

- Recent notes (e.g. `Job Applications/Lithic.md`, `Archy.md`, `Resend.md`) put `Answer: [[<Answer note>#<Application>|<Answer note>]]` under each `> question`. Older notes, and the problem statement, use an inline fenced code block under the question. This skill uses the empty fenced code block form. Moving answers into `Answers/` and linking them stays a manual step.
- Some notes carry extra keys not in the template (`4day`, `industry`, `website`, `location`, `company_size`, `blog`, `correspondence`). The skill emits only template keys.
- `applied` is a `YYYY-MM-DD` date in 206 application notes. One note has a blank `applied` and one has no `applied` key.
- Observed `status` values: `awaiting-reply`, `ghosted`, `rejected`, `declined`, `cancelled`, `offer`. Observed `job_type` values: `fulltime`, `parttime`, `contractor`.
- Duplicate-company numbering is currently inconsistent. Some groups start at `(0)` (`Close (0)`, `Close (1)`), others start at `(1)` with no bare note (`Walmart (1)`–`(3)`, `Meta (1)`–`(2)`), and one `(0)` stands alone (`Allstate (0)`). `Metal.md` exists alongside `Meta (n)` notes, which is why FR8 requires exact name matching.
- `Close (1).md` has `title: Close (2)`, a legacy mismatch. Existing applications are therefore identified by filename, not by the `title` key. The Obsidian Linter's `yaml-title` rule derives `title` from the filename.

**Obsidian configuration.** Community plugins include `obsidian-linter` (lint on save), `dataview`, `obsidian-footnotes`, `easy-typing-obsidian`, and `obsidian-completr`. The linter sets `date_created`/`date_modified` from file-system timestamps in `"YYYY-MM-DD HH:mm"` format, sets `title` from the filename, and title-cases headings.

**Sample input.** `.agents/plans/auto-fill-applications/sample-jd.txt` is raw page text copied from a Greenhouse posting: the job description followed by the application form. Form labels end with `*` when required, and dropdowns show `Select...` on the next line. The sample contains:

- Two included questions:
  - "What do you think are our most complex technical challenges based on the very little you know about Lithic?"
  - "What did you get when you cracked the code?", preceded by its "Crack the code" instructions and encoded blob.
- Excluded fields: contact and identity fields, sponsorship and its follow-up, salary expectations, camera confirmation, working location, the travel expectation question and its "Other" follow-up.
- Two candidate company names, "Privacy" (product) and "Lithic" (parent). The salary range is "$200,000 - $220,000 plus equity". The job title is "Staff Software Engineer" and the role is Remote.
- `Job Applications/Lithic.md` has `applied: 2026-09-04`. A run on the sample using company "Lithic" within six months of that date is a duplicate under FR10.

**Related skills.** The user's `d*` workflow skills (`dscope`, `dplan`, etc.) live in home-manager at `~/.config/home-manager/files/.claude/skills/` and are the stylistic reference for skill structure. `dapplication` is vault-specific, so it lives in this repo instead.

## Risks

- K0: Exclusion categories may not cover every trivial question type (e.g. "Where did you hear about this role?", pronouns, referral names). Uncovered types get included as noise. Conversely, a borderline question may be excluded when the user wanted it recorded, leaving the application history incomplete. FR54's excluded-question report mitigates the second case.
- K1: JD text is copied from varied job boards (Greenhouse, Ashby, Workable, Lever, etc.) with different form layouts. Question boundaries, helper text, preceding prompt content, and dropdown markers may be misread, causing merged, split, or truncated questions.
- K2: Company name extraction may pick the wrong entity (a recruiter, a parent vs. product brand, or a job board name). That creates a misnamed note, and it breaks the duplicate check and numbering, so a recent application may go undetected.
- K3: The duplicate check matches filenames exactly. Earlier applications filed under a name variant (e.g. "Lithic, Inc." or a product brand) are not detected, allowing a repeat application within six months.
- K4: Duplicate numbering follows FR16, but existing groups are inconsistent (starting at `(0)` or `(1)`). New numbers may not match whatever convention the user expects for a given company, which may need manual renaming.
- K5: Company names containing characters that are invalid or awkward in filenames or Obsidian links (`/`, `:`, `#`, `|`, `[`, `]`) could produce a failed write or unlinkable note.
- K6: Pay ranges or job titles copied verbatim may contain characters that break YAML parsing (e.g. `:`), making the note's frontmatter invalid for Dataview and the linter unless properly quoted (NFR3).
- K7: The Obsidian Linter may rewrite `date_created`/`date_modified` from file-system timestamps, or title-case the heading, on first save. This causes small unexpected diffs.
- K8: Embedded prompt content included under FR47 may be long or contain Markdown-significant characters (e.g. a base64 blob or code). This makes the blockquote hard to read or renders it incorrectly in Obsidian.

## Assumptions

- A0: The skill runs on the day the application is submitted, so `applied` is the current date.
- A1: A newly created application's status is always `awaiting-reply`, and `recruited` is `false`.
- A2: Input JD files are plain text copied from a job posting page and include the application form's questions, in the shape of `sample-jd.txt`.
- A3: Existing notes are never renamed to normalize duplicate numbering. Only the new note's suffix is chosen.
- A4: Only the frontmatter keys in `_meta/Templates/Job Template.md` are emitted. Extra keys seen in older notes are not.
- A5: Linking questions to `Answers/` notes and updating `Questions/` notes stays manual.
- A6: The user runs Claude Code from the vault root, so the repo-local skill at `.claude/skills/dapplication/SKILL.md` is discovered.
- A7: "Within the last six months" means an `applied` date on or after the current date minus six calendar months.
