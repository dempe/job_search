---
type: interview
application: "[[Job Applications/NinjaCat]]"
company: NinjaCat
round: 3
date:
kind:
interviewers:
outcome:
title: NinjaCat - Interview 3
date_created: "2026-11-04 18:10"
date_modified: "2026-11-04 18:10"
---

## Pair-programming Interview (45 min)


> A pair programming project in your choice of language - There's 3 choices - PHP, Kotlin and TypeScript. Which would you prefer? We'll send you a link to the repo beforehand and you can run it, or we can run it from our end while you tell us what to do / control the screen.

I chose Kotlin. Need to finish the Kotlin koans to learn about Kotlin idioms.

Remember to focus on communication.

### Retrospective

Fuck the task was super easy. Made some obvious blunders, though. It's like I'm docked 20 IQ points during an interview coding session. Anyways.

Couldn't get it to load on my comp, so Steve drove.

Was basically a pair programming task with three people.

[Here's](https://gitlab.com/ninjacat-public/technical-interview-exercises/kotlin-etl-exercise) the repo/explanation.

#### Pros

- Solved the problem
- Solved the "bonus" problem
- Used an extension function, which Steve mentioned he liked
- Made a separate `TransformException` class for clarity

#### Cons

- **Missed the `map` in the "fix the failing test" part** and created an unnecessary `set`. Maybe, what I need to do is just go a bit slower. Read each line. Understand each line. Like in salsa — RELA-JE-SE.
- Had a few syntactic errors come up, but they both weren't sure either.
- **Missed the `toLowercase`** in the "bonus" part to determine score. When the test failed, it should have been obvious that we missed converting to lowercase.
- I didn't have Gradle set up. Luckily, since Steve drove, it didn't matter. Not sure how big of deal this would be overall, but I do **need to learn Gradle**.
