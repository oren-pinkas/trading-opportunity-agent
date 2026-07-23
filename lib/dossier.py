"""Dossier frontmatter validation and I/O."""
import yaml

STATUSES = ["scouted", "researched", "scheduled", "simulated", "analyzed"]
EVENT_TYPES = {"geopolitical", "economic", "earnings", "product", "macro", "regulatory", "ipo"}

# Required top-level keys introduced at each status (cumulative).
_REQUIRED_AT = {
    "scouted": ["id", "title", "status", "created", "event", "tickers", "sources"],
    "researched": ["hypothesis", "plan", "research"],
    "scheduled": [],
    "simulated": ["simulation"],
    "analyzed": ["postmortem"],
}


def _required_keys(status: str) -> list[str]:
    keys: list[str] = []
    for s in STATUSES:
        keys += _REQUIRED_AT[s]
        if s == status:
            break
    return keys


def validate_frontmatter(fm: dict) -> list[str]:
    errors: list[str] = []
    status = fm.get("status")
    if status not in STATUSES:
        errors.append(f"status: must be one of {STATUSES}, got {status!r}")
        return errors  # can't check requirements without a valid status
    for key in _required_keys(status):
        if key not in fm or fm[key] in (None, "", [], {}):
            errors.append(f"{key}: required at status '{status}' but missing/empty")
    ev = fm.get("event")
    if isinstance(ev, dict) and ev.get("type") not in EVENT_TYPES:
        errors.append(f"event.type: must be one of {sorted(EVENT_TYPES)}")
    return errors


def load(path: str) -> tuple[dict, str]:
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        raise ValueError(f"{path}: missing frontmatter fence")
    lines = text.split("\n")
    if lines[0] != "---":
        raise ValueError(f"{path}: missing frontmatter fence")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i] == "---")
    except StopIteration:
        raise ValueError(f"{path}: missing closing frontmatter fence")
    fm_block = "\n".join(lines[1:end])
    body = "\n".join(lines[end + 1:])
    return yaml.safe_load(fm_block) or {}, body.lstrip("\n")


def save(path: str, fm: dict, body: str) -> None:
    fm_block = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"---\n{fm_block}---\n\n{body}")


def append_revision(path: str, fm_updates: dict, note: str, ts: str) -> None:
    fm, body = load(path)
    fm.update(fm_updates)
    body = body.rstrip() + f"\n\n---\n### Revision {ts}\n{note}\n"
    save(path, fm, body)
