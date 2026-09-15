## Enveritas

[[Enveritas]]

> What are your favorite ways to learn about new trends and advancements in software development?

```
I keep up with the latest trends via HackerNews and engineering-focused Youtube channels like Dave's Garage or tscoding.

To actually learn new technologies or applications, there's no substitute for learning by doing. For example, my latest learning foray has been with Nix for fully declarative package management and config (basically IaC for your personal computer).  LLMs help a lot here having a 24/7 tutor available.

I also read engineering books.  Currently reading Designing Data-Intensive Applications. I've worked through a few of their examples and built a DB in bash and a graph DB in Postgres.
```

## Rivora

[[Rivora]]

> Tell us about the last time you had to get productive in an unfamiliar codebase or tool within a few days, not weeks. What was your actual approach?

```
I was working on a contract for Teletone, an audio software company. They had  some proprietary audio file downloads (up to 30GB) sitting in S3, randomly public via ACLs. They needed them locked down. But their stack was Next.js on Vercel, Firebase/Firestore, and a Shopify Liquid theme. I hadn't used any of that before!

My first step was to start exploring the code and understanding the tech. I asked Claude questions about the codebase, recent commits, and had it ask ME questions to make sure I understood the part I was to update.

I then started experimented with the tools (installing Vercel CLI, for example), pulling down the env vars, calling the Firebase API, etc. making sure to not run any write or delete commands. I'm a big believer in learning by doing.

After I had a good understanding of how everything fit together, I started on a plan that met all the client's requirements. I worked with Claude on this and we went through a few iterations before I was happy. For example, I wanted a seamless rollback if anything didn't work.  All existing infra and data stayed in place, so that a rollback was as simple as `git revert && git push` (e.g., all S3 URLs remained in Firestore).

Within five days of starting, I had migrated their content to a single S3 bucket with prefix-based access behind CloudFront (OAC and signed cookies) and made the frontend updates to use it.
```
