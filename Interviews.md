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

## Missed and Partial

```dataview
TABLE WITHOUT ID application AS "Application", round AS "Round", date AS "When", L.grade AS "Grade", L.section AS "Question"
FROM "Applications"
WHERE type = "interview"
FLATTEN file.lists AS L
WHERE L.grade = "missed" OR L.grade = "partial"
SORT date(substring(string(date), 0, 10)) DESC, L.grade ASC
```

## Scorecard

```dataview
TABLE WITHOUT ID application AS "Application", round AS "Round", date AS "When", length(filter(file.lists, (l) => l.grade = "right")) AS "Right", length(filter(file.lists, (l) => l.grade = "partial")) AS "Partial", length(filter(file.lists, (l) => l.grade = "missed")) AS "Missed"
FROM "Applications"
WHERE type = "interview" AND length(filter(file.lists, (l) => l.grade)) > 0
SORT date(substring(string(date), 0, 10)) DESC
```
