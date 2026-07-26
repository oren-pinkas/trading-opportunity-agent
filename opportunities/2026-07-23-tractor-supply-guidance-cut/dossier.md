---
id: 2026-07-23-tractor-supply-guidance-cut
title: Tractor Supply cuts 2026 comp-sales guidance, pulls long-term outlook
status: researched
created: '2026-07-23T22:07:07Z'
event:
  type: earnings
  summary: Tractor Supply cut FY2026 comparable sales guidance to flat-to-down 1%
    (from +1-3%) and withdrew its December 2024 long-term framework, citing a continued
    consumer pullback.
  impact_window: '2026-08-06'
tickers:
- TSCO
sources:
- title: "Tractor Supply Cuts Guidance, Withdraws Long-Term Outlook on Weaker Sales - Bloomberg"
  url: https://www.bloomberg.com/news/articles/2026-07-23/tractor-supply-cuts-outlook-as-shoppers-continue-pullback
  accessed_at: '2026-07-23T22:07:07Z'
hypothesis:
  statement: >-
    TSCO's FY2026 comp cut and withdrawal of the Dec 2024 long-term framework was
    absorbed without the base-rate gap down (7/23 pre-release USD 30.22 -> 7/24 close
    approximately USD 31.03, +2.7%), indicating the negative revision was largely
    discounted into a name already down from approximately USD 57 (Jul-2025) to
    approximately USD 31 over four quarters. Neither the "bad news, no downside" long
    nor the "credibility event" short survives cost and gap-risk adjustment, and an
    unhedged Q2 print inside the 2026-08-06 impact window dominates any residual edge.
  direction: none
  confidence: 62
plan:
  ticker: TSCO
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
    Bull's unresolved claim: the de-risked guide creates genuine asymmetry -
    management has "kitchen-sinked" FY2026, so an in-line-or-better Q2 print on
    2026-08-06 is more likely than not, and near-zero modeled EV understates a
    right-skewed payoff. Quant's counter: the EV model already prices that scenario
    and the earnings-gap tail still swamps it. Unresolved because the panel had no
    options-implied-move data to test whether a defined-risk call spread is cheap
    enough to flip the sign of EV. Score this NO-TRADE against what the 8/6 print
    actually does: an in-line-or-better beat with a positive reaction favors the
    bull's asymmetry read; a fresh miss or second guidance cut favors the quant's
    "no edge, don't hold through the binary" read.
  last_updated: '2026-07-26T02:54:51Z'
---

## Scouted 2026-07-23T22:07:07Z

## Researched 2026-07-26T02:54:51Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), run in isolation on
this opportunity only. Core finding: TSCO's after-hours comp-guidance cut and long-term
framework withdrawal (2026-07-23) did not produce the -9% to -12% base-rate gap typical
of a dual-negative retail disclosure - price went from USD 30.22 (pre-release close) to
approximately USD 31.03 (next full session close), a +2.7% move, the highest close of
the month. All three personas independently converged, after rebuttal, on "no
directional edge net of costs": quant's EV came out to +0.15% long / -0.55% short, both
inside the noise band, with an unhedged Q2-earnings-gap tail (likely inside the
2026-08-06 impact window) carrying an adverse-tail-to-edge ratio above 50x. Bear raised
a data-integrity concern (TSCO's real historical range is USD 50-60, not USD 30) that
the orchestrator resolved independently by pulling further-back bars (2025-07-15 approx.
USD 57.35, 2026-01-15 approx. USD 50.77, 2026-07-24 approx. USD 31.03) - a continuous
declining series, confirming the ticker and price level are legitimate, not a data
artifact. Per prior lessons (DAL, LEVI): when the most rigorous quantitative read is
~0 EV and the strongest dissent aligns with it, synthesize to NO-TRADE rather than a
token position. Revisit only on a decisive break below the pre-news reference of
USD 29.36, or after the 2026-08-06 Q2 print resolves the bull/quant asymmetry dissent.
