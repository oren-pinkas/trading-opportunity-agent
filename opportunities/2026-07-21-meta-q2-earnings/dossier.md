---
id: 2026-07-21-meta-q2-earnings
title: Meta Platforms Q2 2026 earnings report
status: researched
created: '2026-07-21T15:25:19Z'
event:
  type: earnings
  summary: Meta reports Q2 2026 results after market close July 29 2026 amid scrutiny
    of AI infrastructure spending
  impact_window: '2026-07-29'
tickers:
- META
sources:
- title: Meta Sets Q2 2026 Earnings Release for July 29 - StockTitan
  url: https://www.stocktitan.net/news/META/meta-to-announce-second-quarter-2026-sdasry9e3xzw.html
  accessed_at: '2026-07-21T15:25:19Z'
hypothesis:
  statement: META enters its July 29 post-close print in the mid-upper third of
    its 12-month range (~USD 644-648, ~14-19 percent off highs), not oversold, with
    Street set near top-of-guidance capex (~USD 139B) -- i.e. neither priced-for-perfection
    nor beaten-down. The one-day reaction distribution is wide (3-12 percent band,
    fat tails both sides) with a directional split (~55/45 up) that sits inside the
    confidence interval of a coin flip given small n. Critically, the disappointment
    tail is fatter in magnitude than the benign upside (the May 2026 -8.55 percent
    capex-shock precedent, quantified), so a long carries negative expected value;
    a short carries an un-hedgeable catastrophic up-tail. No pre-print public proxy
    exists to independently verify the AI-capex ROI thesis before the print, so the
    one signal that could create edge is unavailable on this timeline. A defined-risk
    wrapper (call or put debit spread) fixes the risk leg but not the edge leg --
    EV on both spreads runs roughly -1 percent to +1 percent of debit, short of the
    ~2 percent net-EV bar and the 7-8x adverse-tail-to-edge threshold. There is no
    exploitable directional edge to be the numerator.
  direction: no-trade
  confidence: 68
plan:
  ticker: META
  action: no-trade
  entry:
    time: null
    target_price: null
    trigger: Monitor only; re-open if a verifiable pre-print proxy for ad-pricing/impression
      growth or Advantage+ adoption surfaces clearly firm or clearly soft in the
      days before July 29 (the bull/bear dissent below), or if META sells off toward
      the USD 600-613 range pre-print such that a short-premium structure (credit
      spread/iron condor) could capture the vol-risk premium instead of paying it.
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
  dissent: 'Is the AI-capex ROI reaction independently checkable BEFORE the print,
    or only readable DURING it? The bull staked the entire path-to-edge on pre-print
    channel checks (ad-pricing/impression/Advantage+ adoption) being a hard gate
    that could flip 55/45 into a real signal. The bear directly rebutted that no
    public proxy exists before the July 29 close -- that the Wolfe/Wedbush capex-risk
    flags exist precisely because ROI is not independently verifiable yet -- reframing
    the same metrics as during-print-only. The quant sided with directional edge
    near zero partly because it treated no usable pre-print signal as available.
    If the bull is right that a verifiable pre-print signal exists and reads clearly,
    the zero-edge premise collapses and a small defined-risk long (call debit spread)
    becomes defensible -- turning this into a too-conservative NO TRADE rather than
    a disciplined one. Post-mortem should check empirically whether any credible
    pre-print proxy for META ad-pricing/impression trend appeared in the ~8 days
    before July 29, 2026, and whether it had predictive content for the actual reaction.'
  last_updated: '2026-07-23T00:30:03Z'
---

## Scouted 2026-07-21T15:25:19Z

## Researched 2026-07-23T00:30:03Z

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). META trades
mid-upper range (~USD 644-648), not near its 52-week low or high -- neither
priced-for-perfection nor beaten-down. Bull opened long (confidence 52, defined-risk
call debit spread) on the AI-capex-ROI-flip narrative; bear opened skeptical
(confidence 38, defined-risk put spread at most) citing the May 2026 -8.55 percent
capex-shock precedent as a direct comp; quant opened NO TRADE (confidence 32) with
an explicit EV calc showing both long and short carry negative expected value after
frictions. Round 2 converged: both bull and quant revised down (52 to 47, 32 to 30)
after the quant showed that capping the tail with a defined-risk spread fixes the
risk leg of the no-trade filter but not the edge leg -- EV on either spread lands
roughly -1 percent to +1 percent of debit, short of the ~2 percent bar. Bear held
near its opening view (38 to 34). Synthesized to NO TRADE (confidence 68 in the
no-trade call itself). Full debate with citations in `transcript.md`.
