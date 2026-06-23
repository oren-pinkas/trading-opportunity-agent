"""`toa` CLI — the deterministic seam that agent skills shell out to."""
import argparse
import json
import sys

from lib import dossier, ledger, marketdata, pnl


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
    return 2


if __name__ == "__main__":
    sys.exit(main())
