---
id: 2026-07-12-rocketlab-iridium-acquisition
title: Rocket Lab to acquire Iridium in $8B cash-and-stock deal
status: scouted
created: '2026-07-12T13:03:15Z'
event:
  type: regulatory
  summary: Rocket Lab agreed to acquire Iridium for $54/share ($27 cash + stock, ~$8B
    EV); deal needs Iridium shareholder and regulatory approval, must close by June
    28, 2027.
  impact_window: '2027-06-28'
tickers:
- RKLB
- IRDM
sources:
- title: Rocket Lab to Acquire Iridium in Historic Deal (Rocket Lab investor news)
  url: https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully
  accessed_at: '2026-07-12T13:03:15Z'
hypothesis:
  statement: >-
    IRDM trades below the $54 deal terms on an assumed completion probability
    (~0.80) high enough for a small unhedged long to carry modestly positive EV,
    but only if entered below fair value (~$52, per quant's 0.80x54 + 0.20x44
    blend) on the first post-announcement print. Fair value rests entirely on
    that completion estimate holding against genuine CFIUS/FCC novelty (no clean
    satellite+defense precedent) over an ~11.5-month runway to the 2027-06-28
    deadline. The RKLB "narrative re-rating" momentum leg and the long-IRDM/
    short-RKLB pairs hedge were both rejected: the RKLB leg has no deal-arb
    anchor and is plausibly wrong-signed (acquirers often weaken on
    dilutive-deal announcements), and the hedge is only coherent under an
    unconfirmed fixed-ratio exchange mechanism and loses on both legs in a
    deal-break scenario (IRDM falls, RKLB typically bounces on relief).
  direction: long
  confidence: 60
plan:
  ticker: IRDM
  action: buy
  entry:
    time: '2026-07-13T14:00:00Z'
    target_price: 51.5
  exit:
    time: '2027-06-25T19:55:00Z'
    target_price: 53.5
  expected_profit_pct: 1.2
research:
  strategy: three-round-panel
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  last_updated: '2026-07-13T08:25:02Z'
status: scheduled
---

## Scouted 2026-07-12T13:03:15Z

## Researched 2026-07-13T08:25:02Z

Three-round panel (bull/bear/quant), single-opportunity review. Verified pre-announcement
baseline via twelvedata: IRDM $50.075 / RKLB $80.93, both Fri 2026-07-10T19:59Z close — no
Monday print exists yet as of synthesis time (2026-07-13T08:25Z, pre-open). Implied spread
to the $54 deal price: ~7.8% (~8.4% annualized over the ~11.5-month runway to 2027-06-28) —
not a distressed-wide spread (broken/contested deals typically trade 15-30%+), but thin
enough that the trade's EV is fragile to the completion-probability assumption.

Bull proposed an outright IRDM long plus a standalone RKLB momentum sleeve (platform
narrative re-rating, independent of deal completion). Bear flagged the ~7.8% premium as
abnormally low for strategic M&A (typical 20-40%), plus RKLB dilution/financing risk,
CFIUS/FCC regulatory novelty, and ~11.5-month duration risk; proposed a long-IRDM/
short-RKLB pairs trade instead of an outright long. Quant modeled EV explicitly:
P(complete)=0.83→0.80 after haircutting for regulatory novelty, fair value $52.00 (0.80×54
+ 0.20×44), requiring a fill below $52 for positive EV; break-even P(complete)=0.75.

**Synthesis rejected both embellishments.** The RKLB momentum leg was cut — it has no
deal-arb anchor (no $54 convergence target), is pure directional beta on a high-vol name,
and is plausibly wrong-signed (stock-funded acquirers often weaken on dilution overhang);
tell: bear wanted to *short* the exact leg bull wanted to *long*, meaning it was never one
priced opportunity. The pairs hedge was also cut — coherent only under an unconfirmed
fixed-ratio exchange mechanism, and even then loses on both legs in a deal-break scenario
(IRDM falls, RKLB typically bounces on relief), while paying ~1%/yr borrow drag.

**Recommendation: small unhedged long IRDM only**, strictly gated on the first
post-announcement print. Entry 2026-07-13T14:00:00Z (valid Monday session, 30min after
open) contingent on IRDM printing ≤$51.50 — stand down entirely if it opens ≥$52 (fair
value, EV flips negative). Size ~1.5% of paper book (cut from quant's initial 3% given the
thin margin). Exit on a $53.50 profit-take limit, or time-stop rolled back from the
2027-06-28 legal deadline to the nearest valid trading session, Fri 2027-06-25T19:55:00Z
(per lessons on not using legal/corporate deadlines as literal execution timestamps).
Kill-switch: exit immediately on negative CFIUS/FCC headlines intraday.

**Dissent (unresolved, preserved for post-mortem):** is the left tail correctly priced?
Bear holds that CFIUS/FCC novelty plus ~11.5-month duration means quant's break-price
($44) and break-odds (0.20) understate true downside, pushing the trade toward or below
its own 0.75 break-even. Quant holds the 8.4%-annualized spread is not distressed-wide, so
only a modest haircut (0.83→0.80) was warranted. If this deal breaks, the post-mortem
should test whether completion probability was miscalibrated for regulatory-novel deals,
not whether the trade structure itself was wrong. Full transcript: transcript.md.
