# Research Debate Transcript — 2026-07-22-qantas-pilots-strike-ballot

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. Processed in isolation — no other opportunity referenced.

Event: Australia's Fair Work Commission approved a strike ballot for Qantas's
1,700 long-haul pilots. Voting opens 2026-07-27 and closes 2026-08-03. Pilots are
pushing for pay above Qantas's 3% offer plus work-life-balance ("golden day")
leave concessions. Ticker: QAN.AX. Dossier impact_window: 2026-07-27. Source:
["Qantas Faces Potential Long-haul Pilot Strike" — LoyaltyLobby](https://loyaltylobby.com/2026/07/20/qantas-faces-potential-long-haul-pilot-strike/)
(accessed 2026-07-22).

Institutional lessons injected: (1) a headline alone is not proof of a tradeable
price dislocation — require confirmed price/volume reaction; (2) simulate-plans
has no path-dependent monitoring, so invalidation must be a concrete price level
or date, not prose.

---

## Round 1 — Independent Research

### BULL (sonnet)

**Data gap disclosure:** `toa price QAN.AX <ts> --provider twelvedata` returned
HTTP 404 for both event-window timestamps and a control historical date —
indicating no usable real price data for this ticker in this environment. No
confirmed price/volume reaction could be cited.

**Thesis:** The ballot opening (Jul 27 – Aug 3 voting window) is a procedural
escalation step, not a strike. History suggests Qantas management resolves these
disputes before mass long-haul disruption, with resolution acting as a bullish
catalyst. The pilots' asks (golden leave days, more callout notice, pay slightly
above 3%) are moderate and bridgeable, not an existential 2011-style dispute.

**Evidence:**
- Ballot mechanics: FWC approved the ballot; voting for ~1,700 long-haul pilots
  runs Jul 27 – Aug 3, 2026; a ballot is not itself a strike and protected action
  typically requires further notice after a "yes" vote — [HR Leader](https://www.hrleader.com.au/law/28418-qantas-pilots-to-vote-on-industrial-action),
  [Australian Aviation](https://australianaviation.com.au/2026/07/qantas-long-haul-pilots-to-vote-on-industrial-action/)
- First long-haul pilot industrial-action vote in 15 years, following two years
  of AIPA/AFAP negotiations — [HR Leader](https://www.hrleader.com.au/law/28418-qantas-pilots-to-vote-on-industrial-action)
- Gap between sides is narrow: work-life-balance concessions plus pay "slightly
  above" the 3% offer — [NZ Herald](https://www.nzherald.co.nz/business/companies/airlines/qantas-pilots-to-consider-strike-as-long-awaited-project-sunrise-aircraft-about-to-arrive/premium/3SUJXLBDKNELFEHV75VQVMCCFA/)
- 2011 precedent: once that dispute resolved and operations resumed, QAN shares
  rose 5.5% on certainty over prolonged disruption fear — [ParlInfo chronology](https://parlinfo.aph.gov.au/parlInfo/search/display/display.w3p;query=Id:%22library/prspub/1248920%22)
- Timing coincides with Qantas's Project Sunrise long-haul aircraft arrival, a
  positive fleet/growth catalyst the market may be underweighting — [NZ Herald](https://www.nzherald.co.nz/business/companies/airlines/qantas-pilots-to-consider-strike-as-long-awaited-project-sunrise-aircraft-about-to-arrive/premium/3SUJXLBDKNELFEHV75VQVMCCFA/)

**Proposed action:** Long QAN.AX. Entry only on confirmed ≥2% intraday weakness
below last close prior to the Jul 27 headline, verified at Jul 27 Sydney open.
Exit +4% from entry or by 2026-08-10, whichever first. Invalidation: close below
-5% from entry, or any confirmed protected-action strike-notice date issued
before 2026-08-10 (exit same-day, no averaging down).

**Confidence: 35/100.** No confirmed price data to anchor entry logic; 2011
precedent is one 15-year-old data point under different conditions; cannot rule
out a "yes" vote reading as escalation rather than de-escalation.

**Key risks:** no confirmed price reaction exists to trade against; a strong
"yes" vote could read as escalation given pent-up 15-year grievance; Qantas's
post-2011 reputational sensitivity is asymmetric downside if talks fail publicly;
the Aug 10 invalidation window may be too short if talks drag past ballot close.

---

### BEAR (sonnet)

**Thesis:** The ballot (voting Jul 27 – Aug 3) follows pilots rejecting a 25%-
over-4-years offer, now demanding pay above 3% plus golden-day leave. This would
be the first long-haul industrial-action vote in 15 years. Qantas's 2011 history
shows disputes can escalate faster/costlier than management signals, and
long-haul disruption hits Qantas's highest-margin international/Project Sunrise
routes disproportionately. The market may be underpricing disruption/cost risk
into early August.

**Evidence:**
- Ballot approved by FWC, voting opens Jul 27, covering 1,700 long-haul pilots —
  [LoyaltyLobby](https://loyaltylobby.com/2026/07/20/qantas-faces-potential-long-haul-pilot-strike/)
- Pilots rejected a 25%-over-4-years EA offer (two-thirds against), demanding
  golden days, callout notice, and >3% p.a. — [Australian Aviation](https://australianaviation.com.au/2026/04/qantas-long-haul-pilots-knock-back-pay-deal-despite-union-support/),
  [HCA Mag](https://www.hcamag.com/au/specialisation/industrial-relations/qantas-long-haul-pilots-to-vote-on-industrial-action/583006)
- First long-haul strike vote in 15 years, potential actions from work stoppages
  to sign-on delays — [Inquirer News](https://newsinfo.inquirer.net/9080/qantas-pilots-move-towards-first-strike-in-45-years),
  [HR Leader](https://www.hrleader.com.au/law/28418-qantas-pilots-to-vote-on-industrial-action)
- TWU/AIPA framing this as a "step towards strikes" over a "subpar offer" —
  [TWU press release](https://www.twu.com.au/press/qantas-group-pilots-take-step-towards-strikes-over-subpar-offer/)

**Data gap:** No verified QAN.AX price via `toa price --provider twelvedata`
(HTTP 404 across all tested dates). A WebSearch aggregator snippet mentioned an
unverified, non-timestamped price near AUD 10.41 — not treated as ground truth.
No evidence of a confirmed price/volume dislocation tied to the Jul 20 headline.

**Proposed action:** Short QAN.AX. Entry at verified ASX close 2026-07-27. Exit
at close 2026-07-31 (before the Aug 3 ballot close). Invalidation: hard stop-out
if QAN.AX closes ≥3% above verified entry before 2026-07-31 (cover immediately);
if no verified price obtainable by 2026-07-28, treat as void/no-fill. Fallback:
if no confirmed price reaction exists by Jul 27, recommend NO TRADE — a
ballot-approval headline three days before voting opens, with the actual outcome
not known until Aug 3 plus further notice periods, is too early and diffuse a
catalyst.

**Confidence: 35/100.** Real IR-risk narrative but zero confirmed price/volume
evidence; ballot is a procedural step, not a strike; 2011 history shows
management can neutralize disruption faster than expected.

**Key risks:** no confirmed dislocation to short into (may already be priced);
long lead time to actual disruption via FWC notice requirements; Qantas
fleet/margin resilience (Project Sunrise, strong domestic/leisure demand); data
gap prevents plan execution as written; daily-close invalidation checks are not
continuous monitoring, so an intraday spike could go uncaught.

---

### QUANT (opus)

**Thesis:** No tradeable edge exists at the Jul 27 impact window. It is an
informationally empty date — the ballot approval was already public Jul 20-22,
results don't land until ~Aug 3, and protected action then requires 3 business
days' notice before any stoppage. Recommend NO TRADE.

**Evidence / quantitative reasoning:**
- The Jul 27 date is a non-event: ballot news already in the tape by the impact
  window; nothing decision-relevant resolves on that date —
  [LoyaltyLobby](https://loyaltylobby.com/2026/07/20/qantas-faces-potential-long-haul-pilot-strike/),
  [HCA Mag](https://www.hcamag.com/au/specialisation/industrial-relations/qantas-long-haul-pilots-to-vote-on-industrial-action/583006)
- Base rate: Australian protected-action ballots almost always pass
  (P(pass) ≈ 0.90); it's been 15 years since Qantas long-haul pilots last
  struck, and ballots are overwhelmingly used as negotiating leverage
  (P(any protected action | passes) ≈ 0.40; P(material long-haul strike |
  action) ≈ 0.30) → P(material long-haul strike) ≈ 0.11, and none of it falls
  inside the 7/27 window
- Magnitude: the 2011 full-fleet grounding — a far more extreme event — cost
  ~A$68M against ~A$16B revenue (<0.5%), and shares rose 5.5% on resolution —
  [Wikipedia — 2011 Qantas industrial disputes](https://en.wikipedia.org/wiki/2011_Qantas_industrial_disputes),
  [Al Jazeera 2011](https://www.aljazeera.com/amp/economy/2011/10/30/qantas-grounds-fleet-over-labour-dispute).
  Long-haul is the smaller, lower-margin segment vs domestic (~A$6B intl/
  ~A$689M EBIT vs ~A$8B domestic/~A$977M EBIT) — [Stockhead](https://stockhead.com.au/uncategorized/criterion-project-sunrise-promises-a-new-dawn-for-qantas-and-investors/).
  A ~1% pay gap is cheap to bridge, favoring settlement over stoppage
- EV after ASX short costs (borrow, FX/spread) is negative or indistinguishable
  from noise given no confirmed dislocation and no bounded monitoring
- Data caveat: `toa price QAN.AX --provider twelvedata` returned HTTP 404 for
  all tested timestamps — no confirmed spot, baseline, or volume reaction. Per
  lesson 1, a headline is not inferred as a dislocation.

**Proposed action:** NO TRADE on QAN.AX. No entry, exit, or invalidation — no
defined edge, no verifiable price anchor. If future data confirms a real
gap-down on ballot-pass (Aug 3+) that later de-escalates, the tradeable setup
would be a mean-reversion long on resolution (the 2011 analogue) — a different
event, out of this window's scope.

**Confidence: 78/100** on the NO TRADE call.

**Key risks:** data blindness (an actual gap-down could exist that can't be
seen); escalation surprise if the union hard-lines given Project Sunrise raising
Qantas's cost of a stoppage (more leverage to pilots); post-COVID Australian IR
may be more strike-prone than the 15-year gap implies; the genuinely tradeable
event may be Aug 3 + strike notice, not Jul 27.

---

## Round 2 — Rebuttal

### BULL rebuttal

Concedes Quant's base-rate math (≈11%) is reasonable but argues it should size a
position, not preclude one — an 11% tail with a demonstrated 2011 upside
resolution and a market that reliably overprices near-term IR headline risk is a
setup for a disciplined contrarian long. Pushes back on Bear: if QAN.AX hasn't
moved by Jul 27, that's evidence the market already agrees disruption risk is
low, undercutting the short rather than confirming it. Argues neither addressed
investor positioning going into results — IR ballots this close to a
fleet-renewal narrative (Project Sunrise) tend to be treated as noise by
long-only holders, so any selloff is more likely mechanical/liquidity-driven and
mean-reverts.

**Concedes the timing flaw:** Jul 27 is ballot-open, not ballot-result; trading a
dip there fades generic pre-event jitters, not the actual catalyst. Revises
entry window to bracket the real event (~Aug 3 result + 3-day notice period),
matching the 2011 analogue where resolution/de-escalation was the bullish
trigger.

**Revised position:** Long QAN.AX. Entry only on confirmed ≥2% intraday weakness
in the window 2026-08-03 to 2026-08-06, triggered by the ballot result and/or
strike-notice headline — no entry on Jul 27 alone. Exit +4% from entry or by
2026-08-14, whichever first. Invalidation: -5% from entry, OR a confirmed
protected-action notice specifying an actual stoppage date (close and stand
aside, no averaging down). If no entry trigger fires by 2026-08-07, becomes NO
TRADE for the round.

**Confidence: 30/100** (down from 35 — conceding ground on timing, narrowing to
a conditional, event-anchored dip-buy).

### BEAR rebuttal

Pushes back on Quant's framing: the thesis was never "strike happens" but "strike
risk premium gets repriced during peak uncertainty" — an 11% chance of a costly
disruption to the highest-margin flying can produce a few nervous trading days
even if the modal outcome is nothing. Pushes back harder on Bull's 2011 analogy:
2011 was a company-initiated, decisive full grounding that ended uncertainty in
one stroke; this is a pilot-initiated ballot that, if it passes, opens a
multi-week window of ambiguous, incremental escalation with no obvious
circuit-breaker — comparing a sharp shock-and-resolve to an open-ended live-fire
process is comparing different things.

**Concedes ground:** Quant's point that Jul 27 is informationally empty is
correct and is the strongest objection to the original trade — the ballot has
been public since Jul 20-22, so entering specifically at Jul 27 conflates
"ballot period starts" with "material news arrives." Also concedes the magnitude
argument: long-haul being smaller/lower-margin than framed, and a ~1% pay gap
being cheap to bridge, caps plausible downside and weakens the "asymmetric to
the downside" framing.

**Revised position:** NO TRADE for the original Jul 27–31 window (withdraws the
Round 1 short). Conditional watch only: if the ballot passes and is announced
~Aug 3, consider a small short QAN.AX at close 2026-08-03 (or next session open
if after-hours), exit close 2026-08-06 or on confirmed strike-notice filing
(whichever first), invalidation +3% close before exit (cover). Contingent on
verified real price data; defaults to NO TRADE absent that, per the Round 1
fallback rule.

**Confidence: 25/100** on any short (down from 35); ~60/100 that NO TRADE is
ultimately the correct overall call once Aug 3 data is in hand — converging
toward Quant without fully adopting it, since a positive ballot result remains a
real, undertraded dated catalyst worth a small contingent position.

### QUANT rebuttal

Stress-tests the NO TRADE call: Bull's 2011 point cuts against a directional bet,
not for one — that pop resolved a tail event that had already crushed the
stock; there is no analogous overhang here to resolve, so no fear priced in means
no resolution pop to harvest. Bear's margin-concentration point is the stronger
of the two and moves Quant on magnitude (not probability) — a targeted long-haul
stoppage hits mix harder than the 2011 full-grounding comparison implied — but
that only matters downstream of the ~11% branch firing, which happens after
every proposed window anyway; bigger conditional loss × unchanged tiny
probability × wrong window still nets to noise.

Credits both Bull and Bear for refusing to enter on the headline alone (Bull's
≥2% confirmed-weakness trigger; Bear's fallback-to-NO-TRADE rule) as genuinely
disciplined contingent construction — but notes discipline on entry trigger
lowers the variance of being wrong, it doesn't create positive expectancy: Bull
is buying a dip with no identified reason to reverse before results are in; Bear
was shorting a window that closed before his own catalyst (Aug 3) even landed.

**One place the debate moved it:** identifies the only spot with an identifiable
edge — Aug 3+, mean-reversion long, echoing Bull's own 2011 analogue: if the
ballot passes (expected, P≈0.90) and the stock sells off on the headline despite
no strike notice and the mandatory 3-day buffer still ahead, that overreaction
("mandate ≠ stoppage" confusion) is fadeable.

**Final position:** NO TRADE at Jul 27. One armed conditional: half-unit
mean-reversion long QAN.AX, triggered only by confirmed ballot PASS + ≤-3%
verified same-session move + no strike notice, on/around 2026-08-03. Exit +3% or
2026-08-12, whichever first. Invalidation: strike notice filed (immediate exit)
or -3% from entry (stop).

**Confidence: 74/100** on NO-TRADE-at-7/27 (down slightly from 78, crediting
Bear's magnitude point and both sides' entry discipline); 55/100 on the armed
Aug-3 conditional being correctly structured if triggered.

---

## Round 3 — Synthesis (opus, neutral)

### Hypothesis
The Jul 27 ballot-open is informationally empty (news public since Jul 20-22;
results ~Aug 3; protected action requires 3 business days' notice thereafter), so
no trade is warranted in the dossier's stated Jul 27 impact window. The only
structurally sound edge the debate surfaced is a conditional mean-reversion LONG
on a verified over-reaction to the ~Aug 3 ballot result — supported by the 2011
analogue (full grounding, stock +5.5% on resolution), long-haul's cheap-to-bridge
~1% pay gap, and a low base-rate probability (~11%) of material disruption. This
trade is armed, not active, and contingent on real price data that currently
cannot be obtained.

**Direction:** no_trade (near-term); conditional long if and only if the Aug-3
trigger fires. **Confidence:** 72/100 on NO-TRADE-at-7/27; 52/100 on the armed
Aug-3 long being correctly structured if triggered.

### Plan
- **Ticker:** QAN.AX
- **Action:** no_trade (armed conditional buy)
- **Entry:** 2026-08-03 to 2026-08-06, IF ballot result confirmed PASS AND
  QAN.AX prints a verified same-session move ≤-3% vs prior close (real data
  required, no stub) AND no protected-action strike notice specifying an actual
  stoppage date has been filed. Half-unit size. Expires unfilled if no trigger by
  2026-08-07 close.
- **Exit:** +3% from entry (take-profit), or 2026-08-12 hard time-stop, whichever
  first.
- **Expected profit:** +3% target on a half unit (~+1.5% position-level); net EV
  only marginally positive after ASX costs, hence half-size and hard contingency.
- **Invalidation (concrete):** strike notice specifying a stoppage date filed at
  any time → immediate exit/do not enter; -3% from entry → hard stop; entry
  price unverifiable via real market data → trade voided; no qualifying
  dislocation by 2026-08-07 close → expires NO TRADE.

### Dissent
The unresolved core disagreement is direction, and it is not cosmetic. Bear's
Round 1 thesis — first long-haul strike vote in 15 years, long-haul as the
highest-margin segment, asymmetric downside into early August — was conceded by
Bull and Quant on timing and magnitude but never actually refuted on direction.
The panel's convergence on a mean-reversion long rests on one load-bearing
assumption: any Aug-3 drop is an over-reaction that reverts (the 2011 analogue).
If instead the ballot passes by a wide margin and the union signals intent to
file notice, the same -3% print is not a dislocation to fade — it is the start
of a repricing, and the armed long buys directly into a falling knife. The
trigger's "no strike notice filed" guard is thin: notice can follow entry by
days, inside the holding period, leaving the -3% stop as the sole backstop.
Post-mortem test: if the Aug 3 trigger fires, check whether a strike notice
followed within the 8-day hold and whether the stop or the profit target hit
first.

### Rationale
Quant's timing argument was treated as dispositive for the Jul 27 window because
both directional personas explicitly conceded it — the dossier's own impact
window is anchored to a non-event, and neither could construct a trade there
that survives "ballot results don't land until ~Aug 3." That collapses the
near-term decision to NO TRADE with high agreement. On the conditional trade,
the long/mean-reversion framing was favored over Bear's short because the weight
of falsifiable evidence favors it: the 2011 precedent is a directly comparable,
higher-severity event that resolved upward; the ~1% pay gap is quantifiably
cheap to bridge; and the ~11% compound base rate means the market is more likely
to over-react to a headline than to correctly price a low-probability stoppage.
Two of three personas (Bull, Quant) independently landed on the long/
mean-reversion structure, while Bear itself down-weighted its short to 25/100 and
assigned 60/100 to NO TRADE overall.

The decisive confidence-limiter is the unresolved price-data gap: no persona
could obtain real verified QAN.AX prices (`toa price --provider twelvedata`
returned HTTP 404 at every tested timestamp). This is structural, not a modeling
nuisance — every version of the actionable trade depends on detecting and
entering at a verified ≥3% dislocation, and none of that is possible without a
working price feed. Per project memory on the recurring price-stub hazard, real
verified data is made an explicit invalidation criterion (void the trade, do not
fill on stub data), and confidence on the armed long is capped at 52/100 despite
a reasonable thesis, since the edge cannot currently be confirmed executable.
