---
type: job
applied: 2026-09-14
job_type: contractor
channel: form
status: rejected
interviews:
  - 2026-09-18 14:00
source: wellfound
listing: https://wellfound.com/jobs?job_listing_slug=4697979-backend-engineer-5-8-years
company: Rivora
position: Backend Engineer (5-8 years)
contract: true
remote: true
compensation: $135k – $177k • No equity
title: Rivora
date_created: "2026-09-15 10:58"
date_modified: "2026-09-28 18:07"
---

## Application

> Tell us about the last bug you fixed where a type system, type annotations, or a linter caught something before it reached users. What was the bug, and what would have broken if it had shipped?

[[Catching type drift in the payments app#Rivora|Catching type drift in the payments app]]

> Describe a specific time you used an AI coding assistant (Copilot, Cursor, Claude, ChatGPT, whatever you use) on a real task recently. What did it get right, and what did you have to fix or reject?

[[AI-assisted development workflow#Rivora|AI-assisted development workflow]]

> Tell us about the last time you chose between an existing library/package and writing something yourself for the same problem. What did you pick, and why?

[[Choosing between libraries and custom code#Rivora|Choosing between libraries and custom code]]

> Describe a time you had to work across two systems where one side didn't fully control the other, an API you didn't own, a data format shared with another service, anything like that. What broke or almost broke?

[[Building the wholesale customer map#Rivora|Building the wholesale customer map]]

> Tell us about the last time you had to get productive in an unfamiliar codebase or tool within a few days, not weeks. What was your actual approach?

[[Learning new technologies#Rivora|Learning new technologies]]

## Interview 1

### Transcript

![[Transcripts/Rivora - Interview 1]]

### Questions

Model answers, not a record of what was said.

> Walk me through the languages and frameworks you feel most comfortable with, and what you've used in the last four or five years day to day. I know you've done a lot of consulting and played with different technologies, so walk me through your go-to tools and frameworks.

```
My deepest experience is Java and Python. Java is what I built the data ingestion framework at DataRank in, the microservices at SimplyMeasured, and the Kafka Streams pipeline at Octimine.

The last four or five years have been mostly Node and TypeScript. My consulting work is largely greenfield Node services -- the most recent was payment middleware between a Shopify store and a payment gateway -- plus React and React Native on the front end. Postgres is my default database, and everything I build runs on AWS.

For frameworks: Spring Boot when I'm in Java, Express for Node services, Prisma for Postgres access lately. I also have professional Go and Ruby experience, but it's about a decade old, so I'd call that a foundation rather than current fluency.
```

> If you worked with something ten years ago, what does that actually mean today? What's your process to go back to something you've worked with a decade ago?

```
It means I know the shape of the language and I've lost the details -- the idioms, the standard library, the tooling that's appeared since.

My process is to build something real in it as quickly as possible. I'll do a few small exercises to get the syntax back in my fingers, but that only gets you the basics. What actually works is taking a real slice of the system and shipping it: set up the toolchain, the formatter, the linter, the test runner, and let them correct me, because that's where a language's conventions live.

Then I read code written by people who know it well, and I ask for tough code review early. With Go I'd expect to be useful in a week and unremarkable in a month. The concepts transfer -- concurrency, types, deployment -- it's the local conventions that take the time.
```

> And do you feel like you want to work with these languages?

```
Yes, Go especially. It's typed, which matters a lot to me -- I want the compiler catching my mistakes before a user does -- and it's a small language, so a team can agree on how to write it instead of arguing about it. The concurrency model fits the kind of data-heavy services I like building.

I'm happy to work in Ruby too. Rails gets a product moving quickly, and if that's where the business logic lives today, that's where I want to be. What appeals to me about your stack is that it's Rails now and Go later, so there's a migration to help drive rather than just maintenance.
```

> Tell me about a time you built something that was good enough for now and it turned out to be the wrong call. Walk me through why and how, and what you learned about when not to cut corners.

```
I was securing large audio file downloads for an audio software company. The files were sitting in S3, publicly accessible, and they needed them locked down to paying customers.

There are two ways to do that with CloudFront: pre-signed URLs, which are quick to implement, or signed cookies, which are more work. I shipped pre-signed URLs first, because they were simpler and the client wanted something running.

That was the wrong call, and the reason is instructive: a pre-signed URL is a bearer token sitting in the address bar. Anyone who has the link has the file. The whole point of the project was that these downloads shouldn't be shareable, so I had optimized for delivery speed on the one requirement that wasn't negotiable. We went back and did it with signed cookies.

What I took from it: cutting a corner on how something is built is usually fine, and you can revisit it. Cutting a corner on the property the project exists to provide is not, because the shortcut doesn't just cost you rework -- it ships something that looks finished and isn't.
```

> But don't you charge more if you spend more time? Aren't you incentivized to build the more complex solution?

```
You would think so, but it works the other way. I want the next project from that client and the referral after it, and neither comes from billing hours slowly. It comes from them telling someone I got it done.

There's also competition. If someone else can deliver in half the time, my incentive to pad the schedule is worth nothing.

The same logic is behind why I'm applying here. Project work is great for variety and autonomy, but clients mostly want the thing as fast as possible -- they aren't paying for the long-term maintainability that I think is a big part of good engineering. I'd rather own systems I have to live with.
```

## Follow-Up

```
Hi Vera,

Thanks again for speaking with me last Friday. It sounds like you guys have a great product and a great team.

I just wanted see if there were any updates.  I'm still very interest in the role, so please let me know!

Thank you,
Chris
```

## Rejection

```
Hi Chris, thank you so much for following up.
After some careful consideration, we have decided to move forward with other candidates whose skills are more closely aligned with our current needs. However I'd love to stay in touch, and will happily reach out as more roles become available.
Wishing you the best!
Vera
```

### Follow-up

```
Hi Vera,

Thanks for letting me know.  That is totally understandable.

I'd definitely be happy to stay in touch. Any future senior backend opportunities related to in Java, Python, Node.js, AWS, distributed systems, and/or event-driven architectures may be a closer fit!

Wishing you and the team the best.

Chris
```
