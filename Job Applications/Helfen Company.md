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
To be upfront: my agent system is a development workflow with me in the loop, not an unattended business operation. But I use it to ship real client work.

It's a chain of agent-agnostic skills: scope -> plan -> implement -> review.

- scope takes a loosely defined problem (mostly what the client said, plus my own interpretations and follow-up questions) and formalizes it into functional and non-functional requirements, constraints, assumptions, and risks.
- plan reads the scope and builds an implementation plan that covers every requirement and dependency.
- implement follows the plan step by step. It has to write a failing test before it changes code.
- review is a final check by another agent to make sure that each re

Coordination happens through files, not chat history. Each plan gets a `.agents/plans/{plan-name}/` directory in the project repo, holding the scope and the plan. Any agent can pick up where another left off, so I can send a harder problem to a more capable model and an easier one to a cheaper one. Durable decisions go into ADRs in the repo, and my global preferences live in one central file, so one project's context doesn't leak into another. Since it's all Markdown in git, people and agents read and edit the same thing.

The human checkpoints are scope and plan. Those take a lot of back-and-forth, but by implementation the hard questions are answered. I used it to build a Node.js app syncing a client's payment provider with Shopify. Since it was touching payments, it was imperative that my code was correct. Scoping surfaced ambiguities in the provider's API docs that I got resolved with the provider before writing code, and I rejected a hand-rolled SQL migration runner and config loader in favor of well-tested libraries. The client switched payment providers before their old contract ran out.

What I'd change: rules in prose only hold as well as the model follows them, so I'd move more of the deterministic parts into code from the start.

I've also built the same pattern for my job search: a chain of skills that assesses a job posting, creates the application note, drafts answers from my past answers and resume with every claim sourced, and files approved answers so the next draft can reuse them.

Most of my recent contract work has been Shopify: payment integrations, order automation in Shopify Flow, a returns-platform migration, and a multi-warehouse catalog design. I'd like to put the two together.
```
