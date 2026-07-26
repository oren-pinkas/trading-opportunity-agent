---
id: 2026-07-23-tvardi-tti101-hcc-data
title: Tvardi Therapeutics TTI-101 HCC topline data due 2H 2026
status: researched
created: '2026-07-23T00:14:58Z'
event:
  type: regulatory
  summary: Tvardi's Phase 1b/2 REVERT LIVER CANCER trial of TTI-101 in hepatocellular
    carcinoma remains on track for topline data in 2H 2026, a binary readout for a
    clinical-stage STAT3 inhibitor
  impact_window: '2026-09-30'
tickers:
- TVRD
sources:
- title: Tvardi Therapeutics Q1 2026 Results and Business Update
  url: https://ir.tvarditherapeutics.com/news-releases/news-release-details/tvardi-therapeutics-announces-first-quarter-2026-results-and
  accessed_at: '2026-07-23T00:14:58Z'
hypothesis:
  statement: >-
    TVRD offers no exploitable edge into its TTI-101 HCC Phase 1b/2 readout. The
    catalyst is not date-certain ("2H 2026" is company PR language; the dossier's
    2026-09-30 impact_window is an assumption, not a scheduled event), so the
    probability the print even lands inside the trade window is low (~0.28). The
    bull's original entry rationale, a pre-catalyst anticipation runup, is
    empirically falsified: verified twelvedata prints show USD 3.275 (07-10) to
    USD 2.515 (07-24), roughly -23% over 11 sessions, against XBI -5.3% over the
    same window, leaving roughly -13 points of idiosyncratic, name-specific
    decline that sector beta cannot explain. The market has had the STAT3/HCC
    thesis available throughout that decline and sold into it, so "unpriced
    optionality" is not supported. Long-side EV is negative (roughly -13.5% gross,
    -16% net) and stays negative (roughly -6% to -10% gross) even zeroing out
    dilution risk entirely. The mirror-image short shows only a nominal +8% net
    EV, fails a robustness floor (signal-to-noise ~0.21 collapses under small
    perturbations of raise-probability and drift assumptions), depends most on
    the single weakest unverified input, and carries an un-hedgeable
    positive-readout gap tail. Execution is separately impaired: sampled live
    minute-bar coverage on TVRD is only about 42%, making any intraday
    "harvest strength" exit structurally unexecutable.
  direction: none
  confidence: 85
plan:
  ticker: TVRD
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
    Does the roughly -13-point idiosyncratic decline make the setup worse or
    better? All three personas treated the bleed as bearish information, but
    nobody resolved the mechanism, and the mechanism flips the sign. If it is
    the market front-running a dilutive financing or leaking a negative read on
    the program, the decline is informative and NO-TRADE is right for the
    stated reason. If it is indiscriminate microcap tax-loss or liquidity
    bleed, a fixed-absolute-value binary catalyst just got cheaper and the
    long's convexity is rising as price falls; the quant steelmanned this read
    but refuted it only with relative-strength evidence (XBI comparison),
    which shows the decline is name-specific, not that it is
    outcome-predictive. The one fact that would arbitrate, an actual
    cash-and-burn figure from filings establishing whether runway extends past
    the readout, was never sourced by any persona. Testable post-mortem: pull
    TVRD's cash/burn and any financing announced between 2026-07-24 and the
    actual readout date. If a raise came, the consensus was right for the
    right reason; if runway was already funded past the catalyst and the stock
    re-rated on the print, this was a correctly-reasoned NO-TRADE reached on an
    unverified premise.
  last_updated: '2026-07-26T03:16:07Z'
---

## Scouted 2026-07-23T00:14:58Z

## Researched 2026-07-26T03:16:07Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). The bull opened
long on STAT3/HCC catalyst optionality near cash value, planning to harvest a
pre-catalyst momentum runup. Verified twelvedata price history falsified that
premise outright: TVRD printed USD 3.275 (07-10) down to USD 2.515 (07-24), a
steady ~23% decline over 11 sessions with no offsetting news, and no
anticipation buildup. The quant's EV calc put long-side EV at roughly -16% net;
the mirror-image short showed a nominal +8% net EV but failed a robustness
check (signal-to-noise ~0.21 versus a 0.15 floor) and carries an un-hedgeable
gap-up tail on a positive readout. In round 2 the quant tested the bull's
strongest possible counter (falling price = cheaper option on a fixed target)
against XBI as a sector benchmark and refuted it: TVRD -23% vs XBI -5.3%
confirms the decline is idiosyncratic, not sector noise. Live minute-bar
coverage on TVRD sampled at only ~42%, making the bull's intraday exit plan
unexecutable regardless. The bull conceded the momentum thesis and downgraded
to no entry today. Verdict: NO-TRADE, confidence 85. Flips only on price
stabilization plus either a company-confirmed readout date or a verified cash
runway past the catalyst. Full debate with citations in `transcript.md`.
