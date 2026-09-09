---
title: _MOC Questions
date_created: "2023-05-30 15:08"
date_modified: "2025-05-31 13:30"
---

## Non-technical Questions

```dataview
TABLE times_asked AS "Times Asked"
FROM "Job Search/Questions"
WHERE technical = false
SORT times_asked DESC
```

## Technical Questions

```dataview
TABLE times_asked AS "Times Asked"
FROM "Job Search/Questions"
WHERE technical = true
SORT times_asked DESC
```

## Questions for Interviewers

- What are the projects this company thinks are key to its future and how would someone go about getting on them?
- Based on this interview, can you give me some advice on how I might improve? What do you think should I study?

## Resources

- <https://jacobian.org/series/unpacking-interview-questions/>
