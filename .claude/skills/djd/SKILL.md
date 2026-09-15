---
name: djd
description: Evaluate the job description in `./jd.txt` against the user's experience. Summarizes the role, calls out noteworthy details, lists strong fits and gaps, and gives a candid hiring-manager verdict, then creates the application note with `dapplication`. Use when the user wants a JD assessed or asks whether they're a fit for a role.
argument-hint: <source> <listing-url>
---

# Job Description Assessment

Read `./jd.txt`, assess the role against the user's experience, then hand off to the `dapplication` skill to create the application note.

The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as described in RFC 2119.

Follow the steps below in order.

## Constraints

- The assistant MUST use only Claude Code's built-in tools (Read, Bash for read-only `ls`, and Skill). It MUST NOT write or run scripts.
- This skill MUST NOT create or modify any file. The only file created in the run is the application note, and `dapplication` creates it.
- Every claim about the user's experience MUST be backed by the sources in Step 2. The assistant MUST NOT invent or inflate experience, and MUST NOT count a skill as a fit just because it is adjacent to one the user has.
- The assessment MUST be candid. It MUST NOT flatter the user or soften real gaps.

## Output

- The only text this skill writes to the user is the assessment in Step 4.
- The assistant MUST NOT narrate, give progress updates, or add anything before or after the assessment.

## Step 1: Read the JD

- Read `./jd.txt` (relative to the vault root).
- If it does not exist, cannot be read, or is empty, the assistant MUST STOP with one line saying so. It MUST NOT invoke `dapplication`.

## Step 2: Read the user's experience

Read all of these:

- `../resume/resume.yaml`: the source of truth for jobs, dates, bullets, skills, projects, certifications, and education. Include every bullet, whatever its `resume-type`, including `resume-type: []`. Compute years of experience as the file's comments describe: current year − `career_start` − `career_gap_years`.
- Every note in `Answers/`: the user's own accounts of projects, preferences, work style, and constraints. Pay particular attention to:
  - `Work authorization and availability`: where the user works from, which matters for location and time-zone restrictions
  - `Engineering values and deal-breakers`
  - `Preferring backend engineering`, `Seeking engineering growth and meaningful work`, `Seeking mission-driven work`: what the user wants
  - `Salary expectations`

If `../resume/resume.yaml` is missing, continue with `Answers/` alone and say so in one line at the top of the assessment.

## Step 3: Analyze

- **Requirements.** Separate the JD's hard requirements (years, required skills, certifications, location, clearance) from nice-to-haves.
- **Sponsorship.** The user is a US citizen, so visa sponsorship and work authorization are irrelevant. The assessment MUST NOT mention them.
- **Noteworthy details.** Look for anything a candidate should know before applying, for example:
  - no salary listed, or a salary range below or above the user's past expectations
  - contract vs. full-time, or a contract-to-hire path
  - location or state restrictions, time-zone requirements, on-site or travel expectations
  - a security clearance requirement
  - on-call, equity, company stage, team size, or funding signals
  - unusual application steps: puzzles, AI-detection instructions, required cover letters, word limits
  - red flags: vague scope, unrealistic requirement lists, mismatched title and responsibilities
- **Fits.** For each strong fit, name the JD requirement and the specific evidence: the employer and what the user did.
- **Gaps.** For each gap, name the requirement and say whether it is:
  - **missing**: no evidence at all
  - **partial**: related but weaker experience (e.g. Go at SimplyMeasured a decade ago vs. "real fluency in Go")
  - **unclear**: the sources don't say either way
- **Preferences.** Note where the role matches or conflicts with what the user says they want or won't do (backend vs. full-stack, remote, mission, growth, deal-breakers).

## Step 4: Write the assessment

Write the assessment in this structure, using Markdown headings and bullets. Keep it tight: short bullets, no filler.

```markdown
## {Company} — {Role}

### Summary
2–4 sentences: what the company does, what the role is, and what they're really looking for.

### Noteworthy
- ...

### Fits well
- **{JD requirement}** — {evidence}

### Gaps
- **{JD requirement}** ({missing | partial | unclear}) — {explanation}

### Verdict
**{Yes | Lean yes | Lean no | No}** — As the hiring manager, ...
```

The verdict MUST:

- answer the question "if you were the hiring manager for this role, would you hire this candidate?" directly, in the first sentence
- give the two or three deciding reasons
- say what would most likely sink the application (e.g. a hard requirement the user doesn't meet) and, if applicable, what to emphasize in the application to offset it

## Step 5: Create the application note

- Immediately after writing the assessment, invoke the `dapplication` skill with the Skill tool.
- Pass this skill's arguments through unchanged as `dapplication`'s arguments (the source and listing URL). Do not add a JD path; `dapplication` defaults to `./jd.txt`.
- From this point, follow `dapplication`'s instructions, including its output rules. Do not add any text after the assessment.
