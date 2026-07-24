---
id: 2026-07-22-robert-half-q2-earnings
title: Robert Half Q2 2026 earnings (Jul 23) test staffing demand outlook
status: researched
created: '2026-07-22T14:43:29Z'
event:
  type: earnings
  summary: Robert Half reports Q2 2026 earnings July 23 with guidance of .275-1.375B
    revenue and /bin/zsh.20-0.30 EPS; result will signal whether labor-market optimism
    is translating into durable staffing demand.
  impact_window: '2026-07-23'
tickers:
- RHI
sources:
- title: Does Robert Half (RHI) Capture Durable Value from Shifting Labor-Market Optimism
    in Staffing Demand?
  url: https://www.sahmcapital.com/news/content/does-robert-half-rhi-capture-durable-value-from-shifting-labor-market-optimism-in-staffing-demand-2026-07-17
  accessed_at: '2026-07-22T14:43:29Z'
hypothesis:
  statement: RHI's -6.9% post-earnings selloff shows a flat-open-then-all-day-slide
    digest-the-call-then-sell signature consistent with guidance-driven institutional
    distribution, not a headline overreaction; with the move already realized, guidance
    data corrupted, and both defined-risk directions carrying negative EV, no positive-EV
    edge exists into the next session.
  direction: no-trade
  confidence: 68
plan:
  ticker: RHI
  action: no-trade
  entry:
    time: '2026-07-24T14:00:00Z'
    target_price: null
  exit:
    time: '2026-07-28T19:59:00Z'
    target_price: null
  expected_profit_pct: 0
  note: 'Stand aside. Conditional monitoring only (not an active order): if the 2026-07-24
    open gaps more than 3 percent from USD 37.985 (below ~USD 36.85 or above ~USD
    39.12) AND peers MAN/ASGN/KFRC confirm direction, a small defined-risk options
    structure (call spread on reversion, put spread on continuation) could be considered,
    entry ~2026-07-24T14:00Z after a 30-60 min confirmation window, hard exit 2026-07-28T19:59Z,
    ~2.5 percent expected profit on small size; skip entirely if the gap threshold
    or peer confirmation does not fire.'
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
  dissent: Bull vs. bear/quant on whether the USD 37.985 close-at-the-lows is a saturation/capitulation-selling
    signature seeding a reversion bounce (bull), or an institutional-distribution
    digest-then-sell signature with below-average reversion odds (bear, arguing quant's
    30 percent reversion weight is if anything too generous). Unresolved because no
    one could confirm an actual guidance cut vs. consensus given the corrupted dossier
    digits. Bull's core evidentiary claim -- staffing names retrace 20-40 percent
    of the drop within 3-5 sessions -- was challenged by both bear and quant as asserted/unsourced
    and, per quant, already absorbed inside the existing 30 percent reversion weight,
    so it never moved the EV math.
  last_updated: '2026-07-24T01:52:00Z'
---

## Scouted 2026-07-22T14:43:29Z

## Researched 2026-07-24T01:52:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant/synthesizer opus). Earnings already reported and reacted to before this research ran: RHI fell from USD 40.805 (2026-07-22 close) to USD 37.985 (2026-07-23 close), a -6.9 percent close-to-close / -7.8 percent intraday move, on a flat-open-then-all-day-slide pattern read by the panel as guidance/call-driven distribution rather than a headline shock. Dossier guidance figures are corrupted by a shell-substitution bug and were treated as low-confidence throughout. Bear and quant both concluded NO-TRADE with explicit negative expected value in both directions (continuation short -0.15R, reversion long -0.25R, both negative even flexing win-rate assumptions +/-5 percent); bull argued for a small conditional mean-reversion long but reduced confidence to 30/100 and gated entry on next-session confirmation. Synthesis: NO-TRADE, confidence 68/100, with a documented conditional re-entry trigger (>3 percent gap from USD 37.985 plus peer confirmation) logged for monitoring only. Full transcript: opportunities/2026-07-22-robert-half-q2-earnings/transcript.md
