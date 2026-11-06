# 0011: One folder per application

## Context

An application's files were spread across four top-level folders: the application note, its JD, its interview notes, and their transcripts. Everything about one application belongs together.

## Decision

Every application, including one with nothing but its note, has a folder in `Applications/`:

```
Applications/
  _MOC Jobs.md
  {title}/
    {title}.md            application note
    jd.md                 saved JD (ADR 0008)
    Interviews/
      {n}/
        {n}.md            interview note (ADR 0010)
        transcript.md     raw transcript (ADR 0009)
        transcript-processed.md  speaker-labelled transcript (ADR 0012)
```

- `{title}` is the application's title, e.g. `People Data Labs` or `Aescape (1)`. The folder and the note share it.
- The other names (`jd.md`, `{n}.md`, `transcript.md`) repeat in every folder, so links and embeds to them always use the full vault path, e.g. `![[Applications/People Data Labs/Interviews/2/transcript]]`.
- The application note alone keeps a vault-unique name, so short links like `[[People Data Labs]]`, used by every `Answers/` section, keep resolving. Links that a skill writes still use the full path, e.g. `application: "[[Applications/{title}/{title}]]"`.

## How to apply

- To create an application, use `djapplication`. It creates the folder, the note, and `jd.md`. To add an interview, use `djinterview`. Don't create these files by hand.
- Queries over applications use `FROM "Applications"`, which includes subfolders. Filter by frontmatter (`type`, `status`) to tell application notes from interview notes. JDs and transcripts have no frontmatter.
- An application's duplicate check matches folder names: `{Company}` or `{Company} ({n})`.
