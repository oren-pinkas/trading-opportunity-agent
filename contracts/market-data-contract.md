# Market-data contract

`get_price(ticker, timestamp, provider) -> {price, source, fetched_at, timestamp}`

- `ticker`: e.g. "NVDA". `timestamp`: ISO-8601 UTC of a minute (seconds ignored).
- Returns the price for that minute bar. `source` cites where the number came from
  (a stub label or a provider URL). `fetched_at` is when it was retrieved (UTC) or
  None for the stub.
- Providers: `stub` (deterministic, offline) and `twelvedata` (live, free tier).
- All providers honor the same return shape so the provider is a one-arg swap.
- Minute resolution only; seconds in `timestamp` are truncated.
