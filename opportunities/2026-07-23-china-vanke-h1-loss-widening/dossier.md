---
id: 2026-07-23-china-vanke-h1-loss-widening
title: China Vanke H1 loss widening ahead of interim results
status: researched
created: '2026-07-23T09:13:03Z'
event:
  type: earnings
  summary: China Vanke has flagged its H1 2026 loss may widen sharply amid a fresh
    drop in July home sales among the largest developers, with formal interim results
    the next catalyst for property-sector contagion risk
  impact_window: '2026-08-15'
tickers:
- 2202.HK
sources:
- title: 'China''s Property Crisis: Trending News, Latest Updates, Analysis'
  url: https://www.bloomberg.com/latest/china-s-property-crisis
  accessed_at: '2026-07-23T09:13:03Z'
hypothesis:
  statement: "China Vanke's 2026-08-15 interim results are a confirmation event for
    an already pre-announced, maximally-telegraphed loss, not an information event
    -- and independently of thesis merit, no Vanke equity symbol (2202.HK, 002202.SZ,
    VNKAY ADR) is priceable via the configured market-data provider (all HTTP 404,
    while control tickers AAPL/EWH price normally), so no entry, exit, fill, or mark
    can ever be produced for this name in this harness. Separately, 2026-08-15 and
    a candidate 2026-08-22 exit both fall on a Saturday (non-trading session); the
    real reaction session would be Monday 2026-08-17. The opportunity is unactionable
    on data-coverage grounds, independent of the thesis debate."
  direction: none
  confidence: 12
plan:
  ticker: 2202.HK
  action: no-trade
  entry:
    time: '2026-08-17T01:30:00Z'
    target_price: null
  exit:
    time: '2026-08-17T07:00:00Z'
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
  dissent: "Not about the action -- all three personas converged on NO-TRADE. The
    unresolved disagreement is whether quantified EV on unverified inputs is analysis
    or theater: the quant produced a precise-looking net EV (short approx -2.2%,
    long approx +0.2%) from probability/return triplets built on zero verified
    price or IV data; bull and bear both argued the honest statement is 'the
    plausible EV range spans zero and cannot be narrowed without data,' and the
    quant never conceded the point. Preserve for post-mortem: should an EV table be
    gated on a minimum count of verified inputs, and forced to report a range rather
    than a point estimate when key inputs (price, IV, borrow) are missing? Weaker
    secondary dissent: bull/bear held the state-support tail (Shenzhen Metro / PBOC
    / restructuring disclosure) is a fat, uncapped right tail against any short; the
    quant's own Round 1 model capped the benign branch at +18%."
  last_updated: '2026-07-25T06:20:00Z'
---

## Scouted 2026-07-23T09:13:03Z

## Researched 2026-07-25T06:20:00Z -- NO-TRADE / DATA-COVERAGE-FAIL

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). All three
personas independently opened NO-TRADE in Round 1: the July home-sales drop plus
Vanke's own pre-announced loss-widening make the 08-15 interim results a
confirmation event, not a surprise catalyst, and a well-telegraphed multi-year
property-crisis narrative is largely priced in. The QUANT's `toa price` check
(with `--provider twelvedata`, per the known stub-default trap) returned HTTP 404
for 2202.HK, 002202.SZ, and the VNKAY ADR under every symbology tried, while
control tickers (AAPL, EWH) priced normally -- confirming a structural
data-coverage gap, not a bad timestamp: this provider has no HKEX/SZSE coverage
for Vanke under any symbol, so no entry/exit/fill/mark can ever be produced for
this name. The quant also caught that the dossier's impact_window (2026-08-15)
and a candidate exit (2026-08-22) are both Saturdays -- the real reaction session
is Monday 2026-08-17 -- an independent error that would have silently voided the
trade even if pricing worked. Round 2 rebuttals converged further: bull and bear's
proposed options fallbacks (defined-risk put spread / long-vol straddle) were
shown to be structurally unimplementable (no option-chain/IV data source exists,
and the simulator only diffs fixed entry/exit prices), collapsing both conditional
NO-TRADEs to unconditional. A fillable-but-unrelated proxy (EWH, a HK broad-market
ETF with no material China-developer weight) was explicitly considered and
rejected as the worst failure mode -- it would book real P/L against an untested
thesis and pollute the lessons loop. Confidence in NO-TRADE rose from ~85 to ~94-96
across the panel as each additional check failed. Verdict: NO-TRADE, not scheduled,
not simulated. Recorded as `researched` rather than left `scouted` so the
data-coverage-fail and calendar findings are captured; recommend voiding any future
Vanke-ticker dossier at the scout/data gate before spending a debate on it (the
sibling dossier `2026-07-13-china-vanke-bond-default-risk`, if it exists, carries
the same unpriceable ticker). Full debate with citations in `transcript.md`.
