---
id: 2026-07-13-claritev-doj-probe-closed
title: Claritev DOJ antitrust grand jury probe closed with no charges
status: researched
created: '2026-07-13T18:24:37Z'
event:
  type: regulatory
  summary: DOJ Antitrust Division told Claritev on June 17 it is closing the grand
    jury proceeding and the company faces no criminal investigation, removing a legal
    overhang.
  impact_window: '2026-08-15'
tickers:
- CTEV
sources:
- title: Claritev Corp - Form 8-K
  url: https://www.sec.gov/Archives/edgar/data/0001793229/000179322926000056/ctev-20260622.htm
  accessed_at: '2026-07-13T18:24:37Z'
hypothesis:
  statement: The DOJ grand-jury closure for CTEV (disclosed via the ~2026-06-22 8-K)
    is a binary legal-overhang-removal catalyst that was fully public and
    machine-scrapable ~18 trading sessions before the debate date. This event class
    historically produces a +8-12% one-day pop with a 1-3 session half-life and is
    fully priced within days. At T+18 sessions, EV_gross (~+0.34%) does not survive
    round-trip costs/slippage (~0.30-0.60%, skewed high for this illiquid name);
    EV_net is negative (~-0.11%). The stated 2026-08-15 exit is a non-trading
    Saturday with no forward catalyst in the window, and "no criminal charges" does
    not address separable civil/ERISA/FTC/state-AG and leveraged-balance-sheet risk.
    No trade.
  direction: no_trade
  confidence: 82
plan:
  ticker: CTEV
  action: pass
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
research:
  strategy: three-round-panel
  personas:
  - bull
  - bear
  - quant
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  dissent: The EV/decay kill assumes an initial pop happened to decay from, but no
    live price data was available (simulated future date) to confirm the market
    actually reacted at disclosure. If CTEV never priced the news due to thin
    coverage, the "priced-in" prior is inapplicable and genuine underreaction edge
    could exist. Post-mortem should check actual CTEV price action 2026-06-22
    through 2026-07-13.
  last_updated: '2026-07-13T18:38:00Z'
---

## Scouted 2026-07-13T18:24:37Z

## Researched 2026-07-13T18:38:00Z

Three-round panel debate (bull/bear/quant, synthesized by opus). All three personas
converged on PASS by Round 2 via two largely independent objections: negative EV
after decay+costs, and uncompensated structural/litigation risk. Verdict: no_trade,
confidence 82. Full transcript in `transcript.md`. Central dissent: the "already
priced in" assumption was never checked against real price data (unavailable for
this simulated future date) — flagged for post-mortem follow-up.
