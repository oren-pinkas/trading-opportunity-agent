---
id: 2026-07-07-tesla-q2-earnings
title: Tesla Q2 2026 earnings
status: researched
created: '2026-07-07T19:30:32Z'
event:
  type: earnings
  summary: Tesla reports Q2 results Jul 22; deliveries/margins and robotaxi commentary
    are the catalyst.
  impact_window: '2026-07-22'
tickers:
- TSLA
sources:
- title: Kiplinger earnings calendar
  url: https://www.kiplinger.com/investing/stocks/17494/next-week-earnings-calendar-stocks
  accessed_at: '2026-07-07T19:30:32Z'
hypothesis:
  statement: 'The one forecastable leg (Q2 deliveries: 480,126, +18% vs consensus)
    already fired on 2026-07-02 and was SOLD (-7.5% same day) on a ~190-200x forward
    multiple; the Jul 22 AMC print reduces to an un-priceable margin/robotaxi-narrative
    binary. Every executable structure fails the no-trade filter: the naked earnings
    hold carries an uncapped ~9%-implied / -15-20% overnight tail (options non-executable,
    net EV ~ -1.6%); the pre-print intraday positioning trade has zero documented
    edge (~ -0.15% cost bleed); and the bull''s post-print same-session long, while
    gap-free and bar-executable, misapplies multi-week PEAD to a 6-hour intraday scalp
    in the most-arbitraged mega-cap on the tape and fights TSLA''s own gap-fade tendency
    (net EV ~ -0.7%). No structure clears the ~2% EV bar. Stock near 52-wk high, so
    no low-of-range base-rate discount applies.'
  direction: short
  confidence: 25
plan:
  ticker: TSLA
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
  dissent: 'Bull''s structural point (unresolved): the debate rejected the trade on
    EV/instrument grounds, NOT on the fundamental thesis. A genuinely bullish, evidence-backed
    expression may exist in the real world — a MULTI-DAY post-print drift long entered
    only after confirming auto GM ex-credits held >18% and a concrete robotaxi city/fleet
    expansion number on the Jul 22 call. That structure is non-executable in this
    sim (equity-only, single-session bars, no multi-day hold, options don''t fill).
    So the catalyst is real; the instrument is the disqualifier. If the sim allowed
    a 3-5 day conditional hold, the bull would argue for it at ~40 confidence. Secondary
    flag: sim anchor $451.58 sits ~12% above the real ~$404 Jul-7 tape — return-%
    P/L is level-invariant so it doesn''t change EV, but it exposed the bull''s dollar
    targets as unanchored and lowers trust in any precise level.'
  last_updated: '2026-07-07T22:49:52Z'
---

## Scouted 2026-07-07T19:30:32Z

## Researched 2026-07-07T22:49:52Z — NO-TRADE

Three-round panel (bull/sonnet, bear/sonnet, quant/opus; synthesizer/opus) converged UNANIMOUSLY on NO-TRADE.

**Verdict: NO-TRADE, position size 0.** Bull conceded in Round 2 (confidence in a profitable executable trade: 22/100); bear and quant held NO-TRADE at 82/100.

**Why no trade survives:**
- *Catalyst spent.* Q2 deliveries — the only forecastable leg — printed 480,126 (+25% YoY, ~18% over ~406k consensus) on 2026-07-02 and the stock FELL ~7.5% that day. The Miami robotaxi launch (Jul 3) then rallied it back; both catalysts a bull would cite were priced and partially sold in the five sessions before the anchor. Jul 22 is now a pure margin/guidance test.
- *No cushion.* ~190-204x forward P/E, ~92x NTM EV/EBITDA — a multiple that discounts autonomy, not cars. Stock near the TOP of its 52-wk range ($288.77-$498.83), so the 'discount negative base rates near the 52-wk low' lesson does NOT apply.
- *Instrument disqualifies the earnings bet.* Report is AMC Jul 22; the sim fills only 13:30Z-19:59Z equity bars and options don't fill. Capturing the reaction requires a naked overnight hold across a ~9%-implied gap (weekly straddle, OptionSlam) with a -15-20% uncapped tail. Net EV ~ -1.6%; adverse-tail-to-edge >>8x.
- *The gap-free alternatives have no edge.* Bull's post-print same-session long (enter Jul 23 open, exit 19:59Z) removes the overnight tail — a legitimate structural improvement — but it substitutes multi-week PEAD (a small/mid-cap, low-coverage, multi-day anomaly) for a 6-hour intraday continuation scalp in the most-arbitraged mega-cap on the tape. TSLA's tape gap-FADES (largest gap-downs drifted higher to close 67% of the time), and we just watched sell-the-good-news punish continuation-longs twice in a week. Net EV ~ -0.7%. The pre-print positioning trade is ~ -0.15% cost bleed. Neither clears ~2%.

**Base rates (quant):** implied |move| ~9% weekly / ~13% monthly; last print (2026-04-22) reacted -3.55% close / -4.93% max; direction skew ~45% up / 55% down.

**What would flip the call (bear/bull agree):** the actual Q2 automotive gross margin ex-credits, printed Jul 22. >=17% ex-credits (vs the ~13-15% feared) would prove the 480k units were not bought with destructive discounting and validate a post-print long entered INTO confirmed strength — but that information does not exist until after 20:00Z on Jul 22, which is precisely why no pre-print or same-open structure can claim an edge.

Sources: Electrek (deliveries, 2026-07-02); TradingKey (delivery drop analysis + Q1 preview, 2026-07); OptionSlam (implied move + Apr-22 history, accessed 2026-07-07); Motley Fool (Jul-22 preview, 2026-07-07); Intellectia / BingX (margin, valuation); 24/7 Wall St (robotaxi relief-rally framing, 2026-07-06); Vantage (real ~$404 Jul-7 tape). Full transcript with citations in transcript.md.
