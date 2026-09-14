## Lithic

Source: [[Lithic]]

> What do you think are our most complex technical challenges based on the very little you know about Lithic?

```
I bet Lithic's most complex problems revolve around reliability and correctness in a distributed financial system. 

Card processing involves a lot of asynchronous events, retries, timeouts, and partial failures, so I'm sure idempotency is critical. Also, a dropped or partially processed event may need to be recovered without corrupting state.
```
