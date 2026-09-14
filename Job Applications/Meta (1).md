---
type: job
applied: 2023-08-24
interviews:
  - 2023-08-31
  - 2023-09-25
  - 2023-10-19
status: rejected
job_type: fulltime
position: "Software Engineer Infrastructure"
remote: true
industry: tech
website: 
location: san_francisco
company_size: very_large
recruited: true
listing: 
blog: 
correspondence:
  - Linkedin
  - email
  - WhatsApp
title: Meta (1)
date_created: "2023-08-26 12:19"
date_modified: "2025-05-31 13:30"
---

## Application

Recruiter reached out to me on Linkedin back in July. I didn't see the message till a month later. I sent him the following email:

```
Hi Marcelo,


This is Chris Dempewolf. I just noticed your message on Linkedin.  I hope the position you were messaging about is still available.  If it is, please let me know what the role is and what is required.  I would be delighted to learn more.

A little about myself:

I have 6 YOE as a backend software engineer.  I've spent most of my time working in the data ingestion side of things, but also have experience in writing APIs, SDKs, and analytics.  I have extensive experience with Java, ElasticSearch, Postgres, and AWS.

I was hired as Senior Data Engineer at Dennemeyer/Octimine where I lead an effort to build a real time data processing pipeline using Kafka to process and transport data from our data warehouse to ElasticSearch.

What I'm mainly looking for right now in my career is to grow as an engineer. I would like to someday reach the level of staff engineer or tech lead.  I'm looking for a place that can provide me with the challenging problems, autonomy, and regular feedback that I need to make this happen.

If you curious to learn more about me, I recently wrote by own blog from scratch.  You can see my tech-related posts here: https://chrisdempewolf.com/tags/tech.html.  I've also attached my resume.

Thanks for getting in touch, and have a great day!


Best,
Chris
```

He responded by offering a meeting time next Thursday.

## Interview 1 — Recruiter Screen

### Questions Asked

- I see you've never interviewed with FB before, but you must have been recruited. **Why do you want to work for FB now?**
- What is your current role? What projects have you worked on in this role?
- What percentage of your working time did you spend developing and designing? Did you have any responsibilities outside of development?
- In which FB area would you be most fit to work at? (he gave list of FB, WhatsApp, IG, and VR)
- What language do you have most experience in? (java, super simple)
- What area of development do you have most experience in? (data, super simple)
- Would you be willing to relocate to Seattle? (yes, super simple)

### Pros

- Had decent response to all questions
- Showed enthusiasm

### Cons

- Talked too much (I could tell from his backchannel that he was relieved when I got to the point, for example)
- Talked too fast
- Didn't ask enough questions (except for Q about follow-up)
- Used a lot of filler words
- Should have taken notes (of what Qs he asked) during interview

### To-Do

- Research some good Qs to ask recruiters
- Research how to better show enthusiasm
- Record yourself answering those Qs. Make sure you speak clearly and slowly. Reduce filler words.

### Notes (Retrospective)

- He said he would show my resume to "the team" to see if I qualify for the next round.
- He mentioned the follow-up interview would be with an engineer. The engineer will ask me two technical, LC questions. I can have two or three weeks to prepare.
- I can also have a practice interview before the technical screen to see if I'm ready. If I'm not, they can push back the real interview. — Holy shit. That's cool. If I'm accepted for the next round, this could be a lot of potential practice!

## Interview 2 — Mock Interview

Meeting ID: 91629726774 - Passcode: 699648

I think I finally figured out why I've been having issues with zoom audio… After you test it, there is another step — you have to actually click the headphones icon in the bottom left to "join with computer audio". Otherwise, you stuck in some sort of audio no man's land… Genius.

That was the coldest interview I've ever had.

### First Q

Each character maps to a certain value. Given a string and a map, we had to … Do something. I already forgot..

I do remember that I did not get anywhere near the solution and the interview interrupted me saying, "let's move on to the next one." The reason it was so tricky was because the solution required both iteration and recursion in the same function. I've never done that before, and it threw my mind for a loop.

### Three Sum

Well, this was easy. The exact Q I had been studying before the interview. I offered two solutions:

1. Store elements in a fixed size array and use binary search
2. Store the elements in a hashmap that maps value to index (es)

They asked a simplified version that merely asked us to return `true` or `false` if any three elements summed to zero.

I implemented the latter because I thought it would be easier (I now know that Java has `Array.sort` and `Arrays.binarySearch` that would have made the first easier to do).

Basically, the algorithm is this:

1. Loop through the array and add each element to a `HashMap<Int, List<Int>>` of values to indices. Alternatively, sort the array using `Arrays.sort`
2. `for (int I = 0; I < arr.length; i++)`
3. `for (int j = I + 1; j < arr.length; j++)`
4. `int k = -1 * (i + j)`
5. Here we check the hashmap or binary search the array for `k`. If `k` is found, we return `true`
6. Return `false` if loop completes

- Runtime with binary search: $O(n^{2}\log{n})$
- Runtime with hashmap: $O(n^{2}$? According to ChatGPT, at least, that's the answer.

## Interview 3 — Screening Interview

It went better than my mock interview! And I hadn't seen either Q before.

### Check if String is Palindrome given that We Are Able to Remove 1 Element

I wasn't sure how to solve this at first, so I just implemented a basic `isPalindrome(String s)` function first:

```Java
public function boolean isPalindrome(final String s) {
	final int len = s.length;
	
	for (int I = 0; I < len / 2; i++) {
		final char1 = s[i];
		final char2 = s[len - 1 - i];

        // In the interview, I acutally put a check in to see if I and len - 1 - I were equal.  This is completely retarded and makes no sense.


		if (char1 != char2) {
			return false;
		}
	}

	return true;
}
```

Then modified it to be able to remove one element:

```Java
public function boolean isPalindrome(final String s, boolean haveRemoved) {
	final int len = s.length;
	
	for (int I = 0; I < len / 2; i++) {
		final char1 = s[i];
		final char2 = s[len - 1 - i];

        // In the interview, I acutally put a check in to see if I and len - 1 - I were equal.  This is completely retarded and makes no sense.

		if (char1 != char2 && haveRemoved == false) {
			final String s1 = s.remove(i);
			final String s2 = s.remove(len - 1 - i);
			
			return isPalindrome(s1, true) || isPalindrome(s2, true);
		}
		if (char1 != char2 && haveRemoved == true) {
			return false;
		}
	}

	return true;
}
```

Can also be extended to be able to remove up to $k$ elements by making `haveRemoved` an integer and passing in a max removal integer, `k`.

Runtime: $O(n)$ — we need to check each element.

### Find the Longest Consecutive Subsequence (s) of a String and return a List of One Element from Each

This was tricksey and we ran out of time we did.
