---
type: interview
application: "[[Job Applications/Avelis Health]]"
company: Avelis Health
round: 2
date: 2025-11-11 14:00
kind:
interviewers:
outcome:
title: Avelis Health - Interview 2
date_created: "2026-11-04 18:10"
date_modified: "2026-11-04 18:10"
---

### Transcript

![[Transcripts/Avelis Health - Interview 2]]

### Questions

Model answers, not a record of what was said.

> Can you give me an intro, more on a technical level?

```
Sure. I'm a backend engineer, and most of my career has been data ingestion and data pipelines.

I started at DataRank, a startup gathering social and online data so brands could see what people were saying about their products. I built their Java ingestion -- a distributed crawler framework for forums and a framework for social media APIs with token pools and rate limiting -- all normalizing into one canonical model.

Then I moved to Seattle and joined SimplyMeasured, which had a much bigger microservice backend. There I designed APIs and services in Go and Spring Boot, worked on the API gateway that handled auth and rate limiting for all of them, and wrote HBase map/reduce jobs for social analytics.

After that I was the senior data engineer at Octimine in Munich. They processed around 30 million patent and legal documents a week with a fragile Python batch job that took days. I replaced it with a Kafka Streams pipeline in Java, with a dead letter queue and unit tests on every analytic.

Since then I've run my own company, building a React Native app on a serverless AWS backend -- Lambda, API Gateway, DynamoDB -- and contracting on Node.js payment and Shopify integrations.
```

> Why are you looking for a different role outside your company?

```
Three reasons. First, I want to work with other engineers again. I learn more and do my best work when I can bounce ideas off people and get my code reviewed.

Second, running a company means doing everything -- marketing, sales, finances, frontend. That's been a good education, but I want to spend my time on what I'm best at, which is backend and data engineering.

Third, I want new, harder problems to keep growing. A founding engineer role at a company like yours checks all three: there's a real team forming, the work is backend and data heavy, and the problem is genuinely hard.
```

> Would you say frontend is your biggest challenge? Or out of all the previous roles you've held and projects you've done, what would you say was the most challenging and, at the same time, the most interesting for you?

```
Frontend was a real challenge, because it was new to me and JavaScript had changed a lot since I last used it. It changed how I think about modularity -- keeping state local to components and passing it down through props -- and I came to really like async/await.

But the most challenging and most interesting was the Kafka migration at Octimine. I was the only data engineer, so I owned the whole thing: designing the topology, standing up Kafka, porting every analytic out of the batch job, and cutting over without corrupting the data downstream teams relied on. It was hard because it was a live system with no room for bad data, and interesting because I got to make the architectural calls myself and live with them.
```

> Before this, what did you use -- Java and Kotlin?

```
Mostly Java and Python. Java was my main language for about seven years -- DataRank, SimplyMeasured, and Octimine -- with Spring Boot, Hibernate, and Kafka Streams. Python I used for scripting, the API gateway at SimplyMeasured, and data work. I've used Kotlin a little, and I wrote Go for a couple of years at SimplyMeasured. These days it's mostly TypeScript on Node.
```

> Have you explored using state management libraries, like Zustand?

```
Yes, I use Zustand in Athena Math for settings and session state. I like it because it's small, there's no provider boilerplate, and components subscribe only to the slice of state they need, so you don't get needless re-renders.

My general rule is to keep as little state as possible and keep it in as few places as possible. Anything you can derive, you derive. Every extra piece of state is another chance for two things to disagree.
```

> What would you say is the most interesting technical problem you have tackled in the past, aside from frontend?

```
Replacing Octimine's weekly batch job with Kafka Streams. They were processing roughly 30 million patent documents a week with a Python batch job that took days and failed partway through often enough that someone had to babysit it.

I was the only data engineer, so I designed and built the replacement myself: Kafka topics as the backbone, a Kafka Streams topology in Java doing the analytics, a dead letter queue so one bad document couldn't stall the pipeline, and sinks into Elasticsearch and the data warehouse.

The most interesting part was making it trustworthy. I unit-tested every analytic, so we could change analytics in CI without risking corrupting the data, and I documented every failure and recovery scenario so on-call didn't depend on me. The big win was durability -- the data showing up in near real time was a nice side effect.
```

> Why did you choose Kafka?

```
Two reasons: durability and the shape of the workload.

The batch job's failure mode was the problem. If it died halfway through a few days of processing, you started over. With Kafka, every document is persisted in a log, consumers track their offsets, and a failure means you resume where you left off or replay, not redo everything. The dead letter queue meant a single malformed document got set aside instead of killing the run.

Then the workload itself was analytics: joins, grouping, windowing, aggregations. Kafka Streams gives you all of that out of the box, with state stores and compaction. We did consider Airflow, and Airflow is great at scheduling and orchestrating ETL, but it doesn't do the analytics. We'd have been hand-rolling joins and aggregations in tasks around a scheduler.

The fair criticism is operational cost. Running Kafka is more than a small team needs for a pure batch ETL, and if that had been the whole job, Airflow would have been the simpler choice. Given the analytics and the reliability problem, I'd make the same call again.
```

> Did you do any research on what we do?

```
Yes. You find errors in medical claims, and you're currently doing it post-adjudication, working with self-insured employers through their TPAs.

As I understand it, there are two places to catch errors. Pre-adjudication is faster and prevents the overpayment in the first place, so the ROI is quicker. Post-adjudication gives you the remittance data -- the 835s alongside the 837 claims -- which is what you need to know what was actually paid and to train models on outcomes. The downside of post-adjudication is that you then own the recovery process: identifying the overpayment, documenting it, and actually getting the money back.

So starting post-adjudication makes sense for building the data and the models, with pre-adjudication as a natural next step once the detection is proven. And longer term, the bigger waste is in commercial plans, Medicare, and Medicaid.
```

> How do you feel about healthcare generally?

```
Healthcare in the US is badly broken, and a lot of the cost comes from administrative waste rather than care. That's actually what draws me to it.

At SimplyMeasured I was helping marketers get more data about their campaigns, and at some point I asked myself who that was really helping. Catching billing errors in medical claims is different. It's a real economic inefficiency, and recovering that money helps employers and, eventually, the people paying premiums.

I also know it's much more complex than it looks from the outside -- the codes, the payer rules, the regulations, the systems. I'd go in expecting a lot to learn, not assuming I already understand it.
```

> Have you dealt with legacy systems before, like old banking systems?

```
Not systems as old as the COBOL and mainframe era, no. But I've spent most of my career consuming data from systems I didn't control and couldn't change: forum scraping and social media APIs at DataRank, and at Octimine, patent data from many different sources, each with its own formats and quirks.

The lessons carry over. Treat the outside system as the source of truth for what it sends, not what its docs say. Validate everything at the boundary and normalize into your own model as early as you can. Keep the raw input so you can reprocess when you find a parsing bug. And quarantine bad records instead of letting them crash the pipeline -- that's what the dead letter queue was for at Octimine.

With healthcare, I'd expect the same thing at a bigger scale: X12 837 and 835 files, inconsistent payer behavior, and old systems on the other end that aren't going to change for us.
```

> Is dealing with healthcare and its legacy systems something you'd be interested in?

```
Yes, absolutely. Hard, messy integration problems are where I've done my best work, and getting good at untangling complex systems is how you keep growing.

And the stakes are what make it worth it. If the pipeline gets claims data in reliably and the models catch errors, that's money going back to employers and, eventually, lower costs for people. That's a problem I'd want to own.
```

### Preparation

#### My Background

my background isn't so much research, but more phrasing to make it not just a long blog of verbal diarrhea.

> Past → Pivot → Present → Pull.

That means:

- **Past**: your backend experience (Java, Spring Boot, data pipelines, etc.)
- **Pivot**: the entrepreneurial period — starting your company, building apps
- **Present**: what you've learned technically and personally (autonomy, shipping, accountability)
- **Pull**: why those experiences draw you toward a company like Avelis (impact, scaling, real-world effect).

```
I started my career at DataRank, where I was put in charge of data ingestion. I built a crawler framework that scraped various websites, and corresponding system to handle pulling data from APIs.

I continued this work at SimplyMeasured and SproutSocial, though in a little more mature micorservice-based backend. I also worked a lot on API design and standing up new services. A lot of work in Java, SpringBoot, and Python.

My next technical gig was Octimine/Dennemyer. They were doing analytics on legal (IP) data. They had a batch job that ran weekly and ran for at least two days, but the data was coming in in real time. I built a real-time event-driven system based on Kafka. Aside from getting data in real time, this also gave us nice, structred logging, common interfaces for standing up new analytics, and comprehenvie unit tests.

After that, I pivoted to start my own company building educational mobile apps.  It's something I've wanted to do for a while now. I've learned a lot, and I'm grateful that I had the opportunity to do it, but I'm now looking to get back to working on a team. For one, I like working with others, I want to focus on what I do best-designing backend systems-not accounting, marketing, etc. And I'm eager to take on new challenges.

Particularly, I'm interested in health care and ML, so I would love to apply my skills to these domains.
```

Chatgpt's version:

```
I started my career at a startup called DataRank, where I owned the data ingestion pipeline — building web crawlers and API collectors that pulled large volumes of social and market data.

From there I joined SimplyMeasured, later acquired by SproutSocial, where I worked on microservice-based backends — designing APIs, standing up new services, and scaling them in Java, Spring Boot, and Python.

After that, at Octimine (later Dennemeyer), I led a move from slow batch analytics to a real-time event-driven architecture built on Kafka. That system not only delivered data continuously but gave us structured logging, standardized analytics interfaces, and full test coverage — a big step up in reliability.

Then I took a deliberate pivot. I founded my own company to build educational mobile apps. I wanted to broaden my skill set, learn new stacks, and see what it takes to take a product from idea to store. I learned a lot about React Native, AWS serverless, and the realities of shipping and maintaining software end-to-end.

Now I’m looking to bring those experiences back into a collaborative team setting — ideally one working in healthcare and machine learning, where data quality, reliability, and privacy really matter. I’d love to help Avelis design resilient backend systems that make recovery automation both trustworthy and scalable.
```

#### What I've Learned from Javascript

This isn't guaranteed to be asked, but it's good to be ready to speak intelligently and fluently about what lessons I've learned doing frontend development to show that it was not just a stint but actively made me a better engineer.

- Typescript put a harness on Javascript, so that now large JS codebases are maintainable and errors can be caught before runtime.
- Async/await has made me think about asynchronicity within systems, not just between systems. I've got plenty of experience with asynchronous message queues, but now I think in terms of "okay, can i put this process on a separate thread so that it doesn't hold up the build process?"
- React has also taught me a lot about statefulness. Its system of hooks and composed functions are a masterclass in how to manage state and dependencies in a complex, asynchronous environment.

#### Technical Details of the Role

##### Talk Fluently about Everything You've Touched in AWS. Make Sure You Can Explain Your Resume.

##### AWS as it Relates to Health Data

VPC isolation, encryption, PHI handling

The three main HIPPA rules that govern architecture:

1. **Privacy rule**: who can access PHI and under what conditions?
2. **Security rule**: governs how PHI can be accessed. This is where encryption and access control come in
3. **Breach rule**: governs what must be done in the event of PHI leakage. You must detect, report, and notify affected parties.

HIPPA under AWS uses a **shared responsibility** model. Meaning that, once you sign the BAA, AWS provides HIPPA-compliant services. You must use them. On the flippy, you're also responsible for *not* using non-HIPPA-compliant services (Alexa, Comprehend, Rekognition, etc.). On that note, a private VPC is a starting point but doesn't guarantee compliance. You still need encryption, IAM, and audit controls.

Some necessary services to use for HIPPA compliance:

- **CloudTrail**: keeps a record of every API call - when, where, from whom, to whom. Necessary for auditability.
- **GuardDuty**: threat detection service. It continually monitors CloudTrail and logs for anomalies and potential breaches. Findings can be sent to SecurityHub or EventBridge for alerting.
- **Athena**: serverless SQL queries on data in S3 buckets. Can be used to analyze data for breaches
- **Config Rules**: tracks config changes like version control. Can specify rules that ensure that, for example, all EBS volumes are encrypted or there's no public access to S3 buckets or that DynamoDB tables have PITR enabled, etc.
- **Security Hub**: unified compliance dashboard. Aggregates data from GuardDuty etc. More of a high-level tool for compliance. Can enable **automatic remediation** by sending output to Lambda and EventBridge to enable **self-healing infrastructure**.

##### AWS as it Relates to ML

There are two broad paths for ML in AWS: managed and unmanaged.

###### SageMaker

The managed route uses **SageMaker**, a fully managed ML pipeline that covers everything from data prep to deployment. Basically, AWS's "ML OS".

Here's what a typical pipeline might look like: `Data → Prepare → Train → Evaluate → Deploy → Monitor`. You can use any or all of these steps independently or combined.

SM automates a lot. It can launch Jupyter Notebooks in a private VPC (no internet). Can detect data drift or prediction drift, which is crucial for medical data ensuring that model accuracy does not decline. Can build reusable workflows defined in YAML based on Step Functions. Also contains built-in algorithms for many common ML models like XGBoost or logistic regression (via Linear Learner). It reduces infrastructure complexity (e.g., no EC2 babysitting).

SM integrates data science, dev ops, and compliance into one unified system.

###### Customer Managed Pipeline

A lot more work, but you could squeeze out a few more dollars. You'll be training on EC2 spot instances for training since Lambda has ephemeral memory, low memory, and a 15 min cap on run time.

##### The Medical Claims Recovery Process in General

Know: CMS-1500, UB-04, CPT, ICD-10, adjudication process

- **CMS-1500**: standard claim form. It's the standard form for submitting professional medical claims to insurance carriers, including Medicare Part B. Ex: A family doctor bills for an office visit (`99213`) and a flu shot (`90686`).
- **UB-04** (a.k.a. **CMS-1450**): Standard claim form for facility-based billing—room & board, operating room time, nursing care, supplies, etc.
- **837P**: electronic version of CMS-1500. "P" stands for "professional"
- **837I**: electronic version of CMS-1450. "I" stands for "institutional"
- **CPT** or **HCPCS**: Procedure codes (e.g., CPT 93000 (EKG)). If CPT 93000 appears on a customer's bill, there should be a relevant ICD-10 diagnosis code.
- **ICD-10**: Diagnosis codes.
- **Adjudication process**: automated + manual process that decides payment. Multi-layered pipeline blending rule engines, medical logic, and contract pricing that ensures that claims are paid accurately and compliantly
- **Recovery**: identifying and reclaiming incorrectly paid claims (overpayments).
- **837**: claim submission
- **835**: remittance or payment report
- **Coordination of Benefits (COB)**: multiple insurers. Wrong one paid.
- **The lifecycle**: Claims → adjudication → payment → recovery
- **Remittance**: describes why the payer paid what they did and didn't pay what they didn't
- **CARC/RARC** codes: codes for reasons for why an insurer chose not to pay something
- **PHI (Protected Health Information)**: any individually identifiable health data

Error detection can happen either pre-adjudication or post-adjudication. Pre-adjudication has the advantage that it's quicker and cheaper, but you don't get remittance data, so there's less data to train on.

With post-adjudication error detection, you have to deal with recovery; however, you get access to 835 remittance reports which are gold for training ML models.

##### How Can We Automate Recovery? What Would a Recovery Pipeline Look Like?

i need to think about how to automate recovery using AWS technologies so that i can think of a potential working pipeline and how that pipeline might hook into their existing detection pipeline.

where is the data stored? what data is stored? how are errors presented to TPAs/clients? The recovery pipeline will need to read from this.

triggering audits, notifying TPAs. how detection feeds recovery?

##### Potential Challenges, Problems, Bottlenecks in Recovery

##### Basic ML Models

they mentioned that i will not be working on the detection process, but i want to be familiar with what they have (they're likely using xgboost or catboost with SHAP values for auditability), but how are errors manifested?

##### What (if any) ML Can Be Used in the Recovery Process?

##### Data Pipeline + Feedback Loops

They're already doing detection → they'll need validated recoveries to feed back into model training and confidence calibration. You can discuss how to close that loop (data lake partitioning, labeling confirmed recoveries, feature drift tracking).

##### Auditability and Trust

Because this is healthcare, every automated recovery needs an **audit trail**. Think structured logging, versioned models, immutable evidence storage (S3 + Dynamo metadata, signed digests). This is a critical "founding engineer mindset" piece — technical + regulatory.

#### Questions to Ask

- Speaking with Angel, you guys are working with TPAs instead of self-insured employers directly. This makes sense since TPAs cover many clients. You currently have two clients. Did you get these clients from a TPA? Will you be working with the same TPA in the future to get more clients? What's the plan in general for acquiring new clients?
- [Insert competitor list] are some competitors in this space. What does Avelis do differently? Faster turnaround? More accuracy? Catching unique patterns? Lower false positive rate?
- I mentioned to Angel, that I'm currently in Veracruz, Mexico visiting my wife's family. He mentioned that you guys are fully remote. Working on my personal company, I spend about half my time down here between Mexico and the US. Will that be a problem? Or would you prefer that I spend more time in the US?

#### Framing Effect

There are three ways to frame my questions. Examples:

1. What differentiates YOU from YOUR competitors?
2. What differentiates AVELIS from ITS competitors?
3. What differentiates US from OUR competitors?

Number 1 uses an "engaged observer" frame. It's better to use it early in the interview or interview process. Number 2 is an "objective/analytic" frame. It's best to use this to show that you think analytically in terms of systems and markets. Number 3 uses an "in-group" frame. Research has shown that people value people who use the in-group framing technique more than people who don't. It's best to use the in-group framing effect later in the interview or interview process.

You can (and should) switch frames *during* the interview! Just always be sure to *end* using an in-group framing effect.

In order to keep cognitive overhead low, we can start with objective and YOU-framing techniques. Use these while discussing background, technical details, etc. Later, there will be a time for questions. This is your cue to switch to in-group framing.
