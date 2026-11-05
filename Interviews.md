---
title: Interviews
date_created: "2026-11-04 19:08"
date_modified: "2026-11-05 12:43"
---

## Upcoming Interviews

```dataview
TABLE WITHOUT ID application AS "Application", file.link AS "Interview", date AS "When", interviewers AS "Interviewers"
FROM "Applications"
WHERE type = "interview"
FLATTEN date(substring(string(date), 0, 10)) AS day
WHERE day >= date(today)
SORT day ASC
```

## Interview Scorecard

```dataview
TABLE WITHOUT ID application AS "Application", round AS "Round", date AS "When", length(filter(file.lists, (l) => l.grade = "right")) AS "Right", length(filter(file.lists, (l) => l.grade = "partial")) AS "Partial", length(filter(file.lists, (l) => l.grade = "missed")) AS "Missed", round(100 * length(filter(file.lists, (l) => l.grade = "right")) / length(filter(file.lists, (l) => l.grade))) + "%" AS "%", round(100 * sum(filter(file.lists, (l) => l.content != null).content) / sum(filter(file.lists, (l) => l.content_max != null).content_max)) + "%" AS "Content", round(100 * sum(filter(file.lists, (l) => l.delivery != null).delivery) / sum(filter(file.lists, (l) => l.delivery_max != null).delivery_max)) + "%" AS "Delivery", outcome AS "Outcome"
FROM "Applications"
WHERE type = "interview" AND length(filter(file.lists, (l) => l.grade)) > 0
SORT date(substring(string(date), 0, 10)) DESC
```

## Missed or Partial Questions

```dataview
TABLE WITHOUT ID application AS "Application", L.section AS "Question", date AS "When", round(100 * c / cm) + "%" AS "Content", round(100 * d / dm) + "%" AS "Delivery"
FROM "Applications"
WHERE type = "interview"
FLATTEN file.lists AS L
WHERE L.grade = "missed" OR L.grade = "partial"
FLATTEN L.section AS sec
FLATTEN filter(file.lists, (x) => x.section = sec AND x.content != null)[0].content AS c
FLATTEN filter(file.lists, (x) => x.section = sec AND x.content_max != null)[0].content_max AS cm
FLATTEN filter(file.lists, (x) => x.section = sec AND x.delivery != null)[0].delivery AS d
FLATTEN filter(file.lists, (x) => x.section = sec AND x.delivery_max != null)[0].delivery_max AS dm
SORT date(substring(string(date), 0, 10)) DESC, L.grade ASC
```

## Questions Got Right

```dataview
TABLE WITHOUT ID application AS "Application", round AS "Round", date AS "When", L.grade AS "Grade", round(100 * c / cm) + "%" AS "Content", round(100 * d / dm) + "%" AS "Delivery", L.section AS "Question"
FROM "Applications"
WHERE type = "interview"
FLATTEN file.lists AS L
WHERE L.grade = "right"
FLATTEN L.section AS sec
FLATTEN filter(file.lists, (x) => x.section = sec AND x.content != null)[0].content AS c
FLATTEN filter(file.lists, (x) => x.section = sec AND x.content_max != null)[0].content_max AS cm
FLATTEN filter(file.lists, (x) => x.section = sec AND x.delivery != null)[0].delivery AS d
FLATTEN filter(file.lists, (x) => x.section = sec AND x.delivery_max != null)[0].delivery_max AS dm
SORT date(substring(string(date), 0, 10)) DESC, L.grade ASC
```

## Past Interviews

```dataview
TABLE WITHOUT ID application AS "Application", file.link AS "Interview", date AS "When", outcome AS "Outcome"
FROM "Applications"
WHERE type = "interview"
FLATTEN date(substring(string(date), 0, 10)) AS day
WHERE day < date(today)
SORT day DESC, round DESC
```

## Most-Failed Checks

```dataview
TABLE WITHOUT ID key AS "Check", length(rows) AS "Times failed"
FROM "Applications"
WHERE type = "interview"
FLATTEN file.lists AS L
WHERE L.failed
FLATTEN split(L.failed, ",\s*") AS chk
GROUP BY chk
SORT length(rows) DESC
```

## By Question Type

```dataview
TABLE WITHOUT ID key AS "Type", length(rows) AS "Questions", round(100 * sum(rows.c) / sum(rows.cm)) + "%" AS "Content", round(100 * sum(rows.d) / sum(rows.dm)) + "%" AS "Delivery"
FROM "Applications"
WHERE type = "interview"
FLATTEN file.lists AS L
WHERE L.qtype
FLATTEN L.section AS sec
FLATTEN filter(file.lists, (x) => x.section = sec AND x.content != null)[0].content AS c
FLATTEN filter(file.lists, (x) => x.section = sec AND x.content_max != null)[0].content_max AS cm
FLATTEN filter(file.lists, (x) => x.section = sec AND x.delivery != null)[0].delivery AS d
FLATTEN filter(file.lists, (x) => x.section = sec AND x.delivery_max != null)[0].delivery_max AS dm
GROUP BY L.qtype
SORT sum(rows.c) / sum(rows.cm) ASC
```
