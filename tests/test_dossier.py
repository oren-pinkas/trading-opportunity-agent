from lib.dossier import validate_frontmatter, load, save, append_revision


def _scouted():
    return {
        "id": "2026-06-22-oil", "title": "t", "status": "scouted",
        "created": "2026-06-22T09:00:00Z",
        "event": {"type": "geopolitical", "summary": "s", "impact_window": "2026-07-10"},
        "tickers": ["USO"], "sources": [{"title": "a", "url": "u", "accessed_at": "x"}],
    }


def test_valid_scouted_has_no_errors():
    assert validate_frontmatter(_scouted()) == []


def test_missing_field_is_reported():
    fm = _scouted(); del fm["tickers"]
    errs = validate_frontmatter(fm)
    assert any("tickers" in e for e in errs)


def test_bad_status_enum_is_reported():
    fm = _scouted(); fm["status"] = "bogus"
    assert any("status" in e for e in validate_frontmatter(fm))


def test_researched_requires_plan():
    fm = _scouted(); fm["status"] = "researched"
    assert any("plan" in e for e in validate_frontmatter(fm))


def test_save_then_load_roundtrips(tmp_path):
    p = tmp_path / "dossier.md"
    fm = _scouted(); body = "## Scouted\nfound it\n"
    save(str(p), fm, body)
    fm2, body2 = load(str(p))
    assert fm2["id"] == fm["id"]
    assert "found it" in body2


def test_append_revision_keeps_history_and_updates_fm(tmp_path):
    p = tmp_path / "dossier.md"
    save(str(p), _scouted(), "## Scouted\nfirst\n")
    append_revision(str(p), {"status": "researched"}, "added hypothesis",
                    ts="2026-06-23T08:00:00Z")
    fm, body = load(str(p))
    assert fm["status"] == "researched"
    assert "first" in body
    assert "2026-06-23T08:00:00Z" in body
    assert "added hypothesis" in body
