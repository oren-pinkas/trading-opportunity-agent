---
id: 2026-07-13-morgan-stanley-blackrock-earnings
title: Morgan Stanley and BlackRock Q2 2026 earnings
status: researched
created: '2026-07-13T15:12:42Z'
event:
  type: earnings
  summary: Both report July 15 premarket; MS EPS consensus .73 (+28% YoY), BLK EPS
    consensus .55, part of bank earnings week
  impact_window: '2026-07-15'
tickers:
- MS
- BLK
sources:
- title: BlackRock to Report Second Quarter 2026 Earnings on July 15th
  url: https://ir.blackrock.com/news-and-events/press-releases/press-releases-details/2026/BlackRock-to-Report-Second-Quarter-2026-Earnings-on-July-15th/default.aspx
  accessed_at: '2026-07-13T15:12:42Z'
hypothesis:
  statement: For a heavily telegraphed, scheduled dual bank-earnings print (MS + BLK,
    premarket 2026-07-15), the available information set supports no directional
    edge. P(up) sits at the 0.50 base rate for both names; symmetric expected moves
    (~4% MS, ~3% BLK) at 0.50 yield negative post-cost EV for directional equity,
    and a defined-risk vertical call spread carries a worse EV (~-3% to -8% of debit)
    due to two-legged bid/ask and residual net-vega decay, despite its nicer bounded-loss
    shape. Nothing in the dossier closes the ~6-8 point P(up) gap (to ~0.56-0.58)
    that would make even a defined-risk structure defensible. The dossier's own EPS
    consensus figures ($.73 MS, $.55 BLK) are garbled/truncated (plausible reconstruction
    ~$2.73 for MS; BLK realistically prints EPS in the $10+ range), and no options-implied
    expected-move, positioning, or Q2 AUM/market-performance data was available to
    the panel.
  direction: none
  confidence: 82
plan:
  ticker: MS, BLK
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0.0
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
  dissent: 'The strongest unresolved soft spot is the Bull''s symmetry objection,
    which the panel accepted but never fully retired: the Bear''s "sell-the-news
    / already-priced-in" thesis is exactly as evidence-free as the Bull''s "AUM-beta
    tailwind" thesis -- both silently assume positioning facts (proximity to 52-week
    highs, extension into the print) that were never confirmed for either MS or BLK.
    The NO-TRADE ruling is correct on absence of edge, but it is not evidence of
    a short edge; the Bear''s high confidence partly borrows conviction from an unfalsifiable
    claim. The concrete, highest-value action for a future similar setup: fetch options-implied
    expected move + skew and a corrected EPS consensus BEFORE convening the panel
    -- these were the load-bearing missing inputs the entire three-round debate circled
    and never resolved. Also worth preserving: the Quant explicitly invoked the LEVI
    institutional lesson to refuse a token/minimum-size "learning loop" position at
    EV~0, on the grounds that it pollutes the learning loop with noise mislabeled
    as signal. A future post-mortem should check: did either stock in fact move >4%
    (MS) / >3% (BLK) on the July 15 print, and if so was the direction better explained
    by the AUM/positioning inputs nobody fetched, or was it genuinely a coin flip
    as modeled?'
  last_updated: '2026-07-13T19:58:00Z'
---

## Scouted 2026-07-13T15:12:42Z

## Researched 2026-07-13T19:58:00Z — NO-TRADE
