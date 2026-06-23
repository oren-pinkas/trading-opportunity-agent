"""Select post-mortem lessons relevant to an opportunity (learning loop)."""
import os

import yaml


def load_lessons(path: str) -> list[dict]:
    if not os.path.isfile(path):
        return []
    return yaml.safe_load(open(path, encoding="utf-8")) or []


def append_lesson(path: str, lesson: dict) -> None:
    rows = load_lessons(path)
    rows.append(lesson)
    with open(path, "w", encoding="utf-8") as fh:
        yaml.safe_dump(rows, fh, sort_keys=False, allow_unicode=True)


def render_lessons_md(lessons: list[dict]) -> str:
    head = "# Lessons\n\n> ⚠️ PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.\n\n"
    body = ""
    for l in lessons:
        tickers = ",".join(l.get("tickers", []))
        body += f"- [{l.get('event_type', '')} | {tickers}] {l['text']}\n"
    return head + body


def filter_relevant(lessons: list[dict], event_type: str, tickers: list[str]) -> list[dict]:
    want = set(tickers)
    out, seen = [], set()
    for l in lessons:
        hit = l.get("event_type") == event_type or (set(l.get("tickers", [])) & want)
        if hit and l["text"] not in seen:
            out.append(l)
            seen.add(l["text"])
    return out
