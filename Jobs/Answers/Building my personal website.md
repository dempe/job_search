## Close (0)

Source: [[Jobs/Job Applications/Close (0)]]

> Tell Us about Something You Built that You're Proud Of. (We like seeing URLs if Available, but not as a Replacement for a description)

```
I've been working on my personal website (chrisdempewolf. com) over the past few months. I'm trying to set up a blog to practice my writing and show what I'm doing. It's a static website written in PHP using Laravel. I run the Laravel server and use wget to pull down a static version. It's not the prettiest build setup, but it's worth it to use PHP/Laravel for my site. Say what you will about PHP, but it's a fantastic language for HTML templating. And since I'm not using someone else's static site generator, I know how everything works and control everything. Plus, I have a nice SQLite backend that makes working with various relationships (e.g., post<->tags, a many: many relationship) muuuch simpler than without a relational DB. I'm also a huge fan of the Laravel ORM, Eloquent.
```

## Close (1)

Source: [[Jobs/Job Applications/Close (1)]]

> Tell us about something you built that you're proud of. (We like seeing URLs if available, but not as a replacement for a description)

```
I built a static blog (chrisdempwolf.com). I wanted to build my own site for 1) the challenge 2) to have more control. In building my blog myself I've learned a lot more than had I used a generator.

I host my site on S3/Cloudfront. The site, itself, runs on Laravel, but I pull down a static copy using wget. I set up CICD in Github Actions, so my site builds automatically when I push to main. I also have a job that runs every Wednesday to build a stats page by feeding my CloudFront logs to GoAccess (a log analyzer/visualizer).

Here are some of the problems I faced:

- How to handle the post:tag relationsip, a many:many relationship. I use an Sqlite database that builds in 1.4 seconds to resolve tag->post and post->tag queries. This is far easier than an in-memory solution.
- How to handle dynamic content in Markdown files. I use Blade components to display chunks of parameterized HTML like dialogue boxes and images and blockquotes with captions.
- Building and deployment. Making a build script wasn't too bad. Getting it to run on Github was a bit trickier. I now have a working build script on Github that creates a static "snapshot", loads those files to S3, and invalidates the relevant files in Cloudfront.

It was quite an adventure, but it was worth it. Aside from the learnings, I have something that really feels like my own. Now, I just need better content! 😂

More details can be found here: https://chrisdempewolf.com/posts/building-a-static-site-from-scratch.html

```
