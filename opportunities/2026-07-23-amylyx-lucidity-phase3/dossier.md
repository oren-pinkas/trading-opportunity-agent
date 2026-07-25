---
id: 2026-07-23-amylyx-lucidity-phase3
title: Amylyx LUCIDITY Phase 3 Readout Due Q3 2026
status: researched
created: '2026-07-23T04:24:42Z'
event:
  type: product
  summary: Amylyx's Phase 3 LUCIDITY trial of avexitide for post-bariatric hypoglycemia
    reads out in Q3 2026, a binary catalyst for the stock
  impact_window: '2026-09-30'
tickers:
- AMLX
sources:
- title: 10 clinical trials to watch in the second half of 2026 - BioPharma Dive
  url: https://www.biopharmadive.com/news/biotech-pharma-clinical-trials-watch-2026/808255/
  accessed_at: '2026-07-23T04:24:42Z'
hypothesis:
  statement: AMLX into the LUCIDITY Phase 3 PBH readout is a genuine binary with
    plausibly positive skew, but the panel cannot establish a priceable edge -
    P(success) is honestly 0.52-0.70, the magnitude assumptions are unanchored
    guesses (no options IV/skew, no analyst consensus, no short interest), and
    the "Q3 2026" catalyst date is trade-press inference rather than
    company-confirmed guidance. Expected value flips sign inside the panel's own
    confidence band, so the position is unpriceable, not merely risky.
  direction: none
  confidence: 72
plan:
  ticker: AMLX
  action: none
  entry: null
  exit: null
  expected_profit_pct: 0
  reasoning: No trade. Quant's EV calc (P(win) times magnitude(win) plus P(loss)
    times magnitude(loss)) is USD +6.5 percent gross at P=0.70 but swings to USD
    -1.1 percent at the revised P=0.62 and USD -3.7 percent at the low end of the
    0.52-0.70 band - the sign is not stable within the panel's own uncertainty.
    Reopen only if (a) Amylyx confirms an actual readout date via press
    release/8-K rather than a trade-press listicle, and (b) options IV/skew or
    analyst consensus data become available to anchor the assumed magnitude
    figures. With those two inputs, quant's fallback framing (a small ~2.5
    percent notional long in common shares, no options given IV-crush risk on a
    date slip) becomes defensible if EV stays positive at the low end of the
    revised P band.
research:
  strategy: debate-three-round-panel
  personas:
  - bull
  - bear
  - quant
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  dissent: 'Bull''s unresolved objection: base-rate pessimism plus the absence of
    market-pricing data (no IV/consensus/short interest) was treated by bear and
    quant as evidence against the trade, when it may simply be absence of
    evidence - in a first-in-class indication with no approved therapy, that
    data gap is itself part of the asymmetry. If LUCIDITY reads out clean and
    AMLX re-rates 50-150 percent, the post-mortem should ask whether "unpriceable"
    was rigor or a rule that systematically forfeits the only trades that pay for
    the portfolio. Secondary open item: quant''s own P(positive) moved from 0.70
    to 0.62 mid-debate under bear pressure alone, with no new external data -
    worth checking whether that revision was warranted or just deference.'
  last_updated: '2026-07-25T01:02:03Z'
---

## Scouted 2026-07-23T04:24:42Z

## Researched 2026-07-25T01:02:03Z

Three-round bull/bear/quant panel (debate-three-round-panel strategy) converged
on NO TRADE. See `transcript.md` for the full debate. Bear opened skeptical of
the "clean re-rating" bull case, citing Amylyx's 2024 Relyvrio (AMX0035)
confirmatory Phase 3 failure/withdrawal as a management-level prior on
endpoint/narrative risk, and noted nobody had actual options IV, analyst
consensus, or short-interest data to anchor what's priced in. Quant initially
modeled P(positive)=0.70 with a positive net EV, but revised down to P=0.62
(band 0.52-0.70) under bear's pressure - at which point the EV calculation's
sign became unstable across the panel's own confidence band, and quant
withdrew the proposed long. Bull conceded the "Q3 2026" date is trade-press
inference, not confirmed guidance, but did not fully concede the no-trade
verdict. Root cause: an unpriceable data gap (no confirmed catalyst date, no
market-implied pricing signal), not a settled bearish thesis - reopen once a
confirmed date and IV/consensus data exist.
