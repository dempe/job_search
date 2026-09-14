---
title: estimate
date_created: "2026-02-16 11:01"
date_modified: "2026-02-16 13:24"
---

Scope: Secure paid-download infrastructure by placing CloudFront in front of private S3 buckets, implementing signed access, removing public exposure, and updating the application to use the new delivery path.
Estimated effort: ~16 hours
Expected range: 11 - 23 hours depending on authentication and hosting details
Business days: 6

- CloudFront Setup: 2 - 4 hours
	- Create distribution(s)
	- Configure S3 origins
	- Set caching behavior/TTLs
	- Verify large file delivery (Range requests)
	- Configure logging if desired
- S3 Hardening: 2 - 4 hours
	- Enable Block Public Access (BPA) on paid buckets
	- Remove public read policies
	- Restrict bucket access to CloudFront via OAC
- Download Authentication Update: 3 - 6 hours
	- Implement CloudFront signed URLs or cookies
	- Replace long-lived IAM credentials with least-privilage signing approach
	- Validate entitlement flow
- Application Updates: 3 - 7 hours
	- Update download endpoints
	- Validate client behavior
	- End-to-end testing
- Download Progress bar: .5 - 2 hours
	- 0.5–2 hours assuming the current download mechanism exposes byte-level progress.  If not, we may need a different implementation, which I will bring up before spending more time.
- Deployment / Rollout: 1 - 2 hours
	- Controlled cutover
	- Verify direct S3 is no longer accessible
	- Confirm CloudFront delivery


2a) Ensuring people can download a 30gb file - what's the speed look like

Both S3 and CloudFront are designed to handle very large file delivery. A 30GB download is well within normal operating limits.

Putting CloudFront in front of S3 is beneficial mostly for two reasons:
• It distributes traffic across AWS edge locations, improving download consistency for geographically distributed users.
• It allows us to make the S3 bucket fully private while serving downloads through a controlled endpoint.

This improves reliability and reduces the risk of unintended public access.

2b) Need to use automated testing tool to see if there are 100 - 200 users, making sure it can actually handle this sort of load

100 - 200 concurrent downloads of a 30 GB file represents roughly 3 - 6 TB of transfer. This is well within the designed throughput of both S3 and CloudFront.

We can also validate this during rollout by monitoring real-world traffic patterns rather than relying on load tests, which may not reflect large-file download behavior (for example, a load test can vary wildly based on ISP, geographic location, if the cache is warm, etc.).


2c) Question around if we should be splitting up the file - Ryan will send an example but may not be completely necessary. is this even necessary? need to research this a bit - could just be archaic / old school process

Manually splitting large files is generally no longer necessary. HTTP range requests allow clients to request specific portions of a file as needed.

Both S3 and CloudFront support this natively.  On the client-side, modern download manager also support range requests out-of-the-box.

2d) If user quits the session or hits pause, can it somehow pick back up to where it left off

Yes. Because S3 and CloudFront support HTTP range requests (see above), most browsers and download managers can resume interrupted downloads automatically from the last completed byte rather than restarting the entire transfer.

Additional thoughts

The primary priority should be placing the S3 buckets behind a controlled delivery layer (CloudFront). This allows the buckets themselves to remain private while providing a secure, scalable download path.

During review, I noticed that:

• One bucket is publicly accessible.
• Another uses pre-signed URLs with a one-hour expiration (anyone possessing the URL can download during that time).
• One bucket is accessed using long-lived IAM user credentials.

I recommend moving to a role-based, least-privilege setup.  This will reduce security risks and aligns with AWS best practices.