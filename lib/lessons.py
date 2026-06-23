"""Select post-mortem lessons relevant to an opportunity (learning loop)."""


def filter_relevant(lessons: list[dict], event_type: str, tickers: list[str]) -> list[dict]:
    want = set(tickers)
    out, seen = [], set()
    for l in lessons:
        hit = l.get("event_type") == event_type or (set(l.get("tickers", [])) & want)
        if hit and l["text"] not in seen:
            out.append(l)
            seen.add(l["text"])
    return out
