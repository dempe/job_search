---
type: job
applied: 2026-10-22
job_type: fulltime
channel: form
contact:
status: awaiting-reply
interviews:
source: indeed
listing: "https://careers-carecentrix.icims.com/jobs/16881/job?utm_source=indeed_integration&iis=Job+Board&iisn=Indeed&indeed-apply-token=73a2d2b2a8d6d5c0a62696875eaebd669103652d3f0c2cd5445d3e66b1592b0f&mobile=false&width=1370&height=500&bga=true&needsRedirect=false&jan1offset=-360&jun1offset=-300"
company: CareCentrix
position: Platform Software Engineer
contract: false
remote: true
compensation: $90,000 - $100,000 a year
title: CareCentrix
date_created: "2026-10-22 14:52"
date_modified: "2026-10-22 14:52"
---

## Application

> Please briefly describe your hands-on experience with CI/CD pipelines, including the tools used (e.g., GitHub Actions, Jenkins, Azure DevOps, GitLab CI) and your role in building, maintaining, or supporting those pipelines.

```
I've used GitHub Actions, GitLab CICD, and Jenkins.

GitHub Actions: I built and maintain the CI/CD for my own company's app. It's a serverless AWS backend (Lambda, API Gateway, DynamoDB) is defined in SAM/CloudFormation, and the pipeline deploys it automatically with CloudFormation-backed rollbacks. I also set up CI/CD in GitHub Actions for my personal site, which builds and deploys to S3/CloudFront on every push to main, plus a scheduled weekly job that builds a stats page from the CloudFront logs.

Jenkins: At DataRank, our crawler deploys ran through Jenkins, so adding a new data source went from manual server edits to a simple redeploy. I also turned Jenkins into a live status page for the crawler fleet so the support team could see which scrapers had broken without going through an engineer.

At Octimine, I designed a peer-reviewed CI/CD pipeline for Elasticsearch schema updates, made the unit tests for every analytic in our Kafka Streams pipeline run as regression tests in CI, and moved recurring manual tasks into CI/CD.
```
