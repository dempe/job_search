---
title: _MOC Jobs
date_created: "2023-05-30 15:06"
date_modified: "2026-09-15 01:02"
---

## Upcoming Interview

```dataview
TABLE filter(file.inlinks, (l) => contains(meta(l).path, "/Interviews/")) AS "Interviews", source AS "Source"
FROM "Applications"
WHERE status = "interview"
```

## Follow Up

```dataview
TABLE choice(
    date(applied) = date(today),
    "today",
    date(today) - date(applied) + " ago"
  ) AS "Applied", source AS "Source"
FROM "Applications"
WHERE status = "follow-up"
```

## Awaiting Reply

```dataview
TABLE choice(
    date(applied) = date(today),
    "today",
    date(today) - date(applied) + " ago"
  ) AS "Applied", source AS "Source", contract AS "Contract"
FROM "Applications"
WHERE status = "awaiting-reply"
SORT date(applied) ASC
```

## Applied to This Year

```dataview
TABLE date(applied) AS "Applied", source AS "Source"
FROM "Applications"
WHERE date(applied) >= date("2026-01-01")
SORT applied DESC
```

## Offer

```dataview
TABLE filter(file.inlinks, (l) => contains(meta(l).path, "/Interviews/")) AS "Interviews", source AS "Source"
FROM "Applications"
WHERE status = "offer"
```

## Declined

```dataview
TABLE applied AS "Applied", source AS "Source", length(filter(file.inlinks, (l) => contains(meta(l).path, "/Interviews/"))) AS "Num Interviews"
FROM "Applications"
WHERE status = "declined"
SORT applied DESC
```

## Rejected

```dataview
TABLE applied AS "Applied", source AS "Source", length(filter(file.inlinks, (l) => contains(meta(l).path, "/Interviews/"))) AS "Num Interviews"
FROM "Applications"
WHERE status = "rejected"
SORT applied DESC
```

## Ghosted

```dataview
TABLE applied AS "Applied", source AS "Source", length(filter(file.inlinks, (l) => contains(meta(l).path, "/Interviews/"))) AS "Num Interviews"
FROM "Applications"
WHERE status = "ghosted"
SORT applied DESC
```

## Total Interviews

```dataview
TABLE filter(file.inlinks, (l) => contains(meta(l).path, "/Interviews/")) AS "Interviews", source AS "Source", channel AS "Channel"
FROM "Applications"
WHERE length(filter(file.inlinks, (l) => contains(meta(l).path, "/Interviews/"))) > 0
SORT channel, max(map(filter(file.inlinks, (l) => contains(meta(l).path, "/Interviews/")), (l) => string(l.file.frontmatter.date))) DESC
```
