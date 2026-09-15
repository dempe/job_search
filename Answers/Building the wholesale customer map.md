## Rivora

[[Rivora]]

> Describe a time you had to work across two systems where one side didn't fully control the other, an API you didn't own, a data format shared with another service, anything like that. What broke or almost broke?

```
I built a Node.js/React app for a B2B coffee distributor to show the sales team lapsed or about-to-lapse customers via an Excel sheet and an interactive map.

The catch was Shopify's Admin API, which we didn't control. It only returns the last 60 days of orders. I.e., a customer who lapsed 3 months ago produces no  rows in a recent-orders query, so a live query would have silently dropped exactly the accounts the tool existed for.

To get around this, I designed a Postgres projection of customer and order data, refreshed in the background. Each refresh merges recent customers and orders with the stored projection (latest order date wins) and upserts the result. Customer provided historical seed data for the initial run, and the app runs off the projection instead of the API, keeping lapsed accounts visible beyond the 60 day window.
```
