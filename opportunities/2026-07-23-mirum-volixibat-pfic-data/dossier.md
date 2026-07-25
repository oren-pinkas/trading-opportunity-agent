---
id: 2026-07-23-mirum-volixibat-pfic-data
title: Mirum Pharmaceuticals volixibat PFIC data readout
status: researched
created: '2026-07-23T21:02:37Z'
event:
  type: regulatory
  summary: Mirum's volixibat Phase 3 data in PFIC (rare cholestatic liver disease)
    could add a second commercial asset alongside Livmarli, expanding its pediatric
    rare-liver franchise
  impact_window: '2026-08-15'
tickers:
- MIRM
sources:
- title: 10 clinical trials to watch in the second half of 2026 - BioPharma Dive
  url: https://www.biopharmadive.com/news/biotech-pharma-clinical-trials-watch-2026/808255/
  accessed_at: '2026-07-23T21:02:37Z'
hypothesis:
  statement: >-
    The dossier's core premise (a volixibat Phase 3 PFIC readout at MIRM landing
    2026-08-15) is unconfirmed and probably a scout-time data-integrity defect --
    the quant's recollection is that volixibat's disclosed late-stage programs are
    PSC (VISTAS) and PBC (VANTAGE), with PFIC/Alagille being Livmarli's indication,
    not volixibat's (confidence the dossier's drug-indication pairing is correct as
    written is only ~40%). Independently of that, the stated date is soft (sourced
    from a "10 trials to watch in 2H 2026" trade-press listicle, not company IR,
    SEC filing, or ClinicalTrials.gov) and 2026-08-15 is a Saturday, not a trading
    session, implying roughly an 18% chance any real catalyst even lands in a
    tradeable window. Even granting the bull's mechanistic de-risking argument in
    full (IBAT-class precedent via Bylvay/Livmarli, existing commercial franchise),
    the payoff shape of a directional pre-readout long is negative-EV under
    generous assumptions (clean win +12% p=.45, mixed +0.5% p=.25, clean miss -18%
    p=.30 => EV_net ~ -0.28% conditional on the event occurring, ~ -0.38%
    unconditional after the date-risk discount; breakeven requires an undefended
    p(win) > ~0.52-0.58). Signal-to-noise (0.002-0.011) sits one to two orders of
    magnitude below the ~0.15 durability floor, and the dossier contains zero
    efficacy, safety, DSMB, or consensus-PoS data to supply an edge.
  direction: none
  confidence: 18
plan:
  ticker: MIRM
  action: no-trade
  entry:
    time: '2026-08-14T13:30:00Z'
    target_price: null
  exit:
    time: '2026-08-17T20:00:00Z'
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
    Should a dossier whose core event may not exist as stated be excluded from the
    active plan outright (bear's Round 2 escalation), or kept as a low-priority,
    confidence-capped watch item pending a primary-source fact-check (quant's
    preference, arguing the PASS already stands on payoff shape alone and the
    factual question is separable bookkeeping)? The synthesis sided with bear on
    disposition (no position, effectively shelved) but with quant on bookkeeping
    (log the drug/indication mismatch separately rather than folding it into the
    EV math). Secondary dissent: the bull conceded on every axis by Round 2 without
    ever producing a counter-model or a defended p(win) estimate, so the panel's
    convergence may be softer than its stated 82% confidence in the PASS verdict --
    the strongest possible long case (e.g. options-implied-move underpricing of
    realized readout moves, thin-float squeeze mechanics) was never actually
    argued. Testable post-mortem: if a real MIRM binary print occurs near the
    window and moves >20%, ask whether a long-volatility (non-directional)
    structure would have been profitable even though the directional long was
    correctly rejected.
  last_updated: '2026-07-25T17:30:06Z'
---

## Scouted 2026-07-23T21:02:37Z

## Researched 2026-07-25T17:30:06Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). PASS is
over-determined: it holds independently on (1) negative EV under the panel's own
generous outcome distribution, (2) SNR far below the durability floor, (3) a soft,
non-primary-sourced date that falls on a Saturday (not a trading session), and (4)
a live, unresolved possibility that the dossier's drug/indication pairing itself is
wrong (volixibat is PSC/PBC in the panel's recollection, not PFIC -- PFIC/Alagille
is Livmarli's indication). No position taken, long or short. Flags for scout-news:
possible data-integrity defect pairing the wrong asset with the wrong indication,
and a non-trading-session impact date that should have been caught by a calendar
validity check. Re-debate only if ALL of: (a) primary-source (IR/SEC/CT.gov)
confirmation of the drug, indication, and trial identity, (b) a confirmed readout
date on a real trading session, (c) a working, liquidity-gated price provider for
MIRM (twelvedata hit a global HTTP 429 this round; price unverified), and (d) an
options chain showing implied move underpricing realized readout moves -- which
would point to a long-volatility structure, not a directional bet. Full debate with
citations in `transcript.md`.
