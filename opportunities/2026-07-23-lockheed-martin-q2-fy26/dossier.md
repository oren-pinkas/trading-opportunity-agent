---
id: 2026-07-23-lockheed-martin-q2-fy26
title: Lockheed Martin Q2 FY26 earnings
status: researched
created: '2026-07-07T20:34:02Z'
event:
  type: earnings
  summary: LMT reports Q2 FY26 on July 23; F-35 deliveries, backlog and defense-budget
    outlook in focus
  impact_window: '2026-07-23'
tickers:
- LMT
sources:
- title: Lockheed Martin Announces Second Quarter 2026 Earnings Results Webcast
  url: https://investors.lockheedmartin.com/news-releases/news-release-details/lockheed-martin-announces-second-quarter-2026-earnings-results
  accessed_at: '2026-07-07T20:34:02Z'
hypothesis:
  statement: LMT Q2 FY26 earnings (2026-07-23) present no exploitable edge -- backlog-locked
    revenue, heavy analyst coverage (30+), and a stock priced near highs on a multi-year
    defense re-rating make surprise probability low and any positive skew already
    priced. Two independent methods (quant's EV math and the bear's efficiency
    argument) converge on negative-to-negligible expected value after costs on the
    event trade, and the options hedge the bull originally structured around is
    not executable in this equity-only simulator. The bull's fallback pre-earnings-drift
    trade rests on an uncited, story-shaped edge the bull itself only holds at 40
    confidence, which does not clear a reasonable bar in a high-information-efficiency
    name.
  direction: none
  confidence: 72
plan:
  ticker: LMT
  action: no-trade
  entry: null
  exit: null
  expected_profit_pct: 0.0
  rationale: All three personas converged on NO-TRADE for the through-earnings event
    by Round 2 -- bear and quant explicitly NO-TRADE with rising confidence (68->78
    and 30->40 respectively), and bull retracted its own through-earnings trade
    once the options-execution constraint killed its defined-risk structure. The
    only live question -- bull's narrow pre-earnings-drift-only equity trade, held
    at just 40 confidence with no sourced drift data -- does not clear a reasonable
    bar in a heavily-covered, high-efficiency mega-cap. Stand aside; revisit if a
    sourced, non-consensus catalyst (F-35 lot-pricing news, a program delay/cancellation
    report, or budget-bill language) surfaces before 2026-07-22 close.
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
  dissent: 'The bull maintains, at 40 confidence, that a small, defined-stop pre-earnings-drift
    long (flattened before the 2026-07-23 print, no event-day exposure) retains
    a residual qualitative edge that bear and quant never directly rebutted -- bear''s
    Round 2 rebuttal was written against the bull''s original through-earnings trade,
    and quant explicitly declined to evaluate the drift-only proposal. The counter
    is that this edge is uncited drift data in a heavily-covered mega-cap, indistinguishable
    from noise, so the panel''s overall skepticism outweighs an unadjudicated thin
    claim. Post-mortem thread: if LMT exhibits measurable pre-earnings drift into
    2026-07-22 close, was the synthesizer''s rejection of the bull''s narrow drift
    trade too conservative?'
  last_updated: '2026-07-08T14:50:37Z'
---

## Scouted 2026-07-07T20:34:02Z

## Researched 2026-07-08T14:50:37Z — NO-TRADE

Three-round panel (bull/bear/quant, synthesized on opus) converged on NO-TRADE.
Reference price: LMT $375.30 @ 2026-07-08T14:50Z (stub deterministic provider).

Bull's opening thesis (a "reaffirm-or-raise" re-rating via a long $380/$395 call
debit spread targeting $390-400) collapsed once the equity-only sim constraint
removed the options instrument entirely; bull retracted the trade rather than
approximate it with naked equity, and pivoted instead to a small, pre-earnings-only
drift long that fully exits before the print. Confidence fell 58 -> 40.

Bear held that LMT is a heavily-covered (30+ analyst), low-realized-vol mega-cap
trading near highs on an already-priced two-year defense re-rating -- making
disappointment risk under-priced, not over-priced -- citing real precedent for
classified-program/Sikorsky margin charges and F-35 sustainment cost overruns.
Confidence rose 68 -> 78 once the options-hedge fallback was confirmed unavailable.

Quant's EV math anchored the panel: a base 25/35/25/15 scenario table nets to
-0.125% EV before costs; after the bear's fattened miss-tail (18% at -5.0%), the
naked-long EV worsens to -0.36% before costs / -0.44% after, while a naked short
is only marginally positive (+0.28% after costs) and sits on an uncapped tail
against the 24% beat-scenario bucket -- inside noise, not a tradable edge, and
unable to use the options hedge lesson 1 calls for. Confidence in NO-TRADE rose
30 -> 40.

Synthesis: stand aside end-to-end, including on the bull's narrow drift-only
fallback. Confidence in NO-TRADE: 72/100. Reconsideration trigger: a sourced,
non-consensus catalyst (F-35 lot-pricing news, program delay/cancellation report,
or budget-bill language) surfacing before 2026-07-22 close.
