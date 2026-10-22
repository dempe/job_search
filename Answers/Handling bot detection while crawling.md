## People Data Labs

[[People Data Labs]]

> How do you handle anti-scraping mechanisms or bot detection while crawling?

```
First, determine the cuase of the failure. A 429 requires exponential-backoff with jitter.  The site might require logging in.  Make sure you're using a Javascript-capable browser if the website requires it.

If there's an explicit Captcha or access protenction, stop the crawl and check if there's API access.

Also, I make sure that my crawlers have a circuit breaker built in so that they don't keep hitting a site that's blocking them. At DataRank, I even had a live dashboard built in Jenkins that showed crawler status (via automated system tests) for observability.  Mostly for the customer success team to get immediate info.
```
