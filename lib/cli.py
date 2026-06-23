"""`toa` CLI — the deterministic seam that agent skills shell out to."""
import argparse
import json
import sys

from lib import dossier, marketdata, pnl


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
    return 2


if __name__ == "__main__":
    sys.exit(main())
