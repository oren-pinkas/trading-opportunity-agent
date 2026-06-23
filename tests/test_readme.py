from pathlib import Path


def test_readme_has_disclaimer():
    text = Path("README.md").read_text()
    assert "PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE." in text
