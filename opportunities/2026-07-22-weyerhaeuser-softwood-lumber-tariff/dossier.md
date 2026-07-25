---
id: 2026-07-22-weyerhaeuser-softwood-lumber-tariff
title: US softwood lumber AR7 final tariff determination due August 2026
status: researched
created: '2026-07-22T13:34:47Z'
event:
  type: regulatory
  summary: Commerce Dept's AR7 final results on Canadian softwood lumber duties expected
    August 2026, with Section 232 rate holding near 35% until then
  impact_window: '2026-08-31'
tickers:
- WY
sources:
- title: U.S. to Cut Canadian Lumber Duties by 10% - Rate Stays at 35%
  url: https://woodcentral.com.au/u-s-to-cut-canadian-lumber-duties-by-10-rate-stays-at-35/
  accessed_at: '2026-07-22T13:34:47Z'
hypothesis:
  statement: 'All three personas converged on no-trade for WY around the AR7 final
    results: the sign is unresolved (WY is a US producer, so a Canadian duty cut is
    arguably margin-negative, inverting the dossier''s implicit bullish framing),
    the event is already public and unpriced-in-reaction (WY moved only USD 0.6% over
    7/22-7/24 in relative terms, within noise), and the roughly 1.2% expected event
    signal is dwarfed by roughly 9.2% path noise over the window, netting expected
    value of roughly -0.17% after costs. Compounding this, ''expected August 2026''
    is a month-granularity regulatory expectation rather than a scheduled print (~55%
    chance of resolving by the 8/31 impact window), Section 232 versus AD/CVD conflation
    leaves the payoff function ill-specified, and WY''s Q2 earnings fall inside the
    same window, making any post-event attribution impossible.'
  direction: no-trade
  confidence: 12
plan:
  action: no-trade
  ticker: WY
  reason: Signal-to-noise ~0.003 (~50x below the 0.15 institutional threshold); sign
    of the WY/AR7 relationship is unresolved and contested between bull and bear;
    catalyst date is soft/unscheduled (~55% chance of resolving in-window); WY Q2
    earnings fall inside the same window and would contaminate attribution of any
    move.
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
  dissent: 'The strongest residual uncertainty is bear''s untested tail: ''no reaction
    yet'' is consistent with ''already priced in,'' but it does not rule out a sharp
    move if the AR7 final determination diverges materially from the leaked ~10%-cut/35%-hold
    numbers, and no persona had any edge on estimating that surprise probability.
    Two concrete conditions would reopen the question for a later, differently-structured
    trade: (1) a confirmed Federal Register publication date that turns the soft ''August
    2026'' expectation into a real timestamp outside WY''s Q2 earnings window, and
    (2) evidence of a genuine uncertainty overhang -- elevated IV, an option term-structure
    kink at the event, underperformance versus peers, or widened estimate dispersion
    -- none of which are present today. Also unresolved rather than settled: nobody
    established the sign of a duty cut for WY with any rigor; bull retreated to low
    confidence and bear leaned bearish, but neither did the margin/benchmark-price
    work that would actually determine direction. A post-mortem should check the realized
    move around the actual determination and whether WY''s reaction sign matched the
    ''tariffs are a WY tailwind'' prior.'
  last_updated: '2026-07-25T00:45:00Z'
---

## Scouted 2026-07-22T13:34:47Z

## Researched 2026-07-25T00:45:00Z — NO-TRADE

**Confidence in no-trade call: 88/100** (quant), with bull and bear converging.

Round 1 (independent):
- Bull: framed AR7 final as a de-risking/relief-rally catalyst regardless of direction; proposed long WY equity or Sept USD 25 OTM calls, entry Aug 3-14 2026, exit 3-5 sessions post-print by 8/31. Confidence 5.5/10, explicitly flagged the cut could read as margin-negative instead.
- Bear: argued the event is already priced in (7th annual review, headline itself already reports the cut). Flagged that WY is a US timberland/producer for whom Canadian duties are historically a tailwind, so a duty cut is arguably bearish -- the dossier's implicit bullish framing may have the sign backwards. Flagged Section 232 vs AD/CVD conflation. Recommended no-trade or minimal position.
- Quant: base rate for routine AR-final events on an existing order is 0.3-1.5% absolute move; WY has empirically not moved on this news (roughly +0.6% over two sessions, noise). 'Expected August' is month-granularity, not scheduled (~55% chance of in-window resolution). Daily sigma ~1.8% implies ~9.2% path noise over the ~26-session hold, dwarfing the ~1.2% event signal. WY Q2 earnings fall inside the same window, contaminating attribution. EV nets to roughly -0.17% after costs; signal-to-noise ~0.003, ~50x below the 0.15 threshold. Recommended NO TRADE, confidence 0.85.

Round 2 (rebuttals):
- Bull conceded: agreed the base-rate/no-edge argument is decisive and the direction-ambiguity point is a real flaw in the original bullish framing. Concluded no defensible directional plan exists right now; confidence in the original long thesis dropped to 2/10.
- Bear reinforced: agreed with quant's empirical point, pushed back on bull's 'de-risking rally regardless of direction' as incoherent (if truly direction-agnostic-but-vol-positive, the coherent trade would be a straddle, not OTM calls). Converged fully with quant on no-trade.
- Quant reinforced, raised confidence to 0.88: bear's sign-ambiguity point is an independent second kill condition alongside the S/N failure. Noted bull's own thesis, taken literally, implies short-vol rather than the long OTM calls proposed, but declined to recommend shorting vol either (premium too small, no evidence of elevated IV, unhedged earnings-print gamma risk). Key meta-observation: three analysts on the same facts produced long / short-leaning / flat -- when credible readings span both directions, the event's information content is at or below the noise floor, which is itself the no-trade signal.

Full transcript: see transcript.md in this opportunity's folder.

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.
