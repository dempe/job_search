---
title: Secure download links
date_created: "2026-04-29 09:35"
date_modified: "2026-04-29 10:42"
---

This is a Shopify admin task — joy! We'll be installing a Shopify app to protect their audio downloads. Customers should get a one-time, expiring link emailed to them after purchase.

The client has about 50 audio files ranging in size from a few hundred KB to 14 MB.

<https://apps.shopify.com/digital-assets?st_campaign=admin-search&st_source=admin-web>

## 2026-04-29

### 09:40 - 10:00

Investigating. Looks like they link directly to the CDN on the site. Not an issue. They have previews.

### 10:40 - 10:50

<https://cdn.shopify.com/s/files/1/0760/6475/1804/files/COTTON_TOP.mp3?v=1777320771>

<https://cdn.Shopify.Com/s/files/1/0760/6475/1804/files/COTTON_TOP.Ld?V=1776440734>

The full sample is a proprietary `.ld` format.  So you can't play it via normal audio player.

Metafield namespace + ID: `custom.sound_file_url`.  This points to the `.ld` file.

Hopefully, we can call Shopify's API to pull a list of their audio file products, extract the `custom.sound_file_url` for each, and use FileFlare's API to link to the product.

### 16:20 - 

