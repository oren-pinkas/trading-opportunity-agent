#!/usr/bin/env bash
# Run one LLM pipeline stage by invoking its Claude Code skill, headless & unattended.
# Usage: bin/run-stage.sh <skill-name>   e.g. bin/run-stage.sh research-debate
set -euo pipefail

# launchd/cron give a minimal PATH; make claude/toa/python3/git resolvable.
export PATH="/Users/oren/.asdf/shims:/Users/oren/.local/bin:/opt/homebrew/bin:/usr/bin:/bin"

STAGE="${1:?usage: run-stage.sh <skill-name>}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Load secrets (TWELVEDATA_API_KEY) if present; not required for stub runs.
if [ -f .env ]; then
  set -a; source .env; set +a
fi

mkdir -p "$REPO_ROOT/logs"
LOG="$REPO_ROOT/logs/${STAGE}.log"
NOW="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# Headless, non-interactive. Tool permissions come from the repo's scoped allowlist
# in .claude/settings.json — NOT a global permission bypass.
{
  echo "=== run-stage ${STAGE} ${NOW} ==="
  claude -p "Use the ${STAGE} skill. The current UTC time is ${NOW}. Today's date is ${NOW%%T*}."
  echo "=== done ${STAGE} (exit $?) ${NOW} ==="
} >> "$LOG" 2>&1
