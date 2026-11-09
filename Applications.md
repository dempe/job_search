---
title: Applications
date_created: "2023-05-30 15:06"
date_modified: "2026-11-09 12:21"
---

## Follow Up

```dataviewjs
await dv.view("_meta/scripts/applications", {followUp: true, columns: ["ago", "source"]})
```

## Awaiting Reply

```dataviewjs
await dv.view("_meta/scripts/applications", {status: "awaiting-reply", columns: ["ago", "source", "contract"], sort: "asc"})
```

## Applied to This Year

```dataview
TABLE date(applied) AS "Applied", source AS "Source"
FROM "Applications"
WHERE date(applied) >= date("2026-01-01")
SORT applied DESC
```

## Offer

```dataviewjs
await dv.view("_meta/scripts/applications", {status: "offer", columns: ["applied", "source", "interviews"], sort: "desc"})
```

## Declined

```dataviewjs
await dv.view("_meta/scripts/applications", {status: "declined", columns: ["applied", "source", "interviews"], sort: "desc"})
```

## Rejected

```dataviewjs
await dv.view("_meta/scripts/applications", {status: "rejected", columns: ["applied", "source", "interviews"], sort: "desc"})
```

## Ghosted

```dataviewjs
await dv.view("_meta/scripts/applications", {status: "ghosted", columns: ["applied", "source", "interviews"], sort: "desc"})
```
