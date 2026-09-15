this repo contains tracking history for various job applications over the years.  it uses markdown.  i edit it in oblivion, which allows for rich linking between notes. all job application notes have YAML frontmatter for metadata about the job i'm applying to (example provided below).

i've recorded nearly every question on job applications in standard markdown format:

> question

```
answer
```

i've recently used another AI agent to parse these into an explicit answer note type in order to improve retrievability.  job application questions now link back to the corresponding answer note.

i would like to create a claude code skill, `dapplication` that does the following:

- take a specified `jd.txt` as input (see this plan's directory's `sample-jd.txt` for an example).
- create a job application note under `./Job Applications` (append a increasing number like `(1)` if an application for this company already exists in  the directory.
- otherwise, application note title/filename should be the name of the company.
- fill out the new application note's YAML frontmatter with data from `jd.txt` (see `./_meta/Templates/Job Template.md` for an example frontmatter).
- parse all non-trivial questions from `jd.txt`.  for example, visa questions, salary questions, should *NOT* be included.  all non-trivial questions should be added to the application note using the markdown question/answer convention above.  fill out `> question`, but leave the answer block empty for now.

NOTE: your job for this project is to simply produce a SKILL in markdown that i can re-use to run claude code for this purpose.
