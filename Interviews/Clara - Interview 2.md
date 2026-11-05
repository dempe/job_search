---
type: interview
application: "[[Job Applications/Clara]]"
company: Clara
round: 2
date: 2024-02-11 14:00
interviewers:
outcome: declined
title: Clara - Interview 2
date_created: "2026-11-04 18:10"
date_modified: "2026-11-04 18:10"
---

### Transcript

![[Transcripts/Clara - Interview 2]]

### Questions

Model answers, not a record of what was said.

> What's your thought about the challenge?

```
It looks fun. As I understand it, there are two inputs: FHIR bundles from your supplier, which are already deduplicated through the health information exchange, and lab reports that arrive as scanned PDFs or images. The goal is to turn the lab report into valid FHIR, merge it into the patient's record, and get a de-identified copy into Postgres the team can use for evals and training.

My plan would be:

For the bundles: validate against the FHIR spec with an off-the-shelf library like fhir.resources rather than rolling my own. Invalid bundles go to a dead-letter queue with an alert, never into the database. Valid ones are stored, and the whole bundle is written in one transaction, so a failure never leaves a partial record.

For the lab reports: send the image to a vision model with structured outputs, so the response has to match a strict schema -- test name, value, unit, reference range, date. Then map each result to a FHIR Observation that references the patient, and run it through the same validation. The risk is hallucination, so I'd check that each extracted value actually appears in the source, sanity-check units and ranges, and route anything low-confidence to human review.

For de-identification: strip direct identifiers like names, birth dates, contact details, and addresses below the state level, and replace IDs with a keyed hash like HMAC, so the same patient always maps to the same pseudonym and references still line up.

A couple of questions I'd ask up front: do you only ever get data from the one supplier, and where does de-identification need to happen -- in production, or only for the copy that leaves it?
```

> So for each resource, you're proposing a record in the database where we store that record?

```
Yes -- one row per FHIR resource. The key is the resource's ID, which also keeps references between resources resolvable. The main column is the raw resource as JSONB. Keeping the raw resource makes it the source of truth, so anything else can be re-derived later without re-ingesting.

Rather than a table per resource type -- FHIR has well over a hundred -- I'd use one table with a resource_type column and pull a few fields out into indexed columns for the most common lookups: the patient reference, the effective date, and the version. A GIN index on the JSONB covers ad-hoc queries. If something turns out to be slow, you add a generated column for it later.

Writes are upserts keyed on ID and version, so reprocessing the same bundle is harmless, and each bundle is written in a single transaction.
```

> Do you know structured outputs?

```
Yes. Structured outputs let you give the model a JSON Schema and constrain its output to match it. Instead of asking nicely for JSON and hoping, the decoding itself is restricted, so the response always parses and has the required fields and types. OpenAI exposes it as a JSON schema response format in strict mode, and with Anthropic you get the same effect by defining a tool with an input schema and requiring the model to call it.

For this challenge, that means I define a schema for a lab result -- test name, value, unit, reference range, date -- send the image, and get back data I can map straight to FHIR Observations.

The important caveat is that structured outputs guarantee the shape, not the truth. The model can still produce a perfectly valid object with the wrong number. So I'd still validate the content: check that each extracted value appears in the source, sanity-check units and ranges, validate the final FHIR, and keep a labeled set of real reports to measure extraction accuracy whenever the prompt or model changes.
```

### Preparation

```
Hey Chris,

We really enjoyed reviewing your profile, we'd love to move forward with a hands-on technical session. How does your week look? Are you available tomorrow or Wednesday?I'd like to book about an hour of your time for a practical working session. Feel free to use whatever tools make you most productive: AI assistants, your favorite Python frameworks, whatever helps you think and build.

The Goal:
We work with FHIR bundles (healthcare data in JSON format) and need to build robust data pipelines to process and prepare this data for downstream systems.
What we'd like to explore with you:

-   Parsing & organizing FHIR data - How would you approach extracting and structuring the relevant clinical information from raw FHIR bundles?
-   De-identification strategy - Healthcare data requires careful handling. How would you approach stripping PHI while preserving data utility?
-   Pipeline robustness - What strategies would you use to ensure reliable, fault-tolerant data processing at scale?
-   Database ingestion - How would you prepare and validate the processed records for a patient who are fully deidentified before an ML engineer uses this data to fine tune a model?

This isn't about writing production code in an hour - it's about thinking through the problem together and seeing how you approach data engineering decisions.
Looking forward to hearing from you.

Best,
Cuau
```

### Retrospective

Went pretty well except for technical difficulties. *Really* need to buy a new computer. Will buy a Mac Mini when I go back to AR in March.

I think they would likely want a follow-up actually, but… They are exclusively in-office, so even with a relocation package and competitive pay, this is a no-go. They basically told me there is zero chance of any hybrid setup.
