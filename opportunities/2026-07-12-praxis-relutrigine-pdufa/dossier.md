---
id: 2026-07-12-praxis-relutrigine-pdufa
title: Praxis relutrigine PDUFA extended to December
status: researched
created: '2026-07-12T17:02:21Z'
event:
  type: regulatory
  summary: FDA extended Praxis Precision Medicines' relutrigine NDA review by three
    months to a new PDUFA date of December 27, 2026, after accepting a major-amendment
    sensitivity analysis.
  impact_window: '2026-12-27'
tickers:
- PRAX
sources:
- title: Praxis Precision Medicines, Inc. - Form 8-K - FY2026
  url: https://www.sec.gov/Archives/edgar/data/0001689548/000168954826000069/prax-20260629.htm
  accessed_at: '2026-07-12T17:02:21Z'
hypothesis:
  statement: Two weeks post-8-K, PRAX has already repriced the relutrigine major-amendment
    PDUFA extension (~-15% cash-session move on 2026-06-29); no residual reaction-trade
    edge remains. The only live thesis is the December 27, 2026 PDUFA approval binary
    itself, but its expected value is small, rests on a disputed base-rate reference
    class (efficacy-sensitivity-analysis extension vs. CMC-driven comparables), and
    cannot be responsibly sized today given the system's unreliable price feed.
  direction: none
  confidence: 72
plan:
  ticker: PRAX
  action: no_action
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0.0
  conditional_plan: If a reconciled live price feed, a defensible base-rate backtest
    for efficacy-sensitivity-analysis PDUFA extensions specifically, and confirmation
    that no FDA advisory committee is scheduled all become available, revisit as a
    long-dated out-of-the-money call spread on PRAX expiring after 2026-12-28 (the
    PDUFA date of 2026-12-27 is a Sunday; 2026-12-25 is a market holiday), sized at
    low-single-digit percent of risk capital against a modeled ~+5.3% gross EV vs.
    a ~-50% CRL left tail. Entry would be taken on any valid trading session (e.g.
    2026-07-13, a Monday); resolution/exit at the first open session after the PDUFA
    date, 2026-12-28.
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
  last_updated: '2026-07-13T05:20:12Z'
  dissent: >-
    Bull and quant anchor December-PDUFA approval odds to a ~75-88% generic
    priority-review/no-adcom/no-CMC-flag base rate (quant's central estimate 79%
    after adjustment); bear argues this is the wrong reference class since this
    extension was driven by an efficacy-sensitivity-analysis on a trial (EMBOLD)
    stopped early for efficacy -- a more fragile data type than the CMC-driven
    comparables (Krystal/B-VEC, Syndax/revumenib) used to build that base rate --
    and that a 10-15pt haircut plus Praxis's DMC-override governance history
    (Essential 3/ulixacaltamide, 2025) collapses the edge to flat/negative.
    Unresolved -- no backtest with a defensible denominator exists for
    efficacy-sensitivity-analysis-type extensions specifically. Resolver -- such a
    backtest, plus confirmation on whether an adcom is scheduled for December.
---

## Scouted 2026-07-12T17:02:21Z

## Researched 2026-07-13T05:20:12Z

Three-round debate panel (bull/bear/quant, sonnet/sonnet/opus, synthesized on opus)
concluded **no position today**. All three personas agreed the announcement-day
reaction trade is closed (net EV ~0 after costs, ~10 trading sessions post-8-K).
The only live edge is the December 27, 2026 PDUFA approval binary, but the panel's
central estimate for its gross EV (~+5.3%, per quant's revised 79%-approval
central case) is small enough that a plausible base-rate haircut (bear's
efficacy-sensitivity-analysis argument, +Praxis's DMC-override governance history
on ulixacaltamide/Essential 3) flips it to roughly flat-to-negative. Separately,
the system's PRAX price feed returned inconsistent values across calls
($74.81 / $238 / $295 / $472) that don't reconcile with reported real-market
levels (~$280-335 around the event), which independently disqualifies sizing any
position today regardless of thesis. See `transcript.md` for the full three-round
debate with citations, and the `plan.conditional_plan` field above for what would
need to change to justify a capped-risk (call-spread) position later.
