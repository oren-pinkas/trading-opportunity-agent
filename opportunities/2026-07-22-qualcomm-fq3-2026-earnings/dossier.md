---
id: 2026-07-22-qualcomm-fq3-2026-earnings
title: Qualcomm fiscal Q3 2026 earnings
status: researched
created: '2026-07-22T10:15:35Z'
event:
  type: earnings
  summary: Qualcomm reports fiscal Q3 2026 results Jul 29 after close
  impact_window: '2026-07-29'
tickers:
- QCOM
sources:
- title: Qualcomm Schedules Third Quarter Fiscal 2026 Earnings Release and Conference
    Call
  url: https://www.qualcomm.com/news/releases/2026/07/qualcomm-schedules-third-quarter-fiscal-2026-earnings-release-a
  accessed_at: '2026-07-22T10:15:35Z'
hypothesis:
  statement: No verifiable directional or volatility edge exists for the QCOM FQ3
    2026 print. The panel has only a scheduled date and a "USD 170.90" reference
    close (2026-07-23T19:59Z) -- no consensus estimates, no options chain or IV/skew,
    no historical earnings-move distribution, and no current China handset or
    Apple-modem-transition status. Bull's diversification thesis (auto/IoT, premium
    Android, QTL licensing floor) and Bear's structural Apple in-sourcing risk are
    each directionally credible but oppose one another at similar, unquantified
    conviction, netting to no directional signal. Every proposed options structure
    is a long-premium bet against a systematic pre-earnings vol-crush edge and
    cannot be shown positive-EV without the missing chain data; defined-risk caps
    the loss but does not flip the sign of a negative-EV trade.
  direction: no_trade
  confidence: 82
plan:
  ticker: QCOM
  action: no_trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
  notes: Record-only synthesis; no capital deployed. Bull opened long (40) via a
    call debit spread but retreated to confidence 25 after conceding a defined-risk
    structure is not the same as a positive-EV one without IV/skew data. Bear opened
    a small OTM put tail hedge (35) against Apple modem in-sourcing risk but likewise
    retreated toward NO TRADE after conceding the hedge could just be overpaying
    into rich pre-earnings vol. Quant held NO TRADE throughout (78, then 80) on
    base-rate EV grounds -- no data, no edge, and the two opposing fundamental
    theses net to zero signal.
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
  dissent: 'The options may be underpricing the event (implied move < historical
    realized move). If so, Bull''s call debit spread would be genuinely positive-EV
    and NO TRADE would be a missed opportunity rather than correct discipline.
    Unresolved because the options chain, IV, and QCOM''s own historical
    earnings-move distribution were never available to the panel. Post-mortem
    action: pull QCOM implied-vs-realized earnings-move history and pre-print
    IV/skew; if implied consistently underprices realized, the no-trade filter
    needs a carve-out to check implied-vs-realized before defaulting to NO TRADE
    on defined-risk long-premium setups.'
  last_updated: '2026-07-24T01:20:00Z'
---

## Scouted 2026-07-22T10:15:35Z

## Researched 2026-07-24T01:20:00Z

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Real reference
price "USD 170.90" at 2026-07-23T19:59Z (twelvedata), not a stub. Panel converged
on NO TRADE (confidence 82): Bull opened long (40) on a diversification/licensing
thesis via a call debit spread, but retreated to 25 after conceding "defined-risk"
does not mean "positive-EV" absent IV/skew data. Bear opened a small OTM put tail
hedge (35) against Apple modem in-sourcing risk, but likewise retreated toward
NO TRADE after conceding the hedge could be overpaying into a vol crush. Quant
held NO TRADE throughout (78, then 80): only a date and a reference price were
available, no options chain, no consensus estimates, no historical earnings-move
distribution -- a decisive data gap rather than a thin edge. Full debate with
citations in `transcript.md`.
