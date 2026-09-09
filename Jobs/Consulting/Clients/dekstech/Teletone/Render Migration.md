---
title: Render Migration
date_created: "2026-04-06 13:54"
date_modified: "2026-04-10 10:30"
---

## Plan

- Download Blueprint file of existing project
	- In the main dashboard, select the checkbox next to `teletone-audio-downloads-server`
	- Click "Generate Blueprint"
- Commit `render.yaml` to repo `teletone-audio-downloads`
- On new account, click New -> Blueprint and connect to `DeKs-Technology-Solutions-LLC/teletone-audio-downloads` repo on Github. Deploy it.
- Download the environment variables from the DekTech's Render account in the Environment Variable tab. Hit export and save the generated `.env` file.
- In the new Render account, go to the tab for Environment Variables, select "Add from .env" and import the `.env ` file.
- Do a test deploy under a temporary name to ensure that everything builds. Be sure to hit an actual URL and verify that it works.
- Shutdown DeksTech Render project to free up the domain name `https://teletone-audio-downloads-server.onrender.com`
	- There will be about **10 - 15 min downtime**
- In the new account, enable the option to "Render Subdomain" (the `.onrender` domain).
	- **Note**: this might already be enabled by default
- Deploy a new version with the new domain
- Ensure that everything works, especially downstream services that call this URL

## Progress

- [x] Download Blueprint file of existing project
- [x] Commit `render.yaml` to repo `teletone-audio-downloads`
- [x] On new account, click New -> Blueprint and connect to `DeKs-Technology-Solutions-LLC/teletone-audio-downloads` repo on Github. Deploy it.
	- [x] Hit a snag here… Have to wait for DeksTech to Authenticate with Teletone's Render acct…
	- [x] Will just connect with personal GH account and make note to change that over later.
- [x] Download the environment variables from the DekTech's Render account in the Environment Variable tab. Hit export and save the generated `.env` file.
- [x] In the new Render account, go to the tab for Environment Variables, select "Add from .env" and import the `.env ` file.
- [x] Do a test deploy under a temporary name to ensure that everything builds.
- [x] Hit an actual URL and verify that it works.
	- [x] Looks like there are only 3 end points — `/`, ` /test-firestore`, and `/events/order-paid`
	- [x] <https://teletone-audio-downloads-server.Onrender.Com/test-firestore>
	- [x] Ran `curl -Xv POST https://teletone-audio-downloads-server-gvu7.onrender.com/events/order-paid` and got `400 Bad Request` on both
	- [x] Ran it with a POST body as well: `curl -Xv POST https://teletone-audio-downloads-server-gvu7.onrender.com/events/order-paid -H "Content-Type: application/json" -d '{}'`. Same `400 Bad Request` on both!
- [ ] Shutdown DeksTech Render project to free up the domain name `https://teletone-audio-downloads-server.onrender.com`
- [ ] In the new account, enable the option to "Render Subdomain" (the `.onrender` domain).
- [ ] Deploy a new version with the new domain
- [ ] Ensure that everything works, especially downstream services that call this URL

## Timelog

### 2026-04-06

- 12:00 - 12:10 — commit `render.yaml`, login to Teletone acct, realize that I'm blocked and msg Luke and Julia

### 2026-04-10

- 9:45 - 10:00 — deploy Teletone Render
- 10:10 - 10:30 — Test new deploy

### 2026-04-22

- 19:50 - 