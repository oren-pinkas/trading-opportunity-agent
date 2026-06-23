from pathlib import Path

import yaml

SKILLS = ["market-data", "simulate-plans"]


def _frontmatter(path):
    text = path.read_text()
    assert text.startswith("---"), f"{path} missing frontmatter"
    _, fm_block, _ = text.split("---", 2)
    return yaml.safe_load(fm_block)


def test_skill_files_exist_with_frontmatter():
    for name in SKILLS:
        p = Path(f".claude/skills/{name}/SKILL.md")
        assert p.is_file(), f"missing {p}"
        fm = _frontmatter(p)
        assert fm.get("name") == name
        assert fm.get("description")


def test_simulate_skill_references_toa():
    text = Path(".claude/skills/simulate-plans/SKILL.md").read_text()
    assert "toa simulatable" in text and "toa simulate" in text and "toa reindex" in text
