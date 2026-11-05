---
type: interview
application: "[[Applications/NinjaCat]]"
company: NinjaCat
round: 2
date: 2023-07-09 13:00
interviewers:
outcome: advanced
title: NinjaCat - Interview 2
date_created: 2026-11-04 18:10
date_modified: 2026-11-04 18:10
---

## Technical Project Interview (45 min)


> A project deep dive ("Tell us about a recent project you worked on…")

This is the first part of a two-part 90 min technical interview. I already discussed Kafka in my interview with Andy and Winnie. I don't feel comfortable talking about that one for 45 minutes.

Instead, I will opt to talk about a Laravel app that I built/will build.

I think this is a good idea for the following reasons:

- They use Laravel, hence it will be good to show experience in it. Also, this pairs well with my chosen language for the pair-programming interview, Kotlin. It shows that I have experience with two of their main tech stack languages.
- I *want* to learn more about Laravel
- It's much more *recent* than my Kafka experience
- Plus, I have *control* over it — I can and will continue to develop and work on it over the next week. Unlike the Kafka project which I worked on a year ago.

I guess the only real downside is that it doesn't show any sort of team experience given that it's a solo project.

**Steps**:

1. Write blog post detailing current Laravel app and how it's deployed.
2. Create branch for non-static features
3. Add user login
4. Add basic account management
5. Add commenting/comment management
6. Add a fuzzy search feature for posts
7. Time permitting, write a follow-up blog post about full app

ChatGPT-generated Qs:

- Can you give a high-level overview of this project? What was the business need or problem that this project was addressing?
- What was your role in this project? How big was the team and how was it structured?
- How did you start this project? What were the steps taken in the planning phase?
- What were the main technologies or tools used in this project and why were they chosen?
- Can you discuss the architecture of the system you developed? What were the key components and how did they interact?
- Did you face any major challenges or obstacles during the project? How did you overcome them?
- How did you ensure the quality of your code? Did you use any testing frameworks or practices?
- How was the project managed? Did you use any project management methodologies or tools like Agile,

### Retrospective

I talked about both Kafka and Laravel — Kafka in my background story/section, Laravel as my chosen project.

#### Pros

- Laughed, smiled, joked, had a good conversation.
- Described my past experience with Kafka well.
- Think I covered my use cases for Laravel pretty nicely.
- Asked decent questions. A few technical, a few not.
	- "You mentioned that you are splitting your Laravel app out into microservices. What exactly are these microservices? APIs?"
		- Basically, when something in the Laravel app needs updating, they move it to a dedicated microservice.
	- "How do you deploy your microservices? Containers?"
		- Using K8s, Helm
	- "Is there on call?"
		- No. The infra team, possibly, but not for devs.
		- You are given a high degree of trust and responsibility to make sure your tasks are working as they should.
		- Maybe will have on call in the future.
	- "How's the feedback system? 1:1s?"
		- You set the cadence for your 1:1s!
		- They have some program that allows you to request or submit feedback for any co-worker.

#### Cons

- Should have offered to **share my screen to show Laravel app**
- I asked "how do you like NinjaCat?" Steve raised an eyebrow haha.
