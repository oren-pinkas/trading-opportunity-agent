---
id: 2026-07-16-bloom-energy-scandium-short-report
title: Bloom Energy disputes Hunterbrook short report ahead of Q2 earnings
status: researched
created: '2026-07-16T07:53:17Z'
event:
  type: economic
  summary: Hunterbrook Media alleged Bloom Energy is dependent on Chinese scandium
    supply and can't realistically scale to 5GW annual output; Bloom denies the claims,
    with Q2 earnings on July 28, 2026 the next test of the narrative.
  impact_window: '2026-07-28'
tickers:
- BE
sources:
- title: Bloom Energy Stock in the Spotlight After a Week of Short-Seller Reports
  url: https://www.benzinga.com/trading-ideas/movers/26/07/60413546/bloom-energy-stock-in-the-spotlight-after-a-week-of-short-seller-reports-analyst-commentary
  accessed_at: '2026-07-16T07:53:17Z'
hypothesis:
  statement: BE's Q2 print on 2026-07-28 collides with an unresolved, structural
    short-seller dispute (China scandium dependency, 5GW scaling doubt) that a single
    quarter cannot confirm or refute; the setup is a wide-variance binary with no
    differentiated directional edge, and expected value net of vol crush, spread,
    and slippage is negative for any committed directional or premium-buying
    position.
  direction: none
  confidence: 26
plan:
  ticker: BE
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
  dissent: "The unresolved core disagreement is whether BE's public denial carries
    directional information. The bull holds that a costly, specific, falsifiable
    denial (named supply chain, named capacity number) skews probability modestly
    above 45 percent up. The quant counters that denials are near-universal (base
    rate of firms denying credible short reports approaching 100 percent), so the
    probability of vindication given a denial collapses to the unconditional base
    rate and the denial's signal value is near zero. This was never reconciled -
    it is the fault line a post-mortem should test: did the specificity of the
    denial in fact predict the post-earnings direction, or did it prove
    informationally worthless as the quant argued."
  last_updated: '2026-07-22T08:20:00Z'
---

## Scouted 2026-07-16T07:53:17Z

## Researched 2026-07-22T08:20:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). BE trades around
USD 225.70 as of 2026-07-21T19:55Z, one week into the Hunterbrook short-report
dispute (China scandium supply dependency, doubts on scaling to 5GW annual output),
with Q2 earnings on 2026-07-28 the next hard catalyst. The BULL argued the public
denial is a soft tell and proposed a size-reduced call spread into the print; the
BEAR argued the dispute is structural and cannot be confirmed or refuted by a single
quarter, and that the week-old coverage has already priced most of the directional
edge. The QUANT's EV math was decisive both rounds: assumed ~13-15% implied
post-earnings move, no differentiated directional edge (45/45/10 split), so any
directional bet or long straddle is negative EV after costs and crush, and a short
straddle carries an un-sizeable vindication-or-indictment tail. Confidence set
moderate-low (26, direction "none") because the debate converged cleanly on skip but
the denial-as-signal question was never resolved between bull and quant. Verdict:
NO-TRADE (not scheduled, not simulated), with a single contingent watch: fade a
post-print overshoot beyond ~1.5x the implied move if the tape reverses. Full debate
with citations in `transcript.md`.
