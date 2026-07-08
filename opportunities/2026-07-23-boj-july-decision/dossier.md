---
id: 2026-07-23-boj-july-decision
title: Bank of Japan July rate decision
status: researched
created: '2026-07-07T21:37:40Z'
event:
  type: macro
  summary: BoJ decision Jul 23 after historic June hike to 1%; further tightening
    moves yen and Japan equities (EWJ proxy)
  impact_window: '2026-07-23'
tickers:
- EWJ
sources:
- title: Bank of Japan policy schedule
  url: https://www.boj.or.jp/en/mopo/mpmsche_minu/index.htm
  accessed_at: '2026-07-07T21:37:40Z'
hypothesis:
  statement: 'No executable positive-EV trade in EWJ around the BoJ Jul 23 decision.
    EWJ = (Japan equity) x (JPY/USD): a hawkish BoJ pushes the exporter-heavy index
    down and the yen up, offsetting 40-60% of any move; the modal (hold) outcome reprices
    ~0; net sign is unstable (bank-sleeve positive, bank-corrected E[move] ~+0.13%
    vs carry-unwind-tail negative, tail-loaded E[move] ~-0.24%). The only fillable
    expression is a naked, negatively-skewed overnight gap (decision fires in the
    Tokyo overnight; EWJ opens ~9h-arbitraged) that fails the edge-vs-cost (<=1x)
    and manageability filters. The correct structure (long straddle/put) is a non-fillable
    option. Nominal lean is marginally short, but not enough to trade.'
  direction: short
  confidence: 20
plan:
  ticker: EWJ
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
  dissent: 'Sign of the net EWJ reaction is unresolved. Bull''s bank-channel re-signing
    yields E[move] ~+0.13% (megabanks rally in local terms + yen translation, both
    aligned); quant''s tail-loaded tree yields ~-0.235% (exporter drag + 3% carry-unwind
    fat tail at -4%). Directly checkable at the 2026-07-23 US open: an up-gap vindicates
    the bull''s bank channel, a down-gap/crash vindicates the quant/bear tail.'
  last_updated: '2026-07-08T02:38:24Z'
---

## Scouted 2026-07-07T21:37:40Z

## Researched 2026-07-08T02:38:24Z — NO-TRADE

Three-round panel converged on NO-TRADE (Bull 40/100, Bear 87/100, Quant 85/100). Structural, not macro-call, kill: (1) EWJ self-offsets the BoJ signal via the yen (40-60% compression), leaving a sub-0.5% move whose sign is unstable; (2) at the modal hold outcome the edge is ~0 and below the ~0.15% round-trip cost on either side; (3) the decision fires in the Tokyo overnight, so EWJ can only be held as a naked, negatively-skewed gap (carry-unwind fat tail the -2% stop cannot honor) into an already-arbitraged US open, and the one structure that fits (long straddle/put) is a non-fillable option. Anchor EWJ 400.93 @ 2026-07-07T19:59Z. No institutional lessons on file for macro/EWJ. Full debate in transcript.md.
