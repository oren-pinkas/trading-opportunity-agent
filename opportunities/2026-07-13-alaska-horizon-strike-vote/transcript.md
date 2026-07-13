# Research Debate Transcript — 2026-07-13-alaska-horizon-strike-vote

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `debate-three-round-panel` · Personas: bull (sonnet), bear (sonnet), quant (opus) · Synthesizer: opus

Event: AFA-CWA members at Horizon Air (regional subsidiary of Alaska Air Group) voted
99.8% to authorize a strike amid stalled contract negotiations. Ticker: ALK. Impact
window: 2026-08-13. Source: https://afacwa.org/hzn-strike-vote/ (accessed
2026-07-13T19:27:39Z).

Live anchor price: ALK = $46.765 at 2026-07-13T19:59:00Z (source:
`https://api.twelvedata.com/time_series?symbol=ALK&interval=1min&date=2026-07-13&timezone=UTC`,
via `toa price ALK 2026-07-13T19:59:00Z --provider twelvedata`).

Institutional lessons injected (via `toa lessons-relevant --type economic --tickers ALK`):
1. Anchor entry to a live pre-event quote, not the research-day price; if it has drifted
   >~0.5-1% from plan anchor, re-derive or void rather than fill blind. (2026-07-01-ism-mfg)
2. When the thesis is "catalyst reprices X higher" and X already rallied pre-event,
   treat the move as priced-in: fade or shrink, don't chase. (2026-07-01-ism-mfg)
3. Skip trades whose only positive-EV path is a non-executable conditional entry; if the
   executable leg's EV is ~0, don't record the trade. (2026-07-02-june-jobs)
4. Require a differentiated surprise vs. consensus before trading a known, already-priced
   regime/process. (2026-07-02-june-jobs)

---

## Round 1 — Independent research (parallel, no cross-visibility)

### Bull (Catalyst-hunter)

A 99.8% strike authorization vote is a negotiating lever, not an operational event.
Under the Railway Labor Act (which governs airlines, unlike the NLRA for most
industries), a legal work stoppage requires the union and carrier to exhaust
NMB-supervised mediation, the NMB to formally release the parties, and then a mandatory
30-day cooling-off period (during which a Presidential Emergency Board can further
delay things) before any "self-help" — strike or lockout — is legally permitted. That
process routinely runs many months to multiple years; authorization votes at large
carriers (American, Southwest FAs in recent cycles) have historically been used to
pressure management and the NMB into action, not as a precursor to an imminent
walkout. With the impact window here dated 2026-08-13 — roughly one month after the
vote — the mechanical probability of an actual work stoppage occurring by then is
close to zero. This is Horizon (the regional feeder), not mainline ALK flight
attendants, further limiting the scale of any eventual disruption even if talks do
escalate.

Evidence: dossier facts (AFA-CWA vote at Horizon Air, 99.8% authorization, "stalled
contract negotiations" language consistent with a leverage play); RLA process
(mediation → NMB release → cooling-off → self-help, no strike legally possible without
all three gates); base rate that airline strike-authorization votes are common and
overwhelmingly resolved via settlement; impact window (~1 month out) too short for RLA
gates to clear.

Applying the lessons: no data suggesting ALK is at a 52-week high on this news (lesson
2 doesn't bite); will anchor strictly to the $46.765 live quote and treat >0.5-1%
pre-fill drift as reason to re-derive/void (lesson 1); want the executable cash-open
leg to carry the real edge, not a conditional entry (lesson 3).

**Proposed action:** Long ALK common at live anchor $46.765 (re-anchor at fill time;
void/resize if price has moved >1% from anchor). Exit by/at 2026-08-13, or earlier on
a +3% relief pop; hard stop on ~2.5% down move on escalation headlines. Target +3%
(~$48.17).

**Confidence: 42/100** — thin, low-conviction edge; most of ALK's next-month move will
be driven by factors outside this dossier's scope.

### Bear (Skeptic)

This is not a tradeable catalyst, and there's arguably no bull thesis worth engaging
in the first place. A strike authorization vote at a regional subsidiary is procedural
theater, not news. Under the RLA, unions must clear NMB mediation, a 30-day
cooling-off period, and potential presidential emergency board intervention before any
legal work stoppage — a process that routinely takes months to years. Authorization
votes in the 95-99%+ range are the norm, not the exception (Delta, United, American,
Southwest flight attendant and pilot groups have all posted similar or identical
margins in recent cycles without a strike materializing). A 99.8% yes vote tells you
the union is unified and wants leverage at the table — it tells you almost nothing
about strike probability in any near-term window, let alone by 2026-08-13, roughly one
month out.

Evidence: the dossier itself only cites the union's own press release announcing the
vote — no NMB docket status, no release-from-mediation date, no cooling-off clock
start. Without it, "impact window: 2026-08-13" looks like an arbitrary one-month
marker, not a date tied to any legally binding trigger. Horizon Air is a regional
feeder representing roughly 2-3% of Alaska Air Group's total mainline capacity — even
in the tail-risk scenario, the direct operational hit to ALK group economics is small
and partially substitutable (SkyWest, other regional partners, mainline reallocation).
No evidence in the dossier that the stock has moved meaningfully on this specific
headline, consistent with "already understood as non-event" by the tape.

What would change my mind: an unexpected NMB release-from-mediation announcement
compressing the RLA clock, a public deadline threat with actual strike-date
specificity, or Horizon capacity being more operationally entangled with ALK's network
than the base-rate assumption suggests — any of those would still likely be a modest,
short-lived vol event given Horizon's small size, not a repricing of ALK's fundamental
value.

**Confidence there's a real, tradeable move: 10/100. Proposed action: no trade.**

### Quant (Pragmatist)

Base rate: P(legal work stoppage by 2026-08-13) ≈ 2-4% (call it 3%) — NMB rarely and
slowly releases parties from mediation, and release hasn't even occurred here.

Materiality: Horizon is ~2-3% of ALK capacity/revenue, a feeder route substitutable in
part. Full Horizon shutdown tail case ≈ 3-5% consolidated EBIT hit. A rational desk
prices the headline itself — a vote with no NMB release — at roughly a 0.3-0.8% move,
which likely already printed on the news date (19:27Z), not at the 19:59Z entry.

EV calculation (executable cash leg, entry $46.765): P(any tradeable near-term move)
≈ 25%; conditional direction ≈ 55% down / 45% up (weak bearish tilt); conditional
magnitude ≈ 0.7%. Directional edge = 0.25 × (0.55−0.45) × 0.7% = **+0.0175%** gross.
Round-trip costs + slippage on a liquid large-cap airline ≈ 0.05-0.10%. **Net EV ≈
−0.05%**, negative after costs — mirrors lesson 3 (only positive path is front-running
a headline that already cleared; a post-quote entry can't capture that).

**Recommendation: NO TRADE.** News-noise event: strike is process-blocked for months,
exposed subsidiary is immaterial, rational move is sub-1%, only executable entry is
post-headline, directional EV is negative after fees/slippage. Position size: 0% of
book.

**Confidence: 82/100** that this is correctly a no-trade.

---

## Round 2 — Rebuttal (parallel, each shown the other two Round 1 positions)

### Bull (rebuttal)

Concedes. The "fade the overreaction" thesis required an antecedent selloff that the
record doesn't show occurred — if the ~0.3-0.8% theoretical move already printed at
19:27Z and there's no evidence of it, there's no fear premium to unwind and no relief
pop coming. A relief-rally trade with no antecedent selloff isn't a trade, it's a coin
flip dressed as a thesis. The RLA-timeline point (used in R1 to argue downside is
overstated) cuts both ways — it also means there was never enough mispriced fear to
fade. What would change my mind back to long: actual evidence of an intraday drawdown
on the vote headline that hasn't retraced, or a subsequent PEB/mediator escalation
headline causing a disproportionate selloff — neither exists in the data presented.

**Revised confidence (long edge exists): 15/100. Action: NO TRADE, stand aside.**

### Bear (rebuttal)

Convergence isn't just confirmation — three orthogonal failure modes (procedural/RLA
mechanics, EV arithmetic, sentiment-fade logic) independently landing on "no trade" is
a stronger null signal than one shared read would be. Bull's fade-the-fear has zero
residual merit once staleness is accounted for — it's noise-chasing dressed as a
thesis, and bull's own 42/100 self-rating already conceded that. One unresolved thread
worth flagging, not trading: Horizon disproportionately feeds ALK's PNW/Seattle
short-haul network, so route-level revenue concentration could make a later *actual*
walkout more damaging than the raw ~2-3% capacity share implies — but that's a
Q4-2026/2027-type tail, not an 8/13 catalyst, and the dossier has no route-level data
to size it.

Scenarios that could flip this within 30 days: NMB releases parties early + cooling-off
clock starts inside/near the window (~10-15%, but would still likely need a PEB to not
intervene, which is close to automatic for a carrier this size); escalatory rhetoric
from AFA-CWA leadership (~30% likely, historically doesn't move the stock without an
operational trigger); a copycat mainline (not just Horizon) vote (<5%, no evidence
brewing). None clears the bar for a position.

**Final confidence: 88/100** that no-trade is correct. Recommends closing the dossier
as no-action rather than scheduling a position or re-check date — an NMB release would
arrive as unambiguous news, not something to poll for.

### Quant (rebuttal)

Bull's "fade the overreaction" adds no incremental EV — it's double-counting the same
0.3-0.8% move already priced into the base-rate calc, re-labeled as a reversal bet
with no evidence the initial move even happened. Stress-testing the Round 1 EV model:
pushing P(move) to 40% alone (net ≈ −0.02% to −0.07%) or magnitude to 1.2% alone (net
≈ −0.02% to −0.07%) each leaves net EV negative; only stressing *both* simultaneously
gets to breakeven (gross +0.048%, net −0.002% to +0.002%), and even that requires also
assuming directional confidence beyond the dossier-supported 55/45 split. No-trade is
robust across single-parameter stress — this is fragile edge, not a fragile
conclusion. Short-dated options for NMB-surprise optionality don't rescue it either:
P(early release)<3%, theta bleed over a ~30-day hold, and no dossier evidence that
implied vol is mispriced cheap enough to justify the structure.

**Recommendation: NO TRADE, 0% of book. Confidence no-trade is correct: 85/100** (up
from 82 — all three personas independently converge and the EV call survives
parameter stress).

---

## Round 3 — Convergence (synthesizer)

**Hypothesis:** The Horizon Air AFA-CWA 99.8% strike authorization vote is a
procedural negotiating lever, not a tradeable catalyst within the 2026-08-13 window;
RLA gates make a legal work stoppage near-impossible by then, Horizon is immaterial to
ALK capacity, and any modest headline reprice already printed at news time — leaving
no exploitable edge. **Direction: none. Confidence: 85/100** (confidence in the null
hypothesis — that this is correctly a non-event — not confidence in a directional
trade).

**Plan:** ALK — **no_trade**. No entry, no exit, no position.

**Dissent (carry into post-mortem/future revisit):** Bear's unresolved tail — Horizon
disproportionately feeds ALK's PNW/Seattle short-haul network, so an actual future
walkout could inflict damage out of proportion to its ~2-3% raw capacity share. This is
a Q4-2026/2027-type tail, not an 8/13 catalyst, and the dossier lacks route-level data
to size it. Worth revisiting only if the NMB actually releases the parties from
mediation.

**Why the panel converged:** The RLA process gate is decisive — a legal work stoppage
requires NMB mediation exhaustion, an NMB release, and a 30-day cooling-off period
(with possible PEB delay), which cannot plausibly clear by 2026-08-13; 95-99%+
authorization votes are industry-standard bargaining theater that rarely produce
strikes. Horizon represents only ~2-3% of ALK's consolidated capacity and is largely
substitutable, capping fundamental impact even under an escalation tail. The EV math is
negative under baseline assumptions and stays negative under single-parameter stress
testing. Finally, the staleness point removes the last thread of edge: any rational
reprice would have printed at the 19:27Z news time, well before the 19:59Z anchor,
so the bull's fade-the-overreaction thesis double-counts a move with no evidence it
ever occurred.
