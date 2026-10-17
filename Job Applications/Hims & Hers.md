---
type: job
applied: 2026-10-16
job_type: fulltime
channel: form
status: awaiting-reply
interviews:
source: linkedin
listing: "https://jobs.ashbyhq.com/hims-and-hers/89b79149-e97a-48b8-b411-3fbf01274bb5/application?utm_source=linkedinpremium"
company: Hims & Hers
position: Sr. Software Engineer (Backend)
contract: false
remote: true
compensation: $170K – $190K • Offers Equity
title: Hims & Hers
date_created: "2026-10-16 18:05"
date_modified: "2026-10-16 18:05"
---

## Application

> What languages, frameworks and libraries are you most proficient with?

```
Java (Spring Boot, Hibernate/JPA, Kafka Streams), Python, and TypeScript/Node.js, with React and React Native/Expo on the frontend. I've also worked professionally in Go and use Kotlin in side projects. On the infrastructure side, AWS serverless (Lambda, API Gateway, DynamoDB, SQS/SNS) with SAM/CloudFormation, Docker, Terraform, and GitHub Actions.
```

> Briefly describe a backend distributed system you designed, built, or maintained, and your specific role in it. (1 to 3 sentences)

```
At Octimine, I replaced a fragile weekly Python batch job processing ~30 million patent documents with a real-time, event-driven Kafka Streams pipeline in Java. I designed the system from source to sink, proposed it to my manager and the other backend engineers, and then built it with two other engineers. It had a DLQ, so one bad document couldn't take down the whole run, and customers got their data in real time instead of waiting a week.
```

> Briefly describe your experience designing and building scalable back end services or distributed systems, including which cloud environment you used. (1 to 2 sentences)

```
Mostly AWS: I built a serverless backend on Lambda, API Gateway, DynamoDB, and SQS/SNS with idempotent processing and retries, defined in SAM/CloudFormation with GitHub Actions CI/CD and automated rollbacks. Before that, I designed Spring Boot and Go microservices at SimplyMeasured/Sprout Social behind an API gateway I set up to centralize auth, rate limiting, and request transforms.
```

> Which relational database(s) have you worked with?

```
PostgreSQL, MySQL, and SQLite. Most recently, I designed a Postgres projection of a wholesale distributor's Shopify customer and order data, refreshed in the background, to keep lapsed accounts visible beyond the Admin API's 60-day window.
```
