---
id: 2026-07-12-tesla-q2-fy26
title: Tesla Q2 2026 earnings
status: researched
created: '2026-07-12T17:02:21Z'
event:
  type: earnings
  summary: Tesla reports Q2 2026 earnings July 22 after market close; investors will
    focus on robotaxi expansion (now live in Miami), FSD progress, and margins after
    strong Q2 deliveries.
  impact_window: '2026-07-22'
tickers:
- TSLA
sources:
- title: 'Tesla Q2 2026 Earnings Date: Release Time, Webcast and Key Metrics'
  url: https://www.mexc.com/news/1196267
  accessed_at: '2026-07-12T17:02:21Z'
hypothesis:
  statement: The TSLA Q2 print is a genuine new-information event (audited margin/EPS
    on 2026-07-22), but the tradeable edge collapses under scrutiny -- the delivery-beat
    catalyst is confirmed already-priced-in (a 25% delivery beat bought a -7.4% selloff
    on 2026-07-02), the stock sits inside the analyst consensus band ($400.59-$424.56)
    with no valuation cushion, the tape keys on auto gross margin ex-credits (genuinely
    two-sided), and an exogenous NHTSA/robotaxi regulatory tail is live in the holding
    window. The sole asserted directional edge -- UBS's $0.67 vs $0.49 Street EPS -- is
    a single high estimate (dispersion, not a higher mean), and a real unpriced edge
    would surface as options upside skew, which the ~7% symmetric implied move does
    not show.
  direction: no_trade
  confidence: 78
plan:
  ticker: TSLA
  action: no_trade
  entry:
    time: '2026-07-22T19:59:00Z'
    target_price: null
  exit:
    time: '2026-07-23T19:59:00Z'
    target_price: null
  expected_profit_pct: 0
  notes: Record-only entry/exit times for post-mortem scoring; no capital deployed.
    If forced to trade, panel EV was gross ~-0.10%, net ~-0.4% to -0.6% on a 49/51
    skew after ~7% rich implied vol vs ~4.4% realized -- break-even required
    P(up) > ~0.54, panel's best estimate was 0.49-0.50 (inside estimation error).
    The only defensible structure identified (defined-risk long put spread) was
    rejected for paying rich implied vol against a sub-error-bar skew; revisit only
    if implied move compresses toward realized before the print.
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
  dissent: The strongest unresolved disagreement is the nature of the 2026-07-22
    margin/EPS release itself. Bull argues "twice priced in" conflates two
    already-known facts (deliveries, Miami robotaxi) with a genuinely new, unknowable
    audited margin number -- a market walking in worried about margin sets up an
    outsized relief rally if margin merely holds, an upside asymmetry a symmetric
    50/50 base rate doesn't capture; bull kept this path open, conceding only if UBS
    proves an outlier. Quant argued UBS is likely an outlier (dispersion is not a
    higher mean; no options skew observed) but did not directly disprove the
    underlying mechanism bull points at -- higher unit volume improving fixed-cost
    absorption and thus margin -- answering with market-structure evidence rather
    than the fundamental mechanism. Separately, bear's negative-skew case (run-up +
    zero valuation cushion + NHTSA tail + insider selling) and quant's mild
    0.50-to-0.49 nudge remain in tension over how negative the skew really is. Both
    the bull's upside-relief case and the bear's downside-skew case survived to
    Round 3 unresolved -- they cancel into NO TRADE, they are not jointly settled.
    Post-mortem test -- if margin ex-credits lands >=18-20% AND the stock rallies
    hard, bull's mechanism was right and the panel under-weighted a real
    relief-rally edge; if margin holds and the stock still fades/gaps on an NHTSA
    or guidance headline, bear's negative-skew read was right.
  last_updated: '2026-07-13T13:25:00Z'
---

## Scouted 2026-07-12T17:02:21Z

## Researched 2026-07-13T13:25:00Z — NO TRADE

**Event:** Tesla reports Q2 2026 earnings 2026-07-22 after market close, focus on
robotaxi expansion (Miami, live since July 5), FSD progress, and margins after a strong
Q2 delivery beat (480,126 units, +25% YoY). Dossier source: MEXC, "Tesla Q2 2026
Earnings Date: Release Time, Webcast and Key Metrics" (accessed 2026-07-12).

**Panel verdict (three-round debate, bull/bear/quant + synthesis):** All three personas
converged from independent starting points to NO TRADE. Bull opened long on a
stacked-catalyst thesis (delivery beat, Miami robotaxi launch, FSD subscriber growth,
UBS's $0.67-vs-$0.49-Street EPS model) but, on verifying the actual July 2 price action
(-7.4% on the delivery beat) and the analyst price-target range ($400.59-$424.56, no
discount), conceded the delivery/robotaxi legs of the thesis were already priced in and
dropped to ~40-45% confidence, conditioning further conviction on the UBS estimate not
being an outlier. Bear argued the two known catalysts (deliveries, robotaxi) are spent
gap triggers, valuation offers no cushion (P/E>350, at/above Street average target), and
a live NHTSA "clear pattern" warning on AV/first-responder interference is an
un-hedgeable left-tail risk independent of the print; converged to a NO-TRADE default
(small hedged-short only if cheap, never a conviction short). Quant's base-rate/EV model
(TSLA earnings moves: recent mean ~4.4%, historical fat tail to 21.9%; options-implied
~7% > realized) found no directional edge (P(up)~0.49-0.50) and negative EV after costs
(gross ~-0.10%, net ~-0.4% to -0.6%); confidence in NO TRADE rose from 70 to ~80,
explicitly rejecting both the bull's unhedged long and the bear's short, as well as a
defined-risk put spread (rich implied vol against a sub-error-bar skew).

**Recommendation:** No trade, no capital deployed. See `transcript.md` for the full
three-round debate with citations.
