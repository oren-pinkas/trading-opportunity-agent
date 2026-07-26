# Research Debate Transcript — RTX Q2 2026 Earnings

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

- Opportunity: `2026-07-23-rtx-q2-fy26`
- Ticker: RTX
- Event: RTX (Raytheon Technologies / RTX Corp) Q2 2026 earnings, consensus EPS USD 1.66
- Impact window: 2026-07-23
- Research run: 2026-07-26T01:12:34Z (3 days after the impact window opened/closed)
- Strategy: `three-round-panel` (personas: bull/sonnet, bear/sonnet, quant/opus; synthesizer/opus)
- Institutional-memory lookup (`toa lessons-relevant --type earnings --tickers RTX`): no
  RTX-specific lessons found. Generic earnings-event lessons were injected instead (see below).
- Price series (`toa price RTX <ts> --provider twelvedata`):
  - 2026-07-22 19:59Z (pre-print close): USD 194.60
  - 2026-07-23 13:35Z (post-gap open): USD 208.61
  - 2026-07-23 19:59Z (print-day close): USD 209.10
  - 2026-07-24 19:59Z (day-2 close, last print before the 07-25/26 weekend): USD 213.05
- Reported fundamentals (RTX press release / PRNewswire, 2026-07-23; corroborated by
  StockStory, Yahoo Finance, MarketBeat, Investing.com coverage): adj EPS USD 1.89 vs USD 1.66
  consensus (+13.9%), revenue USD 24.71B (+14.5% YoY, +16% organic), record USD 289B backlog,
  FY26 guide raised to adj EPS USD 7.10-7.25 (from USD 6.70-6.90) and sales USD 95.0-96.0B, FCF
  guide raised to USD 8.50-8.75B. New 52-week high USD 214.50. Sell-side re-rates: Baird to USD
  240, Susquehanna to USD 245, BofA to USD 235, Wells Fargo to USD 230; consensus target USD
  226.82 (23 analysts).

## Lessons injected as context

1. Confidence <=~45 with an un-hedgeable positive tail and net EV <~2% against a ~7-8x
   adverse-tail-to-edge ratio is a no-trade filter, not a size-down; express such earnings
   gap-shorts via defined-risk options, never a naked short. (NKE, 2026-07-06)
2. Discount post-earnings negative base rates when the name is already at/near its 52-week
   low: most of the drawdown is priced in and a benign or one-time-beat print flips the
   reaction positive. (NKE, 2026-07-06)
3. Set intraday exits at least one minute inside the session boundary (19:59:00Z, not
   20:00:00Z): a 1-minute-bar provider has no bar stamped exactly at the close. (TSLA, 2026-07-06)
4. Add a pre-simulation timestamp guard that validates both legs map to available US-equity
   bars (13:30Z-19:59Z). (TSLA, 2026-07-06)
5. A catalyst that already drove a large multi-week run to a 52-week high above the Street
   mean target is priced in — do not re-bet the same fundamental as a fresh gap trigger.
   (DAL, 2026-07-12)
6. When the strongest unrebutted dissent aligns with the quant's own EV math, synthesize to
   NO-TRADE rather than a quarter-size directional position. (DAL, 2026-07-12)
7. When the highest-confidence panelist says directional EV is ~0 and the only positive-EV
   structure is out of mandate, log NO TRADE — do not manufacture a minimal directional
   position "for the learning loop." (LEVI, 2026-07-12)
8. Anchor entry prices to a live quote fetched at the actual entry timestamp, not a stale
   pre-move reference. (LEVI, 2026-07-12)

---

## Round 1 — Independent research

### Bull (sonnet)

RTX reported Q2 2026 on 2026-07-23: revenue USD 24.71B (+14.5% YoY, +16% organic), adj EPS
USD 1.89 vs USD 1.66 Street consensus — a 13.7% beat, not an in-line print. Management raised
full-year guidance: adj sales to USD 95.0-96.0B (organic growth guide raised to 8-9% from
5-6%) and full-year adj EPS to USD 7.10-7.25. This is a genuine beat-and-raise, not a low-bar
clearance. (Sources: RTX press release via PRNewswire/RTX.com, 2026-07-23; StockStory, "RTX
Reports Upbeat Q2 CY2026, Stock Soars," 2026-07-23.)

Price evidence: anchored USD 205.00 at 13:30Z (open) and USD 209.10 at 19:59Z (last minute-bar
inside the session) on print day — a +2.0% intraday move, consistent with the "stock soars"
headline. Twelvedata rate-limited further lookups (HTTP 429) when trying a fresher timestamp
for 07-24/25, so no clean anchor for today's actual level yet.

Why this isn't stale 3 days later: this is a fundamentals-driven raise (backlog/demand-led
guidance increase, not a one-time beat on a soft compare), and defense/aerospace demand is a
multi-quarter tailwind, not a single-print catalyst that fully resolves in one session. A 13.7%
EPS beat plus a full-year guide raise typically re-rates consensus estimates for the following
quarters — analysts revise 2027 numbers upward over the following 1-2 weeks, a slower-moving
second leg of the reaction that a 3-day-old entry can still capture.

**Action:** Buy RTX (long equity or slightly OTM call spread to define risk), entry near the
current market price once a fresh quote is confirmed (mandatory per lesson #8). Target: ride
the post-guide-raise analyst-revision drift over a 5-10 trading day window, or trail a stop
~3-4% below entry.

**Confidence: 55/100.** RTX was not at a 52-week high running into the print — it moved up ON
the print, so the "already priced in" bear case (lesson #5) is weaker here. Main gap: missing
live-quote anchor for today due to the rate limit.

### Bear (sonnet)

RTX beat hard — adj EPS USD 1.89 vs USD 1.66 consensus (+14%), revenue USD 24.7B vs ~USD
22.9B est., organic sales +16% YoY, margins +65bp to 13.59%, record USD 289B backlog — and
raised FY26 EPS guidance to USD 7.10-7.25 (from USD 6.70-6.90) plus FCF to USD 8.50-8.75B.
(RTX Q2 2026 press release via PRNewswire/RTX.com, 2026-07-23; InsiderFinance.)

The market already paid for this: the stock ran from a USD 205.00 open at 13:30Z to USD
209.10 by 19:59Z on print day, a same-session +2.0% move verified via `toa price RTX <ts>
--provider twelvedata`. By 2026-07-26 it's cited at USD 209.16, within ~2.5% of its new USD
214.50 52-week high (Ticker Report). Sell-side has already re-rated: Baird to USD 240,
Susquehanna to USD 245, BofA to USD 235, Wells Fargo to USD 230, with a 23-analyst average
target of USD 226.82.

Evidence a fresh long here is thin edge, not free money: (1) this is a triple beat-and-raise
that already triggered its gap and grind to a 52-week high in the three trading days since —
buying now chases a move that already happened (lesson #5, generalized). (2) Average target
(USD 226.82) sits only ~8.5% above spot — a real but unremarkable margin-of-safety for a name
at a fresh high, not a mispriced gap; much of that upside requires the raised guidance to
convert to delivered cash flow over several quarters. (3) No fresh dissent or contradicting
data point surfaced — itself a risk: a crowded, one-directional consensus at 52-week highs has
no bear cushion if anything disappoints. (4) Entry-price staleness: anchor is a 3-day-old
close-proxy; a live quote must be re-validated before any fill (lesson #8) — twelvedata is
currently rate-limited for 07-24/07-25 pulls.

**Action: NO-TRADE.** No bearish catalyst to short into (this is a beat-and-raise, so lesson
#2's discount doesn't apply — this isn't a down move to fade), but no fresh bullish edge left
either — the move is 3 days stale, the stock is within 2.5% of a new high, and upside to
consensus targets is modest single-digit-percent over an unspecified horizon, not an
earnings-gap-sized asymmetric payout.

**Confidence: 30/100** (in "no residual tradeable edge either direction" as the correct read)
— moderate-low because sell-side momentum could still carry price higher, but that's a slow
re-rating story, not a discrete tradeable event three days post-print.

### Quant (opus)

Verified: adj EPS USD 1.89 vs USD 1.66 consensus (+13.9% surprise), revenue USD 24.7B (+14%
YoY, +16% organic), FY26 guide raised to adj EPS USD 7.10-7.25, sales USD 95-96B, FCF USD
8.50-8.75B, record USD 289B backlog. Clean, high-quality beat-and-raise, no caveat found.

Real price anchors (`toa price RTX ... --provider twelvedata`):

| Timestamp (UTC) | Price |
|---|---|
| 2026-07-22 19:59 (pre-earnings close) | 194.60 |
| 2026-07-23 13:35 (post-gap open) | 208.61 |
| 2026-07-23 19:59 (event-day close) | 209.10 |
| 2026-07-24 19:59 (last close; 07-25/26 = weekend) | 213.05 |

Decomposition: gap +7.20% at the open, then only +0.24% intraday on event day, then +1.89%
day-2 drift. Cumulative +9.48% off the pre-print close. 52-week high USD 214.50 — 0.68% below
it. Street mean target ~USD 226.82 (+6.5%); Baird raised to USD 240.

**Key structural read: the entire move was the gap. Intraday continuation on day 1 was ~zero.
The tradable event is over.**

EV calculation for a fresh 1-3 day long from Monday's open (anchor ≈ USD 213.05): base rate for
large-cap defense/aero beat-and-raise PEAD is real but small, roughly +1 to +2% excess over 60
days (~+0.03%/day), an order of magnitude below RTX's post-print daily sigma (~1.5%). P(up) =
0.55, E[gain|up] = +1.6%; P(down) = 0.45, E[loss|down] = -1.5%. Gross EV = (0.55×1.60) −
(0.45×1.50) = +0.205%. Costs: spread ~1-2bps/side on a ~USD 285B mega-cap, commission-equiv
2bps, slippage 5bps → ~13bps round-trip. **Net EV = +0.075% (7bps).**

Adverse tail: entering at a 52-week high, a 2-sigma risk-off day is -4%. Tail-to-edge ratio =
4.0/0.075 ≈ 53x — versus the institutional no-trade filter that triggers at 7-8x. Not a
size-down; a filter. The reverse trade (fade the gap) is worse: fading a genuine beat-and-raise
with a raised FCF line and record backlog fights the fundamental, and the day-2 +1.89%
follow-through says sellers are not present.

**Action: NO TRADE. Size = 0.** The catalyst has fully discharged; 100% of the edge was
captured in a gap that occurred 3 days before we can act. Net EV of 7bps does not clear costs
with margin, and the tail ratio is ~53x. The only structures with defensible EV (short-dated
defined-risk vol) are out of a cash-equity mandate. The 52-week-low discount rule (lesson #2)
cuts against us here — we're at the high, not the low.

**Confidence: 72/100** in the NO-TRADE verdict. High confidence on the facts; residual
uncertainty only on the exact PEAD magnitude, and even a 3x-larger drift assumption leaves net
EV under 0.3% against a 4% tail.

---

## Round 2 — Rebuttal

### Bull rebuttal

The quant's decomposition is correct on the facts; the arithmetic isn't in dispute. But the EV
framework may mis-specify the trade — three points:

1. **"Gap already discharged" conflates event-day timing with the guide-raise thesis.** The
   original position was never "trade the gap" — it's that a 13.7% EPS beat plus a raised FY26
   guide triggers analyst estimate revisions and price-target moves over 1-4 weeks, not 1-3
   days. The quant's own data shows day-2 drift of +1.89% after a "zero" event-day continuation
   — that could be the revision-drift signature starting. If conceding anything, it's that the
   original "5-10 day drift" framing needs the EV math run over that window, not 1-3 days — and
   that calc wasn't built. Real gap in the case, not a rebuttal.
2. **Bear's "no cushion" point is the stronger one and can't be out-argued with the anchors
   given.** 0.68% off a 52-week high with consensus target USD 226.82 only 8.5% away is a thin,
   unremarkable margin for a name that just re-rated — sell-side targets front-run this kind of
   beat quickly. No variant view that the Street is under-reacting; Baird/Susquehanna/BofA/Wells
   already moved to USD 230-245. No edge over consensus here.
3. **Defined-risk instrument doesn't fix the tail-ratio problem.** A call spread caps downside
   dollar-loss but doesn't change the sign or magnitude of EV — options carry a volatility
   premium into an event with no further scheduled catalyst before the next print, paying up for
   theta/vega with a smaller expected edge than the quant's +7bps for the underlying. Capping
   tail risk while expected value is already ~0 just guarantees a small, near-certain cost
   against a coin-flip payout — same trade with a fee.

**No rebuttal survives the quant's math.** Honest concession: Round 1's "not priced in" framing
was wrong — print-day and day-2 data show it's largely priced in within 48 hours, and the
proposed 5-10 day drift was never actually modeled. Without that calc showing positive EV over
the right horizon, size > 0 isn't justified.

**What would change my mind:** (a) EV math over a 10-20 trading day window using historical RTX
post-beat-and-raise drift distributions showing edge > tail cost at that horizon; or (b)
evidence the guide raise is itself conservative/sandbagged, arguing estimates keep moving up
further than the USD 226.82 target already prices.

**Revised position: NO-TRADE, size 0. Confidence 40/100** (down from 55) — still believe the
fundamental thesis is sound, but can't show a trade that clears cost + tail risk on a
verifiable timeframe.

### Bear rebuttal

The quant's numbers don't soften the bear case, they vindicate it. The decomposition — +7.20%
gap at the open, then ~0.24% intraday on print day (essentially flat) — is the textbook
signature of an efficient, one-shot re-rate: information digested in one jump, continuation
buyers showing up for zero of the remaining trading day. The original "no cushion" framing
undersold it — there wasn't just no cushion, there was no follow-through demand either.

On day 2's +1.89% — is that evidence against "discharged"? Not really, for two reasons. First,
magnitude: 1.89% one day after a 7.2% gap is consistent with ordinary post-event volatility
decay (sell-side price-target updates trickling in, index rebalancing flows, short covering),
not a fresh accumulating trend. Second, and more important, it still leaves the stock 0.68%
below the 52-week high — the day-2 drift ran into resistance rather than breaking out. If this
were genuine unpriced analyst-revision momentum, expect it to punch through the old high, not
stall just under it. Concede the point exists, but weigh it as noise-in-a-decaying-tail, not a
second leg.

That's exactly why the bull's "5-10 day drift" thesis doesn't hold. The quant quantified it:
net EV on a fresh long is +7bps against a 2-sigma tail of -4%, a ~53x tail-to-edge ratio,
dwarfing the 7-8x institutional no-trade threshold. The bull's thesis requires believing
sell-side re-rating (already reflected in the USD 226.82 consensus target, already visible in
Baird/Susquehanna/BofA/Wells notes) will keep pushing price further before the market re-prices
those targets into spot — but a USD 226.82 consensus target 8.5% above spot is itself already
the "priced in" state the bull says doesn't exist. The re-rating *is* the gap that already
happened.

Where to adjust: original 30/100 confidence was calibrated to "I don't have quality data, so
I'm hedging." Now there's hard EV/tail math confirming the mechanical no-edge case, a stronger,
more falsifiable argument than the qualitative "crowded consensus, no cushion" framing.

**Revised action: NO-TRADE, size=0**, agreeing with the quant. **Revised confidence: 45/100**
(up from 30) — still capped because the day-2 drift is a real, if minor, discordant data point
that can't be fully explained away, and because "gap fully discharged" is an inference from two
days of data, not a law of markets.

### Quant rebuttal

Re-verified anchor: RTX 2026-07-24 19:59Z = USD 213.05 (toa price, twelvedata). All numbers
key off the verified series USD 194.60 → 208.61 → 209.10 → 213.05.

**1. Concede the framing, keep the conclusion.** "The entire move was the gap" was sloppy.
Decomposed against the +9.48% cumulative: gap = 7.20pp (76%), day-1 intraday = 0.24pp (2.5%),
day-2 = 1.89pp (20%). So continuation exists. The question is whether n=1 day of it licenses a
drift estimate. RTX post-print daily vol ≈1.6% (elevated vs ~1.3% 30-day). A +1.89% day is
1.18σ — indistinguishable from noise. Bayesian update, prior drift 0.10%/day with prior sd
0.15%, observation noise sd 1.6%: shrinkage weight = 0.0225/(0.0225+2.56) = 0.0087. Posterior
mean = 0.10% + 0.0087×(1.89−0.10) = **0.116%/day**. One day of continuation moves the drift
estimate by 1.6bps/day. To distinguish a 0.30%/day drift from zero at 1.6% noise needs n ≈
(1.6/0.30)² ≈ 28 days. The bull is reading a single coin flip as a biased coin.

**2. Published targets argue AGAINST residual drift.** Documented revision drift rides
*estimate* revisions arriving over weeks; here Baird USD 240, Susquehanna USD 245, BofA USD
235, Wells USD 230 all landed inside 48h — before the day-2 move. That makes the +1.89% the
*consumption* of the revision catalyst, not its precursor. Bear is right on mechanism. And the
bull's own target, taken at face value: consensus USD 226.82 = +6.5% over a 12-month horizon =
0.026%/trading day = +0.19% over 7.5 days, which is *below* the 13bps round-trip cost plus
slippage. The bull's price objective, converted to his own horizon, doesn't clear transaction
cost.

**3. EV at the bull's 5-10 day horizon.** Edge scales with T, tail with √T, so stretching the
horizon genuinely helps — just not enough. At T=7.5 days, drift 0.116%/day: gross **+0.87%**,
minus 13bps = net **+0.74%**. Adverse 2σ tail = 2×1.6%×√7.5 = **8.8%**. Tail-to-edge = 8.8/0.74
= **11.9x** — improved over the 1-3 day 53x, but still above the 7-8x filter. Solving 3.2√T =
7(0.116T − 0.13) gives √T = 4.21, **T ≈ 18 trading days**. Needs ~3.5 weeks of hold to pass the
gate, no longer an event trade, and eats the Q3 print. Worse, the bull's 3-4% trailing stop is
self-defeating at 1.6% daily vol: over 10 days a 3.5% trailing stop is hit by noise with high
probability (rough first-passage estimate ~55-65%), truncating the +0.87% drift while paying
the full stop. Stop-adjusted EV is plausibly negative.

**4. Verdict: NO-TRADE, size = 0. Confidence 78/100** (up from 72). The bull's continuation
evidence is real and shouldn't have been erased, but it's 1.18σ of a single observation, and the
honest Bayesian update leaves drift at 0.116%/day — at that drift, no horizon the bull actually
proposed clears the tail-to-edge filter. Dissent logged: if 3+ consecutive continuation days
print, the shrinkage weight rises and this flips to a small starter position.

---

## Round 3 — Synthesis (opus)

### hypothesis

RTX's Q2 2026 beat-and-raise (adj EPS USD 1.89 vs USD 1.66 cons, revenue USD 24.71B +14.5%
YoY, FY26 guide lifted to USD 7.10-7.25 / USD 95-96B) was fully discharged into price in a
single overnight gap. Verified decomposition: USD 194.60 (07-22 19:59) → USD 208.61 (07-23
13:35) = +7.20% gap, then +0.24% intraday on event day, then +1.89% on 07-24 to USD 213.05 —
cumulative +9.48%, leaving price 0.68% below the 52-week high of USD 214.50 and ~6.5% below
the USD 226.82 consensus target that was itself published before the day-2 move. There is no
residual post-earnings-announcement drift large enough to clear transaction costs and tail
risk on any event-scoped horizon.

- **direction:** none
- **confidence:** 76/100 (in the no-edge conclusion)

### plan

- **ticker:** RTX
- **action:** no-trade
- **entry:** none
- **exit:** none
- **expected_profit_pct:** 0.00% (position size = 0)

| Horizon | Net EV | Adverse 2σ tail | Tail-to-edge | Filter (7-8x) |
|---|---|---|---|---|
| 1-3 day | +0.075% (7bps after ~13bps costs) | -4.0% | ~53x | fail |
| 7.5 day (bull's own horizon) | +0.74% | -8.8% | 11.9x | fail |
| ~18 day | clears | — | ~7-8x | passes, but no longer an event trade — bleeds into the Q3 print |

The bull's proposed 3-4% trailing stop compounds the problem: at RTX's realized daily vol the
first-passage probability of touching that stop within 10 days is ~55-65%, making stop-adjusted
EV plausibly negative even at the horizon where gross EV looks acceptable. All three personas
converged on NO-TRADE by Round 2 (bull 55→40, bear 30→45, quant 72→78).

### dissent

Two unresolved items, ranked:

**(a)** The whole forward view is built on n=1 post-event session. 2026-07-23 was a Thursday,
07-24 Friday was the only full post-gap session before research ran on 2026-07-26 (weekend).
The quant's posterior drift of 0.116%/day is a heavy shrink of a single 1.89% observation
classified as 1.18σ noise — a defensible prior-dominated estimate, but it is one data point,
and "day-2 was consumption of the catalyst" vs. "day-2 was leg one of a breakout" is not
separable from that single bar. RTX closed 0.68% from its 52-week high on rising price. The
quant logged the correct trip-wire (3+ consecutive continuation days flips this to a small
starter position) but no such data can exist until 07-29 at the earliest, by which point the
tradeable window has narrowed further. Post-mortem question: did RTX break USD 214.50 on
Monday 07-27 / Tuesday 07-28? If yes, the panel's "gap-and-stall" read was an artifact of a
two-session sample, not a property of the event.

**(b)** An unreconciled price discrepancy nobody caught. The bear asserted "~USD 209.16 by
2026-07-26" while the quant independently verified a USD 213.05 close on 07-24 — a 1.9% gap
between two personas' spot anchors, never challenged in Round 2. Since 07-25 and 07-26 are a
weekend, USD 213.05 is the correct last print, and the bear's figure appears to be a stale
event-day quote. The bear's Round 1 case ("within 2.5% of the 52-week high," "no cushion
left") was therefore argued off the wrong anchor — the real gap to the high was 0.68%, which
*strengthens* the bear's stretched-valuation point but also means the bear reached the right
verdict via a wrong number. This mirrors the previously logged false-consensus-under-a-data-
blackout failure mode: three personas agreeing is weak evidence when their inputs disagree by
1.9% and nobody reconciles it.

### rationale

The event is over: 76% of the +9.48% cumulative move printed as an overnight gap before any
participant could transact, intraday continuation on the print day was +0.24% (statistically
indistinguishable from zero), and the sell-side re-rate to a USD 226.82 consensus target was
published *ahead* of the last observed move rather than as a leading indicator of the next one.
Every horizon that produces enough gross EV to matter also produces a 2σ adverse tail 12-53x
larger than the edge, and the only horizon that clears the tail filter (~18 trading days)
abandons the event thesis entirely and carries the position into the Q3 print. NO-TRADE at
size zero — the fundamental thesis (backlog, guide raise, margin trajectory) may well be right,
but a correct view that is already in the price is not a trade.

*Paper-trading simulation only. Not financial advice.*
