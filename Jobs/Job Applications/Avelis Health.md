---
type: job
applied: 2025-11-03
interviews:
  - 2025-11-05 10:30
  - 2025-11-11 14:00
status: rejected
job_type: fulltime
position: Senior Backend Engineer
contract: false
remote:
4day: false
industry: healthcare
website:
location:
company_size: 2
recruited: false
listing: https://www.Workatastartup.Com/jobs/84328
blog:
correspondence: workatastartup
compensation: $150K - $250K
title: Avelis Health
date_created: 2025-11-03 15:09
date_modified: 2025-11-10 17:16
source: workatastartup
---

## Application

```
Hello Angel,

Let's get straight to brass tacks.

You mentioned distributed systems, data pipelines, and APIs. I have 9 years of experience working on these problems. Speaking of data pipelines, at Octimine, I converted their 7 day batch job into a real-time, event-driven system based on Apache Kafka. I've worked in Python throughout my career in both microservice and monolithic architectures.

I'm currently running Dempewolf Apps, where I built and shipped an educational app with a serverless AWS backend. But I'm ready to move back to a team environment for three reasons:

1. I miss collaboration - I learn more and do my best work with others
2. I handle everything (frontend, backend, marketing, sales, finance). I want to focus on what I do best: building resilient, scalable systems
3. The engineering problems I want to solve (distributed coordination, massive concurrency, multi-region scaling) don't exist at my current scale. In order to grow as an engineer, I need fresh problems to solve.

I would love to hear about what problems you're facing at Avelis. Let's chat!

Best,
Chris
```

## Interview Preparation

### Healthcare Background

A **self-insured employer** is an employer who pays their employees' medical expense directly instead of paying through an insurer. That is they assume the financial risk directly rather than paying fixed premiums to an insurance carrier. They can save money this way if their workforce is relatively healthy. However, medical billing errors are systemic. According to Avelis's blog (and many external sources), around 80% of medical claims have errors. That's hard cash left on the table. So what do we do?

Most self-insured employers have a **Third-Party Administrator (TPA)** that handle the administrative side of medical billing. They manually check medical bills for errors, but it's extremely complicated, messy, and takes months — it's reactive, not preventative. ML can automate this process and instantly save self-insured employers money (i.e., *pre*-payment rather than *post*-payment recovery).

Moreover, TPAs generally only look at a sample of claims due to time constraints. ML could allow us to check 100% of medical claims.

ML will also start to recognize patterns that a rule-based TPA would miss. And the ML will get faster and more accurate over time as it sees more data.

**Question**: would we work with TPAs and integrate at that layer to streamline the process? What do other companies in this space do?<br/>
**Question**: medical claims data is heavily regulated (HIPAA). How will we get access to data to build our models? Partnerships? Synthetic data?

#### Competition

This space isn't empty. What makes Avelis different?

- Faster processing?
- Fewer false positives?
- Unique error detection that others don't handle?

#### Business Model

- Will we charge per claim reviewed?
- Percent of savings?
- Subscription model?
- Something else?
- How will we prove ROI to first adopters without a track record?
- Initial target customer? large self-insured employers directly? Or TPAs who serve multiple employers?

My initial thought was to target SEIs directly. Why? You get more clients that way rather than a single TPA.

But i guess this logic is flawed. If we sell to a single TPA, we get access to ~50 companies' claims data with only one sale, one integration, one contract negotiation. Moreover, selling to a TPA might be easier — they understand the space deeply in a way that an SEI would not.

### Technical Background

### Go the Extra Mile

### Founding Engineer Mindset

## Follow-up

I asked a lot of good questions. I did a lot of research. I think that part went well. But i got nervous and felt like i talked too much.

Anyways, here are the questions he asked me:

- Where are you calling from?
	- "I'm actually calling from Veracruz, Mexico"
	- I thought that maybe he saw somehow where I was calling from, so given the context, I think this was the appropriate answer. However, it appears that Zoom does not display this information to other participants, so he was probably just making small talk/curious. Going forward, it would be better to just say Fort Smith.
- Are you based [in Veracruz]?
	- "No, I'm based out of Fort Smith, AR. I'm just down here with my wife visiting family."
- Tell me a little about yourself.
	- Need to work on this. Make it more concise. Tie it into what *they're* doing. Bring them into the equation. I did this a little when i mentioned that i have experience working with legal data, somewhat similar to medical data.
- Tell me about your company. What are you building?
- Would you say that your main experience is in app development?
- Okay, so is your main experience in app development or backend?
- So you spent some time down in Mexico during the pandemic?
- Salary expectations?

## Interview with CTO

### My Background

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

### What I've Learned from Javascript

This isn't guaranteed to be asked, but it's good to be ready to speak intelligently and fluently about what lessons I've learned doing frontend development to show that it was not just a stint but actively made me a better engineer.

- Typescript put a harness on Javascript, so that now large JS codebases are maintainable and errors can be caught before runtime.
- Async/await has made me think about asynchronicity within systems, not just between systems. I've got plenty of experience with asynchronous message queues, but now I think in terms of "okay, can i put this process on a separate thread so that it doesn't hold up the build process?"
- React has also taught me a lot about statefulness. Its system of hooks and composed functions are a masterclass in how to manage state and dependencies in a complex, asynchronous environment.

### Technical Details of the Role

#### Talk Fluently about Everything You've Touched in AWS. Make Sure You Can Explain Your Resume.

#### AWS as it Relates to Health Data

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

#### AWS as it Relates to ML

There are two broad paths for ML in AWS: managed and unmanaged.

##### SageMaker

The managed route uses **SageMaker**, a fully managed ML pipeline that covers everything from data prep to deployment. Basically, AWS's "ML OS".

Here's what a typical pipeline might look like: `Data → Prepare → Train → Evaluate → Deploy → Monitor`.  You can use any or all of these steps independently or combined.

SM automates a lot.  It can launch Jupyter Notebooks in a private VPC (no internet). Can detect data drift or prediction drift, which is crucial for medical data ensuring that model accuracy does not decline. Can build reusable workflows defined in YAML based on Step Functions. Also contains built-in algorithms for many common ML models like XGBoost or logistic regression (via Linear Learner).  It reduces infrastructure complexity (e.g., no EC2 babysitting).

SM integrates data science, dev ops, and compliance into one unified system.

##### Customer Managed Pipeline

A lot more work, but you could squeeze out a few more dollars. You'll be training on EC2 spot instances for training since Lambda has ephemeral memory, low memory, and a 15 min cap on run time.

#### The Medical Claims Recovery Process in General

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

#### How Can We Automate Recovery? What Would a Recovery Pipeline Look Like?

i need to think about how to automate recovery using AWS technologies so that i can think of a potential working pipeline and how that pipeline might hook into their existing detection pipeline.

where is the data stored? what data is stored? how are errors presented to TPAs/clients? The recovery pipeline will need to read from this.

triggering audits, notifying TPAs. how detection feeds recovery?

#### Potential Challenges, Problems, Bottlenecks in Recovery

#### Basic ML Models

they mentioned that i will not be working on the detection process, but i want to be familiar with what they have (they're likely using xgboost or catboost with SHAP values for auditability), but how are errors manifested?

#### What (if any) ML Can Be Used in the Recovery Process?

#### Data Pipeline + Feedback Loops

They're already doing detection → they'll need validated recoveries to feed back into model training and confidence calibration. You can discuss how to close that loop (data lake partitioning, labeling confirmed recoveries, feature drift tracking).

#### Auditability and Trust

Because this is healthcare, every automated recovery needs an **audit trail**. Think structured logging, versioned models, immutable evidence storage (S3 + Dynamo metadata, signed digests). This is a critical "founding engineer mindset" piece — technical + regulatory.

### Questions

- Speaking with Angel, you guys are working with TPAs instead of self-insured employers directly. This makes sense since TPAs cover many clients. You currently have two clients. Did you get these clients from a TPA? Will you be working with the same TPA in the future to get more clients? What's the plan in general for acquiring new clients?
- [Insert competitor list] are some competitors in this space. What does Avelis do differently? Faster turnaround? More accuracy? Catching unique patterns? Lower false positive rate?
- I mentioned to Angel, that I'm currently in Veracruz, Mexico visiting my wife's family. He mentioned that you guys are fully remote. Working on my personal company, I spend about half my time down here between Mexico and the US. Will that be a problem? Or would you prefer that I spend more time in the US?

### Framing Effect

There are three ways to frame my questions. Examples:

1. What differentiates YOU from YOUR competitors?
2. What differentiates AVELIS from ITS competitors?
3. What differentiates US from OUR competitors?

Number 1 uses an "engaged observer" frame. It's better to use it early in the interview or interview process. Number 2 is an "objective/analytic" frame. It's best to use this to show that you think analytically in terms of systems and markets. Number 3 uses an "in-group" frame. Research has shown that people value people who use the in-group framing technique more than people who don't. It's best to use the in-group framing effect later in the interview or interview process.

You can (and should) switch frames *during* the interview! Just always be sure to *end* using an in-group framing effect.

In order to keep cognitive overhead low, we can start with objective and YOU-framing techniques. Use these while discussing background, technical details, etc. Later, there will be a time for questions. This is your cue to switch to in-group framing.

## Rejection

```
Hi Chris,

Thank you for taking the time to speak with us for the Founding Engineer role. Ahmad and I were impressed by your background, but just received so many applicants that we can't move forward with everybody. I wanted to get you feedback as soon as possible.

We’ll keep your information on file in case a future role opens up. Wishing you all the best!
```
