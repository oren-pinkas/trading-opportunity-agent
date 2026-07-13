---
id: 2026-07-12-vertex-crinetics-merger
title: Vertex Pharmaceuticals to acquire Crinetics for $10B
status: researched
created: '2026-07-12T07:48:00Z'
event:
  type: regulatory
  summary: Vertex agreed to buy Crinetics for $85/share cash (~$8.8B net), adding
    PALSONIFY acromegaly franchise and atumelnant CAH program; deal expected to close
    Q3 2026 pending shareholder and regulatory approval.
  impact_window: '2026-09-30'
tickers:
- VRTX
- CRNX
sources:
- title: Vertex to Acquire Crinetics Pharmaceuticals
  url: https://www.businesswire.com/news/home/20260706876183/en/Vertex-to-Acquire-Crinetics-Pharmaceuticals
  accessed_at: '2026-07-12T07:48:00Z'
hypothesis:
  statement: The VRTX/CRNX all-cash merger ($85/share, ~$8.8B net) is a clean, likely-to-close
    deal, but at the last verified CRNX print of $83.675 the residual gross spread
    is only ~1.58% (~7.3% annualized over a ~79-day hold). Under P(close)≈0.90-0.93
    and any plausible break-downside (-25% to -40%), merger-arb expected value is
    negative (EV ≈ -0.63% to -1.33%). No supportable long edge at current levels;
    no borrow/signaling case for a short on a ~90%+ likely-to-close deal.
  direction: no_position
  confidence: 78
plan:
  ticker: CRNX
  action: no_action
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
  notes: Flip to a small long CRNX merger-arb only if, after live re-verification
    via `toa price CRNX <ts> --provider twelvedata`, either (a) entry ≤$82.50 (gross
    spread ≥3%) or (b) P(close)≥95-96% backed by confirmed HSR clearance/no second
    request, confirmed vote scheduling, and no financing contingency.
research:
  last_updated: '2026-07-13T12:42:51Z'
  dissent: Break-downside magnitude and P(close) prior remain unresolved. Bull sees
    downside compressed to -15-20% and P(close) 96-97%; Bear/Quant see downside
    -35-45% and P(close) 0.88-0.93 absent confirmed HSR/vote status. No persona
    sourced the pre-announcement unaffected CRNX price — the largest unresolved
    input on the downside leg.
---

## Scouted 2026-07-12T07:48:00Z

## Researched 2026-07-13T12:42:51Z

Three-round panel debate (bull/bear/quant, synthesized) converged on **no_position / PASS**.
Gross spread to deal terms (+1.58% at CRNX $83.675, 2026-07-10 print) does not compensate
for break-downside risk (-30% to -40% modeled) at base-rate P(close) of 0.90-0.93. EV
negative (-0.63% to -1.33%) across the debated range. See `transcript.md` for full debate.
Entry triggers if revisited: CRNX ≤$82.50 (spread ≥3%) or confirmed P(close)≥95-96%
via HSR/vote-status evidence.
