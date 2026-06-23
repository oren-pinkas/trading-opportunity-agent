---
name: market-data
description: Fetch a citable historical price for a ticker at a UTC minute. Use whenever a skill needs a real price; never estimate prices yourself.
---

# market-data

Prices come from tested code, never from your own estimate. To get the price of a
ticker at a specific UTC minute, run:

```bash
toa price <TICKER> <ISO-8601-UTC> [--provider stub|twelvedata]
```

Example:

```bash
toa price USO 2026-07-10T13:00:00Z --provider twelvedata
# -> {"price": 78.62, "source": "https://api.twelvedata.com/...", "fetched_at": "...", "timestamp": "..."}
```

Use `--provider stub` for offline/dry runs (deterministic fake prices). Use
`--provider twelvedata` for real data (requires `TWELVEDATA_API_KEY` in the
environment). Always record the returned `source` when you cite a price.

If the provider has no data for the requested date (US market holiday, weekend, or a
gap), the command exits non-zero with a `MarketDataUnavailable` error — that minute
simply has no trade data. Treat it as "not available", not as a price of zero.
