---
id: 2026-07-12-avanos-medical-merger-vote
title: Avanos Medical shareholder vote on $25/share cash buyout set for July 22
status: researched
created: '2026-07-12T13:03:15Z'
event:
  type: regulatory
  summary: AVNS holders vote July 22, 2026 on merger agreement to be acquired for
    $25.00 cash per share.
  impact_window: '2026-07-22'
tickers:
- AVNS
sources:
- title: Avanos Medical merger proxy statement (StockTitan)
  url: https://www.stocktitan.net/sec-filings/AVNS/defm14a-avanos-medical-inc-merger-proxy-statement-87e13f78bbaa.html
  accessed_at: '2026-07-12T13:03:15Z'
hypothesis:
  statement: AVNS is a late-stage all-cash merger (AIP, $25.00/share, vote 2026-07-22,
    expected close by 2026-07-27) with regulatory approvals already received. At every
    reported price ($24.75 to $24.92) the expected value of a FRESH long entry is
    negative once the panel's sourced break-downside (~$14.53 pre-announcement reference,
    i.e. ~$10/share tail loss) is weighed against the ~$0.08-0.25/share upside. Breakeven
    requires P(break) <= ~0.5% at $24.92 and <= ~1.9-2.0% at $24.75 -- a near-certainty
    bar that cannot be justified while AIP's financing/'certain funds' status and
    vote mechanics remain unconfirmed. The reward:risk at the best-case verified fill
    is roughly 1:41. There is no positive-EV trade to initiate.
  direction: no-trade
  confidence: 82
plan:
  ticker: AVNS
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0.0
  notes: 'No fresh entry. At $24.92 net EV negative at all tested P(break) (breakeven
    needs P(break)<=0.48%); at $24.75 EV is at best +$0.011/share (~+0.04%, effectively
    zero) only if P(break)<=2%. Downside on break ~-$10.25/share (to ~$14.53) vs upside
    +$0.08 to +$0.25. Conditional GO only if a PRIMARY verified tick shows a fill
    <= $24.76 (spread >= ~0.97%) AND AIP financing/''certain funds'' is confirmed
    -- treat as not-met by default. If already long from a prior entry: hold to close,
    do not add. Do not short (deal protection, unanimous board, no topping bid, 72%
    premium make a short low-probability and capped-upside).'
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
  dissent: Bull vs. Bear/Quant on how to read the tight spread. Bull reads it (plus
    regulatory clearance, unanimous board, no topping bid after 3 months, only boilerplate
    litigation) as evidence true P(break) is ~1-2%, not the generic 3-5% base rate
    -- which would make the $24.75 print marginally positive EV and justify a small
    long. Bear and the revised Quant read the tight spread as mechanical time-decay
    compression this close to a fixed closing date, NOT confirmation that the two
    named gaps (AIP financing/'certain funds' status; vote-threshold mechanics/ISS-Glass
    Lewis recommendation) have been resolved -- no persona could confirm financing
    status, the single fact that would move P(break) most. The panel converged on
    the no-trade decision without resolving this disagreement about the true break
    probability.
  last_updated: '2026-07-12T17:17:00Z'
---

## Scouted 2026-07-12T13:03:15Z

## Researched 2026-07-12T17:17:00Z — NO-TRADE

**Panel: bull(sonnet)/bear(sonnet)/quant(opus), synthesizer(opus). Full transcript: see transcript.md.**

Three-round convergence to NO-TRADE. Bull opened at 62/100 confidence long; Bear opened at 58/100 no-new-entry; Quant opened at 25/100 point-EV (no live price data, stub feed for AVNS confirmed broken -- returns $171-$486 vs a $25.00 deal price). By Round 2, Bull cut confidence to 50/100 after conceding neither reported price ($24.75 Bear / $24.92 Bull, both secondary-sourced via WebSearch, not a primary tick) clears his own persona's or Quant's GO threshold under base-rate break odds. Bear sourced a hard downside-if-break reference of ~$14.53 from the deal's own disclosed 72.1% takeover premium (better evidence than an assumed haircut). Quant, once given real (if secondary) price data, recomputed EV at both reported prices across P(break) 2-5%: negative in every cell except a rounding-error-thin +$0.011/share at $24.75 and P(break)=2%. Quant explicitly conceded direction to Bear: 'the market has priced this correctly and there is no compensated edge at these levels.' Reward:risk at the best case is ~1:41 (nickels in front of a steamroller). Key unresolved fact: no persona could confirm AIP's (a PE sponsor, not strategic buyer) financing/'certain funds' status, nor vote-threshold mechanics/ISS-Glass Lewis stance -- these remain the two gaps that could move the decision. Data-quality caveat: the house `toa price AVNS` stub tool is confirmed unusable for this ticker; all price inputs used were secondary-sourced and diverge by $0.17, which straddles the breakeven -- but the no-trade conclusion is robust to that uncertainty since even the more favorable read is only a scratch.
