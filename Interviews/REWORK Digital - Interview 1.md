---
type: interview
application: "[[Job Applications/REWORK Digital]]"
company: REWORK Digital
round: 1
date:
interviewers:
outcome: rejected
title: REWORK Digital - Interview 1
date_created: "2026-11-04 18:10"
date_modified: "2026-11-04 18:10"
---

They accepted my application, but their "interview" was just a series of questions that I had to write an answer for. Seems like companies are getting lazier and lazier with all the advantage they have right now — Loom videos, essays, etc. No one actually wants to sit down and interview anymore.

```
Hi Hannah,

Sure thing! Here are my answers:

System Design:

At my previous company, Octimine, they had a weekly batch job that ran for at least two days. Sometimes it would even overlap with the next week.

I suggested we migrate to a real-time, even-driven system (data was coming in continuously anyways). We were debating between Airflow and Kafka. I suggested we use Kafka, since we were processing a lot of analytics and Kafka Streams directly supports analytics processing.

After the migration, customers were able to see data in real-time as opposed to waiting a week. Moreover, we had a much nicer suite of unit tests for all of our analytics and clearly documented code. That, in addition to structured logging, monitoring, alerting, and CICD with deployment via Docker containers, meant we spent way less time babysitting the system and more time building new features. Both my manager and our customers were happy.

Error Handeling:

Design for failure, and assume all steps will eventually fail.

The first thing I'd do is place a message queue in between each step to decouple producers and consumers. This allows producers and consumers to communicate asynchronously, and eliminates failed requests from slow connectoins. For example, the agent can fire and forget a message to the message queue. The CRM or another program polls the queue and retrieves the accumulated messages, processes them, and sends back a message to another queue, which the agent then polls from.

For rate limits specifically these usually return a HTTP 429 error code and have specific rate-limit headers set. The key would be to process these headers and apply an appropriate back-off strategy for retrying them (exponential backoff is the usual go-to).

Requests that timeout can be sent to a dead letter queue (DLQ) after a certain amount of time. They can later be retried up to a certain point. Set a limit on the number of retries. When that limit is hit, send an alert. Or batch alerts of all failed messages in the DLQ at a certain time interval. We can handle them manually later -- either update the code to handle the error or document it.

Give each message an idempotency key so that retries do not generate new messages and a single message can be traced through the entire system.

Aysnc Communication:

I worked in Germany for a year. They have very lenient vacation policies in Germany. I also happened to be the only data engineer on the team. That meant that I had to have top-notch documentation for all of the systems I owned for when I was not present.

I first start with the basics -- define everything, how things interact with each other, steps to take. Use clear headings, structure, and emphasis to make the documentation easy to read.

Another thing -- good, comprehensive documentation can't be done in a single day. It's a cumulative process. Everytime I have a problem, I document it for my future self and others. That way, we solve a problem once and it's documented forever. Make sure to have a clear "Troubleshooting" section for these cases.

System Review:

The problem here is that OpenAI and HubSpot are communicating synchronously. That means that HubSpot waits for OpenAI to respond. A better solution would be for HubSpot to write to a message queue. Another program then polls the queue and sends the request to OpenAI later. Once OpenAI responds, it writes to a different queue. We have another program (or HubSpot itself) poll from the second queue to receive the response.

We'd also want to use idempotency keys to ensure no duplicated messages, a DLQ to save failed messages, structured logging, monitoring, and alerting to ensure that we are aware of any dropped leads and can investigate manually if need be.
```
