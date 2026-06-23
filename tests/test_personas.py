import re
from pathlib import Path

import yaml

PERSONAS = ["bull", "bear", "quant", "investigator", "critic"]


def test_personas_exist_with_frontmatter():
    for name in PERSONAS:
        p = Path(f"personas/{name}.md")
        assert p.is_file(), f"missing {p}"
        _, fm_block, body = p.read_text().split("---", 2)
        fm = yaml.safe_load(fm_block)
        assert fm.get("name") == name and fm.get("role")
        assert len(body.strip()) > 50


def test_personas_are_model_agnostic():
    for name in PERSONAS:
        text = Path(f"personas/{name}.md").read_text().lower()
        assert not re.search(r"\b(haiku|sonnet|opus)\b", text), f"{name} names a model"
