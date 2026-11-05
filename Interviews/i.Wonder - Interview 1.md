---
type: interview
application: "[[Applications/i.Wonder]]"
company: i.Wonder
round: 1
date: 2026-11-04 12:00 - 12:30
interviewers: Rob Godfrey
outcome: advanced
title: i.Wonder - Interview 1
date_created: "2026-11-04 18:10"
date_modified: "2026-11-04 18:10"
---

### Transcript

![[Transcripts/i.Wonder - Interview 1]]

### Questions

Model answers, not a record of what was said.

> Can you tell me about your previous experience in AWS and distributed systems, API infrastructure -- just the back-end layer?

```
Most of my recent AWS work is serverless. The backend for my Athena Math apps is API Gateway in front of Lambda. A request comes in with an Apple transaction, Lambda verifies it with Apple, and if it's valid I write the entitlement to DynamoDB. Those writes are idempotent -- a duplicate event is a no-op upsert on the same ID -- and they use conditional updates so an out-of-order event can't downgrade someone, like a stale subscription overwriting a lifetime purchase. Failures go to SQS for async retries, and to a dead-letter queue if they still can't be processed. It's all defined in a SAM template and deployed from GitHub Actions, and I've barely had to touch it since.

For clients, I've set up CloudFront in front of a private S3 bucket with origin access control for large paid downloads, and EC2 deployments.

My first real distributed system was at DataRank. I built the crawler framework: a MySQL-backed URL queue, and an orchestrator on each of four servers that locked rows off the queue and handed them to a pool of about a hundred workers. Then I built a sister framework for the social APIs, with a shared token pool, rate limiting, and backoff, so standing up a new source meant writing the API calls and nothing else. Later at Octimine I replaced a batch analytics job with Kafka Streams.
```

> Imagine Julius is executing a 40-step mission. It completes 25 steps, then a server crashes. How would you make sure it resumes from the correct point without repeating completed actions?

```
The mission's state can't live in the process that's running it. I'd keep a durable step log in Postgres: mission ID, step number, status, and the step's output. A step is only "done" when its completion is committed there.

When a worker picks up a mission, it takes a lease with an expiry and keeps renewing it with a heartbeat. If the server dies, the lease runs out, another worker claims the mission, reads the log, sees steps 1 through 25 are committed, and starts at 26. Completed steps never rerun, and because their outputs are stored -- including what the LLM returned -- we don't re-call the model and get a different answer.

The tricky one is step 26, the step that was in flight when it crashed. It may have half-happened. So every step that has a side effect gets an idempotency key, like mission ID plus step number, and either passes it to the external API or checks before acting -- does a PR for this branch already exist? -- so running it twice is safe.

I'd also look hard at Temporal before building this myself. Durable execution with replay is exactly what it does, and it's battle-tested.
```

> If Wonderland suddenly grows from 1,000 to a million users -- or say 100,000 -- how would you approach scaling the infrastructure without sacrificing reliability?

```
I'd split the system by what holds state, because each part scales differently.

The stateless API layer -- accounts, the marketplace, the wallet -- runs as containers behind a load balancer and autoscales on CPU and request rate. That part is easy.

The multiplayer worlds are stateful, so you scale them by sharding: each world or session lives on one game server, and a session directory routes players to the right one. Adding capacity means adding servers, not making one server bigger. For Unreal dedicated servers I'd look at something like GameLift rather than writing fleet management myself.

Julius missions go through a queue, and the workers scale on queue depth. Per-user quotas there protect both reliability and the inference bill.

The database is the usual bottleneck: managed Postgres, multi-AZ, connection pooling, read replicas, and caching for hot reads.

For reliability specifically: load-test past the target before each wave, roll out with canaries so a bad deploy hits a few percent of users, and degrade gracefully -- a waitlist or queue at the door beats the whole platform falling over. Your alpha and beta waves are a good fit for this, because each wave tells you where the next bottleneck is before it matters.
```

> If I gave you responsibility for making Julius' mission execution reliable, what would your first 30 days look like?

```
Week one is understanding and measuring. I'd map the mission lifecycle end to end, list every way it can fail -- a crash mid-step, a step running twice, a model or API timing out, rate limits, the reviewer rejecting work -- and add structured logs and metrics tagged with mission and step IDs. Then pick the number we're improving: the share of missions that finish without anyone stepping in.

Week two is durable state: missions as a state machine in Postgres, step checkpoints, worker leases so only one worker runs a mission at a time, and idempotency keys on every step with a side effect.

Week three is failure handling: timeouts on every step, retries with backoff and a retry budget, and a dead-letter state for missions that exhaust it, with the reason recorded so a person can resume or cancel it. Then I'd prove it with tests that kill a worker mid-mission and check that it resumes without redoing anything.

Week four is operations: alerts on the success rate and stuck missions, a dashboard, backups with a restore actually tested, and short runbooks.

By day 30 the goal is simple: a server can die in the middle of a mission and nobody notices.
```
