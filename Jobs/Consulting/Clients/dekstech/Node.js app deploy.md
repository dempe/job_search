---
title: Node.js app deploy
date_created: "2026-05-01 11:42"
date_modified: "2026-05-01 11:42"
---

Can't find previous notes... I do remember i was at 2:15 hours.

Got the domain name, `app.hvpowersports.com.hvpowersports.com` (lol).  Will pickup here.

## 2026-05-01

### 11:53 - 12:40

- Run certbot to get SSL for domain name 
- Update `.toml` files and `.env` to point to correct domain
- Re-build app
- Shopify Partners gets the app URLs via the `.toml` files, so needed to run `shopify app deploy`
- But had to install `shopify-cli`
- Then had to symlink `xdg-open` to `echo` so that i could actually copy the generated URL and verify
- After all of that, I verified in HV power sports admin panel that the app is successfully loading

### 15:00 - 15:10

Redeploy with correct domain name — `app.hoversports.com` 


## Total

2:10 + :50 + :10 = 3:10