---
type: job
applied: 2026-07-29
job_type: fulltime
recruited: false
status: rejected
source: matcha
interviews:
listing: https://jobs.Ashbyhq.Com/radai/0143d5f5-b1a4-4684-a9bd-763990f4ccf8
company: Rad AI
position: Staff Software Engineer, Reporting Integrations
contract: false
remote: true
compensation: $175K – $230K • Offers Equity
title: RadAI
date_created: 2026-07-29 10:28
date_modified: 2026-07-29 10:36
---

## Application

> Describe a concrete example from the last month where AI meaningfully improved your work (tool used + impact)

```
I built a scope->plan->implement->review cycle for developing new features or projects using skills. I copy the same skill files to Claude, Codex, and OpenCode, so it's an agent-agnostic workflow, one of its main advantages, since any agent can pick up where another left off. All data stored in a central directory.

I used it to build out a Node.JS app for a client's payment provider. The app needed to sync payment data between the provider and Shopify.  Since it was touching payments, it was imperative that my code was correct.

First, I give a rough overview of the problem to the agent in Markdown (mostly what the client said and my own interpretations/follow-up questions).

Then I run the `scope` skill, which helps formalize the problem into concrete functional and non-functional requirements. This usually requires a lot of back-and-forth with the model, but it helps me really understand the problem.

After scoping, I run the `plan` skill to start planning the implementation based on the requirements we landed on. This, too, usually requires a lot of back-and-forth.

Once we hit the `implement` phase, it's normally smooth sailing, since all the hard questions have already been addressed in scoping and planning.

For the payment integration app that I built, this cycle surfaced a number of ambiguities in the provider's API documentation, which I was able to bring up to the provider and client and have reconciled.

In the end, it was a complete success, and the client was able to switch their payment provider before their existing contract ran out. I now rely heavily on this flow for new projects. I'm still making refinements, though the core scope->plan->implement->review remains.
```
