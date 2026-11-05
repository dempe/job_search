---
title: Interviews
date_created: "2026-11-04 19:08"
date_modified: "2026-11-04 21:16"
---

## Upcoming

```dataview
TABLE WITHOUT ID application AS "Application", file.link AS "Interview", date AS "When", interviewers AS "Interviewers", outcome AS "Outcome"
FROM "Applications"
WHERE type = "interview"
FLATTEN date(substring(string(date), 0, 10)) AS day
WHERE day >= date(today)
SORT day ASC
```

## Scorecard

```dataview
TABLE WITHOUT ID application AS "Application", round AS "Round", date AS "When", length(filter(file.lists, (l) => l.grade = "right")) AS "Right", length(filter(file.lists, (l) => l.grade = "partial")) AS "Partial", length(filter(file.lists, (l) => l.grade = "missed")) AS "Missed"
FROM "Applications"
WHERE type = "interview" AND length(filter(file.lists, (l) => l.grade)) > 0
SORT date(substring(string(date), 0, 10)) DESC
```

## Missed or Partial

```dataview
TABLE WITHOUT ID application AS "Application", round AS "Round", date AS "When", L.grade AS "Grade", L.section AS "Question"
FROM "Applications"
WHERE type = "interview"
FLATTEN file.lists AS L
WHERE L.grade = "missed" OR L.grade = "partial"
SORT date(substring(string(date), 0, 10)) DESC, L.grade ASC
```

## Right

```dataview
TABLE WITHOUT ID application AS "Application", round AS "Round", date AS "When", L.grade AS "Grade", L.section AS "Question"
FROM "Applications"
WHERE type = "interview"
FLATTEN file.lists AS L
WHERE L.grade = "right"
SORT date(substring(string(date), 0, 10)) DESC, L.grade ASC
```

## Past

```dataview
TABLE WITHOUT ID application AS "Application", file.link AS "Interview", date AS "When", outcome AS "Outcome"
FROM "Applications"
WHERE type = "interview"
FLATTEN date(substring(string(date), 0, 10)) AS day
WHERE day < date(today)
SORT day DESC, round DESC
```
