---
title: time-log
date_created: "2026-02-16 10:57"
date_modified: "2026-02-21 09:42"
---

Feb 16<br/>
10:00 - 10:30 consulting call<br/>
11:05 - 11:15: accounts setup<br/>
11:15 - 11:25: initial repo review<br/>
11:45 - 12:30: initial repo review<br/>
12:35 - 13:15: initial repo review

## S3 + CloudFront

### 02-20

12:30 - 13:30: set up CF<br/>
14:30 - 15:30: trying to get access to app; connected second origin to CF<br/>
16:30 - 17:00: trying to get access to app<br/>
20:45 - 21:15: installed Vercel CLI tool; loaded app in browser

Total: 180 min - 3 hours

### 02-21

11:20 - 11:30: verify s3 access; determined that only 1 bucket will be needed
11:50 - 12:20: confirmed pre-signed URLs work with key pair; added `teletoneistruments` origin
13:15 - 14:00: configure OAC for CF to `teletoneinstruments`; figured out why i'm getting 403s via CF -- objects in `teletoneinstruments` have their ACLs set to *object writer*, not *bucket owner*.  This will need to be remediated.
14:45 - 15:20: verifying what is public and what is private; and plan
15:40 - 16:00: planning migration to new S3 bucket with ACLs off and BPA on
16:20 - 16:40: investigating what public content is being used
18:30 - 19:30: setup `teletonemusic` CF

Total: 220 min - 3.5 hours

### 02-22

-12:15 - 12:30
	- updated shopify theme repo to DL music from CF;
	- added CORS to `teletonemusic` CF
-13:00 - 15:25
	- setup single origin, `teletone-assets`
	- Removed other CF distribution.
	- Removed other origins from the existing CF distribution and added `teletone-assets` origin
	- Added behavior for `/music/*` prefix
	- Rest of time spent debugging why requests to CF are 403ing
	- Started script to sync `teletoneinstruments` to corresponding prefixes (`paid`, `public`) in `teletone-assets`.
-17:30 - 19:00
	- Migrated public content in `teletoneinstruments` to `teletone-assets/instruments/public/`
	- Likewise for paid content.
	- Confirmed that signed URLs work for accessing content in `teletone-assets/instruments/paid/`
	- Confirmed that unsigned URLs to `teletone-assets/instrumentes/paid/*` do NOT work (403). Public content is still accessible.
	- Removed random ACL access in favor of prefix-based semantics

Total: 290 min - 4 hours

### 02-23

- 10:30 - 12:30
	- Made shopify theme PR
	- Posted update to channel
	- Created plan for frontend updates
- 15:15 - 16:20
	- Finding login for site
	- Checking out the URLs in Firestore
	- Built script to add CF URLs to Firestore
- 18:15 -
	- Add `cf_url` field to URLs in Firestore
	- 

Total: 5 hours. Ish?

### 02-24

- 10:00 - 14:00
	- Started frontend changes
	- Added ACM cert for CF
	- Finished frontend changes

Total: 4 hours.  Ish?

## 03-03

- 9:45 - 10:20
	- Sign up for Loom
	- Install Loom
	- Outline
	- First recording
- 