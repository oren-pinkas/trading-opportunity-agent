---
id: 2026-07-14-newmont-gold-macro-catalyst
title: Newmont trades deeply below price target ahead of CPI/FOMC gold catalysts
status: researched
created: '2026-07-13T05:37:17Z'
event:
  type: macro
  summary: NEM sits about 44% below its .35 consensus target after gold's June/July
    pullback, with the July 14 CPI print and the July 28-29 FOMC decision as the next
    hard catalysts for a gold price recovery.
  impact_window: '2026-07-14'
tickers:
- NEM
sources:
- title: Gold and Silver Recovery—3 Precious Metals Stocks for H2 2026
  url: https://finance.yahoo.com/markets/commodities/articles/gold-silver-recovery-3-precious-141500657.html
  accessed_at: '2026-07-13T05:37:17Z'
hypothesis:
  statement: >-
    The July 14 CPI print already fired as the exact macro trigger this thesis
    depends on, producing a one-day pop from USD 93.74 (7/13 pre-print) to USD
    96.84 (7/14, +3.31%) that fully round-tripped within three sessions to USD
    90.25 (7/17) and USD 89.98 (7/20) -- a net -4.01% versus the pre-CPI level
    and -7.08% off the post-print high. That is a rejection of the "gold
    catalyst repricing" thesis on its cleanest test, not a consolidation. The
    44%-below-consensus-target discount is arithmetically undisturbed (no
    estimate revisions), but a gap the market has now failed to close on its
    most mechanically-linked catalyst reads as a valuation story, not a
    FOMC-timed trading edge. Quant's EV calc for a naked directional trade into
    FOMC (2026-07-28/29) -- ~3% assumed move, 50/50 direction absent any
    skew evidence, ~0.40% round-trip cost -- comes to roughly -0.40%, negative
    by construction; clearing costs would require directional probability
    near 57%+ for which no evidence exists. The elevated realized vol from the
    CPI round-trip (~3.3% one-day, ~7% five-day) also implies FOMC options are
    likely to be marked rich rather than cheap, so a long-volatility structure
    (straddle/strangle) is not clearly mispriced either. No structure surviving
    review clears costs on current evidence.
  direction: none
  confidence: 78
plan:
  ticker: NEM
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
  dissent: >-
    Bull frames the twice-failed 44% discount (June/July pullback, then the
    CPI round-trip) as a still-live valuation entry that would re-engage long
    near USD 88 on value grounds, independent of any FOMC catalyst. Bear
    reframes the same repeated failure to close the gap as evidence of an
    emerging de-rating rather than a correctable anomaly. Neither side can
    resolve this without gold spot/futures momentum data, FOMC options-implied
    skew, or a multi-quarter NEM FOMC-day base rate -- all flagged as missing
    by quant. Testable post-mortem: if NEM approaches USD 88 pre-FOMC, was
    that a value opportunity or confirmation of structural de-rating.
  last_updated: '2026-07-21T09:24:34Z'
---

## Scouted 2026-07-13T05:37:17Z

## Researched 2026-07-21T09:24:34Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). NEM's dossier
thesis rests on the July 14 CPI print and the July 28-29 FOMC decision as gold
macro catalysts. By debate time (2026-07-21) the CPI catalyst had already fired and
fully round-tripped: USD 93.74 (7/13 pre-print) to USD 96.84 (7/14, +3.31%), then
back down to USD 90.25 (7/17) and USD 89.98 (7/20) -- net -4.01% versus the
pre-CPI level. All three personas converged on low confidence after this evidence:
BULL started at 58/100 favoring a long/call-spread into FOMC, then conceded the
round-trip was rejection not consolidation and quant's EV math, dropping to 30/100.
BEAR (20 to 15/100) argued the cleanest test of the thesis already failed and there
is no basis for FOMC to do better. QUANT (20/100, then 15/100 naked-directional and
25/100 for a defined-risk options structure) showed naked-directional EV is
approximately -0.40% under a 50/50 assumption with no evidence of favorable skew,
and that the CPI round-trip's high realized vol implies FOMC options are likely
priced rich, undercutting the long-volatility alternative too. Verdict: NO-TRADE
(not scheduled, not simulated). Flips only on independent gold momentum data, an
options-skew edge, or a hard dovish Fed signal before 2026-07-28/29. Full debate
with citations in `transcript.md`.
