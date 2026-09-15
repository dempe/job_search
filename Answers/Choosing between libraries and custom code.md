## Rivora

[[Rivora]]

> Tell us about the last time you chose between an existing library/package and writing something yourself for the same problem. What did you pick, and why?

```
As mentioned in the previous answer, Claude wanted to hand-roll a custom SQL migration runner and a bespoke config loader for a client's payment app. I told it to use off-the-shelf libraries for both (`node-pg-migrate` for migrations and `envalid` for config validation).

I almost always choose to go with existing libraries, because it's less code to maintain and less surface area for bugs, especially when the libraries are well-used and thoroughly tested as was the case here.  Moreover, the app was touching payments, so it was critical that the code was correct.

That being said, I don't always pick the library. When I built my personal blog, I wrote my own static site generator instead of using someone else's. Mostly, because I wanted fine-grained control. Also since it was a personal project the stakes were much lower. It also turned out to be a great learning experience!
```
