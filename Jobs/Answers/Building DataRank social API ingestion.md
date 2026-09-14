## Ashby

Source: [[Jobs/Job Applications/Ashby]]

> Describe an interesting software abstraction you've built and or made major contributions to in a professional context.

> The abstraction should address a real-world problem, have a non-obvious solution, and necessitate an understanding of a complex system or technology. It doesn't have to be infrastructure-related; we're looking for your most impressive contribution here. We're open to personal projects if they are used in a professional context (e.g., OSS library used by companies).

> In our initial calls, we'll cover this in more detail, so please keep your response brief (~3 paragraphs maximum). Write enough detail so we can understand the problem and meet the requirements outlined above.

```
My first big greenfield software project was a framework for retrieving selected data from various social media APIs and normalizing the data into a common model for ingestion into our system.

The company I was working for, DataRank, was collecting data about what people were saying about certain products. A lot of this data came from social media. When I joined we had bespoke handlers for Facebook and Twitter, but they were error prone and not reliable. And we needed new handlers for other APIs.

The solution I came up with was distributed across 4 servers and had generic queuing logic, generic token pools, generic rate limiting and retry strategies, etc. This allowed us to quickly spin up new APIs like Pinterest and Instagram, and replaced Facebook and Twitter with a more resilient system.
```

## Openly

Source: [[Jobs/Job Applications/Openly]]

> Please briefly describe your experience with API management:*

```
At DataRank, I set up a distributed API manager to spin up generic API consumers for various social media APIs. It had a generic token pool, throttling, and SDK methods for consuming data.

At SimplyMeasured and SproutSocial, I was on the producer side of APIs, where I built APIs in Go and SpringBoot for various microservices. I also setup and maintained the API gateway to our backend, so consumers could have a unified interface to our various microservices.
```
