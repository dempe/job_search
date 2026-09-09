---
type: job
applied: 2026-08-04
job_type: fulltime
recruited: false
status: rejected
interviews:
source: matcha
listing: https://jobs.Ashbyhq.Com/ashby/0f5dbf59-687b-4d88-88a7-73ee0a66b48
company: Ashby
position: Staff Platform Engineer - Americas
contract: false
remote: true
compensation: $232K – $270K • Equity
title: Ashby
date_created: 2026-08-04 21:41
date_modified: 2026-08-04 21:58
---

## Application

> Describe an interesting software abstraction you've built and or made major contributions to in a professional context.

> The abstraction should address a real-world problem, have a non-obvious solution, and necessitate an understanding of a complex system or technology. It doesn't have to be infrastructure-related; we're looking for your most impressive contribution here. We're open to personal projects if they are used in a professional context (e.g., OSS library used by companies).

> In our initial calls, we'll cover this in more detail, so please keep your response brief (~3 paragraphs maximum). Write enough detail so we can understand the problem and meet the requirements outlined above.

```
My first big greenfield software project was a framework for retrieving selected data from various social media APIs and normalizing the data into a common model for ingestion into our system.

The company I was working for, DataRank, was collecting data about what people were saying about certain products. A lot of this data came from social media. When I joined we had bespoke handlers for Facebook and Twitter, but they were error prone and not reliable. And we needed new handlers for other APIs.

The solution I came up with was distributed across 4 servers and had generic queuing logic, generic token pools, generic rate limiting and retry strategies, etc. This allowed us to quickly spin up new APIs like Pinterest and Instagram, and replaced Facebook and Twitter with a more resilient system.
```

## Rejection

They actually sent a useful rejection email.  Stings even more that they didn't want to talk to me.  Sounds like a great company.

```
Hey Christopher!

Thanks a lot for applying to the Staff Platform Engineer - Americas role.

We've reviewed your background, and right now, we don't see an ideal fit for this position. This rejection simply means we couldn’t get the signal we needed from your resume and application to feel there was a fit — it is by no means a rejection of your skills and experience in general.

We have a high applicant volume and a relatively small team to review them. So, we can’t provide feedback about your specific resume or application, but we can give some reasons we commonly reject folks. These reasons may not apply to you, and they’re not the only reasons we reject folks, but we’re sharing them in the off-chance they help you:

-   More than 2 years of tenure at the same place - It's important for our Engineers to have experienced the consequences of their decisions, iterated based on those consequences, and honed their judgment for future decisions. We believe the outcomes of the most challenging engineering work sometimes take years to shake out.
    
-   Experience developing products outside of a consulting or agency environment - Our engineers make product decisions and are highly user-focused here at Ashby, We believe consulting environments do not encourage the strong sense of ownership that is needed to succeed here. We also favor profiles that worked on full products, versus internal tools, research teams, and teams working on a technology component with no end-to-end workflow.
    
-   Experience outside of infrastructure - We believe that SREs do their best when they understand the broader context of the engineering team and also have the ability to just into application code and make changes.
    
-   Experience in an early-stage startup that is fast-paced - For understandable reasons, the product cycle tends to be longer at larger companies and every feature released requires more research and consensus. At Ashby, one of our strengths in the market is how fast we ship features, and we do this by removing blockers from engineers and relying on them to maintain a solid pace. We hire engineers who have proven they can thrive in that environment.
    
-   Description of individual contributions that is specific - This is an individual contributor role, and while we love hiring people who have leadership experience, we need to see sufficiently specific depiction of what you've done personally to assess the impact of it. Resumes with vague verbiage, such as "achieved performance improvements" are difficult to assess. In that example, we would need an extra line explaining exactly how you did that.
    

We’re happy to reconsider you for the role in the future, but please note that we have application limits that limit how quickly you can reapply.

Thanks for considering Ashby and for taking the time to apply. We really appreciate your interest!

Ashby Hiring Team
```