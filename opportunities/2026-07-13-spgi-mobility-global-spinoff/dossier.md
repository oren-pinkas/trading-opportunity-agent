---
id: 2026-07-13-spgi-mobility-global-spinoff
title: S&P Global's Mobility Global begins standalone NYSE trading
status: researched
created: '2026-07-13T16:16:37Z'
event:
  type: economic
  summary: S&P Global completed the spin-off of its Mobility division into independent
    NYSE-listed Mobility Global (MBGL), leaving SPGI to re-rate as a leaner ratings/data
    business.
  impact_window: '2026-07-31'
tickers:
- SPGI
sources:
- title: S&P Global Completes Mobility Spin-Off
  url: https://intellectia.ai/news/etf/sp-global-completes-mobility-spinoff
  accessed_at: '2026-07-13T16:16:37Z'
hypothesis:
  statement: The Mobility spin-off is a completed, already-priced catalyst (distribution
    closed 2026-07-01, record date 2026-06-15) - SPGI has been flat (roughly -0.3
    percent) for about 12 sessions since going ex-Mobility, leaving no differentiated
    edge before the 2026-07-31 window closes. The anchor price of USD 438.42 already
    sits an estimated 12-14 percent above the pre-spin sum-of-parts stub fair value
    (USD 385-393), sell-side price-target cuts (Goldman, Baird) have compressed the
    remaining upside tail even as ratings held Buy, and the lone live catalyst in
    the window - Q2 earnings and the first standalone guide on 2026-07-28 - is a
    near-symmetric event whose probability-weighted EV does not clear execution
    and variance costs.
  direction: no_trade
  confidence: 74
plan:
  ticker: SPGI
  action: no_trade
  entry: null
  exit: null
  expected_profit_pct: -0.3
  note: No long - the "re-rating still in progress" leg of the bull case did not
    survive rebuttal (12 trading days flat is digestion, not momentum), and the
    bull's own sum-of-parts stub math implies price already sits above modeled
    fair value, cutting against further catch-up inside a 17-session window. No
    short either - despite price-target cuts, every covering analyst's target
    (Goldman USD 490, JPM USD 535, Baird USD 520) remains above the USD 438.42
    spot, so cuts compress upside rather than signal a sell; the quant's
    probability-weighted EV moved from +0.40 percent to roughly -0.3 percent net
    of costs once the bull's best evidence was absorbed, which is a reason to
    skip, not to reverse and short. Nothing tradeable until the 2026-07-28
    standalone guide resolves the open question.
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
  dissent: 'Bull argues the 2026-07-28 print is not a coin-flip EPS variable but
    the first clean standalone guide (margin framework, capital-return/buyback
    plans) carrying independent re-rating power that the quant''s 40 percent-weighted
    "flat" scenario underprices. Bear and the quant treat that same guidance event
    as already discounted, folding it into a near-zero/negative-skew EV. This is
    unresolved and load-bearing: if the standalone guide surprises to the upside,
    the panel''s no_trade call is wrong in the bullish direction. Secondary
    unresolved item: an unreconciled price-anchor discrepancy across personas
    (an unconfirmed USD 447 intraday peak / USD 430.50 swing cited by the bear
    versus the flat USD 438-440 closes the others cite), which prevents fully
    verifying pre-event drift.'
  lessons_applied:
  - 2026-07-01-ism-mfg
  - 2026-07-02-june-jobs
  last_updated: '2026-07-14T05:12:26Z'
---

## Scouted 2026-07-13T16:16:37Z

## Researched 2026-07-14T05:12:26Z

Three-round panel debate (bull/bear/quant) concluded **no_trade** at 74/100
confidence. The spin-off catalyst (completed 2026-07-01) is stale by the time
of this research - SPGI has traded flat for ~12 sessions since, already sitting
above its own pre-spin sum-of-parts stub fair value, and sell-side price-target
cuts have compressed rather than reversed the remaining upside. Both bear and
quant independently converged on skip and raised confidence after rebuttal (75,
76); the quant's own EV estimate flipped from +0.40 percent to roughly -0.3
percent net of costs once it absorbed the bull's best evidence. The bull
conceded the "re-rating still in progress" thesis and retreated to a much
smaller, hedged structure at 55/100. The open, unresolved question - whether
the 2026-07-28 standalone guide re-rates the multiple independent of the EPS
print - is preserved as dissent for a future post-mortem rather than resolved
away. Full transcript: `transcript.md`.
