---
type: interview
application: "[[Applications/NinjaCat]]"
company: NinjaCat
round: 4
date: 2023-07-10 14:00
interviewers:
outcome: advanced
title: NinjaCat - Interview 4
date_created: 2026-11-04 18:10
date_modified: 2026-11-04 18:10
---

## Peer Interview (30 min)


> This is an interview with a fellow engineer on the team to learn about how you deal with engineering challenges day to day.

This sounds like a behavioral/cultural fit interview.

**Things to study**:

1. Behavioral questions
2. Culture at NinjaCat

**ChatGPT-generated Qs**:

1. **Technical Problem-Solving**:

   - How do you approach solving complex technical problems?
   - Can you describe a recent challenging problem you faced and how you resolved it?
   - What tools or strategies do you use to debug and troubleshoot issues?

2. **Collaboration and Communication**:

   - How do you effectively collaborate with teammates to tackle engineering challenges?
   - Can you give an example of a time when you had to work closely with others to overcome a technical hurdle?
   - How do you communicate technical concepts to non-technical team members or stakeholders?

3. **Decision-Making and Prioritization**:

   - How do you prioritize tasks and make decisions when faced with competing deadlines or conflicting requirements?
   - Can you discuss a situation where you had to make a trade-off between quality, speed, and resource constraints?
   - How do you approach evaluating and selecting technology or frameworks for a project?

4. **Continuous Learning and Improvement**:

   - How do you stay updated on emerging technologies and industry trends?
   - Can you describe a time when you identified an area for improvement in your technical skills or processes and took action to address it?
   - How do you encourage a culture of learning and knowledge sharing within your team?

5. **Handling Challenges and Mistakes**:

   - How do you deal with setbacks or unexpected obstacles in your work?
   - Can you share an example of a mistake or failure you encountered and how you learned from it?
   - How do you approach risk assessment and mitigation when implementing technical solutions?

**GPT4 Qs**:

- Can you tell me about a challenging technical problem you've had to solve, and what your process was to solve it?
	- My previous job had a batch processing job written in Python to process about 30 million legal documents per week. The problem was that I twas super slow. It would take multiple days to run, normally 2 or 3, but if we had a serious issue, it could overlap with the next week's job.
	- I proposed we migrate to a realtime event-driven system. There was no reason to be processing these documents in batch anyways as they came in continuously.
	- All (three) backend engineers and our infra guy met to analyze our current set up and how to proceed.
- How do you approach learning a new technology or tool?
	- I think the only way to really learn something is to start using it. This is the difference between knowledge and know-how. Just because you have knowledge of how to ride a bike, doesn't mean you can ride a bike. I find this applies to many things, engineering included.
	- For programming languages, I see if there is a set of koans to solve to become familiar with the syntax. Then I try to start programming some simple programs for example, Project Euler, Advent of Code, or LeetCode problems are nice simple, problems to get started.
	- For tools, Docker has made this quite easy. Just download an image of the tool you want to learn, find a tutorial, and start building a PoC.
	- Lastly, with the advent of ChatGPT, I like to give ChatGPT a "socratic tutor" prompt so that it asks me questions to guide my understanding, without explicitly telling me the answers. I find this is a great way to learn the "hows" and "whys".
- Can you describe a time you received critical feedback and how you dealt with it?
	- At Octimine, they mentioned that I didn't know enough on the legal side. I took this as a learning opportunity to brush up on my legal knowledge. I made a bunch of Anki flashcards about IP legal topics and started studying. It's important to **never take critical advice personal**. That gets you no where.
	- I think this is a good way to approach any sort of "failures" or shortcomings. They are great learning opportunities, a way to improve as a engineer, a person. This is called the "growth mindset".
	- Sometimes, you might be in a bad mood or someone gives you critical advice in a rude manner. If you feel yourself starting to take something personal, just meditate for 10 minutes.
- Have you ever disagreed with a team member about a technical approach? How was it resolved?
	- Try to understand their point of view. Ask them **questions** to make sure you understand perfectly. People these days ask far too few questions. A lot of disagreements can be solved by asking probing questions and making an effort to communicate and understand each other.
	- Use an evidence-based approach. Once we understand each other, weigh the pros and cons of each approach based on what we know. Don't make assumptions, don't speculate. Use what we know and go from there.
	- Maintain a focus on project goals. It's also very important to maintain a focus on the end goal. What exactly are we trying to achieve? Which approach would accomplish this goal? If it comes down to a tradeoff between speed and quality, there's always a larger goal — which approach fits better with company objectives, with **what our CUSTOMERS want**?
- Can you give an example of a technical compromise you had to make?
- Can you explain a complex technical concept to me as if I were a non-technical team member?
	- Sure, let's talk about containerization.
	- We have an app that we need to run on my machine, on your machine, in the cloud, in a variety of environments, but it needs to function exactly the same. How can we do that?
	- We can use containers. Containers a way to run an exact replica of an app in a variety of environments.
	- How do you think they might do that? For one, all containers run the Linux operating system. They're small because they only contain the code necessary to run your app, nothing more. In contrast to a virtual machine, which runs the entire operating system.
	- Since they're small, they can easily be deployed wherever you like.

### Retrospective

Overall, I think it went really well. Was basically just like a chat with friends. Felt very informal. They asked about my time in Germany. They asked what challenges I had there. I told them the problem I had at the gym (thank god they didn't ask anymore), because that was not one of my most sterling moments. **Matthew** followed up with a question — "did you experience any challenges like that at work?" I can tell now exactly what he was doing — he was trying to ask me in a roundabout, informal manner, "What challenges did you face in your previous job and how did you resolve them?" I didn't really pick up on that in the heat of the moment. I mentioned that we didn't really have any disagreements at work. Which was pretty true. At least at the time of the interview, I couldn't think of any. But now I realize I maybe could have mentioned the small conflict we had over the existence of Midlayer post-Kafka.

#### Pros

- Asked a lot of questions
- Smiled and laughed (maybe try to smile even bigger)
- Felt like a good convo
- Made a few jokes

#### Cons

- **Try to smile even bigger**. I think at one point Matthew looked at me after a joke he told. I was smiling but not super noticeably.
- Try to talk less about old workplaces. It paints you as a gossipy person who talks about others behind their backs. I think this is the biggest regret I have from this interview. I feel like I might have come off as bad talking my previous employer.
- Try to be more aware what people are really asking. Matthew was asking about challenges at my previous job, but he did so in and indirect fashion that I didn't pick up on.
- Also, have a list of stories ready to tell for these common questions. It might also help you pick up on when someone is asking something indirectly.
- My camera was off for about 10 mins. I apologized and everything was fine, but sth to check.
