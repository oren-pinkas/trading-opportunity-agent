---
id: 2026-07-12-big-bank-earnings-kickoff
title: Big bank earnings kick off Q2 2026 season
status: researched
created: '2026-07-12T17:02:21Z'
event:
  type: earnings
  summary: JPMorgan, Citigroup, Wells Fargo and Bank of America report Q2 2026 earnings
    July 14, opening the earnings season.
  impact_window: '2026-07-14'
tickers:
- JPM
- C
- WFC
- BAC
sources:
- title: 'Stock market next week: Outlook for July 13-17, 2026'
  url: https://www.cnbc.com/2026/07/10/stock-market-next-week-outlook-for-july-13-17-2026.html
  accessed_at: '2026-07-12T17:02:21Z'
hypothesis:
  statement: >-
    The big-bank Q2 earnings kickoff (JPM/C/WFC/BAC, July 14, 2026) is a fully-priced,
    non-edged catalyst, not a genuine dislocation. The capital-markets-momentum
    thesis is itself consensus and already embedded in elevated options-implied
    moves (JPM ~4.4%, BAC ~4.5%, WFC/C ~5.5%); consensus EPS was revised up into
    the print and several names (notably BAC) are running into record/near-record
    highs rather than depressed levels, which inverts the "bad news already priced
    in" setup into a "raised bar, sell-the-beat" setup. No persona surfaced a
    non-consensus directional read that survives transaction costs and option
    theta/vega decay: every structure examined (directional long, long straddle,
    long call/call-spread) is negative-EV, and the one structure with positive raw
    EV (naked short premium, capturing an implied-over-realized variance gap) is
    disqualified by an un-hedgeable guidance/credit-provision gap tail (Citi
    restructuring execution risk, WFC's unconfirmed asset-cap headline, subprime
    credit divergence).
  direction: none
  confidence: 74
plan:
  ticker: JPM/C/WFC/BAC
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: null
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
    The sharpest unresolved fault line is between the Bull's convexity argument
    and the Quant's "convexity is priced" rebuttal. The Bull (ended at 52/100,
    reduced to a single JPM call-spread leg) maintains that a defined-risk call
    spread's asymmetric payoff shape (bounded loss, exposure to a trading-revenue
    operating-leverage right tail) could justify a small position even at ~zero
    average-move EV. The Quant counters that option skew/premium already prices
    that convexity in, leaving a "bounded-loss lottery ticket with negative EV."
    Neither side had IV-percentile/skew data to adjudicate whether the right tail
    is genuinely mispriced (Bull) or merely elevated-but-fairly-priced (Quant); both
    flagged the same missing input. Revisit only if: (1) real IV-percentile/skew
    data becomes available showing the right tail is actually rich/mispriced, not
    just elevated; (2) the stub-price-vs-web-price mismatch (flagged independently
    by both Bear and Quant) is reconciled, restoring confidence in sourced
    valuation math; or (3) a single authoritative (not secondary-press) source
    confirms the WFC asset-cap-removal status one way or the other.
  last_updated: '2026-07-12T17:38:07Z'
---

## Scouted 2026-07-12T17:02:21Z

## Researched 2026-07-12T17:38:07Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). All three
personas converged on NO-TRADE. Bull opened Round 1 at 60/100 confidence long
defined-risk calls on JPM + WFC, citing capital-markets momentum, already-priced
NII-guidance-cut, and options implied moves it read as "not pricing much fear."
Bear opened at 28/100 confidence in any genuine edge, noting options already price
implied moves of 4.4-5.5% (the market's own edge estimate), consensus EPS already
revised up into record-high prices (a raised, not lowered, bar), a WFC NIM/margin
headwind undercutting the Bull's asset-cap story, and real Citi-specific execution
risk. Quant (no live web access) opened at NO-TRADE from first principles: base-rate
EV for a directional long ≈ -0.08% net of costs, long straddle ≈ -0.5% to -1%, short
premium thin vs. an un-hedgeable tail — confidence 65/100 in magnitude, 15/100 in
direction. In Round 2, Bull conceded BAC's record-high setup and WFC's NIM-dilution
mechanism, cutting the trade down to a single reduced-size JPM call spread (52/100).
Bear reinforced to 20/100, reframing Bull's "sell-rumor-buy-news" thesis as
inapplicable to a raised-bar setup ("sell-the-beat"). Quant re-ran EV using Bear's
real implied-move data: directional/straddle structures stayed negative, and the
only positive-EV structure (naked short premium, +1-2% gross) was rejected on
un-hedgeable-tail grounds consistent with the on-file NKE lesson; confidence in "no
reliable directional edge" rose to 75/100. Synthesizer weighted the Quant's
self-stress-tested quantitative convergence and the Bear's independently-derived
qualitative convergence most heavily over the Bull's retreating, convexity-based
case, landing on NO-TRADE at 74/100 confidence. Full debate with citations in
`transcript.md`.
