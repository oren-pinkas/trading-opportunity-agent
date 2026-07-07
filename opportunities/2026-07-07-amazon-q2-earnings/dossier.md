---
id: 2026-07-07-amazon-q2-earnings
title: Amazon Q2 2026 earnings
created: '2026-07-07T19:30:32Z'
event:
  type: earnings
  summary: Amazon reports Jul 30; AWS growth and retail margins are the catalyst.
  impact_window: '2026-07-30'
tickers:
- AMZN
sources:
- title: Kiplinger earnings calendar
  url: https://www.kiplinger.com/investing/stocks/17494/next-week-earnings-calendar-stocks
  accessed_at: '2026-07-07T19:30:32Z'
hypothesis:
  statement: >-
    Vol-risk premium is the only quantified edge into the Jul 30 after-close print:
    realized move should undershoot the ~8.9% implied, with a marginal downside skew
    from the $200B 2026 capex / collapsed-FCF overhang. No directional conviction —
    directional EV ~0, failing the lesson-1 no-trade filter. The panel's positive-EV
    expression is a defined-risk iron condor (unrepresentable in a single-leg plan);
    the recorded short is a low-confidence directional proxy of that view.
  direction: short
  confidence: 48
plan:
  ticker: AMZN
  action: short
  entry:
    time: '2026-07-30T19:59:00Z'
    target_price: 211.0
  exit:
    time: '2026-07-31T19:59:00Z'
    target_price: 205.0
  expected_profit_pct: 2.5
research:
  strategy: three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  last_updated: '2026-07-07T21:42:23Z'
status: scheduled
---

## Scouted 2026-07-07T19:30:32Z

## Researched 2026-07-07T21:42:23Z

Three-round panel (bull/bear/quant). Consensus: **defined-risk short volatility**, not
direction. Only quantified edge is the vol-risk premium — realized moves undershoot
implied on AMZN prints (last print +0.76% vs 11.22% implied); Jul 30 prices ~8.9% weekly.
Directional EV ≈0 pre-cost / negative after (quant), fails lesson-1 filter. Bull's
long call spread rejected as long the mispriced vega. Marginal price skew is slightly
down (capex/FCF overhang, P(down)=53%), so the schema-forced single-leg proxy is a small,
low-conviction short. **Real recommendation = defined-risk iron condor (~$192/$230 shorts,
$183/$239 wings, ~+0.4% EV after costs)** — see transcript.md. Entry/exit set to
19:59:00Z inside session bars per lessons 3–4. Status → scheduled (plan times future).
