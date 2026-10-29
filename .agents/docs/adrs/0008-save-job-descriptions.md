# 0008: Save each job description alongside its application note

## Context

`./jd.txt` is overwritten by every new JD, and job postings disappear once a role closes. Interview prep, later `djanswers` runs, and questions about hiring trends all need the JD after it's gone.

## Decision

- `djapplication` copies the JD byte for byte to `Job Descriptions/{title}.md`, where `{title}` is the application note's title (e.g. `Aescape (1)`).
- Application notes link to it in a `jd` frontmatter key, right after `listing`: `jd: "[[Job Descriptions/{title}]]"`. The key is part of `_meta/Templates/Job Template.md`, so the link is part of the schema.
- JDs live in their own folder, not in the application note, so their quotes and lists aren't mistaken for Q/As by `djq`, `djmvanswers`, or `djtrans`.

## How to apply

- To look up a role's JD, follow the note's `jd` link. Notes created before this decision have no `jd` key and no saved JD.
- Skills that need the JD for an existing application should read the linked file rather than `./jd.txt`, which may hold a different company's JD.
