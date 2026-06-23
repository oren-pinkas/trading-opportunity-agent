"""Price access behind a single provider-swappable contract."""
import hashlib
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

_CACHE: dict[tuple[str, str], dict] = {}
_BASE = "https://api.twelvedata.com/time_series"


class MarketDataUnavailable(Exception):
    """No price data for the requested ticker/date (holiday, weekend, or gap)."""


def _truncate_to_minute(timestamp) -> str:
    # Accept a str ("2026-07-10T13:00:45Z") or a datetime (PyYAML parses unquoted
    # ISO timestamps into datetime objects). Always return "YYYY-MM-DDTHH:MMZ".
    if isinstance(timestamp, datetime):
        dt = timestamp if timestamp.tzinfo else timestamp.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
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
    try:
        with urllib.request.urlopen(f"{_BASE}?{params}", timeout=30) as resp:
            payload = json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        raise MarketDataUnavailable(f"{ticker} {date}: HTTP {exc.code}") from exc
    if payload.get("status") != "ok":
        raise MarketDataUnavailable(f"{ticker} {date}: {payload.get('message')}")
    return payload


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
