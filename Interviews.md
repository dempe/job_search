---
title: Interviews
---

## Upcoming

```dataview
TABLE WITHOUT ID application AS "Application", round AS "Round", file.link AS "Interview", date AS "When", interviewers AS "Interviewers", outcome AS "Outcome"
FROM "Applications"
WHERE type = "interview"
FLATTEN date(substring(string(date), 0, 10)) AS day
WHERE day >= date(today)
SORT day ASC
```

## Past

```dataview
TABLE WITHOUT ID application AS "Application", round AS "Round", file.link AS "Interview", date AS "When", interviewers AS "Interviewers", outcome AS "Outcome", filter(file.outlinks, (l) => endswith(l.path, "/transcript.md")) AS "Transcript"
FROM "Applications"
WHERE type = "interview"
FLATTEN date(substring(string(date), 0, 10)) AS day
WHERE day < date(today)
SORT day DESC, round DESC
```

## Undated

```dataview
TABLE WITHOUT ID application AS "Application", round AS "Round", file.link AS "Interview", interviewers AS "Interviewers", outcome AS "Outcome"
FROM "Applications"
WHERE type = "interview" AND !date
SORT file.path ASC
```
