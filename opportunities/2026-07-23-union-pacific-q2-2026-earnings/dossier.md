---
id: 2026-07-23-union-pacific-q2-2026-earnings
title: Union Pacific Q2 2026 Earnings Release
status: researched
created: '2026-07-23T05:29:18Z'
event:
  type: earnings
  summary: UNP reports Q2 2026 results today with analysts expecting EPS growth on
    freight pricing and volume mix strength
  impact_window: '2026-07-23'
tickers:
- UNP
sources:
- title: Union Pacific Corporation Announces Second Quarter 2026 Earnings Release
    Date - BusinessWire
  url: https://www.businesswire.com/news/home/20260625996926/en/Union-Pacific-Corporation-Announces-Second-Quarter-2026-Earnings-Release-Date
  accessed_at: '2026-07-23T05:29:18Z'
hypothesis:
  statement: 'There is no executable positive-expected-value trade in UNP as of
    2026-07-26. The dossier itself is only a date announcement (no actual EPS,
    revenue, or guidance figures were ever provided), and the only hard evidence
    is the realized price path around the print - "USD 309.90" at the 2026-07-23
    open, "USD 304.365" at the earnings-day close (a decline of 1.79 percent), and
    "USD 307.46" at the next session close (a recovery of 1.02 percent, leaving
    the stock about 0.79 percent below the pre-print open). That two-bar sequence
    cannot distinguish a genuine miss being partially bought back from noise
    around an in-line-or-better print. The event is three days stale, so any
    entry now is a fresh continuation-or-mean-reversion bet, not an earnings
    trade. Quant expected-value estimate: assumed P(down) 0.51 versus P(up) 0.49,
    magnitude plus or
    minus 1.3 percent, gross EV about plus 2.6 basis points against roughly 7
    basis points of round-trip cost, net EV about minus 4.4 basis points -
    negative and smaller in magnitude than the transaction cost itself. Missing
    fundamentals are symmetric ignorance - they do not shift the point estimate,
    they only widen the error bars around an already sub-cost expected value,
    which makes standing aside more correct, not less.'
  direction: none
  confidence: 88
plan:
  ticker: UNP
  action: no-trade
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
  dissent: 'Nobody on the panel ever sourced the actual Q2 2026 EPS, revenue, or
    guidance figures - the dossier''s "analysts expecting EPS growth" framing was
    unsourced boilerplate from a date-announcement press release, and the debate
    proceeded entirely from four verified price points rather than fundamentals.
    Convergence to NO-TRADE therefore happened under a fundamental-data blackout,
    which is weaker corroboration than agreement reached against verified facts -
    the open question for a post-mortem is not whether NO-TRADE was correct but
    whether this dossier should have reached a research round at all with only a
    press-release date announcement as its content. Second, narrower dissent: the
    bull''s initial read - that a 1.79 percent earnings-day fade followed by a
    1.02 percent recovery is the signature of an overreaction being absorbed by
    dip-buyers, rather than a real miss being partially digested - was withdrawn
    on expected-value grounds (55 to 25 confidence) but never falsified on
    pattern grounds; the quant''s rebuttal was that a two-point sample cannot
    support the inference either way, which is an insufficient-evidence argument,
    not a contrary-evidence one. Even if the overreaction read were true, the
    remaining retracement (about 0.79 percent) would not clear round-trip costs,
    so it would not have changed the plan. Log as an untested hypothesis for a
    future post-earnings-drift study on Class I rail names, not as a live edge.'
  last_updated: '2026-07-26T05:30:02Z'
---

## Scouted 2026-07-23T05:29:18Z

## Researched 2026-07-26T05:30:02Z

NO-TRADE. See transcript.md for the full three-round debate (bull, bear, quant;
synthesized on opus). Verdict confidence 88/100 that standing aside is correct;
20/100 confidence in any directional view. This research pass is based solely on
this dossier's own event summary and four verified UNP price points fetched via
`toa price UNP <timestamp> --provider twelvedata` - no other opportunity's dossier
was consulted.
