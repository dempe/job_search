---
type: job
applied: 2025-12-04
interviews:
  - 2025-12-08 11:00
status: rejected
job_type: fulltime
source: indeed
position: Solutions Architect
contract: true
remote: true
4day: false
industry:
website:
location: Hartford, CN
company_size:
channel: form
listing:
blog:
correspondence:
compensation: $68 - $75 an hour
title: Onward Search
date_created: "2026-10-13 12:09"
date_modified: "2026-10-21 18:10"
---

## Application

Nothing to see here. Standard application without any option for customization. They're going to check my resume and portfolio. If I match, they'll set up a interview with an AI. Great.

## Interview

### Transcript

```
Hello? Hello? We look forward to get to know you better.  This quick interview is your chance to showcase your skills and personality. Rest assured, an onward search recruiter will carefully review your responses along with your full app application to assess your fit for the ral. We're excited to see what you bring to the table.  Let's get started. Hey, sounds good. All right, thanks for being ready.  To start us off, can you tell me are you legally authorized to work in the United States without sponsorship? Yes, I am. Awesome.  Thanks for confirming that. Let's move on. Could you describe an end to end architecture you designed for integrating multiple enterprise systems?  Why were the chosen patterns the best fit? Yeah, so, at my previous job, I worked at a startup company called Octamine, and we needed to process a bunch of legal, well, analytics on patent data. So they had a batch job in place that took around 48 hours, which was a long time, but in addition to that, the data was coming in consistently.  So it didn't really make sense to run it in batch, it would make more sense to just process the data as it came in. So I set up a an ETL pipeline based on Apachik Kafka that processed the data in real time and also did things like analytics on the data and put the data into elastic search so that we so the customers are API and the.. Setting up an ETLipeline with real time capabilities must have been been quite the shift for the team, sounds like it made a big impact.  I'd love to dig it a little deeper. What were some of this specific patterns you used in that architecture? For example, were there key design decisions around things like fault tolerance or data scaling?  So I used Apache Kafka, and that has things like fault tolerance built in. But I guess the system as a whole used an event driven architecture since the data coming in were the events which were added to the Kafka que and that initiated the whole whole pipeline. In terms of actual code patterns, it was all written all of our Kafka streams processes were written in Java.  So I used inheritance and standard interfaces for implementing things like different analytics. Ah, I see. Using Apache Cask's built in fault tolerance and an event driven architecture makes a lot of sense for processing incoming data in real time.  And layering that with jogg for the student processor sounds pretty robust. All right, let's keep going. What was the most difficult software development project you have been involved in?  I guess recently, so I've started my own company to build mobile apps. It's something I wanted to do for a while just to explore that. But the thing is, I've worked as a back end engineer, pretty much my whole career.  So I had to learn all the front end from scratch. So that was that was a lot of work, but it was fun and I learned a lot. JavaScript has evolved quite a bit since I used the last well over a decade ago.  So, I mean, a lot of the patterns that they use in JavaScript, they make really accessible, like a sink a wave. The extreme modularization each component is its own has its own state, which you pass around via props. All of those patterns, I think have helped me grow as a back end engineer as well.  Oh, wow, that's impressive. Jumping into mobile act development and learning slight ends from scratch is no small feat, especially after years and back end. It must have been a huge shift both technically and creatively.  All right, building on that what's your experience with agile methodologies? So pretty much all the teams I've worked for have used agile. I've worked with one week sprint and two week sprints.  And I think it helps the company a lot, you know, just to define what's actually needed and try and make these into workable chunks. And also the whole estimation process, I know that it gets a lot of tension and backlash, but I think it's good to sometimes, you know, reflect on these things. Like, what does the task actually require?  And the estimation process forces you to do that. Right. That's a solidid take.  It's great that you' worked in with agile frameworks. Those estimations and sprint retrospects do help refine the process. Let's dive into something a bit broader now.  What is your architectural or technical exam with native systems, especially with AWS and GCP and their c offerings? So I have a lot of experience with ADS. I've used it at, um two my previous employers now.  All of my all the back into my personal company is running on AS Servculus, Lambda, Dynamo DB, ABI Gateway, and it's all defined in sand templates for infrastructure as code. I haven't used other cloud providers like DCP or Azure, but I'm sure that the topics will translate very easily. Yes, I have an extensive experience, cloud experience with Aabas specifically.  Wow. It sounds like you really died deep into AWS, especially with silverless setups, Landa, Dyno DV, and API Gateway are powerful tools for fully scable systems. And defining infrastructure with sand templates certainly adds to your expertise in modern cloud practices.  All right, do you have any questions for me? Yeah, can you tell me a little bit more about the role, how will I be what's considered success for this role? Great This is for Sutions architect with a leading healthc company, and it's a fully remote position based out of Hartford, Connecticut.  Your success in this role would involve collaborating withakeers like product own, business analysts, and technical leads to refineed requirements and delivery exemplary solution artifacts. You need to utilize your expertise in systems, integration, design, and development of complex systems to ensure efficient and effective solutions. Success may also be measured your ability to work seamless in an agile environment.  Communicate clearly across teams and implement modern technologies such as Java, JavaScript like AWS. Anything else you'd like to know? Could you go into any more specific details on their tech stack?  What do they have? Honestly, I don't have the full detailed breakdown of their text app for this role. From what's been shared, their environment uses modern technologies like Java, JavaScript, and cloud Serv, specifically AWWS, and GCP.  And you'd likely be working with those as core moments. If you'd like to know more, the recruiter can share more specifics when you reach the next stage. Anything else you're curious about?  Oh, I guess most of my other questions were specific to the role. I'm not sure how much you know. I guess how are the.  Can you tell me, you know how the teams are structured? How do they are architecture decisions made? Because I'm assuming as a solution architect, I'll be a big part in that decision-making process, so I'd like to know a little bit more about how that would work.  That's a really thoughtful question. While I don't have the exact details on how their teams are structured or how architecture decisions are made, given the role of the solutions architect, you'll definitely play a significant part in shaping those processes. Generally, architects leads heavily with stakeholders, like productors and technical leads to guide decisions and insure alignment with business goals.  The recruiter will have more specifics on their team dynamics and decision structure. Is there anything else you're wondering about? I know, I guess that's all.  I mean, I'll say I'll save the more specific questions for the recruiter. Thank you. Got it.  Thanks so much for your time and thoughtful responses. And onward search recruiter will review your interview and full profile shortly. We're excited about the possibility of working together.  Great job and talk to you soon. Okay, thank you.
```

### Preparation

This will be my first non-test AI interview. Shows how much they really care. I guess it's just a volume issue. I think it will probably be just a bunch of behavioral questions. I'll study up on those. Maybe things like "describe a time you had to make a difficult tradeoff."

### Retrospective

> Describe a time when you integrated various different enterprise solutions

I responded with my go-to Kafka pipeline story. I didn't freeze, but I think I missed the mark a bit. They were concerned with *integrations* of various different technology. Also, my response was a bit long-winded. The AI actually cut me off, which it doesn't normally do because, with this program, you had to hit the spacebar to indicate that you were done speaking.

### What Went well

- Had answers for all of their questions
- No long pauses
- Gave examples
- I think my "flow" of speech is getting better overall. I speak more fluently that when I first started interviewing.

### What Could Be Improved

- Need to tailor my responses more the question being asked
	- E.g., the "integration" question. I should have emphasized integration more. Rather, I just talked about what I did. A cool project, but not precisely what they were asking for.
- Need to reduce "uhh"s and "umm"s
- I say "I guess" a lot. Need to stop that.
