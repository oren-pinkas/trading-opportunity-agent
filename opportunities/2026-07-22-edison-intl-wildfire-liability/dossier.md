---
id: 2026-07-22-edison-intl-wildfire-liability
title: Edison International falls on new Southern California wildfire
status: researched
created: '2026-07-22T12:26:30Z'
event:
  type: geopolitical
  summary: Edison International shares fell 1.75% as the fast-moving Sandy Fire broke
    out in Simi Valley (180+ acres, 0% contained), reviving utility wildfire-liability
    concerns
  impact_window: '2026-07-25'
tickers:
- EIX
sources:
- title: Edison International stock falls on California wildfire concerns
  url: https://ng.investing.com/news/stock-market-news/edison-international-stock-falls-on-california-wildfire-concerns-93CH-2517130
  accessed_at: '2026-07-22T12:26:30Z'
hypothesis:
  statement: The -1.75% Sandy Fire dip is a low-information sentiment reaction on
    a still-small (180-acre, 0% contained) fire, but with no CAL FIRE cause finding
    possible inside the 3-day window, the setup is a binary event dressed as mean
    reversion. Quant math is decisive - long carries negative EV (~USD -0.68 to
    -0.83% net) because a 20%/-12% left tail eats the 70% fade edge, and the
    2026-07-22 15:30Z to 18:00Z bounce (USD 79.59 to USD 80.62) means most of the
    reversion is already captured. Short is only thin-positive (~USD +0.50% net)
    and explicitly contingent on a catalyst (confirmed SCE-equipment causation or
    containment data) that does not yet exist before the window closes.
  direction: none
  confidence: 68
plan:
  ticker: EIX
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
  dissent: 'Strongest unresolved disagreement is the P(escalation) weighting used
    in the quant EV calc. Quant anchors it at 0.20 (SCE-equipment naming as a
    smaller subset of that). Bull argues the observed intraday bounce and the
    still-small 180-acre size should push it well below 20%, which would flip
    long EV positive. Bear argues SCE equipment history in this same corridor
    (Woolsey originated in adjacent Simi Valley/Ventura County) should push it
    above 20%, deepening long''s negative EV and weakening even the contingent
    short. This single parameter flips the trade among long, short, and pass,
    and none of the three personas could resolve it without out-of-window CAL
    FIRE cause data. Post-mortem should check the realized 2026-07-25 price
    against which escalation weight was closer to correct.'
  last_updated: '2026-07-23T12:58:31Z'
---

## Scouted 2026-07-22T12:26:30Z

## Researched 2026-07-23T12:58:31Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Sandy Fire
(Simi Valley, 180+ acres, 0% contained as of 2026-07-22T12:26:30Z) dropped EIX
1.75% intraday on revived CA utility wildfire-liability fear. Real prints show
the stock already clawing back from USD 79.59 (15:30Z) to USD 80.62 (18:00Z) the
same day. BULL argued this is a knee-jerk sentiment gap on a fire two-plus orders
of magnitude smaller than the fires (Thomas, Woolsey) that historically drove real
EIX liability re-ratings, and pushed a modest long into the reversal. BEAR argued
the liability trigger is equipment-causation, not fire size, that CAL FIRE
cause-findings take weeks-to-months (far outside the 2026-07-25 window), and that
this is a binary event dressed as mean reversion — stay out. QUANT's EV math was
decisive: P(fade)=0.70/+2.5%, P(escalation)=0.20/-12%, P(chop)=0.10/-0.3% makes
long EV negative (~-0.68 to -0.83% net) because the fat left tail eats the fade
edge, and the already-observed intraday bounce means most of the fade upside is
already captured, not available to a fresh entrant. A contingent 0.25R short was
only thin-positive (+0.50% net) and requires a causation/containment catalyst
before 2026-07-24 that does not exist yet. Verdict: NO-TRADE (not scheduled, not
simulated) — pass on both directions absent a confirmed CAL FIRE catalyst. Full
debate with citations in `transcript.md`.
