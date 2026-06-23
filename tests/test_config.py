import json
from pathlib import Path


def test_research_config_shape():
    c = json.loads(Path("config/research.json").read_text())
    assert c["strategy"] == "three-round-panel"
    assert set(c["personas"]) >= {"bull", "bear", "quant"}
    assert {"bull", "bear", "quant", "synthesizer"} <= set(c["models"])


def test_postmortem_config_shape():
    c = json.loads(Path("config/postmortem.json").read_text())
    assert c["strategy"] == "investigator-critic"
    assert {"investigator", "critic"} <= set(c["roles"])


def test_scout_config_shape():
    c = json.loads(Path("config/scout.json").read_text())
    assert c["dedupe_window_days"] == 14
    assert "source_hints" in c
