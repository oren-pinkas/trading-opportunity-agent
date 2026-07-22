---
id: 2026-07-13-oil-iran-tension-surge
title: Oil surges 6-7% as US-Iran tensions escalate
status: simulated
created: '2026-07-13T13:04:45Z'
event:
  type: geopolitical
  summary: Brent and WTI jumped sharply as US-Iran tensions escalate ahead of bank
    earnings week
  impact_window: '2026-07-20'
tickers:
- USO
- CL
sources:
- title: Oil surges on Iran, bank earnings ahead
  url: https://www.ig.com/en/news-and-trade-ideas/weekly-market-navigator-13-jul-2026-260713
  accessed_at: '2026-07-13T13:04:45Z'
hypothesis:
  statement: USO is trading ~7% rich to its CL-tracking fair value -- during the exact
    intraday window USO accelerated hardest (2026-07-13T14:00Z to 19:55Z, +5.19%),
    the WTI it tracks actually fell (-0.85%), falsifying the "informed flow into the
    long-oil trade" read of the divergence. The spike is a geopolitical-rhetoric premium
    plus an ETF dislocation, not a physical-supply repricing. Expect mean-reversion
    of the USO/NAV premium and/or decay of the unconfirmed Hormuz risk premium toward
    the 2026-07-20 horizon, barring a confirmed physical disruption (tanker seizure,
    export-infra strike, Hormuz transit halt, Gulf war-risk insurance spike).
  direction: short
  confidence: 60
plan:
  ticker: USO
  action: short
  entry:
    time: '2026-07-14T13:35:00Z'
    target_price: 117.0
  exit:
    time: '2026-07-20T14:30:00Z'
    target_price: 111.75
  expected_profit_pct: 4.2
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
  dissent: 'The strongest unresolved disagreement is the Bear''s data-provenance objection,
    which survives even after the fade case won on merits: the entire short thesis
    rests on an inferred ~7% USO-to-NAV premium that was never confirmed with actual
    creation/redemption or published-NAV data -- only implied from a divergence in
    a thin, choppy price series that all three personas sampled at slightly different
    reference prints. The Quant''s continuation/chop/fade probabilities (0.25/0.30/0.50)
    are an unsourced subjective prior presented with false-precision decimals, not
    a queried historical hit-rate. The Bull''s residual point -- that the divergence
    could be genuine bullish ETF flow or a contract-curve mismatch rather than a mechanical
    arbitrage error -- is weakened by the concurrent-hours CL-down/USO-up evidence
    but not logically eliminated without the NAV data. Direction is well-supported;
    sizing should stay humble (<=1% portfolio risk / <=15% notional, hedged through
    bank-earnings week with a small OTM USO call), and the NAV-premium confirmation
    step is a genuine open risk, not a formality. Hard invalidation: cover on any
    confirmed physical disruption (tanker seizure, export-infra strike, Hormuz transit
    halt, Gulf war-risk insurance spike).'
  last_updated: '2026-07-13T20:10:00Z'
simulation:
  ran_at: '2026-07-21T22:31:54Z'
  fills:
  - leg: entry
    planned_price: 117.0
    actual_price: 120.98
    source: https://api.twelvedata.com/time_series?symbol=USO&interval=1min&date=2026-07-14&timezone=UTC
    fetched_at: 2026-07-14T13:35Z
  - leg: exit
    planned_price: 111.75
    actual_price: 124.099998
    source: https://api.twelvedata.com/time_series?symbol=USO&interval=1min&date=2026-07-20&timezone=UTC
    fetched_at: 2026-07-20T14:30Z
  realized_profit_pct: -2.5789
  outcome: loss
  matched_hypothesis: 'no'
---

## Scouted 2026-07-13T13:04:45Z

## Researched 2026-07-13T20:10:00Z — SHORT

Bull, Bear, and Quant independently researched the same 6-7% Brent/WTI headline surge, then rebutted each other with fresh price pulls rather than just narrative. The pivotal fact surfaced in Round 2 (Quant): between 2026-07-13T14:00Z and 19:55Z, WTI (CL) fell -0.85% while USO rose +5.19% in the same trading hours -- the exact window USO accelerated hardest is the window the barrel it tracks moved the opposite direction. That directly falsifies the Bull's Round 1 read that USO's outsized move confirmed "hot informed long-oil flow" (informed flow into a commodity trade should show up in the commodity, not against it). The Bull conceded ground in Round 2 rather than defending the long outright: cut size, staged entry, tightened the stop from $113 to $114.50, and pre-committed to going flat (not short) even if proven wrong.

Two largely independent fade channels point the same direction: (1) the historical base rate that unconfirmed Iran-tension risk premiums (Abqaiq, Soleimani, 2023-24 Israel-Iran flare-ups) decay within 1-3 weeks absent an actual barrel removed from the market, and (2) a ~7.1-7.3% USO premium to CL-tracking fair value that is closer to a mechanical ETF-arbitrage compression than a geopolitical bet (Quant estimates P(>=50% compression in 5-10 days) ~0.65-0.70). Bank-earnings-week is folded in as a variance/gap-risk factor (not a mean-shifting one) -- hence hedging with a short-dated OTM USO call rather than relying on a bare stop that could gap through overnight.

Confidence is capped at 60, not higher, because the Bear's core objection was never closed: the ~7% premium is inferred from a thin, choppy price series (three personas pulled three slightly different reference prints), never confirmed against actual USO NAV/creation-redemption data. That means conviction and sizing are being set on the same unverified series being traded -- so size is kept at the low end of the range discussed (<=1% portfolio risk / <=15% notional), split half now / half on NAV-premium confirmation, with a hard invalidation on any confirmed physical supply disruption.

---
### Revision 2026-07-21T22:31:54Z
Simulated USO short: -2.5789% (loss, matched=no)
