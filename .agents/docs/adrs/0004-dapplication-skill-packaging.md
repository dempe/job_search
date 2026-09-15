---
title: dapplication is a repo-local, auto-invocable, instructions-only skill
status: accepted
superseded_by:
---

# Context

The user's other `d*` skills are global and managed by home-manager (`~/.config/home-manager/files/.claude/skills/`). `dapplication` only makes sense inside this Obsidian vault, because it depends on `Job Applications/` and `_meta/Templates/Job Template.md`.

The note needs a current local timestamp (`YYYY-MM-DD HH:mm`) for `date_created` and `date_modified`, which Claude Code doesn't otherwise know.

Plan: `auto-fill-applications` (FR0, FR1, NFR0, NFR1).

# Decision

- The skill lives in the repo at `.claude/skills/dapplication/SKILL.md`, versioned with the vault.
- It has no `disable-model-invocation`, so Claude may invoke it when a request matches its description, as well as via `/dapplication <path>`.
- It is a single Markdown instruction file with no scripts.
- The Bash tool is permitted only for `date "+%Y-%m-%d %H:%M"`. The six-month cutoff is computed by calendar reasoning, not by BSD- or GNU-specific `date` flags.
- Section comments carry `auto-fill-applications` task and requirement references for traceability.

# Consequences

- The skill is available only when Claude Code runs from the vault root. It isn't shared with other projects and needs no home-manager switch.
- Auto-invocation means a request like "log this application" can trigger note creation without the slash command. The duplicate check and the company and `listing`/`source` prompts still happen before anything is written.
- Behavior can only be verified by running the skill or by dry-running its rules, since there's no code to unit-test.
