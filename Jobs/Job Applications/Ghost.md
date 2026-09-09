---
type: job
applied: 2026-02-19
interviews:
status: rejected
job_type: fulltime
source: 4dayweek
position: Senior Platform Engineer
contract: false
remote: true
4day: true
industry: publishing
website: https://ghost.Org/
location:
company_size:
recruited: false
listing: https://4dayweek.io/remote-job/senior-platform-engineer-AJcvL-ghost
blog:
correspondence:
compensation: $140,000 - $200,000
title: Ghost
date_created: "2026-02-17 15:33"
date_modified: "2026-02-24 13:04"
---

## Application

> What's one thing you'd improve about Ghost's developer experience, and why? *

```
Right now the install-from-source flow is decent, but it still relies on devs having the right Node/Yarn/Docker versions and a working local setup. Ghost already uses Docker for the backend. I think we could make this process a lot more deterministic by using Docker for the frontend as well. Then we could do things like...

- Pin Yarn version,
- Make `postCreateCommand` run `yarn setup`
- Provide tasks like:
  - "Start Ghost", which runs `yarn dev`
  - "Start Ghost Analytics", which runs `yar dev:analytics`
  - "Reset Data", which runs `yarn reset:data`
```

> Tell us about a tool or product you shipped that you're proud of. What made it great? *

```
I released my first app this summer. I've built basic websites before, but this was my first real deep-dive into the frontend. Working in Typescript/React Native taught me a lot about composibility/modularity, state management, and concurrency. Those are lessons that apply to backend work as well.

Speaking of backend, my app's backend is in AWS serverless (API Gateway, Lambda, DynamoDB, SQS), defined in a SAM template.  Infra as code is something I'm quite passionate about.

If you'd like to check out the app, here it is:  https://apps.apple.com/us/app/athena-math/id6747783222
```

> How are you using AI in your day-to-day work right now? *

```
I use raw Claude Code.  I've found that batteries-included IDE solutions like Cursor are a bit too opinionated for my tastes.

A neat little trick I found is to have it repeat the contents of `CLAUDE.md` on every response to make sure that it stays in the context window - the few hundred tokens is `CLUADE.md` is nothing compared to the tokens spent writing code.

In fact, I feel like most "agentic hacks" revolve around properly maintaining its context window. I have guides for it on how to research problems I ask it to solve.  Always be sure to ask it to read back to you the contents of the guide it read.

I haven't written any custom MCP stuff yet, but I have some ideas that have been brewing.  One, for example, would be to call out to a smarter model if it gets stuck.  Another would be to produce its own guides/tutorials based on web searches for niche domains that it may not know very well.
```

> What do you hope to find here, that you haven't found at current or previous jobs? *

```
Fulfillment.  I'm an amateur writer, so publishing is something I'm fond of, especially when the tools are open source.  This benefits everyone.  Also, being a writer, myself, lets me connect to the customers and understand their needs better. Ghost gives writers independence from algorithmic feeds, ad-driven incentives, and the whims of platform owners.  That's a mission I can get behind.
```

> What are your salary expectations (in USD)? *

```
$163,000
```
