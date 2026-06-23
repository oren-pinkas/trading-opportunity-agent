"""`toa` CLI — the deterministic seam that agent skills shell out to."""
import argparse
import json
import sys

from lib import dedup, dossier, ledger, marketdata, pnl
from lib import lessons as lessons_mod


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="toa")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("price")
    sp.add_argument("ticker"); sp.add_argument("timestamp")
    sp.add_argument("--provider", default="stub")

    pl = sub.add_parser("pnl")
    pl.add_argument("action"); pl.add_argument("entry", type=float)
    pl.add_argument("exit", type=float)

    va = sub.add_parser("validate")
    va.add_argument("path")

    ls = sub.add_parser("ls")
    ls.add_argument("--status", required=True); ls.add_argument("--base", default="opportunities")

    si = sub.add_parser("simulatable")
    si.add_argument("--now", required=True); si.add_argument("--base", default="opportunities")

    sm = sub.add_parser("simulate")
    sm.add_argument("path"); sm.add_argument("--now", required=True)
    sm.add_argument("--provider", default="stub")

    ri = sub.add_parser("reindex")
    ri.add_argument("--base", default="opportunities"); ri.add_argument("--out", default="INDEX.md")

    pt = sub.add_parser("postmortem-targets")
    pt.add_argument("--base", default="opportunities")

    dc = sub.add_parser("dedup-check")
    dc.add_argument("--tickers", required=True); dc.add_argument("--today", required=True)
    dc.add_argument("--base", default="opportunities"); dc.add_argument("--window", type=int, default=14)

    lr = sub.add_parser("lessons-relevant")
    lr.add_argument("--type", required=True, dest="etype"); lr.add_argument("--tickers", default="")
    lr.add_argument("--store", default="lessons.yaml")

    rp = sub.add_parser("record-postmortem")
    rp.add_argument("path"); rp.add_argument("--root-cause", required=True, dest="root_cause")
    rp.add_argument("--lesson", action="append", default=[], dest="lessons")
    rp.add_argument("--now", required=True); rp.add_argument("--store", default="lessons.yaml")

    rl = sub.add_parser("render-lessons")
    rl.add_argument("--store", default="lessons.yaml"); rl.add_argument("--out", default="LESSONS.md")

    no = sub.add_parser("new-opportunity")
    no.add_argument("--id", required=True, dest="oid"); no.add_argument("--title", required=True)
    no.add_argument("--type", required=True, dest="etype"); no.add_argument("--summary", required=True)
    no.add_argument("--impact-window", required=True, dest="impact_window")
    no.add_argument("--tickers", required=True); no.add_argument("--source-title", required=True, dest="stitle")
    no.add_argument("--source-url", required=True, dest="surl"); no.add_argument("--now", required=True)
    no.add_argument("--base", default="opportunities")

    args = p.parse_args(argv)
    if args.cmd == "price":
        print(json.dumps(marketdata.get_price(args.ticker, args.timestamp, args.provider)))
        return 0
    if args.cmd == "pnl":
        print(json.dumps(pnl.compute_pnl(args.action, args.entry, args.exit)))
        return 0
    if args.cmd == "validate":
        fm, _ = dossier.load(args.path)
        errs = dossier.validate_frontmatter(fm)
        print(json.dumps({"valid": not errs, "errors": errs}))
        return 1 if errs else 0
    if args.cmd == "ls":
        ids = [i["id"] for i in ledger.list_by_status(args.status, base=args.base)]
        print(json.dumps({"ids": ids}))
        return 0
    if args.cmd == "simulatable":
        ids = [i["id"] for i in ledger.find_simulatable(args.now, base=args.base)]
        print(json.dumps({"ids": ids}))
        return 0
    if args.cmd == "simulate":
        print(json.dumps(ledger.simulate_dossier(args.path, args.now, args.provider)))
        return 0
    if args.cmd == "reindex":
        ledger.regenerate_index(base=args.base, out_path=args.out)
        print(json.dumps({"written": args.out}))
        return 0
    if args.cmd == "postmortem-targets":
        print(json.dumps({"ids": [i["id"] for i in ledger.find_postmortem_targets(base=args.base)]}))
        return 0
    if args.cmd == "dedup-check":
        cand = {"tickers": [t for t in args.tickers.split(",") if t]}
        dup = dedup.is_duplicate(cand, ledger.existing_for_dedup(base=args.base),
                                 today=args.today, window_days=args.window)
        print(json.dumps({"duplicate": dup}))
        return 0
    if args.cmd == "lessons-relevant":
        rows = lessons_mod.load_lessons(args.store)
        tickers = [t for t in args.tickers.split(",") if t]
        print(json.dumps({"lessons": lessons_mod.filter_relevant(rows, args.etype, tickers)}))
        return 0
    if args.cmd == "record-postmortem":
        print(json.dumps(ledger.record_postmortem(args.path, args.root_cause, args.lessons,
                                                  args.now, lessons_path=args.store)))
        return 0
    if args.cmd == "render-lessons":
        text = lessons_mod.render_lessons_md(lessons_mod.load_lessons(args.store))
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(json.dumps({"written": args.out}))
        return 0
    if args.cmd == "new-opportunity":
        event = {"type": args.etype, "summary": args.summary, "impact_window": args.impact_window}
        sources = [{"title": args.stitle, "url": args.surl, "accessed_at": args.now}]
        path = ledger.create_opportunity(args.oid, args.title, event,
                                         args.tickers.split(","), sources, args.now, base=args.base)
        fm, _ = dossier.load(path)
        print(json.dumps({"path": path, "status": fm["status"]}))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
