---
id: 2026-07-14-morgan-stanley-q2-fy26
title: Morgan Stanley Q2 FY26 earnings
status: researched
created: '2026-07-07T11:00:01Z'
event:
  type: earnings
  summary: Morgan Stanley reports Q2 2026 results July 14 pre-market; trading/IB and
    wealth flows in focus.
  impact_window: '2026-07-14'
tickers:
- MS
sources:
- title: 'Q2 2026 Earnings Season: Key Dates (Plus500)'
  url: https://us.plus500.com/en/newsandmarketinsights/q2-2026-earnings-season
  accessed_at: '2026-07-07T11:00:01Z'
hypothesis:
  statement: 'No executable edge. The print is untradeable (pre-market gap, options
    non-fillable, naked overnight banned by lesson #1); the only clean structure —
    a 2026-07-13 pre-print intraday drift long — is negative-to-zero EV because its
    best-case gross (+0.8-1.0%) sits inside round-trip costs (~1-1.5%), and its peer-read-through
    catalyst has no transmission channel into the deterministic sim price series and
    rests on an unverified peer calendar. Mild fundamental lean is nominally long
    but immaterial.'
  direction: long
  confidence: 20
plan:
  ticker: MS
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
  dissent: 'Whether the 07-13 pre-print drift long is a genuine small-edge candidate
    or dead-on-arrival. Bull: mildly positive-EV IFF the sim charges realistic liquid-equity
    costs (single-digit bps, not a fixed ~1.5%) — a sim-cost-model question unresolvable
    from the transcript. Quant/bear treat ~1-1.5% round-trip as binding, making it
    negative-EV. Flips to a small-size long only if a future run confirms low liquid-equity
    costs AND a verified peer calendar placing JPM/C/WFC beats on tape before 07-13.'
  last_updated: '2026-07-07T23:15:00Z'
---

## Scouted 2026-07-07T11:00:01Z

## Researched 2026-07-07T23:15:00Z — NO-TRADE

Unanimous NO-TRADE. The print itself is untradeable: MS reports pre-market on 2026-07-14, options do not fill in-sim, and a naked overnight hold trips institutional lesson #1 (un-hedgeable tail, effectively infinite adverse-tail-to-edge). The only structurally clean idea — the bull's 2026-07-13 pre-print intraday drift long (enter 13:35:00Z / exit 19:59:00Z, target +0.8-1.0%) — fails on two independent grounds: (1) arithmetic, best-case gross target is inside the ~1-1.5% round-trip cost band, so EV is zero-to-negative even if the thesis works (quant distributional EV ~-1.15%); (2) no signal in the fillable data, the peer-read-through catalyst has no channel into the deterministic stub price series and rests on an unverified peer report calendar (money-centers may print the same day as MS, erasing the 07-13 window). Bull conceded 58->38 and did not defend against a no-trade ruling; bear 84, quant 85. See transcript.md.
