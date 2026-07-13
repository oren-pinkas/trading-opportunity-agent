---
id: 2026-07-12-spacex-starship-flight13
title: SpaceX Starship Flight 13 test launch targeted for July 16
status: scheduled
created: '2026-07-12T13:03:15Z'
event:
  type: product
  summary: SpaceX (SPCX) targets a Starship Flight 13 test launch window opening July
    16, 2026, debuting Starlink V3 satellites on the newly public company's next major
    test.
  impact_window: '2026-07-16'
tickers:
- SPCX
sources:
- title: SpaceX ignites all 33 engines on Starship booster ahead of Flight 13 (Space.com)
  url: https://www.space.com/space-exploration/launches-spacecraft/spacex-ignites-all-33-powerful-engines-on-starship-booster-test-ahead-of-flight-13-test-launch
  accessed_at: '2026-07-12T13:03:15Z'
hypothesis:
  statement: SPCX Starship Flight 13 is a telegraphed, negative-skew event whose modal
    outcome (approximately 40%) is a scrub with no move, and whose only surviving edge
    is a small, conditional fade of a launch-day relief pop that the Flight-12 analog
    and the still-pending lockup supply (first tranche after Q2 earnings, late July)
    suggest will not durably hold. There is no attractive unconditional long -- the bull's
    "mispriced dip" framing does not survive the fact that the lockup supply it blames
    for the past selloff is still ahead, not behind, and the Flight-12 precedent shows
    a "broadly successful" outcome still round-tripped to new lows.
  direction: no-trade
  confidence: 72
plan:
  ticker: SPCX
  action: short
  entry:
    time: '2026-07-16T22:45:00Z'
    target_price: 165
  exit:
    time: '2026-07-18T20:00:00Z'
    target_price: 151
  expected_profit_pct: 0.25
  notes: 'Default posture is NO-TRADE. This short is CONDITIONAL and only arms if a
    launch-day pop actually prints: entry window 2026-07-16T22:45:00Z (launch window
    open) through 2026-07-17T02:00:00Z, or a next-day continuation if the launch slips
    within the dossier window. Trigger: only enter if spot trades into the $160-180
    pop-zone (>=~+8% above the $147.93 reference print) on a confirmed clean/partial-success
    launch. If scrub or no pop above ~$160, stand aside -- no entry, no P/L. Instrument:
    defined-risk call-credit spread (e.g. short ~$170 call / long ~$185 call, nearest
    weekly), not naked short. Size <=0.25% NAV. Hard time-stop 2026-07-18T20:00:00Z
    (~1.5 trading days post-launch -- spike-then-fade thesis, not a hold). Cover/take
    profit on retrace toward $150-152; hard stop if spot closes above $182 (pop extending,
    thesis invalidated). Expected profit +0.15% to +0.35% of NAV, realized only in the
    ~38-50% branch where a pop actually prints -- this is a thin, conditional edge, not
    a high-conviction directional bet.'
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
  dissent: 'The strongest unresolved disagreement: does the commercial proof point (20
    operational Starlink V3 satellites -- the first real commercial payload on Starship)
    make Flight 13 a fundamentally different, less-discounted catalyst than the pure
    engineering milestones that round-tripped after Flight 12? Bull holds yes -- this
    is the sole surviving pillar of his case after conceding lockup timing and gap-through-stop
    risk; a successful commercial deployment could re-rate the stock in a way a clean
    test flight never did. Bear and quant hold no -- the dominant near-term driver is
    float/supply mechanics (lockup tranche still ahead) plus an orthogonal intrinsic-value
    overhang (~$30B annualized cash burn) and an unresolved legal tail (Boca Chica
    lawsuit), meaning any pop becomes exit liquidity regardless of payload success.
    Post-mortem hook: a successful launch that still fades confirms bear/quant; a
    successful launch that holds/re-rates vindicates the bull''s "Flight-13 exceptionalism"
    claim and would mean the fade structure this plan is built on was on the wrong side.
    Process note: both bull and bear/quant independently hit `toa price SPCX ... --provider
    twelvedata` HTTP 400 errors for same-day/near-real-time timestamps (TwelveData does
    not yet carry this ~1-month-old listing); only the bull''s 2026-07-10T15:00:00Z
    pull succeeded ($147.93), which the panel adopted as its reference spot. Current
    SPCX spot could not be independently verified through the sanctioned pricing tool
    at debate time.'
  last_updated: '2026-07-13T10:15:00Z'
---

## Scouted 2026-07-12T13:03:15Z

## Researched 2026-07-13T10:15:00Z — CONDITIONAL SHORT (default NO-TRADE)

**Event:** SpaceX (SPCX) targets a Starship Flight 13 test launch window opening
2026-07-16T22:45:00Z (Starbase, TX), debuting 20 operational Starlink V3 satellites.
Sole dossier source: Space.com, "SpaceX ignites all 33 engines on Starship booster ahead
of Flight 13" (2026-07-12).

**Panel verdict (three-round debate, bull/bear/quant + synthesis):** The panel converged
toward caution. Bull argued the stock's slide to all-time lows (~$145-150, down from a
post-IPO ATH of $225.64) is driven by float/lock-up mechanics and a forced Nasdaq-100
index-inclusion sell-through, not Starship execution doubt, making the launch catalyst
"free" on top of a record-duration 33-engine static fire (2026-07-10) and a commercial
proof point (first V3-generation Starlink payload); confidence fell from 62 to 55 after
conceding the quant's fatter failure-tail math exposed real gap-through-stop risk in his
original plan. Bear countered that the lockup supply the bull blames for the past selloff
is still ahead (first tranche after Q2 earnings, late July), positioning any launch-day
pop as exit liquidity for insiders rather than a durable re-rate, and that the Flight-12
precedent (a "broadly successful" test that still round-tripped to new lows) supports
fading rather than riding any pop; confidence rose from 62 to 66. Quant's base-rate/EV
model (40% scrub, 38% clean success, 12% partial, 10% failure/RUD) put the revised gross
equity EV at approximately -0.20% (net -0.35% to -0.40%) with negative skew — no edge for
an unconditional long, and long options are clearly negative-EV given ~169% weekly ATM
IV; confidence rose from 70 to 74 on "stand aside," with the sole surviving idea being a
small, strictly conditional fade if a pop actually materializes (Flight-12 gives it real
empirical support; the 40% scrub probability means there may be nothing to fade at all).

**Recommendation:** No unconditional trade. Conditional, defined-risk short (call-credit
spread, <=0.25% NAV) armed only if spot pops into the $160-180 zone post-launch; stand
aside otherwise. See `transcript.md` for the full three-round debate with citations.
