---
type: job
applied: 2026-10-26
job_type: fulltime
channel: form
contact:
status: awaiting-reply
interviews:
source: wellfound
listing: "https://wellfound.com/jobs?job_listing_slug=4867200-e-commerce-automation-operations-engineer-clone"
company: Helfen Company
position: AI Agent Systems Builder — E-Commerce Operations & Automation
contract: false
remote: true
compensation: $80,000–$120,000 depending on experience
title: Helfen Company
date_created: "2026-10-26 16:57"
date_modified: "2026-10-26 16:57"
---

## Application

> In the "What interests you about working for this company?" box, please describe an AI agent system you've built that runs in production — see the last section below for details.<br/>
> Please include with your application<br/>
> Describe an agent system you've built that runs in production. What does each agent do, and how do they coordinate? How is memory and context stored, and how is it shared between agents and between people? What would you change if you built it again? Links, demos, or diagrams are welcome.<br/>
> What interests you about working for this company?

```
To be upfront: the agent system I run daily is a personal one, not an unattended business operation. It runs my job search end to end, with me reviewing everything before it goes out.

It's a chain of Claude Code skills (agent-agnostic, so Codex or OpenCode can run them too):

- djd reads a job description and writes a candid fit assessment, using only my resume and my past answers as evidence.
- djapplication creates the application note: metadata, a duplicate check against anything I applied to in the last six months, and the form's questions.
- djanswers drafts each answer from my past answers, resume, client project notes, and past agent conversations. Every claim has to be backed by a source, and it reviews its own drafts against a rubric before writing.
- djmvanswers files approved answers verbatim into topic notes, leaving a backlink, so the next draft can reuse them.
- djtrans turns interview transcripts into the questions I was asked, with model answers to study.

Coordination is simple: each skill hands off to the next, and they share state through files, not through a chat history.

Memory is plain Markdown in a git repo (an Obsidian vault), which is what makes it shareable between agents and people. I read and edit the same notes the agents do. Project decisions live in ADRs in the repo, and global preferences live in one central file, so context for one project doesn't leak into another.

What I'd change: rules written in prose only hold as well as the model follows them. When I needed a random practice question, I moved the picking into a script, because a model's "random" isn't random. I'd push more of the deterministic parts into code from the start. I also added the review rubric only after a draft came out generic, so I'd build the review step in on day one.

On the e-commerce side, most of my recent contract work has been Shopify: payment integrations, order automation in Shopify Flow, a returns-platform migration, and a multi-warehouse catalog design. I'd like to put the two together.
```
