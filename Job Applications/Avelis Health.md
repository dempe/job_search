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
channel: form
listing: https://www.Workatastartup.Com/jobs/84328
blog:
correspondence: workatastartup
compensation: $150K - $250K
title: Avelis Health
date_created: "2026-10-13 12:09"
date_modified: "2026-10-21 18:20"
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

## Interview 1

### Preparation

#### Healthcare Background

A **self-insured employer** is an employer who pays their employees' medical expense directly instead of paying through an insurer. That is they assume the financial risk directly rather than paying fixed premiums to an insurance carrier. They can save money this way if their workforce is relatively healthy. However, medical billing errors are systemic. According to Avelis's blog (and many external sources), around 80% of medical claims have errors. That's hard cash left on the table. So what do we do?

Most self-insured employers have a **Third-Party Administrator (TPA)** that handle the administrative side of medical billing. They manually check medical bills for errors, but it's extremely complicated, messy, and takes months — it's reactive, not preventative. ML can automate this process and instantly save self-insured employers money (i.e., *pre*-payment rather than *post*-payment recovery).

Moreover, TPAs generally only look at a sample of claims due to time constraints. ML could allow us to check 100% of medical claims.

ML will also start to recognize patterns that a rule-based TPA would miss. And the ML will get faster and more accurate over time as it sees more data.

**Question**: would we work with TPAs and integrate at that layer to streamline the process? What do other companies in this space do?<br/>
**Question**: medical claims data is heavily regulated (HIPAA). How will we get access to data to build our models? Partnerships? Synthetic data?

##### Competition

This space isn't empty. What makes Avelis different?

- Faster processing?
- Fewer false positives?
- Unique error detection that others don't handle?

##### Business Model

- Will we charge per claim reviewed?
- Percent of savings?
- Subscription model?
- Something else?
- How will we prove ROI to first adopters without a track record?
- Initial target customer? large self-insured employers directly? Or TPAs who serve multiple employers?

My initial thought was to target SEIs directly. Why? You get more clients that way rather than a single TPA.

But i guess this logic is flawed. If we sell to a single TPA, we get access to ~50 companies' claims data with only one sale, one integration, one contract negotiation. Moreover, selling to a TPA might be easier — they understand the space deeply in a way that an SEI would not.

#### Technical Background

#### Go the Extra Mile

#### Founding Engineer Mindset

### Retrospective

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

## Interview 2

### Transcript

```
Hello? Hey. Hello.  How are you? Can you hear? Yeah, I can hear you fine.  How's it going, man? How are you? I'm doing all right.  I was. You're joined with a different name from your. It's Chris.  Oh, Chris. Yeah, yeah, sorry, my name's Chris. That's my Google username.  I have it. It's my name backwards. Oh, I see.  ICI. I guess I should have changed that in the. I see.  Oh, interesting. Interesting. Yeah, so how's it going, man?  How are you? I'm doing all right. Yeah.  Yeah, thank you for taking the time to speak to me today. No problem. I name is Ahmad and I am cofounder in CR, here at Vis.  I'm sure you stranger, right? Yeah, yeah. We spoke Thursday, I think, yeah.  Yeah, and he gave you like a note review of what we do, what we're trying to hire for and all of that. Yeah, he mentioned that you guys were hiring specifically for the recovery part. Yeah, kind of.  We're actually hiring a full-time, like, bonding engineer. Okay.. Like, it's.  Okay. Boss someone to joined me because there's so much to do and it's just me right now doing all the work, all the technical side of things. Yeah.  So we're trying to get someone to join. So why are you calling from today? I'm in Vetruz, Mexico.  Oh! How's that? How's going over there?  I's really fun. Yeah, it is. It's I mean, it's a great culture.  Everyone's like, so happy here and the food is amazing. My wife is Mexican. That's's why we're here. you live in Mexico?  No, I'm like, maybe like 50-50 between the U.S. and here. Actually, that was going to be one of my questions for you guys. I didn't know if, like, that was going to be a problem if I needed to spend more time in the U.S. or..  Yeah, interesting.erest. Yeah, so.. But I guess we can work that.  I mean, well, we can always talk about it because we currently do not have an office, even though we are looking to get one in San Francisco.. Yeah. Yeah.  So can you, it is supposed to be like a 15 minute call, so Okay. If you imagine giving me like an intro? Yeah, sure.  So on like a technical level, more so than dr of dog angel, likely. Yeah, okay. So yeah, I got I've got about nine years experience. in engineering.  I started with a company called DA Rank. They were gathering like online data and social data from social media PIs. They kind of get what people were saying about different products.  So when I joined there, they just kind of put me on data ingestion. So, yeah, I built out like a bot crawler framework to scrape forums, and I had another system for APIs. And then I moved to Seattle and got a job with a company called Simply Measured, and they were like they had a big micro service back in, so there was a lot bigger than the previous company, so there, yeah, I was mainly working on an API design, spending up microservices, spring boot, Java, Python, all of that.  And then my last technical role was that Octimier Denomine and Germany, and they hired me as a senior data engineer. They had like. So they were processing legal documents for IP data and they had this like weekly batch job that took a few days.  So they ended a faster. So I I set up Kafka and I moved them over to like a real-time event driven system so they get data in real time and provide other nice things like, you know, more comprehensive Unitest and like standard interfaces for new analytics. So that was nice.  And then after that, I pivoted and started my own little like app development company. So I've been working on some like educational mobile apps. It's something I wanted to do for a while. so it's been fun.  It's a new experience. I I never did Friend in Dev before, so it's interesting to see how JavaScript has evolves over here. I haven't used it like over a decades.  And so you're usingative now? Exactly, yeah. React Native.  S's. I mean, T scri can practically you anything with type scripts. Yeah.  Yeah. If you like typescript, it kind of like really, it put a harness on like, it got like guardrails on JavaScript. So you catch more er.  Yeah, it's. Tatch gear has become like. It's become like the the general language for everything.  You can literally build the maps, texttop apps, seven apps, Micros services. That's true. And the only thing is, with things like BON, it's actually just as fast as go.  But B, was it? Oh, you don't know Bond, right? It It's a rough time.  Like, no jazz. Ah, okay. Yeah, it's, um.  So, it's kind of interesting, yeah. Yeah. So how's I going so far with the with your compan so far?  Why are you looking for a different role outside that? Yeah. I've had a lot of fun doing it.  But like I said, it's something I wanted to do for a while. But I guess I am looking for a new role now because one, I want to work with other people again. You know, collaboration.  I do I learn more that way and do my best work that way. Two is that running my own company, I have to do, like, everything, marketing, sales, like, like finances and all that stuff. And and the front end of, too.  I was interesting, but I would like to focus on what I specialize in, which is the backend engineering.. And I guess aside from that, I also am looking for, you know, new problems to solve to keep growing as an engineer. Those are, I guess, the main three reasons.  That makes sense. That's fair. So generally, would you say front ends like your biggest challenge or out of all the previous roles you'veve held and all the previous projects you've done, what would you say is the most challenging at the same time, the most interesting for you?  Yeah, I would say Friday and Dev was up there because I still.. You know, it's changed the way I've thought about a lot of things because, you know, React, it's all. like the state is all encapsulated and within components and you kind of pass it around with the props. So, I mean, that's given me a new, you know, idea, modularity, that and the, oh, and like the ACinca weight pattern.  I really like that. So, um Before now, what did you Java and call me? Yeah, I used Cotlin a little bit in my job, but mostly Java and Python.  Those are my two big ones. So, Python has Isino, I guess, it doesn't have like a proper Ising stuff like or that or Tairi. Yeah, fair enough.  Have you Riy Have you explored using like state management libraries, like Leer Stan? Yeah, yeah, I'm using Zuand for I'm using that for my all the settings I store there. All right, fair enough.  So you generally.. generally won't have to worry about like a lot of state management inside components with. which you stand. Yeah, it's really it's really nice. You like to minimize state as much as possible because once you have a state, that's like that's just an invitation for errors.  So, yeah, the state management in react is amazing. I love it. Interesting.  So would you say that's like your, what would you say is like the most's interesting problem, like you have tackled in the past, technical problem? Aside of like the the issues you have with front hand that. I would say probably the work at Denimiers, I did it in Germany.  That was like the definitely the biggest project I ever ever took on because they only had like two of their back-end engineers and well, they also were they were more full stack. They weren't really back-end. So I was in charge of like all the data and so I pretty much had to do all of that work myself, standing up Kafka, and converting everything over from their batch job into the new real-time streaming system.  So. That was the thing that, yeah, that was probably the biggest project I work on probably my most proud of. Fair enough.  It's cult.. Kafka. Why did you choose Kafka, though?  So, yeah. Okay, in hindsight, it was probably overkill for what they were they were doing, because they so they were importing, I think between like 30 and 60 million legal documents weekly. So that's not.  That's a lot. Yeah, it's a lot. But I think Kafka is normally used for a much bigger scales.  Yeah, fair enough. So or the technology you have chosen instead of. So there's this, I think it was called Airflow.  I think it's it was a python. I was talking with another data scientist. He mentioned that.  I was like, okay, that's probably a lot simpler. I think it was called airflow. Yeah, airflow is Fflow has a pipeline, but it's mostly for uni ETL pipelines.  Yeah, so They weren't using it for like, they were just using it yeah, for that ETL and doing some analytics. So they weren't using Kafka for any sort of messaging or anything like that, async messaging, which is why I think there probably would have been another reason. I think there probably would have been a simpler solution.  But at the end of the day, it got the job done and it's much better than what they had. matches, yeah. At the end of the day. Yeah, so, did you do any research on what we do?  Do you have, like an OMU mobile? Yeah. and stuff? Okay, so youect errors in medical claims.  And as I understand it, there's basically two like places you can do that, you can do it pre adjudication or post- adjudication. Right now, you guys are post-adjudication. And I guess um an advantage doing pre-adjudication is, you know, a quicker turn around, you get faster ROI.  But you don't have access to, I think it's 837, 835 remittance data, which that would be, I guess, pretty useful for training. You need that for training the models. So I guess that would, I'm assuming that's why you guys are post adjudication now, but then I guess the downside with the post adjudication is you have to deal with the whole recovery process.  Yeah.. So I guess in a nutshell, am I tracking so far? Yeah, absolutely.  Okay. Absolutely. Yeah, you are.  So, yeah, that's very interesting. How do you feel about healthcare generally and.. Healthcare in the United States is terrible.  Do you think it's something you want to. It's it's a lot more difficult than it looks on the surface. Like stopping the issues and fixing the problems.  Yeah. It's actually a lot more complex than you can, you can imagine if you don' not have like insight information. So do you think healthcare dealing with healthcare?  I don't know if you've dealt with legacy systems before like old banking systems and all of that. Old banking systems are now. I have been heard legacy code, but not..  Yeah, like most of the legacy stands, like stanch from the late 80s and 90s. No, I haven't. Yeah, okay, so a lot of healthcare is beautiful one.  Kobok. Yeah, it's you have to, I mean, you don't have to interact directly with it, or you have to deal with theaces like that. And yeah it's it's it's an interesting challenge.  I don't think I don't know if you I don't you know much about what's going on behind the scenes but. Do you think it's something you'll be interested in? Yeah, absolutely.  I mean, I love that get on new challenges, so. You know, that's how how you grow. You keep learning new things, so trying to figure out complex systems is, you know, you keep getting better at it and better at it.  So you got to take on more complicated challenges. And also, I think, you know, this is, you guys are solving like,, like a real economic in efficiency here. So my last company is, you know, I was helping the marketers, like influence, get more data.  And at the end of the day, I was just like, okay, what am what am I doing this for? How is this helping anyone? But with, you know, with healthcare, you'rere helping like real people.  It's a real problem. And saves a lot of money, so. Yeah, it's something I could definitely get down with.  Definolutely. All right, that's fine. Thank you.  So do you have any questions for me? I think we're writing out the time. Yeah.  I do have. So. I guess a business type of question.  Angel mentioned that you guys are working with TPAs, which I guess makes sense because they have more clients than working with directly with a self-insured employer. So I guess what's the plan for new clients? Will you take on new TPAs or get new clients from the existing TPA that you're working with?  Oh, so we do plan to expand altit commercial health plans as well as government. Medicaid, Medicare are main focus. Okay.  And I will cover like millions of lives. Yeah. So that is our main.  Currently with TPAs, they cover like a large percentage of like employees. Okay? You get B. That's not where the real waste is.  There's a lot of waste. Yes, but they are incentivized and they're not really incentivized, but they try to at least try to find errors. But we say that Medicare, the fact that like it's government based and there is no incentive.  It's just government money. Exactly, exactly. Or care, you know?  Yeah. So there's so much more waste there and that is something we are gay, eventually. So that is really where the main problem is.  Okay. That is what we have we eventually. But obviously you need to have like a grad point, you know?  You start somewhere. So hence why we're standing with like self-insured employers. I mean, this is inside information, but I don't mind sharing it with.  Oh, yeah, I'm not going to. I going to tell him. Okay..  And I guess. Okay, so you guys are post- adjudication now. Is there any plan to move to the?  So we'll have like if we building like a full stack of software, full-sp, prepaid recovery. There are other things like HD and like, like the insurance flu itself and all of allies and everything else. So there's just so much to do.  Yeah. But yeah, we will do repaid as well. So the technology for post-paid directly applies to rebate.  Just that this post-paid con in batches of like a lot of claims one at a time. Okay. So that's that's like a, there's also the fact that you don't have access to like payment details, payment information on that Sp claim.  So the process of all detain is kind of different. It's more so hope. It's like, it's more like preventive than trying to like correct what has been done.  So it's, right. However, you're the line and the kind of errors you can find are practically kind of the same, almost the same. Okay.  Yeah. That makes sense. Yeah.  So, I guess a little follow-up. So will there always be a place for recovery, a posterjudication, even if you switched to? Okay.  That's. I will be always because it's it's also a lot easier to like, it's always a lot easier to get like help plans to just send all data that has been for now. So there's always room for post space.  And you know how much healthcare it's like every single day there, like billions and billions to deal away. Yeah. Yeah, there's always room for it.  Okay. So you guys are all in AWS or. Yes.  Yeah, we are all in on AWS right now. Okay. Yeah, absolutely.  All in on EWBS right now. However, we do have a couple of like data warehouses, which I'm not going to share on the score but we will have data warehouses outside it, yes. Okay.  Are you using like a custom pipeline, like with like spot EC2 instances for training or using. We're using spot ECT instances. We're not really using we're not using the offerings that AOness provides.  Sageemaker. Yeah, yeah, we're not using those right now, but Sagemaker is something we definitely will explore. We use it, but we are mostly doing everything, like Okay.  Yeah, I heard the cost is kind of tricky with Sage Maker since it covers like so many different services. Yeah, yeah. It's it's It gets very complex if you start to deal with AWS problems.  Yeah. Then it's sometimes a lot easier to just deal with Leonard's problems than eight of less problems. Yeah.  So, yeah. Let's see, what are So, yeah, I guess those were all my main questions I have right now.. Awesome.  Thank you very much, Chris. Thank you for taking the time to speak to me and you'll definitely get a feedback from us. Okay.  However, the next next step is. Okay. Sounds good.  Very nice to meet you, Ahmed. Yeah, you too, great. I look forward to hearing from you.  Have a good one, yeah. You too.
```

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

## Rejection

```
Hi Chris,

Thank you for taking the time to speak with us for the Founding Engineer role. Ahmad and I were impressed by your background, but just received so many applicants that we can't move forward with everybody. I wanted to get you feedback as soon as possible.

We’ll keep your information on file in case a future role opens up. Wishing you all the best!
```
