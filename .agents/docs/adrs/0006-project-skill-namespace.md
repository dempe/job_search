# 0006: Project skills use the `dj` prefix

## Context

The user's personal skills are namespaced `d` (`/dscope`, `/dplan`, ...), globally. This vault's own skills need a namespace of their own, so that typing `/dj` lists only the job-search skills.

## Decision

New skills in this project's `.claude/skills/` are named `dj` + a short name, for example `djd`, `djtrans`, `djfill`, `djq`.

## How to apply

Name any new skill in this project `dj<name>`, without being asked. Older skills (`dapplication`, `danswers`, `dmvanswers`) predate the convention. Leave them as they are unless the user asks for a rename.
