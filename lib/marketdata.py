"""Price access behind a single provider-swappable contract."""
import hashlib
import json
import os
import time
import urllib.parse
import urllib.request

_CACHE: dict[tuple[str, str], dict] = {}
_BASE = "https://api.twelvedata.com/time_series"


def _truncate_to_minute(timestamp: str) -> str:
    # "2026-07-10T13:00:45Z" -> "2026-07-10T13:00Z"
    base = timestamp.replace("Z", "")
    return base[:16] + "Z"


def _stub_price(ticker: str, minute: str) -> float:
    h = hashlib.sha256(f"{ticker}|{minute}".encode()).hexdigest()
    return round(10.0 + (int(h[:8], 16) % 49000) / 100.0, 2)  # 10.00–500.00


def parse_twelvedata(payload: dict, timestamp: str) -> float:
    if payload.get("status") != "ok":
        raise ValueError(f"twelvedata error: {payload.get('message', payload.get('status'))}")
    minute = _truncate_to_minute(timestamp)          # "2026-07-10T13:00Z"
    want = minute[:-1].replace("T", " ") + ":00"     # "2026-07-10 13:00:00"
    for bar in payload.get("values", []):
        if bar["datetime"] == want:
            return float(bar["open"])
    raise KeyError(f"no 1min bar for {want}")


def _fetch_twelvedata(ticker: str, date: str, api_key: str) -> dict:
    params = urllib.parse.urlencode({
        "symbol": ticker, "interval": "1min", "date": date,
        "timezone": "UTC", "outputsize": 5000, "apikey": api_key,
    })
    time.sleep(8)  # throttle: free tier is 8 req/min
    with urllib.request.urlopen(f"{_BASE}?{params}", timeout=30) as resp:
        return json.loads(resp.read().decode())


def get_price(ticker: str, timestamp: str, provider: str = "stub") -> dict:
    minute = _truncate_to_minute(timestamp)
    if provider == "stub":
        return {"price": _stub_price(ticker, minute),
                "source": "stub:deterministic", "fetched_at": None, "timestamp": minute}
    if provider == "twelvedata":
        key = os.environ.get("TWELVEDATA_API_KEY")
        if not key:
            raise RuntimeError("TWELVEDATA_API_KEY not set")
        date = minute[:10]
        cache_key = (ticker, date)
        if cache_key not in _CACHE:
            _CACHE[cache_key] = _fetch_twelvedata(ticker, date, key)
        price = parse_twelvedata(_CACHE[cache_key], timestamp)
        url = f"{_BASE}?symbol={ticker}&interval=1min&date={date}&timezone=UTC"
        return {"price": price, "source": url,
                "fetched_at": minute, "timestamp": minute}
    raise ValueError(f"unknown provider: {provider!r}")
