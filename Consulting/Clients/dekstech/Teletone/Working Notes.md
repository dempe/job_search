---
title: Working Notes
date_created: "2026-02-20 12:53"
date_modified: "2026-02-22 13:14"
---

## Private S3 + CloudFront

- Created staging buckets `staging-bucket1-efd44166`, ` staging-bucket2-cce4fe4c `
- Created CF distribution `teletone-secure-downloads-prod`
	- Selected pay-as-you-go until we have more usage data
	- WAF estimated cost: $14 for 10 million requests/month

## 02-22

okay, the easy part is done:

- setup CF distribution for `teletonemusic` s3 bucket.
- setup CORS for `teletonemusic` CF distribution
- changed shopify theme URLs that were pointing to S3 to point to CF
- confirmed I can access these URLs via CF

tomorrow:

- explain progress to Luke
- ask how to deploy the site
- ask if anything else is or might be hitting the raw s3 bucket
- deploy site
- verify that it works
- turn on BPA on `teletonemusic` bucket

now:

- create a `teletoneinstruments-private` and `teletoneinstruments-public` buckets
- connect my AWS CLI to teletone AWS
- write script to determine if content in `teletoneinstruments` is public or private and copy it to the corresponding bucket.
- set up CF origin for `teletoneinstruments-private` and `teletoneinstruments-public`
- verify that i can access content from both via CF
- turn on OAC for both
- enable pre-signed URL access only to `teletoneinstruments-private`
- verify that it works

- Previously, buckets had items that were randomly public via ACLs.  Now, they are public (or private) based on path.

```
## CloudFront Migration

Migrates file downloads from direct S3 URLs to CloudFront with signed cookies and uses the browser's native download manager.

### What changed
- **Download auth**: replaced per-file S3 pre-signed URLs with CloudFront signed cookies (48 hr TTL, wildcard policy covering all files in one cookie set)
- **Download UX**: replaced JS fetch+blob approach with browser-native downloads. Eliminates memory crash risk on large files and hands off progress/pause/resume/progress bar complexity to the browser's download manager
- **Download modal**: now fetches all version URLs server-side in one request and renders plain anchor tags; user clicks to trigger each download
- **Admin panel**: Files tab now reads/writes the `cf_url` field (CloudFront) instead of `url` (S3); URL validator updated to `cdn.teletoneaudio.com`
- Added CloudFront env vars (`CLOUDFRONT_DOMAIN`, `CLOUDFRONT_KEY_PAIR_ID`,
`CLOUDFRONT_PRIVATE_KEY`). They are set in the Vercel project page

### Rollback
The original S3 `url` field is preserved on all Firestore records, and the original buckets are still live in AWS. Reverting the code is sufficient to fall back to S3.
```

## Re-Implementation Strategy

```
i've updated the backend to ensure that all content now requires authorization to access.

before moving on with the frontend, i wanted clarify a few things first.

the 403s that we encountered today were due to the signed cookies, not the browser's download manager.  for example, we verified that we could successfully download content that didn't require authorization.
 
i can easily update the branch to use pre-signed URLs instead of signed cookies.  this should resolve all of the 403s that we were seeing and make testing muuuch easier.

if we continue to use the in-app download logic, there is a strong possibility of the clients running out of memory unless we implement streaming downloads as well.

i wanted to bring this up, since the reason for this project was to ensure and secure large file downloads, and i think using the browser's download manager is the best option given this goal.
```