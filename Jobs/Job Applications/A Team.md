---
tags:
applied: 2023-06-02
job_type: contractor
application_stage: rejected
interviews:
remote:
industry: consulting
website: https://platform.a.team/chrisdempewolf
location:
company_size:
recruited:
listing: https://remotive.com/remote-jobs/software-dev/senior-independent-software-developer-814298
title: A Team
date_created: "2023-06-02 18:10"
date_modified: "2025-05-31 13:30"
---

## Application

Submitted an application on [their site](https://platform.a.team/chrisdempewolf). Added 3 projects:

### First Open Source SDK for the Pinterest API (2015)

At my first employer (DataRank), I wrote a Java SDK to consume the Pinterest API. I published it under the Apache License, and released it on maven.org.

It uses fluid, functional interfaces to chain commands together. For example, final PinResponse pin = pinterest.getPin("<PIN_ID>", new PinFields().withLink().withCreatedAt().withColor();

Later converted to Kotlin.

### Kafka Data Ingestion Pipeline

My previous company (Dennemyer/Octimine) needed to process ~30 million XML legal documents weekly, and they had some hacky Python scripts set up to run a weekly batch job that ran between 2 and 4 days if nothing went wrong. Using a batch job didn't make sense, as the data came in continuously.

After some team meetings, I started the migration to using Kafka. All code is now in a single, unit-tested repo, and moreover, all data and data analytics arrive continuously from the data warehouse (Postgres) to ElasticSearch for the front-end API to consume.

### Personal Website Using Laravel

I've been working on my personal website (chrisdempewolf. com) over the past few months. I'm trying to set up a blog to practice my writing and show what I'm doing. It's a static website written in PHP using Laravel. I run the Laravel server and use wget to pull down a static version. It's not the prettiest build setup, but it's worth it to use PHP/Laravel for my site. Say what you will about PHP, but it's a fantastic language for HTML templating. And since I'm not using someone else's static site generator, I know how everything works and control everything. Plus, I have a nice SQLite backend that makes working with various relationships (e.g., post<->tags, a many: many relationship) muuuch simpler than without a relational DB. I'm also a huge fan of the Laravel ORM, Eloquent.
