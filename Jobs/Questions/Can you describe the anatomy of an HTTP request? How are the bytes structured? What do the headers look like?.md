---
type: question
times_asked: 1
technical: true
title: Can you describe the anatomy of an HTTP request? How are the bytes structured? What do the headers look like?
date_created: "2023-05-30 21:43"
date_modified: "2025-05-31 13:30"
---

An HTTP request consists of a request line that specifies the HTTP method, requested URL, and HTTP version. After this line follows various headers, key/value pairs, each to one line, where the key is terminated by a colon. After the headers is the body of the request. This is optional, but it's usually provided with a POST or a PUT.

Some of the most common request headers are:

- `Host` — distinguishes between various DNS names sharing a single IP address, allowing name-based virtual hosting.
- `Accept` — what type of content the client accepts
- `Accept-Language` — list of languages the client accepts
- `Accept-Encoding` — list of encodings the client accepts
- `Connection` — `keep-alive` or `close`

"How are the bytes structured?" Not sure if I misheard or not, but this question makes no sense to me. Couldn't get any more info out of Wikipedia, ChatGPT, or Mozilla…

## Asked by

- [Close (0)](Close%20(0).md)
