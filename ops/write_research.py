#!/usr/bin/env python3
"""Apply research-debate results to dossiers.

Reads a manifest JSON produced by the research-debate orchestrator and, for each
opportunity, writes hypothesis/plan/research frontmatter, appends a body note, sets
status (no-trade -> researched, otherwise -> scheduled), saves, and validates.

Usage: python ops/write_research.py <manifest.json>
Manifest shape:
{
  "last_updated": "2026-07-07T12:30:00Z",
  "models": {"bull":"sonnet","bear":"sonnet","quant":"opus","synthesizer":"opus"},
  "personas": ["bull","bear","quant"],
  "strategy": "three-round-panel",
  "opportunities": [
    {"id": "...", "hypothesis": {...}, "plan": {...}, "dissent": "...", "body_note": "..."}
  ]
}
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from lib import dossier  # noqa: E402


def main(manifest_path: str) -> int:
    m = json.loads(Path(manifest_path).read_text())
    ts = m["last_updated"]
    rc = 0
    for opp in m["opportunities"]:
        oid = opp["id"]
        path = ROOT / "opportunities" / oid / "dossier.md"
        fm, body = dossier.load(str(path))
        plan = opp["plan"]
        status = "researched" if plan.get("action") == "no-trade" else "scheduled"
        fm["status"] = status
        fm["hypothesis"] = opp["hypothesis"]
        fm["plan"] = plan
        fm["research"] = {
            "strategy": m["strategy"],
            "personas": m["personas"],
            "models": m["models"],
            "dissent": opp["dissent"],
            "last_updated": ts,
        }
        verdict = plan.get("action", "?").upper()
        note = f"## Researched {ts} — {verdict}\n\n{opp['body_note'].strip()}\n"
        body = body.rstrip() + "\n\n" + note
        dossier.save(str(path), fm, body)
        errors = dossier.validate_frontmatter(fm)
        print(json.dumps({"id": oid, "status": status, "action": plan.get("action"),
                          "valid": not errors, "errors": errors}))
        if errors:
            rc = 1
    return rc


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
