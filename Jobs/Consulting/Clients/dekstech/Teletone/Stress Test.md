---
title: Stress Test
date_created: "2026-04-21 15:53"
date_modified: "2026-04-21 21:50"
---

## Reconnaissance

Render's backend is a separate service (Shopify webhooks, order handling, email) — not in the download hot path.

Stress-test implications

Hot path is Vercel + Firestore, not Render:

1. Vercel serverless function concurrency on `/api/products/download` — cold starts and per-region concurrency caps. Default limit matters.
2. Firestore reads 2 per request (serial and product). Free-tier/quota concerns if N is large. Firestore is also single-region-primary so latency floor is real.
3. CloudFront/S3 for bytes. No the worries here.

## Plan

### Prerequisites

1. Get test credentials. Need at least one serial/SKU/email tuple that will pass validation (serial_numbers.status ∈ {distributed, redeemed}, products.downloads_active = true).
2. Confirm cold-start baseline. Let the Vercel function idle ~15 min before kicking off test #1 so we actually measure a cold start.

### Burst Test

- Target: `POST /api/products/download` with valid JSON body
- Fire 50 requests in < 1 sec (hey -n 50 -c 50 … or equivalent)
- Capture: p50 / p95 / p99 latency, any 5xx, any Firestore throttling
- Rerun once warm (no idle) to see warm-path numbers
- Pass criteria: no 5xx, p95 warm < ~500ms, cold start p99 < ~3s

### Handful of Real 30 GB Downloads

- 3–5 concurrent end-to-end downloads
	- different network conditions (home, fiber, cellular tether, etc.) would be ideal
- Measure per session:
	- Time-to-first-byte after CF URL issued
	- Sustained throughput (MB/s averaged over download)
	- Total duration
- Pass criteria:
	- throughput saturates the client connection
	- no mid-stream failures

### Resume-after-interruption Test

Three sub-cases, same download file:

1. Mid-stream network blip. Disable network briefly (10–30s), re-enable. Browser should auto-resume via range
2. Pause + resume within TTL. Pause in Chrome/Safari download manager, wait ~1 hr, resume.
3. Pause + resume after TTL expired. Pause, wait 25+ hrs, resume. Expect: 403

### UI expired-URL Audit

- Check `frontend/src/app/serials/page.tsx` and the download modal code to see if there's any handling for expired signed URLs. If not, that's a finding for the client — resume after 24h silently fails. Options: shorten TTL + auto-refresh, or add a "re-issue link" button.

### Cost Sanity Check

- Pull actual CF egress + request pricing from the client's AWS billing (6 TB * $0.085/GB ≈ $510)

## Execution

### 2026-04-22

#### 16:30 - 17:00

basic script running

###  2026-04-23

#### 12:00 - 13:00

`k6` can generate reports automatically, just need to set the env vars:

```

```

Trying to generate a good report. Testing against localhost at the moment, but it quickly saturates the server.  Vecel has automatic horizontal scaling built-in.

`k6 run --vus 20 --duration 60s stress-test/burst.js` -- running this against localhost


```
⏺ End-to-end call chain per iteration:

  1. k6 → POST https://teletone-audio-downloads.vercel.app/api/products/download with
  {serial_number, product_sku, email} body and customer_access_token cookie.
  2. Vercel edge routes to the Next.js serverless function at
  frontend/src/app/api/products/download/route.ts.
  3. authenticate() middleware fires first — it extracts the customer_access_token cookie and
  calls Shopify Storefront GraphQL API to verify the customer is logged in and get their email.
   (This is the biggest chunk of latency — external network hop to Shopify.)
  4. Firestore read #1 — fetch serial_numbers/{serial} document.
  5. Validation: serial's product_sku matches the request, assigned_email matches
  (case-insensitive), status is distributed or redeemed.
  6. Firestore read #2 — fetch products/{sku} document.
  7. Validation: downloads_active === true.
  8. For each file in each version of the product, call generateSignedUrl() — which uses
  @aws-sdk/cloudfront-signer to produce a CloudFront signed URL with 24h TTL. Pure CPU, no
  network.
  9. Return JSON {success: true, versions: {...}} with all signed URLs.

  What the test measures: end-to-end signing-endpoint latency under concurrency. Roughly:
  Shopify auth RTT + 2 Firestore reads + N×CF-signing (CPU) + serialization overhead.

  What it does NOT measure: the actual 30 GB file download from CloudFront. That's a separate
  concern — CloudFront + S3 handle it, not the Vercel function. The function just hands out
  pre-signed URLs; the browser/client then downloads directly from cdn.teletoneaudio.com over a
   CF edge.

  So this burst test validates the "can the signing endpoint keep up when 50-200 customers hit
  download simultaneously" question. The "can CF/S3 serve 30 GB × 200 concurrently" question is
   answered by your planned real-download test, separately.

```

#### 14:50 - 15:30

Writing stress test summary for client.

