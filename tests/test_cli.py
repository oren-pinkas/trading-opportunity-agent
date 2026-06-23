import json
import subprocess
import sys


def _run(*args):
    return subprocess.run([sys.executable, "-m", "lib.cli", *args],
                          capture_output=True, text=True)


def test_cli_price_stub():
    r = _run("price", "NVDA", "2026-07-10T13:00:00Z")
    assert r.returncode == 0
    assert json.loads(r.stdout)["source"] == "stub:deterministic"


def test_cli_pnl():
    r = _run("pnl", "buy", "100", "110")
    assert json.loads(r.stdout)["outcome"] == "win"
