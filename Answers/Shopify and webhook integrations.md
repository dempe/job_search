## dekstech

[[dekstech]]

> Do You Have Experience with Shopify at All?

```
No, but I'm familiar with the general patterns. For example, Shopify pushes events to your backend via webhooks. You call back into it through the API. I've built similar webhook-driven backends. Verify the signature on each request, make the handler idempotent because webhooks can be delivered more than once, and push the slow work onto a queue so you can respond fast.
```
