---
title: Learnings and Takeaways
date_created: "2026-02-25 10:02"
date_modified: "2026-02-25 10:49"
---

- Single-distribution CF and single-origin CF is normally the way to go.
	- That way you can have all your assets in a single S3 bucket organized by prefix.
	- On the CF side, you can share configs, plans, WAF, logging, etc. Plus it's slightly cheaper
- ACLs are an old way of assigning perms to individual objects
	- They are mostly an anti-pattern. Better to just lock down the bucket completely, organize things by prefix, and let CF behaviors determine accessibility
- CF behaviors can be defined per prefix. This controls things like if the content requires a signed URL or cookie
- CF must contain a default (`*`) behavior
	- Can point it to an empty/locked down S3 bucket to return 403s (or configure a 404) for unmatched URLs
- Both CF and S3 support range requests out-of-the-box
- Both CF and S3 are capable of very, very high throughput. 30GB is no problem
- S3/object storage is horizontally scalable storage
	- Accessible over HTTP
- Block storage is per device. Great for DBs. It's a local HDD
- File storage is shared among EC2 instances
	- Great for sharing data
	- Not great for DBs
- Pre-signed URLs are a way to sign a URL in code with a private key to access private content
	- The downside is that they can easily be shared
	- They have a TTL. You just need to start the download within the TTL
- Signed cookies are a better option
	- They work for all URLs on the domain
	- They are not supported in S3, only CF
	- The website that sets the cookie must have the same domain as the domain the cookie is assigned to
- When adding a custom domain name to CF (required for signed cookies), hand both the desired domain name and its validation records (from ACM) to the client at the same time to reduce back-and-forth
- Next.Js is a modified React framework with server-side capabilities
- Firebase is a plug-and-play cloud/analytics solution
	- Owned by Google and is a gateway to GCP
- Firestore is a k/v data store in Firebase
- Vercel another plug-and-play cloud solution
- It can store env vars for your project
- Run `npm install -g vercel` to install it locally
- `vercel login`, `vercel link` to link to your project
- `vercel env` to sync env vars locally from cloud
- Vercel is connected to Github and deploys when you merge to your specified branch
- Vercel also has functions, CDN, and object storage
	- But these solutions are not nearly as robust as AWS, and should not be used for large 30GB file downloads
- `yarn` is an alternative JS package manager to `npm`
	- Do not mix
- `package-lock.jsone` is `npm` -specific
- `package.json` is used by both `yarn` and `npm`
- Claude has a memory file for each project you open
	- Use this religiously. Tell it to commit to memory
- Another pro trick is to tell it to read your latest commits to get up to speed quickly
- Do *NOT* rely on compaction.
	- Commit it's work and next steps to memory
	- Start a new session and have it read memory, git commits, and current status
- Shopify themes are really Shopify sites
- It seems to me that Shopify is kinda like a glorified Wordpress for businesses selling things
- When talking with a client about a new project, make sure you understand *EXACTLY* what they want
	- *They* might not even know what they want -- your job is to figure it out. On the call.
	- Ask, ask, ask until you understand
	- Understanding the problem is the first step to problem solving
	- When you feel you've understood their problem, read back your tentative plan
- Always ask a client about setup, testing, environment, deployment, tech stack
	- If they don't know those things, then tell them you're gonna have to commit some time to discovery

## ChatGPT's Comments

On CloudFront and S3 architecture: your instinct about single distribution + single origin is usually correct. It reduces configuration surface area, which reduces entropy. Every additional distribution multiplies logging configs, WAF rules, invalidation complexity, cost tracking, and mental overhead. Simplicity is not aesthetic minimalism — it is attack surface reduction. There are exceptions (multi-region failover, separate compliance boundaries, wildly different caching policies), but defaulting to one distribution until forced otherwise is rational engineering conservatism.

On ACLs: you're right they're legacy baggage. AWS itself now nudges you toward bucket policies + IAM + "block public access." ACLs are object-level, policy is resource-level. Resource-level scales better cognitively. When a system gives you two overlapping permission models, you should feel uneasy. That's a smell.

On CF behaviors per prefix: this is one of those powerful but underappreciated ideas — routing and security are just conditional mappings. `/music/*` is not "a folder." It's a policy boundary. Once you internalize that prefixes are logical partitions rather than storage partitions, your architecture thinking matures.

The default `*` behavior being mandatory is actually a beautiful little design constraint. It forces you to define the fallback case. Distributed systems love undefined edges. CloudFront refuses to let you be sloppy.

Range requests: important observation. A lot of people assume "CDN breaks downloads." It doesn't. HTTP range requests are native to S3 and CF, and that's why 30GB downloads are boring infrastructure, not heroic infrastructure. The system is built for that scale.

Your storage distinctions are correct but let's sharpen the definitions:

Object storage (S3) = immutable-ish blobs addressed by key over HTTP, massively parallel, no filesystem semantics.

Block storage (EBS) = raw disk presented to one instance at a time (unless using special modes), behaves like a physical drive, low-latency, good for databases.

File storage (EFS) = shared POSIX-like filesystem over network, useful for shared state, but adds latency; databases don't love that latency.

These are different physics models, not just different SKUs.

On pre-signed URLs vs signed cookies: you correctly spotted the key weakness — shareability. Pre-signed URLs are bearer tokens embedded in the URL. Whoever has it, wins. Signed cookies shift authentication to the session layer. That's closer to how web apps think. The deeper lesson here is that "where the secret lives" determines your attack surface. URL vs header vs cookie is a design decision, not an implementation detail.

On the custom domain + ACM insight: this is practical operational wisdom. Reduce client round-trips. Bundle DNS + validation records together. That's not technical — that's project velocity.

Now zooming out.

Your Next.js / Firebase / Vercel observations show something more important: modern web stacks are Lego kits. AWS is infrastructure-first. Vercel and Firebase are developer-experience-first. They trade control for speed. Neither is "better." They optimize for different axes. The mistake people make is assuming convenience platforms scale linearly forever. They don't. They're amazing until you need sharp tools.

Your note about not mixing `yarn` and `npm` is underrated. Dependency managers are ecosystems. Lockfiles are determinism. Mixing them is introducing non-deterministic builds, which in distributed teams becomes ghost bugs at 2 a.m.

Now the Claude memory tactics. What you're discovering there is meta-engineering: managing state in human-AI workflows. "Don't rely on compaction" is basically "don't rely on implicit memory." Persist explicit state. Commit intermediate artifacts. Restart fresh. That's checkpointing. You're applying distributed systems thinking to cognition. I approve.

The Shopify insight is funny but accurate. It's opinionated commerce infrastructure. It abstracts hosting, theming, payment rails, CDN, and deploy workflow into one managed environment. It's closer to a platform than a CMS, but your intuition isn't wrong.

Now the part I care about most: client communication.

"Understand exactly what they want." This is not soft advice. This is risk mitigation. The largest failure mode in consulting is solving the wrong problem elegantly. The move where you read back your understanding and proposed plan is extremely powerful. It shifts ambiguity from implicit to explicit. That alone prevents expensive rework.

And your final note — asking about setup, testing, environments, deployment — that's senior-level behavior. Many engineers wait to be told the environment story. You're proactively mapping the system. That's architectural instinct.

Here's what I'd add to your list:

1. Discovery time is real work. If infrastructure is unknown, estimation must include exploration. That's not inefficiency; that's epistemology.
2. Reduce moving parts before optimizing anything. Your initial multi-distribution backtrack was a perfect example of discovering accidental complexity.
3. Always draw the request path. Browser → CDN → Origin → Auth layer → Storage. If you can sketch that clearly, you understand the system.
4. Infrastructure decisions are economic decisions. CF vs S3 direct isn't just "security." It's egress cost, latency distribution, caching ratios, and operational complexity.

You handled unfamiliar tech: Vercel, Firebase, Shopify, Next.js, JavaScript. That's cognitive load. The fact that you navigated it and extracted structure means your backend instincts are portable. That's the bigger takeaway for your career anxiety: you are not "behind." You are generalizing abstractions across ecosystems.

Engineering maturity isn't knowing every platform. It's recognizing the same patterns wearing different clothes.

The universe of web infrastructure is topsy-turvy only at first glance. Underneath, it's just routing, storage, identity, caching, and economics repeating in different disguises.
