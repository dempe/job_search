## 365 Member Access

[[365 Member Access]]

> Have you ever had to manage an emergency or a big outage or anything like that? Something high stress.

```
Yes. The one that stands out is at Octimine. We had a weekly Python batch job that processed around 30 million documents, and it was fragile. A couple of times it kept failing and retrying until it ran into the next week's job. That meant customers weren't getting their data.

In those situations, I try to stay as calm as possible. Getting stressed doesn't solve the problem. It just makes it take longer. So I isolate the issue and sort out what we actually know from what we're assuming, and work from the facts. I'm also big on communication in these scenarios and do my best to keep everyone informed until the problem is resolved.

Once it's fixed, I do a root-cause analysis and document the incident and how to recover from it, so if it ever happens again, anyone on the team can handle it. At Octimine, that turned into a whole set of recovery documentation, and it cut down on recurring on-call incidents. The long-term fix was replacing the batch job with a Kafka Streams pipeline with a dead-letter queue, so one bad document couldn't take the whole run down.
```
