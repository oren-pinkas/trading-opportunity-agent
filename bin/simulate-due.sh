#!/usr/bin/env bash
# Deterministically simulate every plan whose exit time has passed.
# Cron-safe: pure `toa`, no LLM, no permission prompts. Captures real prices
# while the provider still has the intraday bars (the retention invariant).
set -euo pipefail

# Cron has a minimal PATH; make `toa`/`python3`/`git` resolvable regardless.
export PATH="/Users/oren/.asdf/shims:/Users/oren/.local/bin:/opt/homebrew/bin:/usr/bin:/bin"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"
[ -f .env ] && { set -a; source .env; set +a; }

PROVIDER="${TOA_PROVIDER:-twelvedata}"
[ -n "${TWELVEDATA_API_KEY:-}" ] || PROVIDER=stub   # fall back if no key

NOW="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
mkdir -p "$REPO_ROOT/logs"
LOG="$REPO_ROOT/logs/simulate-due.log"

{
  echo "=== simulate-due $NOW (provider=$PROVIDER) ==="
  IDS="$(toa simulatable --now "$NOW" | python3 -c "import sys,json; print('\n'.join(json.load(sys.stdin)['ids']))")"
  if [ -z "$IDS" ]; then
    echo "nothing due"
  else
    while IFS= read -r id; do
      [ -z "$id" ] && continue
      echo "-- simulating $id"
      toa simulate "opportunities/$id/dossier.md" --now "$NOW" --provider "$PROVIDER" \
        || echo "FAILED: $id"
    done <<< "$IDS"
    toa reindex
    echo "reindexed"
  fi
  echo "=== done $NOW ==="
} >> "$LOG" 2>&1
