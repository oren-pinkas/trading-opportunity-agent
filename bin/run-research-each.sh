#!/usr/bin/env bash
# Run research-debate on EACH scouted opportunity in its OWN isolated claude session,
# so no hypothesis agent ever sees more than one data point (no cross-opportunity
# context pollution). Optional arg caps items per run to bound token spend.
# Usage: bin/run-research-each.sh [max_items]   (0/omitted = all scouted)
set -uo pipefail

# launchd/cron give a minimal PATH; make claude/python3/git resolvable.
export PATH="/Users/oren/.asdf/shims:/Users/oren/.local/bin:/opt/homebrew/bin:/usr/bin:/bin"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# `toa` on PATH collides with an unrelated asdf 'foreman' CLI; route to the project CLI.
mkdir -p "$REPO_ROOT/ops/shims"
printf '#!/usr/bin/env bash\ncd "%s" && exec python3 -m lib.cli "$@"\n' "$REPO_ROOT" > "$REPO_ROOT/ops/shims/toa"
chmod +x "$REPO_ROOT/ops/shims/toa"
export PATH="$REPO_ROOT/ops/shims:$PATH"

[ -f .env ] && { set -a; source .env; set +a; }
mkdir -p logs
LOG="$REPO_ROOT/logs/research-each.log"
MAX="${1:-0}"

IDS="$(toa ls --status scouted 2>/dev/null | python3 -c 'import sys,json; print("\n".join(json.load(sys.stdin).get("ids",[])))' 2>/dev/null)"
if [ -z "$IDS" ]; then
  echo "$(date -u +%FT%TZ) research-each: no scouted opportunities" >> "$LOG"
  exit 0
fi

n=0
while IFS= read -r id; do
  [ -z "$id" ] && continue
  n=$((n+1))
  if [ "$MAX" -gt 0 ] && [ "$n" -gt "$MAX" ]; then n=$((n-1)); break; fi
  NOW="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  {
    echo "=== research-each ${id} ${NOW} ==="
    claude -p "Use the research-debate skill for EXACTLY ONE opportunity: ${id}. Do NOT run any discovery step (skip 'toa ls --status scouted'); process ONLY '${id}'. Do not read, load, reference, or compare against any other opportunity's dossier — form the hypothesis for '${id}' on its own merits alone, so judgment is never polluted by other data points. The current UTC time is ${NOW}. Today's date is ${NOW%%T*}."
    echo "=== done ${id} (exit $?) ${NOW} ==="
  } >> "$LOG" 2>&1
done <<< "$IDS"

# Persist all new hypotheses once.
{
  echo "=== persist research-each (${n} items) $(date -u +%FT%TZ) ==="
  git add -A
  if git diff --cached --quiet; then
    echo "no changes to persist"
  else
    git -c user.name="trading-agent-bot" -c user.email="trading-agent-bot@users.noreply.github.com" \
        commit -m "feat: per-item research hypotheses ($(date -u +%Y-%m-%dT%H:%MZ))"
    git pull --rebase origin main && git push origin main || echo "push failed (offline?) — committed locally"
  fi
} >> "$LOG" 2>&1 || true

echo "$(date -u +%FT%TZ) research-each: processed ${n} opportunity(ies)" >> "$LOG"
