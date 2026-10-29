## People Data Labs

[[People Data Labs]]

> Describe how you've structured unstructured or semi-structured data into a useful schema.

```
At DataRank, everything we collected -- crawled forum posts, review sites, and social API data -- had to land in one canonical model, so analysts worked with the same shape no matter where the data came from.

We split it into two entities: authors and comments. The author had demographic fields where we could get them -- name, gender, age, location, etc. The comment had the text, posting date, a link back to the source, and the author reference. Every crawler and API handler parsed its source and filled in that model, and it was persisted to HBase.

The decisions that made it useful: every record kept the source and the source's own ID, so we could deduplicate and trace anything back to where it came from. Dates and locations were normalized to one format. Fields that many sources didn't have were optional instead of filled with guesses.  We also stored all the raw data for both author and comment in the model as well, so if a parsing error was ever discovered down the line, it did not require a re-crawl, we could just fix the parser and re-run on the already collected data.
```
