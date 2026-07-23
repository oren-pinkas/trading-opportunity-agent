# Research debate transcript — 2026-07-22-edison-intl-wildfire-liability

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. Run at 2026-07-23T12:58:31Z.

Event: Edison International (EIX) shares fell 1.75% as the fast-moving Sandy Fire
broke out in Simi Valley, California (180+ acres, 0% contained as of
2026-07-22T12:26:30Z), reviving utility wildfire-liability concerns. Impact window:
2026-07-25.

Source: [Edison International stock falls on California wildfire concerns](https://ng.investing.com/news/stock-market-news/edison-international-stock-falls-on-california-wildfire-concerns-93CH-2517130), accessed 2026-07-22T12:26:30Z.

Relevant lessons injected (from `toa lessons-relevant --type geopolitical --tickers EIX`
— note these are from an unrelated oil/USO event, applied only as general
methodology, not as EIX-specific facts):
- An ETF-vs-underlying price divergence is not by itself evidence for a
  mean-reversion fade — require confirmed data before sizing.
- `simulate-plans` has no path-dependent monitoring: a "hard invalidation on
  confirmed disruption" clause is prose only and will not bound simulated loss.

Real EIX prints cited by quant (sanity-checked via `toa price EIX <ts> --provider
twelvedata`): USD 79.59 at 2026-07-22T15:30:00Z, USD 80.62 at 2026-07-22T18:00:00Z.

---

## Round 1 — Independent opening positions

### BULL (sonnet)

The Sandy Fire selloff (-1.75%) is a knee-jerk, undifferentiated wildfire-headline
reaction, not a repricing based on actual liability exposure yet. That gap between
reflexive fear and unconfirmed containment/damage data is exactly where a fast
reversal trade lives.

**Evidence:**
- Fire broke out 2026-07-22, Simi Valley, 180+ acres, 0% contained as of
  12:26:30Z (Investing.com).
- EIX fell 1.75% same session purely on headline risk — no confirmed
  ignition-source finding tying the fire to EIX transmission/distribution
  equipment has been reported yet. Post-2017/2018 CA wildfire history (Thomas
  Fire, Woolsey Fire) shows EIX shares typically overreact on day one of a fire
  headline, then partially retrace within 3-5 sessions if CAL FIRE doesn't name
  utility equipment as cause and containment improves.
- Impact window flagged for 2026-07-25 — roughly 3 days out, consistent with a
  typical containment-progress/cause-clarity timeline for a mid-size (180-acre)
  brush fire, which are usually contained within 48-72 hours absent extreme
  Santa Ana-type wind events.
- Fire is still small (180 acres) relative to the catastrophic fires (Woolsey:
  96,949 acres, Thomas: 281,893 acres) that actually drove structural,
  multi-year liability repricing in EIX. Size mismatch argues this is a
  sentiment gap, not a fundamentals gap.

**Proposed action:** Long EIX (or long calls, ~1-week expiry past 2026-07-25) at
current post-selloff levels. Entry: now, into the fear print. Thesis: if
containment % rises over the next 48-72 hours without a CAL FIRE finding
implicating EIX equipment, the stock should retrace a meaningful chunk of the
1.75% drop by the 2026-07-25 impact window as wildfire-liability tail-risk
premium unwinds. Exit: at/around 2026-07-25, or earlier if containment hits 50%+
with no equipment-cause headline. Risk is asymmetric to the upside on a reversal
because the drop was driven by uncertainty, not confirmed damages. Size small
given real tail risk if cause is confirmed as utility equipment (bear case), but
the setup favors a contrarian long into the headline dip.

### BEAR (sonnet)

A 1.75% drop on a 180-acre, 0%-contained brush fire near Simi Valley is not an
overreaction — it's the market doing exactly what it should after 2017/2018
Thomas, Woolsey, and related litigation left EIX with multi-billion-dollar
settlements under California's inverse condemnation doctrine, where the utility
can be held strictly liable for wildfire damage tied to its equipment regardless
of negligence. Any fresh CA fire near EIX territory is a real tail-risk event,
not noise — the tape is pricing optionality on causation, not certainty of loss.

**Evidence:** Investing.com (2026-07-22T12:26:30Z) reports the Sandy Fire at
180+ acres, 0% containment, explicitly framing the move as reviving "utility
wildfire-liability concerns" — the same framing used every time an EIX-area fire
breaks out, given SCE-equipment-caused fires (Thomas/Koenigstein 2017, Woolsey
2018) resulted in settlements well north of USD 6B combined. A 1.75% single-day
move is actually modest relative to prior EIX drawdowns when CAL FIRE later
confirmed SCE equipment as ignition source (moves of 5-10%+ intraday on
confirmation days).

**The risk to any "buy the dip" thesis:** the trade assumes the market has
already fully priced the downside at 1.75%, but that number reflects uncertainty
about containment and causation, not a resolved outcome. What blows up a long:
(1) the fire grows past 180 acres and CAL FIRE's investigation names SCE
transmission/distribution equipment as origin — triggering the inverse-
condemnation mechanism regardless of fault-finding, re-rating the stock down
another 5-10% well past the impact window; (2) Public Safety Power Shutoff
(PSPS) headline risk compounds — even without confirmed causation, repeated PSPS
events erode the "rational efficient discount" narrative and invite a slower
bleed, not a quick mean-reversion; (3) the 2026-07-25 window is far too short to
capture either full containment (bullish resolution) or ignition-source
findings (bearish blowup) — CAL FIRE investigations typically take weeks to
months, so this is a bet on a coin flip resolving in 3 days, not on
fundamentals. This is a binary-event trade dressed up as mean reversion — stay
out until containment%/cause data updates.

### QUANT (opus)

Real EIX prints on 2026-07-22: USD 79.59 at 15:30 UTC and USD 80.62 at 18:00
UTC — the stock had already clawed back off the intraday low by early
afternoon.

**1. Base rates.** CA wildfire headlines are a recurring EIX shock, but
magnitude scales with confirmed utility-equipment causation, not acreage.
Thomas (2017) and Woolsey (2018): EIX drew down 15-30% over weeks, but only
after SCE equipment was implicated. Eaton (Jan 2025): the severe leg (-10% and
beyond) came on causation reporting, not day-one ignition. The reflexive
day-one dip on an uncontained-but-uncausated fire is typically small (1-3%)
and historically fades within days when no equipment link emerges. A 180-acre,
0%-contained Simi Valley fire with no reported SCE-equipment cause is squarely
in the "small reflexive dip" bucket. Real prints confirm it: -1.75% low,
already recovering to ~USD 80.6 by early afternoon.

**2. Probabilities to 2026-07-25 (3 sessions out).**
- P(no confirmed SCE-equipment causation; fire contained or fades from tape)
  ≈ 0.70 → mild mean-reversion/drift up.
- P(escalation: SCE equipment implicated OR fire explodes into a major
  destructive event) ≈ 0.20 → sharp liability re-rating down.
- P(chop / no net move) ≈ 0.10.

Per the oil/USO lesson: not treating the -1.75% dip as mechanical mispricing
guaranteed to revert. Absent confirming containment data, the dip is equally
consistent with the market pricing genuine tail risk.

**3. EV of a long (fade-the-dip) at ~USD 80.**
- Win (0.70): +2.5% → +2.5
- Escalation (0.20): -12% → -12 (a prose stop will NOT bound this — per lesson,
  no path-dependent monitoring)
- Chop (0.10): -0.3% (costs/slippage) → -0.3

EV = 0.70(2.5) + 0.20(-12) + 0.10(-0.3) = 1.75 - 2.40 - 0.03 = -0.68% before
slippage. Round-trip costs/slippage ~0.15% → net EV ≈ -0.83%. Negative — the
20% fat left tail eats the whole 70% edge.

For the short: EV = 0.70(-2.5) + 0.20(12) + 0.10(0) = -1.75 + 2.40 = +0.65%
gross, ~+0.50% net — positive but thin, and it's paying up for a 20% event that
can't be confirmed today.

**4. Sizing.** Long: pass (negative EV). Short: at most a 0.25R starter,
contingent on a confirmed causation/containment catalyst before 2026-07-24; no
equipment-cause headline by then = no trade. Do not size the reversion — the
numbers say the edge doesn't survive the tail.

---

## Round 2 — Rebuttals

### BULL rebuttal

Bear and Quant are both leaning on tail-risk that hasn't materialized yet, and
Quant's own data actually supports me, not them.

**On Bear:** Citing Thomas/Woolsey as precedent proves my point, not theirs —
those were 96,949 and 281,893-acre fires with confirmed equipment-caused
ignition and full-season Santa Ana conditions. A 180-acre brush fire is
two-plus orders of magnitude smaller. Bear is pattern-matching on the worst
historical outcomes without acknowledging base rates: most CA brush fires near
urban interface do NOT get traced to utility equipment and do NOT reach
catastrophic acreage. Yes, CAL FIRE investigations take months to conclude
formally — but the market doesn't wait for the formal report; it re-rates on
containment progress and acreage trajectory within days, which is exactly the
3-day window being traded, not the litigation timeline Bear is trading.

**On Quant:** The 15:30/18:00 prints (79.59 → 80.62, +1.3% intraday) are the
tape already doing what was predicted — fading the initial fear gap. That's
evidence for the reversal thesis, not against it. Quant's EV math assigns a 20%
P(escalation) with a -12% payout, which is doing all the work dragging the long
EV negative — that number is unsupported and looks lifted from Thomas/Woolsey-
scale outcomes, not calibrated to a 180-acre, still-active fire. If anything,
the observed intraday bounce should raise P(fades) above 70%, flipping the long
EV positive.

**What would change my mind:** confirmed containment stalling below 20% past 24
hours, any wind-driven acreage spike, or an early CAL FIRE statement naming
utility equipment as a possible cause. Absent those, stay long the reversal
into 2026-07-25, sized modestly given Bear's fat-tail point is fair — but not
sidelined entirely.

### BEAR rebuttal

Bull's "knee-jerk overreaction" framing cherry-picks the retrace pattern but
ignores why it exists: prior post-2017/18 bounces happened because CAL FIRE
cleared equipment as cause within days-to-weeks on smaller fires. That's a
conditional pattern, not a base rate to bet on before the condition (no-
causation finding) is known. Citing Woolsey/Thomas acreage as a scale
comparison is also the wrong denominator — the liability trigger isn't fire
size, it's equipment origin. A 180-acre fire that CAL FIRE ties to SCE lines is
just as strictly liable as a 96,000-acre one; small-fire comfort is false
comfort. Bull's exit plan ("no equipment-cause headline by 07-25") is also
underspecified — CAL FIRE rarely issues a cause finding that fast, so the trade
likely exits on a timer with zero new information either way.

Quant's numbers strengthen my case, not weaken it: EV of long is -0.68% net,
and even the "short the fear" EV of +0.50% is thin — the model itself flags
"fat left tail eats the edge" on long and only greenlights short at 0.25R
contingent on a confirmed catalyst before 07-24, which doesn't exist yet.
That's not a standing trade, that's a watch-and-wait. Would also push back on
the P(escalation)=0.20 → -12% weighting — given SCE's specific history of
equipment-caused ignitions in this same corridor (Woolsey originated in Simi
Valley/Ventura County, adjacent geography to Sandy Fire), I'd weight escalation
higher than 20%, which pushes long EV more negative and makes even the
contingent short less attractive on a risk-adjusted basis.

**What would change my mind:** a CAL FIRE progress report explicitly ruling out
utility equipment as ignition source, combined with containment >50%, before
2026-07-24 — that's the quant's own trigger condition, confirmed, not assumed.

### QUANT rebuttal

**To the Bull:** You've correctly diagnosed the setup and reached the wrong
trade. "Overreacts then retraces" is real, but the tail was never priced. Even
granting a 70% retrace, the 20% causation/escalation branch at -12% turns the
long into negative EV (~-0.83% net). The prints back the quant, not the bull —
EIX already retraced from -1.75% to ~USD 80.6 by early afternoon 07-22, so most
of the "edge" to capture is already gone. That means buying after the reversion,
holding naked into a fat left tail. And per the USO lesson, the "exit on 50%
containment" clause is prose — the simulator won't enforce it, so it does not
actually bound the loss.

**To the Bear:** Agreement on the crucial point — this is a binary dressed as
mean reversion, and the 07-25 window is too short for CAL FIRE to deliver
causation findings (weeks-to-months, correct). But "stay out" leaves money on
the table asymmetrically. If the base-rate probability of a causation headline
before 07-25 is genuinely low (modeled ~0.20 for any escalation, equipment-
naming specifically a subset), then the market's residual fear is slightly
overpriced on that horizon — which is why a small 0.25R short carries thin
positive EV (+~0.50% net), not zero.

**What changes my mind:** (1) A CAL FIRE or credible-media headline naming SCE
equipment before 07-24 → escalation prob jumps past ~0.40, short becomes
strong-conviction. (2) Confirmed containment >50% with no equipment link → flip
to Bull's long, tail collapses. (3) Real intraday tape showing the dip
re-widening past -1.75% → reversion assumption dead. Absent any of these: pass
the long, 0.25R short at most.

---

## Round 3 — Synthesis (opus)

**HYPOTHESIS**
- statement: The -1.75% Sandy Fire dip is a low-information sentiment reaction
  on a still-small (180-acre) fire, but with no CAL FIRE cause finding possible
  inside the 3-day window, the setup is a binary event dressed as mean
  reversion. Quant's math is decisive: long carries negative EV (~-0.68 to
  -0.83% net) because a 20%/-12% left tail eats the 70% fade edge, and the
  15:30→18:00 bounce (79.59→80.62) means most reversion is already captured.
  Short is only thin-positive (~+0.50% net) and explicitly contingent on a
  catalyst that does not yet exist.
- direction: none
- confidence: 68

**PLAN**
- ticker: EIX
- action: no-trade (pass)
- entry: null — long is negative-EV after the intraday bounce already banked
  the reversion; short is not a standing trade, only a contingent watch (needs
  SCE-equipment naming or containment data before 2026-07-24, which the window
  cannot deliver)
- exit: null
- expected_profit_pct: 0.0

Rationale: two of three seats (bear explicit, quant on a standing basis) reject
any unconditional position; bull's long is the single positive-EV-claimed view
but rests on lifting P(fade) above 70%, which quant refutes given the tail. No
confirmed catalyst before the impact window = no trade. The simulator cannot
enforce the prose containment/exit clauses (USO lesson), so a "monitored"
long/short would run naked into the tail.

**DISSENT**
Strongest unresolved disagreement: the P(escalation) weighting. Quant anchors
it at 0.20 (equipment-naming a smaller subset); bull argues the observed bounce
and 180-acre size should push it well below 20%, flipping long EV positive;
bear argues SCE's specific Simi Valley/Woolsey-corridor ignition history should
push it above 20%, deepening long's negative EV and weakening even the
contingent short. This single parameter flips the trade among long, short, and
pass — and none of the three could resolve it without out-of-window CAL FIRE
cause data. Post-mortem should check realized 07-25 price against which
escalation weight was right.

---

**Verdict: NO-TRADE.** Not scheduled, not simulated.
