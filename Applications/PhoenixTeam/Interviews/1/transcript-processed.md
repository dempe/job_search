**Justin:** Hello? Hello? Hello, Chris.

**Me:** Hey. How's it going?

**Justin:** Good, how are you?

**Me:** I'm doing pretty good. This got back from my morning run, so...

**Justin:** How was that?

**Me:** Pretty good. I went 40 minutes today.

**Justin:** What's that?

**Me:** I go by time, not distance. So I did 40 minutes.

**Justin:** Dang, dude. That's good. I'm just starting back up the couch to 5K. Oh, nice. To get that going, because I've been I've been sitting in the chair for way too long.

**Me:** It happens. Yeah. Yeah.

**Justin:** It's Ryan. Hey, Ray. He just finished a, he just finished a run, so I'm just gonna, I don't know if you run, Ryan, but I don't, so definitely I got the humbled.

**Ryan:** I don't run very fast or very far. I need to, I could run. Long, it's faster than me, right?

**Me:** That's what they say, right? You know, you don't have to outrun the bear, just, just, basically.

**Ryan:** That's awesome. Ugh. All right. Are we waiting for anybody else, sir?

**Justin:** I don't think so. I kind of kicked this off, and then saw you join, so you're a better kicker offer than me.

**Ryan:** Norris, Chris, thank you for taking the time to chat with us today. We definitely appreciate it. Obviously, we're talking about AI engineering and everything like that. But we like to kind of start off with getting a fuel for what some of your background is. And given that AI is so new, like, what was your path before AI and how did you make the jump to AI?

**Me:** Yeah, um, so I've been back in engineers since, well, I 1st started professionally in 2013. So it's been a while. I started out in data acquisition. Um, I set up some like distributed, um, frameworks. Well, 2 frameworks at my 1st company, one for like a web scraping framework, that was in Java. And then like a sister framework for pulling data from APIs, which was also in Java. After that, I worked in microservices, like setting up microservices, an API gateway, API design. Most of that was in Java, some go, and Python. Um, and then my next job, I, my main task was converting this, um, old janky batch job in Python over to, um, a real-time event driven system in Coffee Streams. Um, that was also in Java. We were pulling data from our post-gressed data warehouse and putting it into elastic search, which fed our API and UI. Um, And that's that was in 22, 2022. After that, it started my own company, started building some apps and doing some contracting, and that's kind of when AI started to become a thing. And at 1st I tried it out, you know, back in, I guess 2024, it was still not that great. Like, there's a failing unitized. Oh, delete the unit test. So, um, I didn't really start using it heavily, I guess, until 2025 last year. And then this year, I am almost exclusively AI. I do have, I do write some manual code, but, um, 

**Justin:** Yeah, I mean, who's writing code by hand these days?

**Ryan:** All right, Justin. You win the prize on that one, but yeah, I mean, like, it's incredible, the efficiency is that you can gain through, like, leveraging AI, and that's that's what we're all about. We're all about trying to move fast, stay on the cutting edge because obviously this AI stuff is ever changing and disrupting industries no matter where it touches. Um, Talking about like AI tools and everything, it sounds like you've been in the weeds, like working in code, building things. And you walk me through, maybe something that you built that you're most proud of. Like if you had to pick like one thing that you've built, um, what's what you're most proud of and how was AI involved in building it?

**Me:** Um, So I guess my proudest software project was the caucus streams thing that I built at Octimine, but that was pre-AI. So I guess I'll go with my next proudest was a project I worked on recently was a, um, a payment integration. For a client. They were you, they were using Shopify and they needed to new, they needed a new, um, provider. They couldn't use Stripe. So, which Stripe is fully integrated with Shopify. You'd have to really do much. Which is why they needed an app to integrate their payment provider. So I built this all out with AI. The client gave me what they needed and their requirements. So, For all my projects, I kind of have this 4 step process where I specify the problem and kind of lose terms. Basically what I know from the client and what I've deduced. And then the 1st phase that I do with AI is sort of a scoping phase to figure out the requirements functional and non-functional, like, um, constraints, risks, assumptions, all of that stuff. Understanding the problem really is what step one is. Um, so that will produce, um, it requires a lot of back and forth too, I should, I should, uh, um, also emphasize that. But that produces a markdown file and Then I go to this next stage, which is just planning how we're going to actually implement the problem. Making sure all the requirements are met. Um, the order that we need to build things to make sure that, um, yeah, we're building it. We have dependencies specified first. Um, And in this stage, that also, I should also emphasize, that also requires generally a lot of back and forth about how we're actually going to do things. And then, um, part 3 is when we actually implement execute the plan that we've built so far. And by that point, since we've nailed down a lot of things, it generally goes pretty smoothly at that point. Um, I do do like a review. This the last, so it's a 4 stage process at the last stage, I do a review, make sure that all the requirements have been met. Um, anything that could be improved. Um, So, yeah, I built the whole payment for provider with this framework. Um, And it actually caught a pretty big issue so that there, this provider sent us over their document for their API, and we realized, like, we, me and the AI realized that there was, um, They wanted us to confirm payments by a redirect to a successor, cancel URL, which is like a huge no, no. I mean, you can just go to that URL or there could be a network error that stops it. But then they didn't give us like any, like any reason or any recourse, like how do we actually verify payments? So I brought this up to the CTO, which I was in contact with, and he said, oh, just, um, we're working on a web hook, uh, just use that for now. Uh, okay, so we built around that, but, um, I went back to the client and explained them this to them and explained the risk. And, um, so we went back again to the the pain provider and convinced him like, hey, can you please prioritize this web hook? Because this is kind of a big security loophole here. Um, and eventually they they agreed to do that. So we got the web hook in in time, but

**Ryan:** Nice, yeah, that makes me wonder because we're the main focus of the work that we do here is kind of in the mortgage industry. So like, another compliance, heavy environment. Were there any like PCI considerations that you had to make when you were building this or how did you prioritize, like, security, compliance in what you were building? Obviously, given the sensitive nature of payment information.

**Me:** So, um, lovely PCI was not on me. That was on the payment provider. I was just mainly integrating, um, or sinking, um, Shopify order status with a payment status. Um, but I did, you know, need to make sure that we had, like, for example, identity keys and all the requests so that, you know, duplicate payments aren't sent through. Um, And make sure that, uh, everything, you know, has a timestamp, so we don't have like out of order stuff going through. Um, So yeah, I mean, I made sure to check for duplicate web hooks or out of order web hooks, but yeah, luckily the really hard stuff like PCI that was on the payment provider.

**Ryan:** That's a win. Yeah, that's a big pay to the butt to try to try to implement. Now, I'm curious, like what kind of tools did you use to build? Like, was this clawed code? Were you working with like chat GPT? Like, you know, what's your, what do you use? Like, what are some of your tools that you go to?

**Me:** So, um, most of it was built in cloud code. Uh, the, the, the 4 step process that I, um, outlined, that is, um, agent diagnostic, so it just has a, I have a little, um, agents.agents fold directory in my, um, in the project, and so it all writes to markdown files. So any other agent can pick up where it left off and I can use like, for example, like for the review at the at the end, I generally use a less powerful model, like something like Deep Seek. Um, But so yeah, cloud code, Codex, and Deep Seek are the biggest, um, the agents I use the most. Um, and it's all in, I use, I do it in the terminal with,

**Ryan:** Dustin, I saw your eyes move on deep sea. Is that a model we should be getting access to over here, you think?

**Justin:** Give a little, uh...

**Ryan:** Well, first, Jack Ma? Is that the Aleibaba guy?

**Justin:** Yeah, no, I think Ali Laba is, um, Quinn. Um, but Deep Seek, we cannot do because it's from China. So we can't use it on the VA side. But, um, it has different tiers. So when you say a lesser model, like, do you know which which parameter, which version of Deep Sea Q were rocking? I think they have, like, a huge frontier model.

**Me:** Yeah, so they had, um, so I know they've been changing their pricing a lot because people are using it so much because it was so cheap. Uh, I was using, um, so they had Flash and Pro, both of the the API, um, 2 different APIs. Um, I was using pro just because even the pro model was still is so much cheaper than all the rest. I mean, all the other models.

**Justin:** Okay. So you were hitting that API, okay?

**Me:** Oh, yeah, I was going through the API, yeah.

**Justin:** Excellent. Okay.

**Me:** I don't think they have a, like a, just a subscription service like the others. I think you have to go to the AP or maybe they do on the web.

**Justin:** You can you can get a pair of metal, like a digital ocean, and you can get your own box. GPU spun it up, which is like decently expensive. Yeah, I mentioned the frontier models. Yeah. But if you're doing the lower models, it's not that bad.

**Me:** Okay. Yeah, that's really cool.

**Justin:** We're always looking for a way to offset, like, right now, we're pretty frontier and about as cheap as we go with Sonnet, and we are looking for ways to find, like, reproducible patterns, and then have those patterns instead of a frontier model doing it. We start trading a lower level, even, like, a mistral or a quen, or one approved model to just handle that. And as long as the evalves say it's doing a good job, we let it rip and cut that cost down. So, we're always going to hunt for that. But that is not at the VA. So the VA clawed all day, every day, for now.

**Me:** Okay. Yeah, I can imagine, you know, feeding veteran data into DB Chinese government. Love that.

**Ryan:** They'd be all over it. Um, Well, a lot of a lot of the work that we're doing here, um, leveraging AI is a lot of what you were talking about. So, like talking to different business folks, kind of gathering requirements, understanding what their problem is, and leveraging AI solutions to try to help solve that problem for them. And it's pretty awesome because they're excited at the end of the day. They get to say that we're leveraging AI, you know, board's happy, everybody's happy. But sometimes things don't quite go according to plan. Um, Sometimes we make mistakes and maybe we misunderstand some requirements. Sometimes maybe what gets built doesn't meet their expectations or requirements. And so we get some feedback. Can you tell me about a time where maybe you yourself made a mistake and then how it got solved?

**Me:** Um, let's see. So, yeah, I guess another app that I was building out was, um, It was this interactive map so that the client could view their customers and where they, like, if they had lapsed, which meant I hadn't made a purchase within 30 days. Um, so I built this out and they, so I had got this client through an agency, so it was kind of like my communication with them was very indirect and the requirements were not super clear. So, um, always what I do in that case is, you know, try and give to, given what I have formed the most coherent plan that I can and present this to the client that this meets expectations. Um, But some of the some of the stuff was, for example, um, they wanted like different filters and they had mentioned like uh, filter filtering based on name of the companies. Uh, filtering based on, so this was a B to B uh, coffee supplier. So, um, the companies were, I guess, coffee shops. Um, so had filters based on names and uh, places. So I wasn't really quite sure on how they wanted the filters to be, uh, specified. So, um, I think what I had originally built was, um, So on Shopify, you have this, uh, like a corporate, like a corporate, uh, a company and then they have like, um, different, um, places below it. So I was filtering on the wrong one. The lower level one, and I brought this up to the client. They were like, no, we need to, we need all of these aggravated together. So, um, it wasn't like a huge, um, change. I just basically needed to, you know, do a little bit different, uh, call different methods on the API, the Shopify admin API, to get the higher level, um, companies and, yeah, we got that, I got that rectified, but, um,

**Ryan:** awesome. It wasn't like a too bad a mistake. Like, there's there's always mistakes that happen, and, you know, it's just a matter of trying to figure out how do we fix that, how do we learn from that going forward? So, what would you do next time? And I know it's a little bit tough because you weren't really directly working exactly with the folks, the stakeholders.

**Me:** Um, I think, yeah, so that's that's a good point. A huge believer in learning from your mistakes and that's how we learn in general. Uh, so in that case, I think what I should have done was, um, I should have understood the problem a little bit more because that's like something I even try and emphasize a lot in my, um, my 4 step sort of plan is really understanding the problem and evidently I didn't understand it enough. So I think, um, I should have done more um, research there on what they were actually wanting. Um, understanding, um, what Shopify was actually providing, because I was still kind of new to Shopify too, so that, so understanding, you know, what's available, what can I do, and what the client actually wants, um, given what I've been told. Makes sense?

**Ryan:** Yeah. Um, the last question that I've got before I pass you over to Justin is a lot of what we'll do, obviously, is listening to the problems, using AI to solve the problems, and then we demo proof of concepts and everything like that. That can be a very exciting time. It can be very stressful time, depending on how involved the client is and the demo is and everything like that. So if you were getting ready to put together a demo of an AI powered solution that you had just built, let's say, you know, it's 9 in the morning, the demo's at, you know, 2 o'clock in the afternoon. What kinds of stuff are you doing before that demo to make sure that you're ready?

**Me:** Um, so, uh, I would, well, hopefully I'd be mostly ready by then if it's in a couple hours, but, uh, I would try and, you know, make sure I have a walkthrough to, to just walk through the whole thing that I've built. Um, make sure that I'm hitting all the requirements in my walkthrough to the client. Um, the things that they requested. Yeah, I want to make sure I have an outline to make sure I hit all the key features and explain that to the client, make sure that I am, uh, uh, Make sure I emphasize that, you know, open to questions, if they have questions about anything, if they need clarification on anything. Um, especially if it's something like maybe we had to make um, Any sort of a, uh, Or like, if we couldn't actually meet the requirements, we need to make some sort of, uh, the word is slipping my, um, Well, yeah, I guess. I'll leave it that.

**Ryan:** Okay, yeah, that sounds good. And, uh, Justin, I'll uh, I'll pass it over to you if there are any questions that you wanted to dive into.

**Justin:** Yep. So part of the AI engineering role, there's going to be the stand ups of, uh, you understand certain requirements from the VA. You will have access to certain lower level environments of test data, but you're gonna live in that sandbox area as far as the applications that are billed. From there, after the application is built, the value engineers, who mostly would do the demos, would need some support in automation. So, 508 compliance is the entire app compliance. Could you leverage the tools available to you to build some kind of pipeline to say, I have this thing that will run on all of that code, and it will basically come back and refactor for compliance, or at least flag for compliance and say, Here's the things that I found. So they will need some help. It's a step. I know that sounds like dev ops, but it's a step between the prototype and dev ops. There's a connector there that the dev ops would own, but you would probably have to build it.

**Me:** I see. So this, um, It's basically this compliance sort of loop that you were mentioning. that we need to build out?

**Justin:** Yeah, there would be compliance, there's, you would help with QA testing, engineering, for a QA test to build, it would all be agentically built, deterministic applications, but there would just be, once the code is written, and it's basically like a vibe code, right? There's gotta be some checks to say, okay, we missed some stuff. Let's deterministically go and repair and heal this code in these areas and we'll have different stations that heal the code, if you will. And so you're one of your primary roles would be to build the first version of that, automate it, let DevOps run that automation, feedback, and then test it and change it and say, okay, I know how to heal this code now.

**Me:** Okay, gotcha.

**Justin:** Does that sound, um, to me your thoughts on that?

**Me:** That sounds like a really fun problem. I'm glad you mentioned the terministic. I'm a huge fan of, you know, determinism in general, like, um, specifying, you know, what to do, not, uh, how to do it. So I kind of, I even built my, my resume that way. I have like a just a big Yammo file of all different things. So I have like different versions of my resume for like backend and um, full stack.

**Justin:** Oh, you should have just sent the Yaml. I can read Yamble. Oh, every word. No, I'm just kidding. Yeah, that's awesome. Okay, yeah. Hey, sorry, can you hear me? Hello? Hello? Hello? Hello? Hello? Can you hear me? Oh.

**Me:** There you are.

**Justin:** Oh, sorry about that. I think it was a network blip or something. Yeah, I think I went away. Um, So riding the sermonistic code that could almost live forever to do these things and doesn't require an LLM to run is the objective. Um, so, yeah, I think those are all of my questions. There will be some projects, you will have limited access to things, so there's the, uh, corporate side of Phoenix, where, basically, we'll give you all the tools you could ever need to go build things, but then when you get into environments like Livier or, you know, wherever you're positioned, they have very limited access to tool sets.

**Me:** Gotcha.

**Justin:** Um, and so you would have to find ways to, let's use GitHub copilot within BS code, and this is how we have to do this now, versus using Claude code. And then we're always champing more tools from AI, but our super intelligence, I guess, it is. Um, so... That is, that is it for me. That's kind of the roles. Um, I think we covered that, Ryan. So I think I'm good.

**Ryan:** Yeah, Chris, do you have any questions for us about some of the work that we do or anything like that that we can help answer before we let you go?

**Me:** Sure. Would you mind? So yeah, when I visited the website, I saw like mortgage for AI, but then this is for the VA. How does all that fit together?

**Ryan:** Yeah, it's a good question. So we've got a sister company that is called Blue Phoenix. And it's kind of like a two companies basically working together sharing resources. So, some projects we work on are commercial clients, and we're helping out servicers and subservicers and everything like that in the mortgage industry. And some are, like, big government contracts. And so this would be in pursuit of a big honking VA government contract, but we're trying to revolutionize the process to get veterans in homes faster, better. You know, everything like that would bless disruption. So that's another really cool piece of the puzzle, is you can feel really good every day that you're logging into this project and working, because every single day we're making progress on this is helping make life better for veterans and getting approved and into homes.

**Me:** Yeah, I was about to say that. That sounds, that sounds like a really fulfilling work to, because I've worked on like social media, like helping marketers, and it's like, okay, what am I doing? But this sounds like a pretty good project.

**Ryan:** Yeah, it's it's one that you can you can go to sleep though, that you contributed, and for all the naysayers of AI, you know, it could feel good that you've used AI for for a positive thing. So...

**Me:** I jotted a sweet put... yeah, go ahead. Um, so yeah, so I take notes the old-fashioned right here. I got pen and paper. Um, let's see. Oh, yeah. So I saw that this is rollers, there's 3 vacancies. Um, I guess what is the, what is the team that I'd be working with? What would that be like? Are there, is there a manager? And, yeah, who else would I be working with?

**Ryan:** Yeah, yeah, there would be a manager. Um, they are gonna try to shield you from a lot of the working directly with some of the big honkin government folks because there's there's a real different speed of work that happens with government and different approval process and everything like that. And so leaders here try to enable people to do their best work by kind of dealing with some of the administrative government ends of things. And so, like Justin mentioned, you'd be working likely with what we call value engineers. And so, those are the folks that are in there talking to some of those government folks, talking to some of the business folks, trying to understand those problems. Um, in a lot of those meetings that you can understand from a technical perspective, what the problem is that needs to be solved. And then we all kind of put our heads together and figure out after we've learned about what we're calling use cases or a way that we can leverage AI to do things better. How should we best tackle this? You know, what options does Claude think are right? You know, how do we do that? And then actually, as an engineer, you'd be responsible for going out, building it, making sure that it passes some of the requirements that we've got, like Justin mentioned, the 508 compliance, other kind of key pieces. And then we bring it on back, help the value engineers understand it. And then join, like, a proof of concept or demo call for us to kind of explain it to the customer, show it off, collect feedback, continue iterating through, you know, how, like, all good. Yeah.

**Me:** Cool. So it sounds like a pretty collaborative environment.

**Ryan:** Very much so. Yep.

**Me:** Nice. Um, Yeah, so, oh, okay. Can you mention? could you talk a little bit about the the text stack? I saw it like in the, um, in the job listing here. There's a lot of languages like pythons, people's pies, rest go, Java, C sharp, uh.

**Justin:** Yeah, I can talk about that. That is just, as we need you to have some kind of discipline for 2022, and it doesn't matter what it is. Okay. You've got some pretty good Python Go. So you've got some good, strong language, but we really need people that just know what they're doing without AI, 'cause AI, if you know what you're doing without AI, especially a developer, as soon as you get AI, once you get your ego out of the way, no offense, but once you just embrace it and say, this actually does pretty good work, but I still need to watch it, like, we fly. So, but the tech stack, the VA, that's a tricky one also. So right now, what you'll be doing in the VA is supporting an ecosystem where we're in the lower level environment, in the sandbox. We're going to build beta products, but we want to have that pipeline make them so good and secure that when they hit the next level, they pass all tests, right? And they can just ship the production. Because AI is so flexible and we have a lot of cowboys in the VA, and when I say a lot, there's one, refactoring into other languages, like into Rust, and, you know, getting out of, you know, salesforce and building something into, like, go or Java, those conversations arise. I would, I am always for, let's not do that yet. Let's lean into what there is. So there's a lot of salesforce, a lot of Java, things that you'll immediately pick up on for that current stack and then AWS connecting to the endpoints. But yeah, we just have that in there because we need, um, we need folks to have some kind of discipline before AI existed.

**Me:** Okay, cool. Um, so yeah, I guess that covers my most of my main questions I had. Um, So I guess I just to recap on a little bit about myself, um, what I'm really looking for, my next role is, um, The 2 biggest things are like is collaboration and long-term ownership, which sounds like this role would be perfect for that because, um, you know, as I mentioned, I've been working as, uh, mostly as a solo project-based contractor for the past few years and, um, I well, there has been some collaboration, especially with clients, but not like the collaboration with other engineers. Um, and then long-term ownership as well was, uh, the clients are more interested in getting things out the door rather than maintaining this, um, over a long period of time, which is, I think, an important part of engineering. So.

**Ryan:** Yeah, no, definitely. And that is one of the cool things about working here is there is such a vast background of folks with different experience and everything like that, that almost everyone I've talked to, especially in the engineering side, has a totally unique background and maybe some of them are college grads that did, you know, data science and everything like that, machine learning. But a lot of them kind of didn't. They started with a more traditional, you know, developing background and everything. So whenever I'm running into issues and I'm working with Claude to build something or whatever, there is almost someone here that is able to help understand what I'm running into and how to help solve it, basically. If I'm not able to use Claude to figure it out myself. So definitely an awesome team to be able to work with here and very, very collaborative. You know, you're not just gonna be off in a silo building something. It's gonna be, because of that, the rate at how quickly we can build with AI. It's not like we're taking weeks and weeks to do development cycle. You know, we're knocking stuff out quick. We delivering value to clients quick, and that gets people pretty excited. Like, it's pretty important work that we've got going on here, and we're really excited about it, so...

**Me:** Nice. Yeah.

**Ryan:** In any event, thank you very much for taking the time to chat with us today. We're talking to a few different folks, but we'll definitely be in touch as far as next steps go. And, uh, again, really enjoyed the conversation, Chris.

**Me:** Yeah, Likewise, appreciate it.

**Justin:** Nice to meet you, Chris.

**Me:** You too. Bye bye.
