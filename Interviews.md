---
title: Interviews
date_created: "2026-11-04 19:08"
date_modified: "2026-11-05 12:43"
---

## Upcoming Interviews

```dataview
TABLE WITHOUT ID application AS "Application", file.link AS "Interview", file.frontmatter.date AS "When", interviewers AS "Interviewers"
FROM "Applications"
WHERE type = "interview"
FLATTEN date(substring(string(file.frontmatter.date), 0, 10)) AS day
WHERE day >= date(today)
SORT day ASC
```

## Interview Scorecard

```dataview
TABLE WITHOUT ID application AS "Application", file.link AS "Interview", file.frontmatter.date AS "When", length(filter(file.lists, (l) => l.grade = "pass" AND !regexmatch("^[0-9]+$", meta(l.section).subpath))) AS "Pass", length(filter(file.lists, (l) => l.grade = "fail" AND !regexmatch("^[0-9]+$", meta(l.section).subpath))) AS "Fail", round(100 * length(filter(file.lists, (l) => l.grade = "pass" AND !regexmatch("^[0-9]+$", meta(l.section).subpath))) / length(filter(file.lists, (l) => l.grade AND !regexmatch("^[0-9]+$", meta(l.section).subpath)))) + "%" AS "%", outcome AS "Outcome"
FROM "Applications"
WHERE type = "interview" AND length(filter(file.lists, (l) => l.grade AND !regexmatch("^[0-9]+$", meta(l.section).subpath))) > 0
SORT date(substring(string(file.frontmatter.date), 0, 10)) DESC
```

## Failed Questions

```dataview
TABLE WITHOUT ID application AS "Application", L.section AS "Question", file.frontmatter.date AS "When"
FROM "Applications"
WHERE type = "interview"
FLATTEN file.lists AS L
WHERE L.grade = "fail" AND !regexmatch("^[0-9]+$", meta(L.section).subpath)
SORT date(substring(string(file.frontmatter.date), 0, 10)) DESC
```

## Passed Questions

```dataview
TABLE WITHOUT ID application AS "Application", file.link AS "Interview", file.frontmatter.date AS "When", L.section AS "Question"
FROM "Applications"
WHERE type = "interview"
FLATTEN file.lists AS L
WHERE L.grade = "pass" AND !regexmatch("^[0-9]+$", meta(L.section).subpath)
SORT date(substring(string(file.frontmatter.date), 0, 10)) DESC
```

## Past Interviews

```dataview
TABLE WITHOUT ID application AS "Application", file.link AS "Interview", file.frontmatter.date AS "When", outcome AS "Outcome"
FROM "Applications"
WHERE type = "interview"
FLATTEN date(substring(string(file.frontmatter.date), 0, 10)) AS day
WHERE day < date(today)
SORT day DESC, round DESC
```

## Most-Failed Checks

```dataview
TABLE WITHOUT ID key AS "Check", length(rows) AS "Times failed"
FROM "Applications"
WHERE type = "interview"
FLATTEN file.lists AS L
WHERE regexmatch("^\*\*[a-z_]+(:[a-z_]+)?:\*\* .*$", L.text) AND contains(filter(file.lists, (p) => p.line = L.parent)[0].text, "missing::") AND !regexmatch("^[0-9]+$", meta(L.section).subpath)
FLATTEN regexreplace(L.text, "^\*\*([a-z_]+(:[a-z_]+)?):\*\* .*$", "$1") AS chk
GROUP BY chk
SORT length(rows) DESC
```

