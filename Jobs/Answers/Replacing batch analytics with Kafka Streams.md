## Certa

Source: [[Jobs/Job Applications/Certa]]

> Have you been involved in designing and developing the architecture of complex software systems? If yes, please confirm which part you were involved in.

```
At Octimine, I replaced a weekly Python batch job that took 48 hours minimum to run. The problem was that it was prone to breakage and sometimes would even overlap with the following week's job.

I began by analyzing the batch job and what it was doing. I saw that data came in continuously, so a batch job wasn't even required in the first place.

I suggested we migrate to a real-time, event-driven system, and I proposed Kafka Streams for this solution. Other team members suggested using AirFlow for simplicity, but looking at what the batch job was actually doing, it was clear that Kafka Streams was a better fit.  It wasn't a simple ETL job, where AirFlow specializes. The batch job was doing heavy analytics. Kafka Streams provides joins, windows, compaction, grouping, etc. out-of-the-box and would, in the end, make our lives easier.

I designed the system from source to sink and proposed it to my manager and other backend engineers. After we agreed on the plan, I began implementing the new pipeline with two other engineers.

After it was completed, the new pipeline was much more durable. All analytics were unit-tested. We had a DLQ for failed messages, and could quickly diagnose problems. Moreover, problem messages no longer halted the entire run. And, on top of all of that, customers got their data in real time!
```

## Close (0)

Source: [[Jobs/Job Applications/Close (0)]]

> Describe a Software Development Project You Led and Any Lessons Learned from It.

```
I was hired as Senior Data Engineer at Octimine/Dennemyer. They needed to process ~30 million XML legal documents weekly, and they had some hacky Python scripts set up to run a weekly batch job that ran between 2 and 4 days if nothing went wrong. Using a batch job didn't make sense, as the data came in continuously.

After some team meetings, I started the migration to using Kafka. Everything worked great in the end, but I do think that Kafka might have been overkill for our needs. We didn't have a hard requirement for real-time data, so something like Airflow would have worked instead.

Lesson learned: do more research. If no one on your team is knowledgeable, ask around on the internet, and don't stick with something just because you're familiar with it (this is the biggest reason I pushed for Kafka).
```

## Close (1)

Source: [[Jobs/Job Applications/Close (1)]]

> Describe a software development project you led and any lessons learned from it.

```
I was hired as Senior Data Engineer at Octimine/Dennemyer. They needed to process ~30 million XML legal documents weekly, and they had some hacky Python scripts set up to run a weekly batch job that ran between 2 and 4 days if nothing went wrong. Using a batch job didn't make sense, as the data came in continuously.

After some team meetings, I started the migration to using Apache Kafka. Everything worked great in the end, but I do think that Kafka might have been overkill for our needs. We didn't have a hard requirement for real-time data, so something like Airflow probably would have worked instead.

Lesson learned: do more research. If no one on your team is knowledgeable, ask around on the internet, and don't stick with something just because you're familiar with it (this is the biggest reason I pushed for Kafka).
```

## Galactic Advisors

Source: [[Jobs/Job Applications/Galactic Advisors]]

>  Describe one development project you made better. What was one thing you did to make it better?

```
At Octimine, I replaced a weekly batch job that took 2 days to run with a real-time, event-driven pipeline using Apache Kafka. This reduced data latency from 7 days to real-time, enabling immediate data availability across the organization and for our customers. 
```

## Grass

Source: [[Jobs/Job Applications/Grass]]

> Knowledge on how to build large scalable systems*

```
I have built real-time, event-driven systems from the ground up, including a Kafka-based ETL pipeline that scaled from weekly batch jobs to real-time processing.
```

## HireGlide

Source: [[Jobs/Job Applications/HireGlide]]

>  Great! I see from your CV that you've worked with a diverse tech stack including Java, Kotlin, Python, and AWS. What technologies are you most comfortable with, and what's a project you've built that you're particularly proud of?

```
the four technologies that you listed are my strong points - java, kotlin, python, and aws. the project i'm most proud of was building a real-time, event-driven ETL pipeline based on apache kafka at my previous employer. it allowed our customers and in-house data analyists to get data in real time instead of weekly, which was the previous cadence.
```

## JustPaid

Source: [[Jobs/Job Applications/JustPaid]]

>  Please tell us in one or two sentences about the most impressive thing you have built or achieved. *

```
The biggest project I have built in my professional career would likely be an analytics streaming pipeline based on Apache Kafka, which I built to replace a weekly batch job.  It was an over-six-months-long project, but it increased the company's data latency from weekly to seconds.
```

## Kovo

Source: [[Jobs/Job Applications/Kovo]]

> What exceptional work have you done?

```
As Senior Data Engineer at Octimine, I converted a 48-hour batch data job (run weekly) to a real-time, event-driven analytics pipeline in Apahce Kafka. This meant that customers got data in immediately instead of waiting a week.

Aside from that, my main work has been in AWS. I'm currently running a one-man contracting company doing AWS work. I've helped clients set up serverless pipelines in API Gateway, Lambda, DynamoDB with SQS queues. I've helped clients tune their EC2 and RDS instances and set up S3/CloudFront.
```

## Resend

Source: [[Jobs/Job Applications/Resend]]

> Tell us the most impactful project you've worked on before and what your role was in it. Share numbers that help us understand the workload (number of customers, requests per second, etc) and your impact on the project.<br/>
> Answer example: At my previous job, I led the rebuild of our payments service, handling checkout for ~2.3M monthly users at ~1,200 RPS peak.) I owned the technical design and the zero-downtime migration from a Rails monolith to a Go service with Kafka-based event distribution. After 4 months in production, p95 latency dropped from 800ms to 180ms.

```
As Senior Data Engineer at Octimine, I converted a 48-hourish batch data ingestion/analytics job (run weekly) to a real-time, event-driven analytics pipeline in Apahce Kafka. This meant that customers got data in immediately instead of waiting a week.

The data came in continuously to our data warehouse, so it did not make sense to me to use a batch job in the first place. I decided to use Kafka over something like Airflow due to the highly analytic nature of the pipeline. A Kafka Streams topology has joins, compaction, aggregates, etc. built-in and made my work a lot simpler.

We had about 50 customers. The data was all new patent data (new patents or updates to existing patents) in the US and Europe -- about 30 million documents per week.
```
