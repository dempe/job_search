---
title: Working Notes
date_created: "2026-03-23 13:34"
date_modified: "2026-03-23 16:36"
---

## Problem

They use their Shopify storefront for all *pre*-purchase activity. When a customer wants to purchase something, they are directed to **Retail Solutions**. That is, purchases are not done on Shopify.

What actually counts a converstion?

## Overview

## Notes

- Each page loads an Asute pixel `    <script type="text/javascript" src="https://astute52.com/js/811150.js" ></script> <noscript> <img alt="" src="https://astute52.com/811150.png" style="display:none;" /> </noscript>`, so alternative third party tracking does exist
- The checkout domain is `shop.skbcases.com` — a subdomain, not a different domain
- Can't access purchase flow from normal page load
- GTM is being used. Container ID: `GTM-PW5NFX8`
- Safari and Brave can and do block GA entirely
- The site is using direct gtag.js, not Google Tag Manager
- Event tracking context is lost at checkout (`window.dataLayer` is `undefined` once the checkout process starts (i.e., when we are redirected to `shop.skbcases.com`))
- 
