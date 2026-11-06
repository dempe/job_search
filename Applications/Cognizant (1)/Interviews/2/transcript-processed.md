**Ken:** Hello, Chris. Hey. Thank you very much for joining. Nice to see you. Very happy to see that you didn't have any issues trying to join. We already have the panelist here, Si Barash. He will be conducting the interview, and I'm going to live. Have a wonderful interview, both of you.

**Me:** Thanks, Ken. I had this good morning.

**Si:** Hi, good morning. How's it going?

**Me:** I'm doing all right.

**Si:** going good. Yeah, let me start the recording. Okay. Like before starting the procedure, could you please share your ID proof for the verification?

**Me:** Oh, um, yeah, hold on a second. Let me grab it. Oh, yeah, okay, okay. Uh, I guess a passport, okay. Anything, anything here.. What are you doing here? Okay, let's see. Okay, see, so my filters.

**Si:** Thank you.

**Me:** Oh, you can see it? Okay.

**Si:** That's okay. Yeah, yeah, I'm uh, this, uh, this, and you share your technical expertise in your last project and what role and responsibility you perform in your last project, uh, along with your technical expertise.

**Me:** Yeah, um, well, right now I'm running my own sort of like contracting business, so I've been doing like a lot of, um, ADS work and, um, building, uh, some like no JS back-end apps. Um, so that was the last technical project that I've done was, um, Let's see, it was a, um, NoJS app for, so a client wanted to change their, um, their billing provider. They had a Shopify store, and for whatever reason, they couldn't use stripe, which it degrates naturally. So they needed to use a different provider and basically I needed to set up an app that would, um, communicate the payment information with the provider and update Shopify so the orders can be marked as paid or avoided or refunded, canceled, whatever. Um, so basically it was, it was mostly a web hook that uh, communicated between the payment provider and Shopify.

**Si:** So, currently, uh, uh, you open no JS also. Okay.

**Me:** Yeah, um, so yeah, I use that because, um, as it seems to work pretty nicely, like with, because they're using Shopify, like I mentioned, so it works pretty nicely. I think they have, like, there's a Shopify, like, set up that, and I think that's, they recommend the NoGS for their app. So that's that's why I went with that.

**Si:** Well, we won't allow many years of experience to have this...

**Me:** Um, so I have about 11 years total. I started in 2012. Um, including internships. So I was doing internships in 2012. Um, and then I started full-time as a regular employee in 2013. Um, I did take a few years off to go teach English. Back in like 2019 through 20, no, 2018 through 2021. And I went to Germany and, um, they hired me as a, um, as a senior data engineer there. So there I was mostly working in Java and Python, and, um, That's where I helped them set up like a, so they had a batch job that was really, um, janky and when like crash all the time. Um, and sometimes it would take like, it'd take at least 2 days to run. Sometimes it would take almost up to a week. So it would conflict with the next week's back job. So. I, um, set, set up a new system for a, um, a real time event driven system using coffee streams, because the data was coming in continuously, so it didn't actually, we didn't get any advantage from using the batch job in the 1st place. So. Yeah, I set that up for them. that was in Java. We were using caucus streams.

**Si:** Okay. Yeah, good shot. So you work on spring boot, right? You have experience on spring boot.

**Me:** Yeah, um, my 2nd job, I used a lot of spring boot because they were like a big micro. had a big microservice back in. So like when we was out of new microservices, they were pretty much all in spring boot. I think we had a few go and Python, but pretty much all of them were. Using spring group to communicate with the rest APIs, they're communicating synchronously, most of them. We did also have asynchronous communication using Kafka. That's where I learned about Kafka.

**Si:** Okay. I mean, it's pretty good, right? So, um, we have a lot of annotations like uh, Autoway, required, a lot of annotations are there. While starting up the Stringboot, right? What these foundations will do, how the application will have, can it please go, share the views technically? The... So I am with the LA man. I'm just, you know, just developing his pin boot application. You're using a lot of annotations and then, right? The application is starting up. So what is the purpose of these annotation and what is the usage of that and what it will do internally and how the application will up, how the services will help? Could you please elaborate the technically?

**Me:** Oh, okay. Um, so I guess, yeah, the biggest one is auto-wired, uh, which basically tells, you mark a component as auto-wired to tell the spring boot that it will be used, um, Um, so you have it set up in your configuration file to, um, for certain properties and auto wire will tell it to, um, use this component. Um, so, I remember, that actually started moving away from using auto wired and just having the, um, annotations in the constructor and just, Yeah, wiring them up that way, I think, oh yeah, we, I would instantiate them specifically in the, um, in the configuration file with the, with the arguments that they need. And then I would put the, So, yeah, it's been it's been a while since I used Springboot. I'm sure I could get up to it quickly, but I remember I put the annotations on the constructor because that was avoiding, um, Yeah, I guess when you're using auto wide, you don't have the direct control over, okay, I'm going to use this component. And so I remember when I put the annotations on the constructor and then wired it up explicitly, then we had it. I guess more control, more explicit control, we knew exactly what was happening. If there was ever an issue or a bug or something. Um, those, that was a, let me see. So yeah, we then we have like component annotations, um, The main configuration annotation for the configuration file, and let's see. Yeah, like I said, it's been a, it's been many years since I've used spring boot, but those are the, the main ones like.

**Si:** Okay. Um, so have we worked on Microservices, uh, uh, our platform? I go services, uh, you have any Microsoft experience?

**Me:** Yeah, that was my my 2nd job. They were really big. They had a big micro services back end.

**Si:** So will you communicate, um, so I have, I am Microsovices, CAU, Microsovices, B, and I have CET, and E, something like that, uh, 5 or 6 microsovers, so there. So VA wants to retrieve some information from B or C or D. How what kind of communication mechanism used in your project?

**Me:** Um, so if you want to communicate, I guess individually with each, um, I guess, as it depends on,

**Si:** I am, uh, maybe I will give you some example, right? I am the customer service, you are the auto service. So customer service, I just want to know, what are the orders are mapped to my customer ID? I just want to receive some more details from you. And then write pay some payment details or amount details or car details from some other Microsoft.

**Me:** Okay, so you need to aggregate these different

**Si:** Okay. So why would you communicate with each other and what kind of security mechanism you place for the communication?

**Me:** Okay, in that case, I would probably use just a simple rest API to pull from those. And maybe we have, you know, some sort of a low balance earn or something in front of them. Um, So, yeah, I guess we would then call out to the, I guess, the payment, information service, the customer information service, and then we could aggregate that information there within the in memory and logic. Um, Yeah, I guess we would, you know, use standard ACTPS. Um, for, I guess, bigger things, like, so in this case, I'm saying rest API, because I guess the 2 main types of communication would be synchronous and asynchronous. Um, but this case, I think it would make more sense to use the, just the synchronous communication over HTTB rest, uh, for, because it's, we're the, we're the, we're the ones who know when we need the customer information, for example. So it's not something that would make sense to have a have a cue. That's where, I guess, when stuff, now, on the other end, maybe if stuff is coming in, like requests, whatever inch initiated this, then maybe we can have a queue, then this, the service that we're talking about, we could read from that queue, or that message bus. Does that make sense?

**Si:** Okay. So what are the wicks we have? So you mentioned, you will call VRS JP, right? So I am Microsoft one. So if I want to call Microsoft B to, uh, uh, for, uh, call the case JPN is, what are the ways we have uh, technically, right? For example, we have wrist template, right? One way, we will call the AP, right? So likewise, what are the other options we have and which one you use in your application?

**Me:** Uh, sorry, I'm not following which... Which ways do we have for?

**Si:** Oh, for example, you have mentioned, you will, uh, if it is a synchronous way, right? You will call it as a STAPA and you will call the SKPA, right?

**Me:** Okay, yeah.

**Si:** You have mentioned it, right? So there are many ways to call the rest AP, right, from Microsoft one, right? I want to call, uh, decree some information from Microsavice too. Uh, We are STAPI. For example, I can use this template. That is one of the, uh, APA we have or utility we have to uh, call the rest APA. Likewise, do you know about some other methodology to trigger or call the recipe?

**Me:** Um, So I mean like what, so to trigger it or... You mean like?

**Si:** Are you, are you, are you call, uh, RCP from your microservice?

**Me:** Um, we, I would just call it over HCGB that it hit the, uh, we would call it in particular endpoint on the API and.

**Si:** And that's, that's a plain statement, right? Internally, right? You may use some APA or frameworker to call it, right, in spring boot.

**Me:** Oh. Okay, um, What, what, so what framework would I use within spring boot to set up the API?

**Si:** Yeah, give one on sample. Like, this stimulate is one of the, um, the APA which we have, uh, to use are called the best services, right? Uh-huh. Likewise, are you aware of any other stuff?

**Me:** Um, no, I guess I, I mean, sorry, are you showing me a temple?

**Si:** No, I just telling you, resting plate is the one, which is available in spring, right?

**Me:** Oh, okay. Um, so within spring, are there other templates to use for setting up an API?

**Si:** You call the APA, yeah. They will call the.

**Me:** Um, So, let's see, yeah, as, uh, it's honestly been quite a while since I've used spring boot. I don't remember other options.

**Si:** No problem. So, yeah, mentioned you worked on craft custom streams, right? for, you know, A and Raven. So it's the same way, right? Instead of going to go in a synchronous way, right? If I am taking up the option to go with asynchronous way, consider I'm using a Kafka topic for the communication between the Microservices. So what are the things I have to do as a producer as well as a consumer to post the message to a topic, as well as say, to consume a message from a topic?

**Me:** Um, well, I guess the, the biggest thing 1st is to get your, um, uh, topic IDs and partition IDs, make sure you have a, um, a setting system for that and enough partitions because that's the, um, it can be, if you start out with too many part- too many partitions, it's okay. It's easy to expand, but it's very difficult to increase the partitions later because you have to change the the IDs. Um, so that would be, I guess, the biggest thing to start first. What are we going to use for the topic ID and how we're going to set up the partitions? But yeah, I mean, I guess another nice thing is have a, like a schema registry because, you know, the producers and the consumers, they communicate and just rob ites. So we need, um, It's nice to have, like, a centralized way to have the what schema we're using, a suit, presumably JSON or maybe something faster, some binary, um, format. But yeah, so then I guess the producers, the consumers would cash the schema on their, uh, in memory so that, you know, the, um, how to, um, serialize or derealize the messages. Um, So, yeah, I guess, um, then stuff would collect in a topic and then we could have, then you would have producers and they would be polling the topic, okay, are there new messages? So, then retrieve them and continue bowling. Um, Yeah. So, I would, yeah, we did have some, um, coffee mascaging at my 2nd job of using it in that capacity, but then, you know, also Kafka works as, um, just a stream processor. Which was the capacity that I was using in my previous job.

**Si:** Okay. So what are the issues you faced, oil, as a consumer, right, while consuming it, you are trying to consume a message from golf for topic in your UAT phase or in your production phase, right? What are the issues you face and how you handle those issues retrospective to Kafka communication?

**Me:** Um, I guess the most common issue is a bad message or maybe malformed or incomplete. Um, for that case, we I do definitely, that's one of the very nice things about using the stream processing is because we don't have to halt the processing of all the other messages instead of like a batch job that would just crash. So we can have like a separate dead letter queue and just put the bad messages there. And then later go back and retrieve them and figure out what went wrong and then fix the system so this air doesn't happen again or if it was just literally the producer sent us a bad message. Um, then we can just drop it. But, um, So handling bad messages gracefully, that's a common problem. I guess another thing to consider is, um, Do we want, uh, Like, Was it, I forget the name, but, uh, like, one time, like, when it process, how many times do we, can we process the message? Is it identpotent? Um, If, if not, then we need to compact the message. Like what if a different message comes in with the same data later? How do we handle that? Um, So for that, you can use, for example, compaction to make just only the latest message apply. Orby's a superset of, for example, of different messages have different, um, different parts of the data, but they have the same topic key. We can squash those into a single one. Um, So, yeah, I guess those are the some of the main things we need to work out.

**Si:** Okay. So we have mentioned, so sometimes, right, we are seeing a consumer lag, right? For example, in your lens portal, you are seeing for the particular topic, you're seeing a consumer lab, and messages are piling up. So at this time, these kind of scenarios, right? What mitigation you will do to reduce the consumer lack?

**Me:** Um, so that's a that's a good question. We didn't, haven't dealt with this problem luckily, but let's, so, but in this case, um, Maybe, well, let's see. I guess we would need to figure out where the cause of the of the increased processing time is happening. Is it happening because, um, is it memory bound or is it, um, is it because look up time, um, Maybe we need more partitions, maybe the topic is not, um, partitioned enough. So those are some of the things to start looking at. Are the consumers, you can also, I guess, look in the consumer side. How are the consumers? Do we need more consumers or how quickly are they processing them? Um, So I guess those are some of the things I would start looking at in that in that case. So I guess, yeah, the big, the big, the, the big dog goes over, overall ideas. Do we need to increase the producers or the consumers or both or the partitions?

**Si:** Okay. So, um, you have worked on Java situation?

**Me:** Sorry?

**Si:** You have experience on which Java version?

**Me:** I think, so the last one that, so we were, last one I used was, I think, 17. I know I used 11, but yeah, I think.

**Si:** So what is what is what is the main features in Java 17 year compared to previous version?

**Me:** Um, I think the big one is, I'm pretty sure that's the one where they introduced modules, like native Java module. I'm pretty sure that was the version. Let's see what if I... Um, I'm not. I can't think of any specific features. I haven't really kept up too much with it, but I remember, I do read the new, the new releases when they come out. And it seems to me like they're mostly what they're doing is, I guess, because after Cotland came out with all of the new, like, uh, simplified syntax, it seems like Java is trying to import more of those features into, into their, Oh, yeah, I remember that they have data classes now. So that's really nice. So you don't have to let those boilerplates. What else was it?

**Si:** Okay. So you're a man of, uh, uh, uh, steams concept, you have any hands on that part? The streams.

**Me:** Yeah. Yeah. teams. Yeah, um, just basically, um, it's kind of like pseudo-functional programming, so you have a collection and you can make a stream on it and you can put, um, apply different processing to the collection, um, to map it to like a different output. And then collect it into a new collection. It's, I guess, a concise way of doing...

**Si:** I will give one.

**Me:** Sorry, sorry you cut out there a little bit. Your audio.

**Si:** So how confident you are? Can you write a snippet for that? Maybe I will give you one problem. I just need the steel skip it alone. Okay. Yeah. Can you, yeah, can you share your screen and write a snippet? Okay. Maybe write what we can. Yeah, consider I am having numbers, right? 10, 11, 21, 30 on something like that. 41. These are the 5 numbers I have.

**Me:** 10, 11, 31, 41.

**Si:** 10, 11, 21, 31, 41. Okay. I just want to know, all right, um... I just want to know or pick the numbers, which is starting from, starts with one. Okay. Yeah. Using steam's concept, just try to skip it.

**Me:** Okay, can I... Yeah. won't be a share my...

**Si:** Yeah, you can share it.

**Me:** Let's see. Sure, here we go.

**Si:** Okay, no, the entire screen.

**Me:** Okay, all right, can you see that yet?

**Si:** Yeah, I went to CST.

**Me:** Okay, um, I don't have. Let me see here.

**Si:** And if you have a notepad, I also find, no, just I just need a steak at you. Okay. Okay.

**Me:** So let's see, so we have, so we'll have some collection. Let's call it. That streams. And let's see, we'll do... So, um, so it's gonna be, it's a collection of integers, right?

**Si:** Yeah, yeah, yeah, maybe, yeah, well, or, or are we, whatever, right you can have it? This is the number set. I just want to filter out I want to pick the numbers which starts with one. Okay.

**Me:** Um, okay, so I'll map, um, X dot to string. And then, um, it would be something like filter. X. I believe there's a method starts with. And then I think there's, um, yeah, collect, whoops. Collect, something like that. And I guess I'd format it a little bit. Okay. Okay. Are you able to see that?

**Si:** Yeah, yeah, sounds good. yeah. So same way, right? Maybe we can take your name, Christopher. Um, I just want to know each character, right? How many instances are coming in the particular state? Maybe like this, if you take C, right? You have only one instance, which means you have 2 occurrences, right? which is having 2 Something like that, I want to know. Um, Using steams, yeah.

**Me:** Okay, what do you actually, what do you want to know?

**Si:** Um, take this string, pistol fill. Okay, Christopher. I just want to know in each, each character or many instances or occurrences available in this string.

**Me:** Okay, so we went to convert this to account of

**Si:** Yeah. Okay. waiter on sample, right? If it is C character means you have only one occurrence, it means you have 2 weapons. Maybe something like that, right? I just want to know.

**Me:** Okay, um, Do we so you do want this to be a map of a character to account?

**Si:** Uh, anyway, uh, end of the day, right? I just need a result like this, uh, H2. It's good. RH one.

**Me:** For some reason. Oh, yeah. Okay. Is it, for some reason, I can't go back to the the browser. Like if you're showing something, I can't.

**Si:** Oh, not a problem, not a problem. You can open a new notepad, that's fine, yeah.

**Me:** Okay, well, let's see. Um, so...

**Si:** I, are they able to see the thing, the team chatter pink?

**Me:** No, for some reason, I can't pull up the chat. I don't know. when I can't pull up the I can't pull up the window. don't know. Okay, here we go, here we go.

**Si:** We're back We chat, yeah. One starts with one, Christopher. Okay. Yeah, yeah. I need a result like this, yeah, yeah. Okay.

**Me:** A map of the, so, um, Let's see. So, um, so I believe we can call stream directly on this, no, because string string will be an object, so we need to do, um, I guess what is it? 2 character array? Something like I think that's what it's called. But then we need, uh, new, uh, array. That. Okay, string. Yeah. Okay, normally I would format this like, as above, but like, uh, So, okay, stream. Now, I know I could have done this very easily a few years ago, but it's been so long since I've used, I believe there's... So I'm not sure. I know there's account method, um, Mm-mm. Because another thing is we need to, it needs to return, um, a map of each character to the count. I, I, I can't, I can't remember off the top of my head how to do this. Yeah, I'm sure I could get up to speed very quickly, and this is something I could have done very easily about 10 years ago, but it's been a while since I've used Java as my main language.

**Si:** Okay, okay, okay. Have you watched any cloud, um, just?

**Me:** Yeah, um, I'm working on some ADS. Well, I have worked on some ADS projects recently.

**Si:** So you usually any what features of AWSE used in your project?

**Me:** Um, so mostly serverless. I set up cervolus pipelines, just for like low maintenance type of jobs. Um, that run continuously. Um, I also um, helped a client set up their an EC2 instance. Um, I helped a client migrate to uh, Cloudfront, NS3 because they, they had, they needed to serve a bunch of data and they wanted to put that data on a, uh, a CDN. Well, I suggested they put it on a CDN and so we suggested cloudfront for that. Okay, so I guess those are, yeah, the main ones I've used. I've used some RDS, not recently.

**Si:** Have you used any JA tools in your development?

**Me:** Yeah, I, I, I, I think you have kind of have to these days to stay up. So, um, I have a pretty, like, pretty good pipeline that I've been working on that's basically, my problem solved, so I have 4 main problems solving steps that I've been using for many years. The 1st is to really understand the problem, which means basically understanding the requirements, the functional requirements, nonfunctional requirements, constraints, assumptions, all of that. That's what I mean to really understand the problem. And then after that, uh, come up with an implementation plan for the problem that satisfies all the requirements, then actually execute your plan and then review and test. And, I mean, obviously this is not something I use for every little thing that I do, but for whenever it leaves like a big issue or something that I can't figure out, those are the main 4 steps that I do. And, uh, with AI, um, So yes, the technologies, the tools that we're using have changed a lot, but we're still, at the end of the day, we're still solving problems. So it's still, so I basically translated that in those 4 my main 4 problem, solving steps into an AI pipeline, which does the same thing, determine the requirements, given a problem statement. And that normally requires a lot of back and forth to really understand, um, to understand the problem, what the requirements are, and then we go into implementation planning. And this also requires, you know, some back and forth. Sometimes I have to go back to the client because the AI brings up a good point. Okay, maybe we don't know this, we need to figure out what does a client really want here? And those are the 2 biggest steps. So, because all the, you know, the back and forth and the thinking and Um, after those 2 steps, normally the implementation goes pretty smoothly. We just go follow the plane that we made. And and then do a final review step to make sure that everything, all the requirements have been fulfilled. Um, and one thing that I do is, um, I put it in, uh, just a general, like, uh, dot agents, directory, and the project folder, which I will sometimes, uh, if it's a client project, I'll exclude that from, from get, ignorant. Uh, but this makes it agent agnostic, so they're all writing in markdown file, so where one agent finishes, another agent can just pick up. That way, for like the really hard things, I can use cloud code or or something, and then I can use a cheaper model for the less demanding task, like deep seek.

**Si:** Okay. okay, got it. How you deployed your application? You have as a plain team or, Are you worked uh, into in uh, till deployment?

**Me:** Um, so sorry if I've worked on like end-to-end deployment?

**Si:** Yeah, so you have downloaded your application and QA has been validated. So, uh, 3 production deployment, right? You have to you have to deploy or you have a separate team to do the deployment stuff.

**Me:** Oh no, I've, yeah, I've mostly set up the deploys. Mostly lately I've been working a lot on Hiroku, so I just hook that directly up to GetHub and deploy that way. For the AWES stuff, um, I've been using, um, infrastructure as code, so all the several stuff I write in Sam, that way I can put it in version control and then I can, I can run that on GitHub and have a CICD there. Um, it's also, I'm sorry.

**Si:** Then you were, uh, with the ACD script, or what, what tool you have instead?

**Me:** Um, I'm also been using GitHub action, just use GitHub actions to, um, I guess, run tests to make sure 1st make sure it works. If something fails, then we, um, cancel the deploy. Otherwise, just go through with that. Um, I install, um, you know, the 80 best tools that we need to deploy it. And Yeah. Oh, another thing that I found really recently got into was it's called Nick's. Have you heard of Nick's? It's like, uh, it's basically like infrastructure is code, but for your personal computer. So they have like a full operating system, but, um, for example, my resume, I build that from, um, from latex, and it, you know, generates a PDF, and I was never confident in, um, the CICD, um, building the exact PDF. I went to see the PDF before it goes live. I just was, um, what do you call it? Paranoid. Um, However, uh, with Nick's, basically, it gives you a, so all of the packages are get very long hash strings. They hash everything, they take the source code, the compiler that you use, the compiler flags, everything, they make it into one hash, and then every every dependency you use in your project, all of these get hashed together, so you know that, like, cryptographically, you know that it's going to be the same build. So, finally, I got the confidence to put that in, um, in my CICD pipeline. So I just run Nicks and I get to have actions and I can verify it's the exact same build.

**Si:** Another nice open source too.

**Me:** Um, yeah, I've done some open source development. I made a little, um, I made a static site generator based off of Lauraville. So my blog is a static site, and then I set up another site for my company, and I wanted to kind of unify those that experience. So I made a tool, a PHP called Scabbard.

**Si:** Okay. Yakrish, I think they have covered the areas. Yeah, I have covered my part. Do you have anything to ask?

**Me:** Um, yeah, so I guess, um, I guess the general questions. Can you give me an idea of the role will be? Will I be working with you? Would you be the manager? Um, is there, what's the team size?

**Si:** Yeah, this is for a different team. I'm just taking the technical evaluation. So this is for one of the retail giant barrows management system related product, where we have, right, all the latest text track in place like Java 21, Springwood, Microsovers, Kafka, Ashur, Ajur, Cloud, Ajur, Skill, and then right, some components may use GCP. Mm-hmm. Yeah, and since then we have, yeah, taps or 100, sorry, Android apps.

**Me:** Okay.

**Si:** So all the latest tech tag game page for that product.

**Me:** So you guys are using both Azure and GCP.

**Si:** Yeah, need or need-based, right? Some some like some applications using GCP and some using...

**Me:** Nice. And for the Android apps, what framework are you using?

**Si:** I'm not aware of that fantastic, yeah. Yeah, but yeah, they basically they are building the react by react, right? They're building their apps, and then they write, they're deploying in to the under activations.

**Me:** Okay. Um... Okay. So you asked me the Genai question. How are you guys using AI?

**Si:** We have a, you know, so a AA tool, which is, right, a builder, which is using Claude, Sonet, and then like this model has been, right? This tool has been, right, rain will to support the inos needs, right? And all the reports has been right trained and then right, according to the architecture standards of the in-house, right? It will provide the accurate, authorize 80, 90, 85 percentage or 80 percentage, accurate suggestion, and then the data developers are using the mostly predominantly, all boys, right? They are requesting us to use that particular tool for the development or enhancement. before starting on our own, yeah.

**Me:** Okay. One really nice thing that I've noticed about, um, AIs is, so I've always wanted to do more like test driven development. Um, but it's always been, you know, kind of a little bit of extra upfront work that I didn't want to do, but now with AI, it's much more, I mean, much more viable solution, at least for me, just tell it to write some tests. And that also works a lot really well for the continuous deployment, to always run those tests. Have you guys, what type of testing methodologies are you guys using? Do you guys use any of that?

**Si:** Yeah, we have a writer, so as a developer, right, you know, you will have a Jaini disk cases to cover a paper, feature validation, as well as whatever changes you are doing. At 1st level, right? You need to see because Jaini testing will be covered. And then we have automation script, right? Whenever the deployment is tickering on, we have feature level validation overall, right? Using a cucumber framework. We are future level validations, which is right binded with your pipeline. So if that is any of the cases is failing because of your changes or your PR, it will block the deployment and rate there, the corresponding developer has to fix the disk case before proceeding further. Yeah. So we have that framework in place so that we are really missing the difference in the production can be run.

**Me:** Ah, okay, nice. So is, uh, so this will be, this is for a backendroll. How does it work? How was the collaboration with, I guess, front end or design or product or other teams? And which teams is it called?

**Si:** Economically, this is for a backendage, whatever developer role, right? You will be working directly with client, client, will provide the task. The day-to-day data are still basis. Okay. So you have to work and complete the task and deliver it to them. Basically, individual developer role. You have a T, but everyone will collaborate with the client, right? A client will give the tasks, yeah.

**Me:** Okay, that makes sense. So then my, uh, I've been working a lot directly with clients now that I've been working with contractors. I'm used to... Okay. Um, I guess is this a new role that's opening up? Or is it a replacement?

**Si:** So this is like a and sing a team, which all in the team was there. So there's a stand and see the team.

**Me:** Okay. Um, I guess those were my main questions for now. Yeah. Did you have...

**Si:** Okay. Yeah. Thank you.

**Me:** Thanks for your time, to see.

**Si:** Well, thank you. Have a good one
