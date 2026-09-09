---
type: question
times_asked: 1
technical: true
title: Explain the difference between a GET request and a POST request.
date_created: "2023-05-30 21:26"
date_modified: "2025-05-31 13:30"
---

GET and POST are the two most common HTTP verbs. GET gets a resource, while POST creates a new resource. POST usually has a body, while GET requests (should) never have a body (though ElasticSearch seems to violate this).

*(Interviewer probed about the differences in **caching and security** between GET and POST)*

URLs are not secure. They are often **cached**, logged, stored in browser history, and, if the user follows a link from your page to another, sent as a referrer URL. Therefore, any sensitive data should be sent in a POST body. This is true even if using HTTPS and hashed passwords.

POST bodies are rarely cached, since it doesn't make sense to do so. A POST request is usually not idempotent, unlike a GET request.[^1]

## Asked by

- [Close (company)](Close%20 (company). md)

## References

[^1]: <https://en.wikipedia.org/w/index.php?title=HTTP&useskin=vector#Idempotent_methods>
