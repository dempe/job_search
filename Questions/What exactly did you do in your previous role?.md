---
type: question
title: What exactly did you do in your previous role?
date_created: "2023-05-30 15:29"
date_modified: "2025-05-31 13:30"
---

## Longer Version

I was hired as Senior Data Engineer (at Octimine/Dennemeyer, an IP law firm based in Luxembourg. The company that they acquired and that I was working for was doing analytics on patents data). They had a bunch of Python scripts and Java programs hacked together to make a weekly batch job to process incoming patent data for the week.

My main role was to help move this to a more resilient, event-driven system that ran continuously.

## Shortened Version

I was hired as Senior Data Engineer. I made sure data got from our data warehouse to ElasticSearch and the front-end. When I joined, the process they had for this was really janky, took days, and had almost no testing. So I started the effort to migrate everything over to a real-time, event driven system. We chose Kafka.

## Another Version

My previous company (Dennemyer/Octimine) needed to process ~30 million XML legal documents weekly, and they had some hacky Python scripts set up to run a weekly batch job that ran between 2 and 4 days if nothing went wrong. Using a batch job didn't make sense, as the data came in continuously.

After some team meetings, I started the migration to using Kafka. All code is now in a single, unit-tested repo, and moreover, all data and data analytics arrive continuously from the data warehouse (Postgres) to ElasticSearch for the front-end API to consume.

## Asked by

- 3 unknown (2021)
