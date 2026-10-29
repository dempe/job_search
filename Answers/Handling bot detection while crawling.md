## People Data Labs

[[People Data Labs]]

> How do you handle anti-scraping mechanisms or bot detection while crawling?

```
First, determine the cuase of the failure. A 429 requires exponential-backoff with jitter.  The site might require logging in.  Make sure you're using a Javascript-capable browser if the website requires it.

If there's an explicit Captcha or access protenction, stop the crawl and check if there's API access.

Also, I make sure that my crawlers have a circuit breaker built in so that they don't keep hitting a site that's blocking them. At DataRank, I even had a live dashboard built in Jenkins that showed crawler status (via automated system tests) for observability.  Mostly for the customer success team to get immediate info.
```

## People Data Labs (interview)

[[People Data Labs]]

> How did you handle anti-scraping mechanisms or bot detection while crawling?

```
It depends on what's actually blocking you, so the first step is diagnosing it.

Before any of that: if a site's robots.txt or terms say don't crawl, we don't. We'd tell the customer, or reach out to the site about access.

For rate limiting, like a 429, it's exponential backoff with jitter, and per-domain rate limits so we never hammer a single site. For sites that need JavaScript, we escalated to a headless browser, and for login walls, we automated the login form.

Beyond that, the standard techniques are making traffic look less mechanical: rotating proxies so requests don't all come from one IP, rotating and randomizing user agents and headers, randomizing request timing, and keeping sessions and cookies consistent the way a real browser would.

I'd also build in a circuit breaker per site, so if we start getting blocked, the crawler stops instead of burning through proxies and making it worse. If we hit an explicit CAPTCHA or access protection, that's a signal to stop and check whether there's an API or a data partnership, not to escalate.
```
