"""Render the INDEX.md dashboard from dossier summaries."""

_HEADER = (
    "# Opportunity Index\n\n"
    "> ⚠️ PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.\n\n"
    "| ID | Title | Status | Outcome |\n"
    "|----|-------|--------|---------|\n"
)


def render_index(rows: list[dict]) -> str:
    body = ""
    for r in sorted(rows, key=lambda r: r["id"]):
        outcome = r.get("outcome") or "—"
        body += f"| {r['id']} | {r['title']} | {r['status']} | {outcome} |\n"
    return _HEADER + body
