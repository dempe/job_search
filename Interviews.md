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
TABLE WITHOUT ID application AS "Application", round AS "Round", date AS "When", length(filter(file.lists, (l) => l.grade = "right")) AS "Right", length(filter(file.lists, (l) => l.grade = "partial")) AS "Partial", length(filter(file.lists, (l) => l.grade = "missed")) AS "Missed", round(100 * length(filter(file.lists, (l) => l.grade = "right")) / length(filter(file.lists, (l) => l.grade))) + "%" AS "%", outcome AS "Outcome"
FROM "Applications"
WHERE type = "interview" AND length(filter(file.lists, (l) => l.grade)) > 0
SORT date(substring(string(date), 0, 10)) DESC
```

## Missed or Partial Questions

```dataview
TABLE WITHOUT ID application AS "Application", L.section AS "Question", date AS "When", L.grade AS "Grade"
FROM "Applications"
WHERE type = "interview"
FLATTEN file.lists AS L
WHERE L.grade = "missed" OR L.grade = "partial"
SORT date(substring(string(date), 0, 10)) DESC, L.grade ASC
```

## Questions Got Right

```dataview
TABLE WITHOUT ID application AS "Application", round AS "Round", date AS "When", L.section AS "Question"
FROM "Applications"
WHERE type = "interview"
FLATTEN file.lists AS L
WHERE L.grade = "right"
SORT date(substring(string(date), 0, 10)) DESC
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
WHERE regexmatch("^\*\*[a-z_]+(:[a-z_]+)?:\*\* .*$", L.text) AND contains(filter(file.lists, (p) => p.line = L.parent)[0].text, "missing::")
FLATTEN regexreplace(L.text, "^\*\*([a-z_]+(:[a-z_]+)?):\*\* .*$", "$1") AS chk
GROUP BY chk
SORT length(rows) DESC
```

