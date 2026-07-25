---
id: 2026-07-23-arabica-coffee-supply-squeeze
title: Arabica coffee stocks hit tightest level since 2024 on harvest disruption
status: researched
created: '2026-07-23T22:07:07Z'
event:
  type: macro
  summary: ICE-certified arabica coffee stocks fell to their lowest since February
    2024 after harvest disruptions undercut hopes for a bumper crop, tightening global
    supply further.
  impact_window: '2026-08-20'
tickers:
- JO
sources:
- title: Daily Agro-Food Commodity Market Outlook - KADI Xchange
  url: https://www.kadixchange.com/market-news/daily-agro-food-commodity-market-outlook-july-14-2026-price-trends
  accessed_at: '2026-07-23T22:07:07Z'
hypothesis:
  statement: 'ICE-certified arabica stock depletion may force short-covering/buyer
    front-loading into 2026-08-20, but the claim rests on a single 9-day-stale blog
    source (KADI Xchange, 2026-07-14) with zero independent corroboration (no ICO,
    Cecafe, Conab, or Volcafe confirmation), and no live instrument exists to express
    it -- JO is delisted (three independent evidence paths converged: two consecutive
    HTTP 404s on toa price, distinct from the normal minute-gap behavior seen on
    SPY/CANE/CORN control tickers, consistent with iPath ETN redemption history),
    and the KC futures alternative is unpriceable in this harness (equity/ETF quotes
    only) and carries roughly USD 131k minimum notional with no fractional sizing.'
  direction: no-trade
  confidence: 12
plan:
  action: no-trade
  ticker: JO
  reason: 'JO is delisted/untradeable (confirmed via three independent evidence
    paths); no viable substitute exists in this harness; both surviving EV estimates
    for a hypothetical KC-futures proxy are negative (-0.4% to -0.99% net after
    costs) even before the instrument problem is considered.'
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
  dissent: 'Unanimous action (no-trade), divergent reasoning worth flagging for
    post-mortem: (1) base-rate spread of 2.5x on durable-move probability -- bear
    argued 10-12% given zero corroboration, quant raised its estimate from 20% to
    25% on the grounds that ICE-certified stock is mechanically KC''s own delivery
    float (a tight causal mechanism), while also widening magnitude assumptions
    to roughly +14%/-12% from KC''s realized ~35-40% annualized vol; unresolved
    whether a tight mechanism justifies a base-rate upgrade when sourcing is weak,
    or whether weak sourcing is the binding constraint regardless. (2) Quant''s
    P(fill)=0 on KC futures is a simulation-harness artifact (only equity/ETF
    quotes supported), not a real-market fact -- a real desk could trade KC futures
    directly. The recorded no-trade therefore conflates "bad thesis" with
    "untradeable in this engine," which could distort later learning from this
    outcome if the harness gains futures support.'
  last_updated: '2026-07-25T01:30:00Z'
---

## Scouted 2026-07-23T22:07:07Z

## Researched 2026-07-25T01:30:00Z -- NO-TRADE

**Confidence in no-trade call: 88/100** (quant), with bull and bear converging.

Data-quality finding (load-bearing): `toa price JO` returned HTTP 404 for both
2026-07-24 and 2026-07-25 via twelvedata -- a symbol-not-found error, not a
no-data-for-that-day gap. Quant confirmed this distinction with a control-ticker
check (SPY/CANE/CORN return normal minute-gap `KeyError`s, not 404s), consistent
with JO (iPath Series B Bloomberg Coffee Subindex ETN) having been delisted or
redeemed, matching iPath's real-world redemption history for this ETN family.

Round 1 (independent):
- Bull: framed the ICE-certified-stock drawdown (KADI Xchange, 2026-07-14) as a
  short-covering/front-loading catalyst into 2026-08-20; conceded JO's 404s
  upfront and pivoted to front-month ICE Coffee C (KC) futures as the cleaner
  instrument (KC's own certified stocks are the delivery mechanic).
- Bear: NO TRADE as constructed -- single stale source (9-day lag, no ICO/Cecafe/
  Conab/Volcafe corroboration), JO's 404s indicate delisting, demand-destruction
  and stock-recertification-reversal risks unaddressed by the bull case. Required
  issuer confirmation plus independent corroboration before any size.
- Quant: pre-check proved JO is symbol-not-found (delisted-consistent) vs.
  control tickers' normal gap behavior. Base rate for a stale single-source
  headline producing a durable 4-week move: ~20%. EV = 0.20x9% + 0.50x0% +
  0.30x(-8%) = -0.6% gross, -0.99% net after costs, assuming a live proxy exists.
  Separately, P(fill)xpayoff = 0 on JO specifically. Recommended NO TRADE, mark
  UNTRADEABLE, 0% size.

Round 2 (rebuttals):
- Bull conceded JO is dead and that the KC pivot fixes tradeability but not the
  underlying evidentiary weakness -- swapping the ticker doesn't repair a stale,
  single-source, uncorroborated thesis. Downgraded from "go long now" to "watch
  for corroboration, no size yet."
- Bear confirmed JO dead as unanimous fact; argued quant's 20% base rate is still
  too generous (proposed 10-12% given zero corroboration), meaning true EV is
  worse than -0.99%. Held firm: NO TRADE, 0% size.
- Quant stipulated JO dead (three independent evidence paths). Flagged KC futures
  is liquid in real markets but unpriceable in this harness (equity/ETF quotes
  only -- a scoring artifact, not a market fact) and carries ~USD 131k minimum
  notional with no fractional sizing. Revised base rate 20%->25% (tight causal
  mechanism: ICE certified stock IS KC's delivery float) but widened magnitude to
  roughly +14%/-12% (KC's real ~35-40% annualized vol was understated at
  +9%/-8%). Re-run EV: -0.1% gross, -0.4% net -- still negative. Recommended NO
  TRADE, 0% size. Would reconsider only with independent stock confirmation
  <=48h old plus evidence the move isn't already priced in.

Full transcript: see transcript.md in this opportunity's folder.

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.
