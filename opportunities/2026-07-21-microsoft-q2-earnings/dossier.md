---
id: 2026-07-21-microsoft-q2-earnings
title: Microsoft Q2 2026 earnings report
status: researched
created: '2026-07-21T15:25:19Z'
event:
  type: earnings
  summary: Microsoft reports Q2 2026 earnings July 29 2026 with focus on Azure AI
    capex and cloud growth
  impact_window: '2026-07-29'
tickers:
- MSFT
sources:
- title: Big Tech Q2 2026 earnings and the AI capex question - IG UK
  url: https://www.ig.com/uk/trading-strategies/big-tech-q2-2026-earnings---the-ai-capex-question-and-what-uk-in-260716
  accessed_at: '2026-07-21T15:25:19Z'
hypothesis:
  statement: MSFT enters its July 29 after-market-close print mid-range, down roughly
    17-18 percent from its January 2026 high of USD 473.91 to USD 390.70 as of July
    22, choppy between USD 384 and USD 402 for three weeks -- neither at a 52-week
    low nor a 52-week high, so neither institutional "priced-in" discount lesson
    applies cleanly. Street focus is Azure AI capex versus cloud growth. The one-day
    reaction distribution is assumed near-symmetric (48/45 to 52/55 up-down split,
    roughly plus/minus 5.5 percent, widened from a 4-5 percent mega-cap base rate
    for capex-scrutiny quarters) with a fatter adverse tail (capex-miss or margin-scare
    gap, roughly minus 9 to minus 10 percent) than the credible upside. No panelist
    produced a validated directional edge beyond that near-coin-flip split. A defined-risk
    call or put spread caps the loss shape but does not fix the sign of expected
    value -- event volatility is already priced into option premiums, so a near-50/50
    long-premium structure still runs roughly negative 0.5 percent to negative 1.5
    percent of premium, mirroring the roughly negative 0.5 percent to negative 0.6
    percent net EV on directional equity. Net EV in both instruments falls short
    of the roughly 2 percent bar and the adverse-tail-to-edge ratio (as high as 30x
    on naked equity) blows through the 7-8x no-trade threshold. There is no exploitable
    directional edge to be the numerator.
  direction: none
  confidence: 28
plan:
  ticker: MSFT
  action: no-trade
  entry:
    time: null
    target_price: null
    trigger: Monitor only; re-open if pre-print channel checks or capex commentary
      leak clearly firm or clearly soft ahead of July 29, or if the stock breaks
      and holds outside the USD 384-402 range pre-print in a way that shifts the
      distribution off coin-flip.
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
  dissent: 'Can a hard-capped, pre-known-max-loss debit spread on a genuine binary
    catalyst be defensible position-sizing under a ruin-avoidance objective even
    at slightly negative EV, rather than a strict EV-maximization no-trade? The
    bull staked the case on this framing after conceding no directional edge; the
    quant rebutted that capping the loss shape does not fix negative expectancy,
    since option premiums already embed the event vol. Unresolved because it turns
    on mandate/objective, not on the arithmetic itself -- worth checking post-print
    whether skipping this forwent a real realized gap.'
  confidence: 71
  last_updated: '2026-07-23T00:39:43Z'
---

## Scouted 2026-07-21T15:25:19Z

## Researched 2026-07-23T00:39:43Z

Three-round panel (bull/bear/quant, synthesizer opus) converged on **NO TRADE**.
MSFT sits mid-range (USD 390.70 as of 2026-07-22, down ~17-18% from its January
high, choppy USD 384-402 for three weeks) ahead of its 2026-07-29 AMC print, with
Street focus on Azure AI capex vs. cloud growth. No panelist produced a validated
directional edge beyond a near-coin-flip (48/52) reaction split; a defined-risk
options spread fixes the loss shape but not the negative expected value, since
event vol is already priced into premiums. Full transcript: `transcript.md`.
