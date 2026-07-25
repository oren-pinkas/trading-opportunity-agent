---
id: 2026-07-23-cxmt-shanghai-star-ipo
title: ChangXin Memory Technologies (CXMT) Shanghai STAR Board IPO
status: researched
created: '2026-07-23T05:29:18Z'
event:
  type: ipo
  summary: CXMT, world's 4th-largest DRAM chipmaker, lists July 27 on Shanghai STAR
    board after pricing a roughly USD 8.6-9.8B IPO, Asia's biggest of 2026
  impact_window: '2026-07-27'
tickers:
- CXMT
sources:
- title: Chinese Memory Giant CXMT Seeks 9.8 Billion in Marquee IPO - Bloomberg
  url: https://www.bloomberg.com/news/articles/2026-07-14/cxmt-prices-ipo-in-marquee-moment-for-china-s-chip-revolution
  accessed_at: '2026-07-23T05:29:18Z'
hypothesis:
  statement: 'CXMT''s STAR board debut on 2026-07-27 very likely produces a large
    first-day pop -- 212x retail / 463x institutional oversubscription, a 0.47%
    allotment rate, a cheap roughly 3x P/B against Samsung 2.22x / SK Hynix 3.73x /
    Micron 5.73x, and a STAR/China semiconductor IPO base rate averaging +140% to
    +227% (SMIC 2020 +202%) all point the same direction; probability-weighted
    day-1 estimate approximately +121%. That edge is unreachable from this system:
    CXMT is an RMB A-share with no confirmed access route (SSE eligibility excludes
    non-A+H, non-index-constituent STAR shares from Stock Connect/retail at
    listing) and no price feed -- toa price returned HTTP 404 on all four symbol
    variants tested (CXMT, 688766.SS, CXMT.SS, 688766), while control tickers
    MU/SMH/ASHR resolved normally, and A-share supplier proxies (NAURA, AMEC) also
    404''d, confirming zero mainland A-share provider coverage rather than a
    symbol error. Two candidate bridges were tested and rejected: MU as a
    memory-cycle proxy nets EV +0.07% +-0.23% (sign undetermined, breakeven hit
    rate 50.64%), and ASHR index transmission is approximately 0 because CXMT
    carries 0% index weight at listing pending seasoning. A live binary
    geopolitical overhang (DoD "Chinese military company" designation under NDAA
    1260H; reported Entity List deliberation, undisclosed timing) is moot for a
    position that cannot be opened, but is sign-ambiguous on the MU proxy and
    shrinks its Kelly size further. Confidence the pop occurs is high; confidence
    any tradable instrument captures it is zero.'
  direction: neutral
  confidence: 0
plan:
  ticker: CXMT
  action: none
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
research:
  last_updated: '2026-07-25T08:03:24Z'
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
  verdict: no-trade
  confidence: 0
  lessons_applied:
  - '2026-07-07-lime-ipo: delay entry to a liquid 30-60min window post-print rather
    than the raw open minute (moot here -- no price feed exists for CXMT at all)'
  - '2026-07-07-lime-ipo: gate IPO opportunities on a confirmed listing date/time
    verified present in the price provider (applied -- listing date is confirmed
    but not present in twelvedata; this alone is disqualifying)'
  dissent: 'Whether a high-confidence forecast on an unreachable instrument has any
    epistemic value worth recording. Bull and quant argue yes -- log the
    approximately +121% day-1 pop forecast for calibration scoring since forecast
    accuracy and tradability are independent variables. Bear argues no -- a
    forecast on something that cannot be held is trivia and inflates the
    calibration record with costless, unfalsifiable-in-practice wins. Also
    unresolved: whether SMIC''s 2020 STAR debut (+202%, also under US export
    restrictions) is a valid comp given bear''s point that SMIC was not under
    active Entity List deliberation at listing the way CXMT reportedly is; and the
    STAR post-pop fade curve was never quantified by any persona despite being
    asserted by bear as the mechanism behind multi-week reversion.'
  transcript: transcript.md
---

## Scouted 2026-07-23T05:29:18Z

## Researched 2026-07-25T08:03:24Z
Verdict: NO-TRADE (neutral, confidence 0). Three-round panel (bull/bear sonnet,
quant opus; synthesizer opus). All three personas independently converged on
no-trade for CXMT itself: quant ran `toa price` against four CXMT/A-share symbol
variants and two A-share supplier proxies (NAURA, AMEC) -- all HTTP 404, while
control tickers MU/SMH/ASHR resolved normally, confirming the provider has zero
mainland A-share coverage (not a CXMT-specific gap). No retail or Stock
Connect/QFII access route exists for a brand-new, non-index STAR listing either.
Bull's thesis (212x retail / 463x institutional oversubscription, cheap ~3x P/B
vs. global DRAM peers, DDR5/HBM supercycle tailwind, SMIC 2020 +202% precedent,
probability-weighted day-1 return ~+121%) was conceded as directionally likely
correct by both bear and quant, but bull explicitly withdrew the actionable
recommendation in Round 2 once no fillable instrument could be confirmed. Two
proxy bridges were tested and killed rather than assumed: MU nets EV +0.07% +-
0.23% (t-stat 0.30, p=0.76, sign undetermined, breakeven hit rate 50.64%, ~48,000
trades needed to distinguish from zero); ASHR carries 0% CXMT index weight at
listing (pending seasoning), so transmission is ~0 even before accounting for the
sign-ambiguous Entity List overhang layered on top. This is logged as an
undefined-EV non-trade, not a low-EV trade -- no entry or exit is scheduled. The
+121% day-1 directional forecast is retained for calibration scoring only, with
zero capital allocated. Full debate with citations in `transcript.md`.
