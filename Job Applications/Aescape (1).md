---
type: job
applied: 2026-10-29
job_type: contractor
channel: recruited
contact:
status: interview
interviews:
- 2026-10-30 13:00 - 13:30
source: inbound
listing: https://jobs.ashbyhq.com/aescape/28f86607-2017-4a05-bc86-b196a0f34086
jd: "[[Job Descriptions/Aescape (1)]]"
company: Aescape
position: Senior Backend Engineer
contract: true
remote: true
compensation:
title: Aescape (1)
date_created: "2026-10-29 11:11"
date_modified: "2026-10-29 16:59"
---

## Application

Dan said that I did not have to submit a formal application, but I took a look at it anyways. Many of the questions have changed slightly since my last application or are net new.

I figured that it would be a good idea to have an answer to each, even though it's not necessary.

### Questions

> Please describe your most recent production Golang experience: what you built, roughly when, and for how long.

> Describe a third-party API integration you built and shipped in production.

> Please share your AI tools experience. E.g. Cursor, Claude Code, etc.

```
I mostly use Codex and Opus, but use DeepSeek for lighter weight stuff.  I use the OpenCode harness in addition to the TUIs for Opus and Codex.

As for how I actually use AI, I have a pretty detailed, constantly-evolving workflow that's really a chain of model-agnostic skills:

scope -> plan -> execute -> verify.  `scope` takes a loosely defined problem and turns it into a more formally defined problem in terms of functional and non-functional requirements, constraints, assumptions, and risks, and outputs `scope.md`.

The next phase is `plan`.  It reads `scope.md`, and builds an implementation plan in `plan.md`, making sure all requirements and dependencies are fullfilled.

There is a lot of back-and-forth with the AI on these first two phases, but it really helps narrow down *what* exactly we're trying to solve and *how* we will solve it.

Since so much time is invested in scoping and planning, the execution and verification phases usually go by pretty quickly, since we know exactly what we need to do by that point.
```

> Why Aescape?

## Interview 1

### Preparation

#### Stories

Dan mentioned that he wants to hear about my recent contracting work, so I better make sure I have those stories down pat.

##### Payment Integration App

##### Interactive Customer Map App

##### Athena Math (Focusing on Infrastructure)
