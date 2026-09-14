## Ghost

Source: [[Ghost]]

> What's one thing you'd improve about Ghost's developer experience, and why? *

```
Right now the install-from-source flow is decent, but it still relies on devs having the right Node/Yarn/Docker versions and a working local setup. Ghost already uses Docker for the backend. I think we could make this process a lot more deterministic by using Docker for the frontend as well. Then we could do things like...

- Pin Yarn version,
- Make `postCreateCommand` run `yarn setup`
- Provide tasks like:
  - "Start Ghost", which runs `yarn dev`
  - "Start Ghost Analytics", which runs `yar dev:analytics`
  - "Reset Data", which runs `yarn reset:data`
```
