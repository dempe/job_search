---
title: notes
date_created: "2026-02-16 11:00"
date_modified: "2026-02-16 11:00"
---

## Authentication

- Client is using pre-signed URLs with S3. This means that downloads are, in fact, authenticated; however, piracy may still be a concern given that a user can share the URL within a given time frame (3600 seconds)
- The download count is tracked but never validated. A customer can download files unlimited times. This line is commented out: `// setDownloadsLimit(firebaseProduct.downloads_limit);`
- `teletonemusic` bucket access is entirely public
- `teletonevideo` S3 bucket also has BPA off, but has a policy that does *NOT* allow public access. Can still be easily added later since BPA is off.
	- Interesting, despite its name, appears to be used as a logging bucket.
- `teletoneinstruments` is accessible via danny's creds only (not just pre-signed URLs CI)

### S3 Recommendations

1. Use a role instead of a long-lived user for accessing `teletoneinstruments`. using a human IAM user for production access is risky; better is a role with scoped permissions
2. Turn on BPA everywhere
3. Limit `teletonemusic` bucket policy since it explicitly allows public access
4. Better yet, if we enable CloudFront, disable all S3 access except via CF


### App Recommendations (in priority order)

  1. Enforce download limits server-side — in the download API route, check downloads_count >= downloads_limit before generating the pre-signed URL
  2. Reduce URL expiration — 15-30 minutes is usually sufficient for a download to start
  3. Add rate limiting on the download endpoint (e.g., max 5 requests per minute per user)
  4. Consider single-use or narrower URLs — e.g., add a response-content-disposition with a unique token, or log and invalidate after first use

## CloudFront

### Code Changes

1. `frontend/src/app/api/products/download/generatePresignedUrl.ts` --  full rewrite
	1. Replace all S3 presigner imports with `import { getSignedUrl } from "@aws-sdk/cloudfront-signer"
	2. Sign against `https://<cloudfront-domain>/<key>` instead of `https://<bucket>.s3.<region>.amazonaws.com/<key>`
	3. Use a CloudFront key pair (RSA private key + key pair ID) instead of AWS access key/secret
	4. The `expiresIn` parameter becomes an absolute expiry date
2. `frontend/src/app/api/products/download/route.ts` -- minor changes
	1. The S3 HeadObjectCommand for file size (lines 23-33) can stay as-is — that's a server-side metadata call, not a download URL
	2. The S3 client (lines 15-21) stays for the getObjectSize function
	3. The URL regex extraction on line 122 may need updating if stored URLs change format
	4. The call to generatePresignedUrl on line 134 stays the same (same signature)
3. New environment variables
	1. `CLOUDFRONT_DISTRIBUTION_DOMAIN=d1234abcdef.cloudfront.net`
	2. `CLOUDFRONT_KEY_PAIR_ID=K1234ABCDEF`
	3. `CLOUDFRONT_PRIVATE_KEY=-----BEGIN RSA PRIVATE KEY-----\n...`
	4. Replaces the need for AWS_ACCESS_KEY_PUBLIC and AWS_SECRET_ACCESS_KEY for signing (though those stay for the HeadObjectCommand).

### AWS Changes