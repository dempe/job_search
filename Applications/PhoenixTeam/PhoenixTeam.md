---
type: job
applied: 2026-11-09
job_type: fulltime
channel: form
contact:
outcome:
source: inbound
listing: "https://recruiting.paylocity.com/recruiting/jobs/Details/4645533/Phoenix-Oversight-Group-LLC/Senior-Software-Engineer-AI-First-Development"
jd: "[[Applications/PhoenixTeam/jd]]"
company: PhoenixTeam
position: Senior Software Engineer, AI-First Development
contract: false
remote: true
compensation:
title: PhoenixTeam
date_created: "2026-11-09 11:25"
date_modified: "2026-11-09 11:25"
---

## Questions

### Do you have 5+ years of professional software engineering experience in Python, C++, Rust, Go, Java, or C#, with most of that foundation established before 2022?

Yes. I have 11 years of professional experience, and most of it predates 2022: about six years of Java at DataRank (2013-2015), SimplyMeasured (2015-2018), and Octimine (2021-2022). At DataRank I built our distributed web scraping and API ingestion frameworks, at SimplyMeasured I designed APIs and microservices in Go and Spring Boot, and at Octimine I built a real-time Kafka Streams pipeline in Java. Python was my other main language alongside Java -- the API gateway at SimplyMeasured was in Lua/Python, and at Octimine I worked on Python batch pipelines.

### Have you personally owned production backend software in Python, including deployment and troubleshooting production issues or incidents?

Yes, though most of my production backend ownership has been in Java and Node.js. In Python, at Octimine I inherited a weekly Python batch job that processed about 30 million patent documents for about 50 customers. It took at least 48 hours to run, broke often, and sometimes overlapped with the following week's run, so customers didn't get their data on time. I supported it in production: when it failed, I tracked down what broke and got it running again. To make that less painful, I split it into phases so a failure meant restarting one stage (e.g. the Postgres and Elasticsearch updates) instead of the whole job, and I automated our Python data processing pipelines with GitLab CI and shell scripts. In the end I replaced it with a real-time Kafka Streams pipeline in Java, with unit tests for every analytic and a dead letter queue.

### Have you used Claude Code, Cursor, Copilot, Codex, or a similar coding agent professionally to implement real software? If so, can you give me one quick example of something the agent got wrong that you caught and corrected yourself?

Yes. Most recently I used Claude Code to build a Node.js app that syncs payment data between a client's payment provider and Shopify. I run every project through a scope -> plan -> implement -> review cycle that I built as Claude Code skills, so the requirements and plan are pinned down before any code gets written.

Two things it got wrong that I caught: it wanted to hand-roll a SQL migration runner and a config loader when well-tested libraries already exist for both, so I rejected those and had it use off-the-shelf solutions. It also started editing the implementation before any test existed. Since it was touching payments, it was imperative that the code was correct, so I stopped it and made it write a failing unit test first, then fix the code until the test passed. The client switched payment providers before their existing contract ran out.

### Are you currently based in the U.S. and authorized to work here now and in the future without PhoenixTeam providing sponsorship or taking immigration-related action? The role also requires occasional client travel and the ability to go through the federal Public Trust process.

Yes. I'm a U.S. citizen based in Arkansas (Central Time), so I don't need sponsorship now or in the future.
