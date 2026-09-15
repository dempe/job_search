## Aescape

[[Aescape]]

> Please share your AI tools experience. E.g. Cursor, Claude Code, etc.

```
I use a variety of models -- mostly DeepSeek v4 and Opus 4.8.  I use the OpenCode harness.

As for how I actually use AI, I have a pretty detailed, constantly-evolving workflow that's really a chain of model-agnostic skills:

scope -> plan -> execute -> verify.  `scope` takes a loosely defined problem and turns it into a more formally defined problem in terms of functional and non-functional requirements, constraints, assumptions, and risks, and outputs `scope.md`.

The next phase is `plan`.  It reads `scope.md`, and builds an implementation plan in `plan.md`, making sure all requirements and dependencies are fullfilled.

There is a lot of back-and-forth with the AI on these first two phases, but it really helps narrow down *what* exactly we're trying to solve and *how* we will solve it.

Since so much time is invested in scoping and planning, the execution and verification phases usually go by pretty quickly, since we know exactly what we need to do by that point.
```

## BitMovin

[[BitMovin]]

> Tell me about a time you used AI to improve how you work. What tool did you use, what was the task, and what changed as a result?

```
I built a scope->plan->implement->review cycle for developing new features or projects using skills. I copy the same skill files to Claude, Codex, and OpenCode, so it's now an agent-agnostic workflow, one of its main advantages, since any agent can pick up where another left off. All data stored in a central directory.

The first project I used it on was to build out a Node.JS app for a client's payment provider. The app needed to sync payment data between the provider and Shopify.  Since it was touching payments, it was imperative that my code was correct.

First, I make a `.agents/plans/{plan-name}/` directory in the project root. In the plan folder, I add a rough overview of the problem in Markdown (mostly what the client said and my own interpretations/follow-up questions).

Then I run the `scope` skill, which helps formalize the problem into concrete functional and non-functional requirements. This usually requires a lot of back-and-forth with the model, but it helps me really understand the problem.

After scoping, I run the `plan` skill to start planning the implementation based on the requirements we landed on. This, too, usually requires a lot of back-and-forth.

Once we hit the `implement` phase, it's normally smooth sailing, since all the hard questions have already been addressed in scoping and planning.

For the payment integration app that I built, this cycle surfaced a number of ambiguities in the provider's API documentation, which I was able to bring up to the provider and client and have reconciled.

In the end, it was a complete success, and the client was able to switch their payment provider before their existing contract ran out. I now rely heavily on this flow for new projects, and I'm constantly making refinements, though the core scope->plan->implement->review remains.
```

## Ghost

[[Ghost]]

> How are you using AI in your day-to-day work right now? *

```
I use raw Claude Code.  I've found that batteries-included IDE solutions like Cursor are a bit too opinionated for my tastes.

A neat little trick I found is to have it repeat the contents of `CLAUDE.md` on every response to make sure that it stays in the context window - the few hundred tokens is `CLUADE.md` is nothing compared to the tokens spent writing code.

In fact, I feel like most "agentic hacks" revolve around properly maintaining its context window. I have guides for it on how to research problems I ask it to solve.  Always be sure to ask it to read back to you the contents of the guide it read.

I haven't written any custom MCP stuff yet, but I have some ideas that have been brewing.  One, for example, would be to call out to a smarter model if it gets stuck.  Another would be to produce its own guides/tutorials based on web searches for niche domains that it may not know very well.
```

## In Tandem

[[In Tandem]]

> Describe your AI-enabled development workflow, from ideation through release.<br/>
Please don't rely on it to write your responses for you - we're most interested in your own voice, experiences, and perspective. Trust us, it's surprisingly easy to spot AI-written answers.

```
I have a chain of constantly-evolving skills that I use: scope -> plan -> execute -> verify.  `scope` takes a loosely defined problem and turns it into a more formally defined problem in terms of functional and non-functional requirements, constraints, assumptions, and risks, and outputs `scope.md`.

The next phase is `plan`.  It reads `scope.md`, and builds an implementation plan in `plan.md`, making sure all requirements and dependencies are fullfilled.

There is a lot of back-and-forth with the AI on these first two phases, but it really helps narrow down *what* exactly we're trying to solve and *how* we will solve it.

Since so much time is invested in scoping and planning, the execution and verification phases usually go by pretty quickly, since we know exactly what we need to do by that point.
```

## RadAI

[[RadAI]]

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

## Rivora

[[Rivora]]

> Describe a specific time you used an AI coding assistant (Copilot, Cursor, Claude, ChatGPT, whatever you use) on a real task recently. What did it get right, and what did you have to fix or reject?

```
I recently used Claude Code to build out a Node.JS app for a client's payment provider. The app needed to sync payment data between the provider and Shopify. Since it was touching payments, it was imperative that my code was correct.

I use a scope->plan->implement->review cycle built from skills. First, I give the agent a rough overview of the problem in Markdown (mostly what the client said and my own interpretations/follow-up questions). The `scope` skill formalizes that into concrete functional and non-functional requirements, and the `plan` skill turns those into an implementation plan. Both require a lot of back-and-forth with the model, but it helps me really understand the problem.

What it got right: this cycle surfaced a number of ambiguities in the provider's API documentation, which I was able to bring up to the provider and client and have reconciled. Then, once we hit the `implement` phase, it was mostly smooth sailing, since all the hard questions had already been addressed.

What I had to fix or reject: Claude wanted to hand-roll a SQL migration runner and a config loader when libraries already exist for those things. I rejected both and had it use off-the-shelf solutions. It also started editing the implementation before any test existed, so I stopped it and made it write a failing unit test first, then fix the code until the test passed.

In the end, it was a complete success, and the client was able to switch their payment provider before their existing contract ran out.
```

## Starbridge

[[Starbridge]]

> Probably will ask something about "prompt engineering." it's mentioned in the job description and it appears their "AI proposal writer" makes heavy use of LLMs.

```
not sure what to say other than I'm a daily user of ChatGPT. i do have various custom prompts.  one I've used for therapy.  
```

## Theori

[[Theori]]

> How do you think AI is changing your role?

```
With AI, I feel like I'm focusing much more on the bigger picture while Claude or Codex write code, fix bugs, and setup dependencies and CICD.

For example, I'm a contractor. I get a lot of sometimes nebulous requests from clients. I have a whole project planning and implementation pipeline built in Claude skills (shared with Codex). We start by formalizing the problem to be solved in terms of functional and non-functional requirements, constraints, assumptions, risks. This normally requires a few passes and brings up a lot of questions for the client.

After that, we do the same for implementation planning. I then have a very clear idea of the scope and work required. I can then send an estimate to the client.

And after we have all this worked out, actually implementing the project is just following a sequence of steps laid out in the plan, sometimes requiring minor re-visits.

In short, with AI, I much more focused on defining the actual problem and planning solutions rather than actual implementation. I would have never imagined I'd be working like this 5 years ago.
```
