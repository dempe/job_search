---
type: job
applied: 2025-04-21
interviews:
  - 2025-04-23 10:30
status: rejected
job_type: fulltime
position:
remote:
4day:
industry:
website:
location:
company_size:
recruited: true
listing:
blog:
correspondence: email
compensation:
title: Meta (2)
date_created: 2025-04-21 12:28
date_modified: 2025-05-31 13:30
---

## Application / Recruiter Screen

Just responded to a recruiter email. There was a button to schedule a call. Though, I never replied to her emails.

She mentioned various tech in her follow-up email. I'll pick some of that and check out the page they sent me to try to do some basic research and express interest in their company.

My story:

```
I graduated in 2013. Worked for 5 years in a mostly data-centric role.  That is, data ingestion, not so much data processing.  I pulled in data mostly from social media sources, but also niche forums and websites via a custom crawling framework that I helped build.  For the social media APIs, I set up token pools and rate limiting, etc.

After about 5 years, I started to the itch to work with people more.  I also wanted to live abroad, not just travel.  So I decided to give teaching english a shot.  I got my TEFL cert and moved to Mexico. I loved it and I learned a lot.

Then I get a job at a german company as a senior data engineer.  So my previous roles were still software engineering, just data-centric.  this role was explicitly data engineering.  Tho, practically, it didn't differ much and I still spent a lot of time developing software.  For ex, I built them a new event-driven data ingestion/processing pipeline using apache Kafka.  This way, we could ingest data in realtime.  Their previous setup ran in batch and required at least two days on a good week.  IF something went wrong, we could easily have two jobs running at the same time.

After I left germany, I hadn't seen my GF in a year, so I decided to take some time off to travel with her a bit.  Then we got married and had a kid.  I was helping to take care of the kid, so my hours were pretty irregular, so I decided to start a company building a few educational apps that i've wanted to build for a while.  This allowed me to work on my own schedule.

I love the work I’m doing now, but my daughter is older now, so i'd really like to get something a little more stable.
```

ChatGPT version:

```
I graduated in 2013 and spent my first five years in a data-centric software engineering role. I focused primarily on building data ingestion pipelines—pulling data from social media APIs and niche web sources using a custom crawling framework I helped develop. I also built systems for managing token pools and rate limiting to handle API constraints at scale.

After five years, I realized I wanted more human interaction and had a strong desire to live abroad, so I made a pivot. I earned my TEFL certification and moved to Mexico to teach English. It was a great experience personally and culturally, and it gave me a fresh perspective on learning and communication.

Eventually, I returned to engineering in a senior data engineering role at a German company. There, I led the development of a real-time event-driven data ingestion and processing pipeline using Apache Kafka. This replaced their old batch system—which often took days—and brought down latency from multiple days to near-instant. It also eliminated reliability issues with overlapping jobs.

After leaving that role, I took time to be with my now-wife after a long stretch apart, and we eventually had our daughter. During that period, I worked irregular hours, so I started a company and began building educational apps—something I’d always wanted to pursue. I’ve loved working independently, but my daughter is older now, and I’m looking to return to a more stable, collaborative environment where I can grow technically and contribute to a larger mission. Meta really stands out as a place where I could do exactly that.
```

- It sounds intentional and cohesive
- It shows you're not flaky—your transitions have purpose.
- It hits all major boxes: technical strength, career ownership, personal growth, current motivation

Questions:

- "I saw you mentioned the Orion AR glasses in your email—I'd love to hear more about what teams are involved in that. Is this still in R&D, or are there engineering roles focused on production and platform integration already?"
- The LLaMA family of open-source models has been a standout contribution from Meta—I was really excited to see a major player invest in openness. Do you know if there are roles focused on infra or tooling around LLM deployment and evaluation?
- "I've been really impressed with the long-term vision Meta has for spatial computing—especially the work coming out of Reality Labs. Do you know if teams working on infrastructure or SDK-level work for VR/AR are currently hiring?"
- What's the interview process with meta?
- Which teams are hiring?
- I've read that meta supports internal transfers. How does that work? Do a lot of engineers do internal transitions?

### Notes

Three pillars to pick - monetization,

Only have on site positions. In decreasing order of competitiveness: bellvue, bay area, NY

Belinda was super nice and very transparent.

- Don't use multiple monitors in tech screen
- Don't reschedule unless absolutely necessary
- Take as much time as you need to prep, but be aware that they are currently on a "sprint" and that some positions currently open may be filled

## Tech Screen

### Prob 1

You are given an input array, `input` of digits (e.g., `[2, 4, 10, 11, 17, 21]`). You need to output the comma-delimited string of all the digits *not* contained in `input` up to `99`. If more than two consecutive digits are absent, they need to be indicated with a hyphen (e.g., ` 12-16 `). So for the provided example, the output should be `"0,1,3,5-9,12-16,18-20,22-99"`

My solution:

```python
def build_str(input: [str]) -> str:
	out = helper(0, input[0])
	for num1, num2 in zip(input[1:len(input) - 1], input[2:len(input) - 1]):
		out += helper(num1, num2)
	out += helper(input[-1], 99)
	return out

# Assume i < j	
def helper(i: int, j: int) -> str:
	if j - i > 2:
		return f"{i}-{j}"
	out = ""
	for k in range(i, j + 1):
		out += f",{k}"
	return out
```

```python
def build_str(input: [int]) -> str:
	def helper(i: int, j: int) -> [str]:
		if j < i:
			raise ValueError(f"i should be less than j. Found i={i}, j={j})
		if j - i > 2:
			return [f"{i}-{j}"]
		
		out = []			
		for k in range(i, j + 1):  # Should not execute if i == j
			out.append(str(k))
		return out
		
	missing = [i for i in range(100) if i not in set(input)]
	
	start = stop = 0
	prev = -2
	in_seq = False
	out = []
	for num in missing:
		if num != prev + 1 and not in_seq:
			start = num
			in_seq = True
		elif num != prev + 1 and in_seq:
			stop = prev 
			in_seq = False
			out += helper(start, stop)
		prev = num
			
	return ",".join(out)
```

Correct solution from ChatGPT:

```python
def build_missing_ranges(input):
#    missing = [i for i in range(100) if i not in set(input)]
	missing = sorted(set(range(100)) - set(input))

    if not missing:
        return ""

    result = []
    start = prev = missing[0]

    for num in missing[1:] + [None]:  # Add sentinel
        if num == prev + 1:
            prev = num
        else:
            if start == prev:
                result.append(str(start))
            elif start + 1 == prev:
                result.append(f"{start},{prev}")
            else:
                result.append(f"{start}-{prev}")
            start = prev = num

    return ",".join(result)
```

### Prob 2

You are a delivery truck driver. Your truck has an overall integer `capacity` that indicates its weight limit. In addition to `capacity`, you are given an array, `trips`, of trips such that each trip is a three element array, `[weight, start, end]`, where `weight` is the weight of the package, and `start` and `end` are where the trip starts and stops. So an overall `trips` array might be `[[4, 1, 5], [3, 2, 6], [6, 1, 2]]`. Note, the trips array is not sorted-you have to determine the best order. Return `True` if it is possible to arrange `trips` in such an order that the packages never exceed `capacity`, `False` otherwise.

Solution I gave:

```python
def is_possible(trips, capacity):
	trips.sort(key=1)
	
	for trip1, trip2 in zip(trips, trips[1:]):
		cap1 = trip1[0]
		cap2 = trip2[0]
		
		if cap1 > capacity or cap2 > capacity:
			return False
		if trip1[1] > trip2[1] and cap1 + cap2 > capacity:
			return False
			
	return True
```

Interviewer said I had the "right idea", but my solution does not pass all cases, because it only ever compares adjacent trips in the array. But more than two trips can overlap, so current weight can be the sum of more than two weights. My solution never checks this case.

E.g., `[[2, 2, 100], [2, 2, 5], [2, 4, 5]]` where `capacity = 5`. My solution would return `True`, but the correct answer is `False`, because the three trips overlap between `[4, 5]`, where the total weight at the point is 6. `6 > 5`
