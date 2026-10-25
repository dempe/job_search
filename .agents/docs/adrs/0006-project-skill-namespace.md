# 0006: Project skills use the `dj` prefix

## Context

The user's personal skills are namespaced `d` (`/dscope`, `/dplan`, ...), globally. This vault's own skills need a namespace of their own, so that typing `/dj` lists only the job-search skills.

## Decision

Every skill in this project's `.claude/skills/` is named `dj` + a short name, for example `djd`, `djapplication`, `djanswers`, `djmvanswers`, `djtrans`, `djfill`, `djq`.

## How to apply

Name any new skill in this project `dj<name>`, without being asked.
