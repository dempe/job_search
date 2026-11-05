---
title: Interviews
---

## Upcoming

```dataview
TABLE WITHOUT ID file.link AS "Interview", date AS "When", application AS "Application", interviewers AS "Interviewers", outcome AS "Outcome"
FROM "Interviews"
WHERE type = "interview"
FLATTEN date(substring(string(date), 0, 10)) AS day
WHERE day >= date(today)
SORT day ASC
```

## Past

```dataview
TABLE WITHOUT ID file.link AS "Interview", date AS "When", interviewers AS "Interviewers", outcome AS "Outcome", filter(file.outlinks, (l) => contains(l.path, "Transcripts/")) AS "Transcript"
FROM "Interviews"
WHERE type = "interview"
FLATTEN date(substring(string(date), 0, 10)) AS day
WHERE day < date(today)
SORT day DESC, round DESC
```

## Undated

```dataview
TABLE WITHOUT ID file.link AS "Interview", interviewers AS "Interviewers", outcome AS "Outcome"
FROM "Interviews"
WHERE type = "interview" AND !date
SORT file.name ASC
```
