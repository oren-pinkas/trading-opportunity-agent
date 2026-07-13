---
id: 2026-07-12-nucor-q2-earnings
title: Nucor Q2 2026 earnings vs raised steel-pricing guidance
status: researched
created: '2026-07-12T18:06:04Z'
event:
  type: earnings
  summary: Nucor reports Q2 2026 earnings July 27 after guiding EPS to $4.70-$4.80,
    above prior estimates, on stronger steel pricing.
  impact_window: '2026-07-27'
tickers:
- NUE
sources:
- title: Nucor guides Q2 2026 earnings to $4.70-$4.80 per diluted share
  url: https://www.streetinsider.com/Corporate+News/Nucor+guides+Q2+2026+earnings+to+$4.70-$4.80+per+diluted+share/26660452.html
  accessed_at: '2026-07-12T18:06:04Z'
hypothesis:
  statement: Nucor's 2026-07-12 pre-announcement of Q2 EPS at $4.70-$4.80 is a routine
    guide issued ~2 weeks ahead of the 2026-07-27 print. The raise is therefore stale/priced-in
    information by the print date, and no panelist identified a verifiable, positive-expectancy
    directional edge into the report. The quant's EV calc stayed negative (-0.45%
    net in Round 1, -0.36% net after rebuttals), and both Bull (55->48) and Bear (60->63
    that bull is wrong) converged toward standing aside from divergent starting priors.
    No live market data was available in any panelist's sandbox to overturn this.
  direction: none
  confidence: 66
plan:
  ticker: NUE
  action: no-trade
  reasoning: 'EV stayed negative through both debate rounds despite input revisions
    in both directions; three panelists with different starting priors converged on
    NO TRADE; institutional lessons #6 (strongest unrebutted dissent aligns with quant''s
    own EV math -> synthesize to NO-TRADE) and #7 (highest-confidence panelist reports
    EV~0/negative -> log NO TRADE, don''t manufacture a token position) both apply
    directly. No live price/IV/HRC data was available to overturn the negative-EV
    finding.'
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
  dissent: 'Sharpest unresolved disagreement is right-tail asymmetry vs. sell-the-news
    fade. Bull argues non-EPS catalysts (buyback, capital allocation, forward-guidance
    tone) can fatten the right tail without symmetrically fattening the left, which
    a call spread could monetize. Quant/Bear counter that any pre-print drift will
    have already occurred by 2026-07-27 (converting Bull''s drift edge into added
    fade risk), and that a past-quarter EPS raise says nothing about the Q3 spot HRC
    trajectory the stock actually needs to re-rate further. Post-mortem trigger: on
    2026-07-27, check whether NUE''s realized print-day move showed right-tail convexity
    from forward guidance (validating Bull) or a symmetric/negative fade (validating
    Quant/Bear); log HRC price trend since 2026-07-12 as the deciding covariate.'
  last_updated: '2026-07-13T04:30:05Z'
---

## Scouted 2026-07-12T18:06:04Z

## Researched 2026-07-13T04:30:05Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), run in isolation on this single opportunity. All three panelists lacked live market-data access in their sandboxes and flagged every number as an assumption; a simulation price-stub showed NUE at $363.17 (source: stub:deterministic, not a real quote). BULL opened long (conf 55) on the pre-announcement-as-catalyst + tariff/demand tailwind thesis, but conceded in rebuttal that pre-print drift (if real) would already be baked in by the print date, cutting confidence to 48 and making any call-spread entry strictly conditional on live verification. BEAR opened at conf 60 that the raise is already priced in ('buy the rumor, sell the news'), citing margin/cost-offset and HRC-reversal risk; held at 63 after rebuttal, open to a small put-spread hedge only. QUANT modeled P(up)~0.49-0.50 vs P(down)~0.50-0.51 with a sell-the-news downside skew, computing EV = -0.45% net (Round 1) and -0.36% net (Round 2 after incorporating both sides' strongest points) — negative in both rounds. Applying institutional lessons #6 and #7 (do not manufacture a minimal directional position when the quant's own EV math says no edge and the strongest dissent supports it), the synthesizer converged on NO TRADE, confidence 66 that no positive directional edge exists. Full debate with citations in `transcript.md`.
