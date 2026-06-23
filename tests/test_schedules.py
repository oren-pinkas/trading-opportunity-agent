import json
import os
import subprocess
from pathlib import Path

SCHED = json.loads(Path("config/schedules.json").read_text()) if Path("config/schedules.json").exists() else {}


def test_timezone_is_new_york():
    assert SCHED.get("timezone") == "America/New_York"


def test_six_jobs_match_spec():
    jobs = {(j["skill"], j["cron"]) for j in SCHED.get("jobs", [])}
    expected = {
        ("scout-news", "0 7 * * *"),
        ("scout-news", "30 12 * * *"),
        ("scout-news", "0 17 * * *"),
        ("research-debate", "0 8 * * *"),
        ("simulate-plans", "30 18 * * *"),
        ("post-mortem", "30 19 * * *"),
    }
    assert jobs == expected


def test_job_names_unique():
    names = [j["name"] for j in SCHED.get("jobs", [])]
    assert len(names) == len(set(names)) == 6


def test_run_stage_script_exists_and_executable():
    p = "bin/run-stage.sh"
    assert os.path.isfile(p)
    assert os.access(p, os.X_OK), "run-stage.sh must be executable"


def test_run_stage_loads_env_and_takes_stage_arg():
    text = open("bin/run-stage.sh").read()
    assert ".env" in text
    assert "$1" in text or "${1" in text
    assert "claude" in text


def test_run_stage_is_valid_bash():
    r = subprocess.run(["bash", "-n", "bin/run-stage.sh"], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


def test_runbook_covers_stages_env_and_disclaimer():
    text = open("SCHEDULES.md").read()
    for token in ["scout-news", "research-debate", "simulate-plans", "post-mortem",
                  "America/New_York", "TWELVEDATA_API_KEY", "NOT FINANCIAL ADVICE"]:
        assert token in text, f"runbook missing {token}"
