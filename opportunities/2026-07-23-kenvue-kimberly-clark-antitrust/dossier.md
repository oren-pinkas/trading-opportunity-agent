---
id: 2026-07-23-kenvue-kimberly-clark-antitrust
title: Kenvue/Kimberly-Clark merger pending antitrust clearance
status: researched
created: '2026-07-23T15:22:32Z'
event:
  type: regulatory
  summary: Kenvue-Kimberly-Clark stock-and-cash merger agreement expected to close
    H2 2026, conditioned on US antitrust and foreign regulatory clearance
  impact_window: '2026-09-30'
tickers:
- KVUE
- KMB
sources:
- title: Kenvue Inc. Form 10-Q FY2026
  url: https://www.sec.gov/Archives/edgar/data/0001944048/000194404826000098/kvue-20260329.htm
  accessed_at: '2026-07-23T15:22:32Z'
hypothesis:
  statement: >-
    The KVUE/KMB merger-arb spread (approximately 1.50 percent gross at 2026-07-24,
    KVUE USD 19.175, KMB USD 109.30) is fully harvested and offers no risk-adjusted
    edge in either direction. Compression from 3.73 percent (2026-02-05) to about
    1.50 percent already occurred on the de-risking events that mattered (US HSR
    expiry 2026-02-04, both shareholder votes, India CCI, EU foreign-subsidy
    clearance). The remaining open tracks (China SAMR information request since
    2026-05-29, Brazil CADE market test opened 2026-07-21 with competitor Santher
    seeking to intervene, and EU merger clearance proper, which is distinct from the
    already-granted FSR clearance) are duration and delay risk, not repricing
    catalysts. Hedged scenario-tree EV is negative (approximately USD -245 to -266
    per 1000 shares net of costs); an unhedged single-leg long is not better -- it
    dilutes the same negative EV with roughly 8.4x the daily variance (KVUE/KMB
    daily-return correlation 0.994). The inverse trade (short the spread, betting on
    delay) is mechanically positive (about USD +130 per 1000 shares) but flips sign
    under mild reparameterization of its two softest inputs (P(break), P(widen)),
    failing the durability floor. Correct action is no position.
  direction: none
  confidence: 78
plan:
  ticker: KVUE
  action: no-trade
  entry:
    time: '2026-07-27T14:00:00Z'
    target_price: null
  exit:
    time: '2026-09-30T19:00:00Z'
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
  dissent: >-
    The strongest unresolved disagreement is factual, not analytical -- whether the
    US antitrust track is genuinely clean. Quant's rejection of the bear's Round 1
    claim of an FTC second request (sourced only from Simply Wall St commentary) was
    stated at approximately 85 percent confidence (MLex reporting plus KMB's 10-Q
    showing a clean HSR expiry on 2026-02-04), not certainty, and the panel then
    adopted it as settled fact. That is the load-bearing input of the whole
    synthesis: if quant is wrong in the residual ~15 percent, P(break) roughly
    doubles and hedged EV degrades to about USD -478 per 1000 shares, which would
    not change the no-trade verdict on the long side but would materially
    strengthen the short-the-spread case that was otherwise rejected only on
    durability grounds. Second, live dissent: bear argues Brazil CADE's market test
    (opened 2026-07-21, four days before the debate, with Santher moving to
    intervene) is fresh negative information that makes quant's P(close by
    2026-09-30) is approximately 12 percent estimate optimistic rather than
    conservative; quant folded this into an existing scenario weight rather than
    re-deriving it, so it was never directly rebutted. Third, methodological: the
    inverse (short-the-spread) trade was disqualified for failing a
    sign-flips-under-reparameterization test that was never applied with equal
    rigor to the primary no-trade verdict -- a note for the post-mortem rather than
    a live objection, since the no-trade verdict is more robust on its face (it
    survives on spread level and duration alone).
  last_updated: '2026-07-25T15:45:00Z'
---

## Scouted 2026-07-23T15:22:32Z

## Researched 2026-07-25T15:45:00Z -- NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Deal: Kimberly-Clark
acquiring Kenvue for USD 3.50 cash plus 0.14625 KMB shares per KVUE share (~USD 49
billion), outside date 2026-11-02 extendable to 2027-05-03 for regulatory approvals.
Bull opened long KVUE on a "4 of 5 gates cleared, SAMR is the last domino" thesis
(US HSR expired clean 2026-02-04, India CCI cleared, EU FSR cleared, both shareholder
votes approved) with a hard exit near the dossier's 2026-09-30 impact window. Bear
opened cautious, initially citing an FTC second request that turned out to rest on a
single commentary source and was retracted in Round 2. Quant's scenario-tree EV
(hedged ratio long KVUE / short 0.14625x KMB) came in negative both directions:
spread history shows compression from 3.73 percent (2026-02-05) to 1.50 percent
(2026-07-24) already happened on vote/HSR de-risking, not on the still-open foreign
tracks (China SAMR information request since 2026-05-29, Brazil CADE market test
opened 2026-07-21 with competitor Santher seeking to intervene, and EU merger
clearance proper -- distinct from the already-granted EU FSR clearance). P(close by
2026-09-30) approximately 12 percent broke the bull's own hard-exit design; bull
conceded in Round 2 and narrowed to a smaller, later-exit position rather than
defending the original thesis. Quant showed the unhedged single-leg long bull
proposed does not improve on the hedged EV -- KVUE/KMB daily-return correlation is
0.994, so unhedged carries roughly 8.4x the daily variance for a marginally less
negative expected value (dilution, not edge). The inverse short-the-spread trade
priced mechanically positive but failed a durability check (sign flips under mild
reparameterization of P(break) and P(widen)), so it was rejected as "a bet on my
own guesswork, not a trade." Verdict: NO-TRADE. Reopens on any of: a primary-source
resolution of the FTC-second-request question in either direction; China SAMR
conditional clearance or a formal Phase-equivalent escalation; Brazil CADE closing
its market test without Santher-driven restrictions, or a Tribunal referral; EU
merger clearance (not FSR) being decided; or the gross spread widening past roughly
4 percent on a headline, which would re-open a genuine risk-premium entry rather
than the current fully harvested one. Full debate with citations in `transcript.md`.
