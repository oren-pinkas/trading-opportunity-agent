#!/usr/bin/env bash
# Run one pipeline stage by invoking its Claude Code skill, headless.
# Usage: bin/run-stage.sh <skill-name>   e.g. bin/run-stage.sh simulate-plans
set -euo pipefail

STAGE="${1:?usage: run-stage.sh <skill-name>}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Load secrets (TWELVEDATA_API_KEY) if present; not required for stub runs.
if [ -f .env ]; then
  set -a; source .env; set +a
fi

# Invoke Claude Code headless and ask it to run the stage's skill.
# (Confirm the exact flags against your local `claude` CLI before activating.)
exec claude -p "Use the ${STAGE} skill. Today is $(date -u +%Y-%m-%dT%H:%MZ)."
