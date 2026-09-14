---
title: CDN Documenation Writeup
date_created: "2026-04-06 08:08"
date_modified: "2026-04-06 08:08"
---

## Data

All data is stored in S3 and accessed via CloudFront.  There is one S3 bucket where all data is stored, `teletone-assets`.  Inside `teletone-assets`, there are three directories, `music`, `trials`, and `instruments`.  This bucket, including all its directories, is completely private and only accessible via CloudFront.

CloudFront writes logs to the S3 bucket, `teletone-assets-logs`.

## Routing

There is a single CloudFront distribution, `E1H1PGEJWNGX2` (`cdn.teletoneaudio.com`), that accesses the data in S3.  Each directory in the S3 bucket has its own CloudFront behavior that determines how it's access:

- `/music/*`: all data in music is publicly accessible via CloudFront (requires no authentication)
- `/trials/*`: all data in the `trials` directory is also publicly accessible via CloudFront (no authentication)
- `/instruments/*`: all data in the `instruments` directory requires a signed URL with a TTL of 24 hours to access.
- Any incoming request that does not match one of the above patterns is sent to the default behavior, which returns a 403 ACCESS DENIED error.

## Performance

CloudFront provides a few performance benefits over raw S3.

- **Edge caching/geographic distribution**: CloudFront caches and distributes content globally placing it closer to end users.  This reduces latency, since users connect to the edge location that is closer to them.
- **Connection optimization**: When a user attempts to download a 30 GB file, they will connect to CloudFront's closest edge location.  CloudFront then connects to S3 via a highly optimized, internal network.  This greatly reduces the chances of timeouts or failed transfers over long distances.
- **Traffic spikes**: S3 has rate limits per prefix.  With a lot of concurrent downloads S3 could start throttling and rate limiting downloads. CloudFront absorbs these traffic spikes and returns data from the cache rather than hammering S3.
- **Cost**: Egress from CloudFront is generally cheaper per GB than S3

## Security

- **Private S3**: all the raw data in S3 is fully private and only accessible via CloudFront (and the AWS console). 
- **Single point of access control**:  Since all traffic flows through CloudFront first, it's straightforward to monitor, audit, and modify access rules.  
- **WAF (Web Application Firewall)**: WAF provides protection against common web exploits, malicious IPs, and bot traffic. Custom rules can also be added if needed.
- **Geographic Restrictions**: CloudFront can also block traffic based on country of origin.

## Logging and Monitoring

CloudFront makes it a lot easier to log and monitor traffic than S3.

- **Standard access logs**: stored in the S3 bucket, `teletone-assets-logs`.  These are the raw request logs.  Can be fed into many programs for analysis or visualization
- **CloudWatch metrics**: CloudFront publishes metrics to CloudWatch automatically: total requests, bytes downloaded/uploaded, error rates, cache hit ratio.  Can also set up alarms on these metrics, for example, if 4xx or 5xx error rates start to spike.
- **WAF logs**: *not currently configured*, but WAF can be logged too — which requests were allowed, blocked, or counts per rule.