---
id: 2026-07-16-eli-lilly-q2-earnings
title: Eli Lilly Q2 2026 earnings
status: researched
created: '2026-07-16T05:04:39Z'
event:
  type: earnings
  summary: Lilly reports Q2 2026 results Aug 5, first full quarter since Medicare
    GLP-1 weight-loss coverage began Jul 1 and amid oral-obesity-drug race with Novo
    Nordisk
  impact_window: '2026-08-05'
tickers:
- LLY
sources:
- title: Novo Nordisk, Eli Lilly roll out obesity pills, prepare for Medicare coverage
  url: https://www.cnbc.com/2026/06/08/novo-nordisk-eli-lilly-obesity-pills-medicare-coverage.html
  accessed_at: '2026-07-16T05:04:39Z'
hypothesis:
  statement: LLY's Q2 2026 print (reported 2026-08-05) is a commentary/forward-guidance
    event, not a results event - the reported quarter (Apr-Jun) closed 2026-06-30,
    one day before Medicare Part D GLP-1 coverage began 2026-07-01, so it contains
    zero Medicare GLP-1 revenue. The only genuinely unpriced element is early "coverage-is-working"
    color (35 days of prior-authorization/utilization/enrollment data, Q3 guidance
    cadence, orforglipron regulatory-timeline language). That edge is real but soft,
    un-quantified, and too small to overcome option-vol arithmetic - implied approximately
    7 percent vs. realized approximately 6-8 percent yields a blended net EV of roughly
    -0.5 percent across the panel's own probability-weighted scenarios.
  direction: none
  confidence: 40
plan:
  ticker: LLY
  action: no-trade
  entry: null
  exit: null
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
  dissent: 'The sharpest unresolved disagreement is instrument-vs-catalyst. The bull
    argues the "coverage-is-working" early-rollout signal is genuinely unpriced and
    modestly positive-skewed (approximately 55/45) because management has a track
    record of not self-inflicting bad news on a tailwind it lobbied for, and the
    bad-news case is already consensus. Quant partially concedes the bull "identified
    the right catalyst" but insists the bull chose the wrong instrument - if the
    thesis is fatter-tailed variance, a long straddle dominates a capped call spread,
    yet that straddle only pays in the approximately 25 percent implied-7/realized-8
    world, which quant cannot distinguish from noise. Neither side resolved whether
    the bull''s directional skew is real signal or hindsight-flavored narrative.
    If LLY prints a large directional move on 2026-08-05, the post-mortem should
    ask: was no-trade correct on EV (a straddle would have won but was un-forecastable
    ex-ante), or did the panel under-weight a genuinely knowable management-guidance
    skew that a call spread would have captured? Re-open conditions: implied compresses
    to <=5 percent while realized estimate holds >=6.5 percent; confirmed put/call
    skew mispricing or elevated call open-interest signaling stretched positioning;
    a pre-earnings CMS/IRA pricing or Novo oral-semaglutide news catalyst.'
  last_updated: '2026-07-22T09:57:08Z'
---

## Scouted 2026-07-16T05:04:39Z

## Researched 2026-07-22T09:57:08Z — NO-TRADE

Research debate (three-round-panel, bull/bear sonnet, quant/synthesizer opus).
Round 1: bull framed the print as a structural TAM-expansion event on the Medicare
Part D GLP-1 coverage start (2026-07-01) plus oral-obesity-drug (orforglipron)
commentary vs. Novo Nordisk, proposing a defined-risk call spread (confidence 58).
Bear argued the Medicare coverage story was telegraphed months in advance and
already embedded in sell-side models, citing rollout-friction, CMS/IRA pricing,
and orforglipron regulatory risk, favoring NO TRADE or a small put spread
(confidence 35). Quant's decisive Round 1 point: Q2 (Apr-Jun) ends 2026-06-30,
before Medicare coverage began 2026-07-01, so the reported quarter has zero
Medicare revenue - this is a guidance/commentary event, not a results event.
Quant's EV math (implied ~7% vs. realized ~6%) showed straddles/calls/call-spreads
all break even or negative after slippage, with a 5-7x adverse-tail-to-edge ratio
(confidence 40).

Round 2: bull conceded the zero-Medicare-revenue point, downgraded the thesis to
a "first-look forward-guidance event," and estimated a soft 55/45 directional skew
(confidence 58 -> 48). Bear agreed the same fact strengthens the priced-in/sell-the-news
case and conceded its put-spread carve-out lacked skew evidence, converging toward
NO TRADE (confidence 35 -> 25). Quant re-centered realized move up to 7-8% to honor
the bull's variance-widening argument, ran three probability-weighted EV scenarios
(35/40/25 weights), and still landed at a blended net EV of approximately -0.5%,
noting the bull's fat-tail argument actually favors a long straddle over the bull's
own capped call spread (confidence 40 -> 42).

Round 3 (synthesis, opus): converged on NO TRADE. All three institutional no-trade
conditions held - sub-45 risk-weighted confidence, negative-to-zero net EV after
costs, and an un-hedgeable positive tail that only pays in the least-likely,
noise-indistinguishable scenario. Full transcript with citations in transcript.md.
