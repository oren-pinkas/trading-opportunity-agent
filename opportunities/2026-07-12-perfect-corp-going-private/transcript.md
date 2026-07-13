# Research Debate Transcript — 2026-07-12-perfect-corp-going-private (PERF)

Strategy: `debate-three-round-panel`. Personas: bull (sonnet), bear (sonnet),
quant (opus). Synthesizer: opus. PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL
ADVICE.

## Event

Perfect Corp signed a definitive all-cash going-private merger agreement with
ProjectNY, an acquisition vehicle led by Alice Chang — Perfect Corp's own
founder/CEO (a management-led buyout) — at a ~48% premium to the
pre-announcement price. Close targeted Q4 2026, subject to shareholder vote.
Impact window: 2026-10-15. Dossier created 2026-07-12T06:44:59Z. Source:
[Morningstar/Business Wire](https://www.morningstar.com/news/business-wire/20260710639441/perfect-corp-enters-into-a-definitive-agreement-for-a-going-private-transaction),
published ~2026-07-10, accessed 2026-07-12T06:44:59Z.

## Institutional lessons injected (event.type=economic)

1. Anchor entry to a live pre-event quote, not the research-day price; if the
   live price has drifted >~0.5-1% from the plan anchor, re-derive
   targets/EV or void the trade rather than filling blind. (`2026-07-01-ism-mfg`)
2. When the thesis is "catalyst reprices X higher" and X has already rallied
   before the event, treat the move as priced-in: fade or shrink, don't chase
   the entry. (`2026-07-01-ism-mfg`)
3. Skip trades whose only positive-EV path is a pre-market conditional entry
   the harness cannot fill; if the executable leg's EV is ~0, don't record
   the trade. (`2026-07-02-june-jobs`)
4. Require a differentiated surprise vs. consensus before trading a data
   print/catalyst that's already in the tape. (`2026-07-02-june-jobs`)

## Data gaps (orchestrator-verified, applies to all three rounds)

- **Deal price corrupted.** The dossier's own summary field is missing the
  actual per-share cash deal price — it reads ".00/share cash" (leading
  digits dropped in scouting). The exact strike price `D` is unknown. Only
  the ~48% premium ratio is known.
- **Price feed unreliable.** `toa price PERF <ts>` returned non-monotonic,
  economically incoherent values across the announcement window:
  $429.69 (2026-07-09), $401.80 (2026-07-10), $304.86 (2026-07-13). A real
  post-announcement print for a 48%-premium cash buyout should gap up and
  then hold in a tight, low-volatility band toward the deal price — not swing
  ~30% inside three days. All three panelists treated this feed as a broken
  stub and refused to anchor EV math to it. The source article itself
  returned HTTP 403 on re-fetch, so the exact deal price could not be
  independently recovered.

---

## Round 1 — Independent Opening Positions

### Bull (catalyst-hunter) — confidence 62/100

Signed, definitive cash merger agreement (not a rumor or preliminary
approach) with a ~48% premium and an insider (founder/CEO) sponsor. Frames
the trade as "does PERF converge to and hold near deal price into close,"
not "will PERF go up" — the repricing event has already happened. Insider-led
deals close at high rates: the buyer already controls the operating business
and has effectively completed diligence, removing the classic strategic-buyer
walk-away/MAC-surprise failure mode. Explicitly refuses to compute a spread
or size a position off the broken price feed or the missing deal price.

**Proposed action:** Long equity (not options — a fixed-outcome cash deal has
no need for optionality and options bleed theta over a 3-month hold with no
upside above the deal price to harvest). Require a sane, cross-checked live
quote before sizing; anchor to a live pre-event quote per institutional
lesson #1, void/minimize if the feed stays broken. Hold toward the
2026-10-15 window/Q4 close harvesting spread compression around the
shareholder vote; exit on any break/litigation-injunction/delay news.

### Bear (skeptic) — confidence 82/100 that the trade is NOT currently tradeable

A ~48% premium announced days before this dossier means the market has
likely already re-rated most of the way to the offer price — the residual
arb spread is probably thin, producing a classic asymmetric setup: capped
upside (a few points of spread) vs. uncapped-ish downside (full reversion
toward the pre-announcement price on a deal break). Named risks: (1)
management-led buyout conflict-of-interest — founder/CEO Alice Chang as both
operator and buyer is the single most common trigger for shareholder
derivative suits, disclosure-only settlement suits (which delay the vote),
activist pressure for a bump, or in the worst case a special
committee/holders concluding the process was unfair and voting it down; (2)
financing risk — zero visibility into whether ProjectNY's cash is fully
committed; (3) Taiwan regulatory risk — Perfect Corp is Taiwan-based, FSC/FTC
review or cross-border capital scrutiny is a named but unconfirmed risk; (4)
shareholder-vote risk — no data on voting/support agreements from a
supermajority; (5) deal-break/timeline-extension risk over the ~3.5-month
hold; (6) the "already priced in" problem. Two independently broken/missing
inputs (deal price, live price) mean no real EV can be computed — disqualifying
for anything beyond a token position.

**Proposed action:** No trade at current information quality. Would change
mind with: a confirmed deal price + trustworthy quote yielding a computable
spread clearing a >10-15% annualized hurdle, evidence of signed supermajority
voting/support agreements, no live competing bid/go-shop, a clean regulatory
path, confirmed committed financing, and a sane monotonic price series.

### Quant (pragmatist) — confidence 35/100 in an executable positive-EV trade (88-90% in the qualitative "deal closes" direction)

Base rate for signed definitive cash mergers: ~90-95% completion absent a
competing bid/regulatory blocker. MBOs draw more litigation than strategic
deals, but litigation rarely breaks these deals — it usually resolves as a
disclosure-supplement settlement or a modest bump. Working estimate
p(completion) ≈ 0.90 (range 0.88-0.92). Regulatory risk assessed as low;
main gate is the shareholder vote, and a 48% premium is a comfortable margin.

Worked the EV symbolically since the deal price `D` is a data gap: spread
`s = (D-M)/M`, break-loss `L ≈ -32%` (reversion to `P0 = D/1.48`), cost
`c ≈ 0.5%`, hold `t = 0.29yr` (to 2026-10-15), hurdle 12%/yr annualized.

```
EV = p·(s - c) - (1-p)·(|L| + c) = 0.90·s - 0.037
Breakeven spread s* ≈ 4.1%  (EV = 0)
Hurdle-clearing spread s* ≈ 7.9%  (to clear 12%/yr net)
```

Decision rule: `s < 4%` → no trade; `s` 4-8% → marginal/small size only;
`s > 8%` → nominally clears the hurdle **but is itself a red flag** that `p`
should be revised down (wide spreads on definitive deals are usually
informative about elevated break risk, not free money).

**Proposed action:** No trade / "priced-blind void" until `D` and a clean `M`
arrive. Contingent plan: size 1/4-1/2 normal if `s` lands 4-8%, stand down if
`<4%`, re-interrogate `p` (not celebrate) if `>8%`.

---

## Round 2 — Rebuttals

### Bull rebuttal — confidence revised to 58/100

Pushes back that the bear's risk list (MBO litigation, financing,
Taiwan regulatory, vote risk) is generic base-rate pattern-matching, not
case-specific evidence — no actual disclosure suit, FSC review, or go-shop
bid exists in the record. Litigation "rarely breaks these deals" per the
quant's own numbers — mostly a delay/bump risk, arguably mildly positive
for a holder. Argues spread compression post-announcement is the expected,
normal mechanism of merger arb, not evidence against the trade. Pushes back
on the quant's `L ≈ -32%` as a worst-case unconditional loss — the modal
litigation outcome (delay/bump) implies a more bimodal loss distribution,
not a single large-loss number.

**Concedes:** sizing a full position off a corrupted deal price and a broken
feed is not defensible risk management. Revised proposal: a small starter
position (~1/4 size) using only a cross-checked live quote (never the broken
feed), hard stops tied to deal-break signals (litigation escalation, competing
bid, regulatory review opening, vote delay) rather than price stops, scaling
to full size only once the deal price is confirmed via the actual merger
agreement/proxy and the quote is sane.

### Bear rebuttal — confidence revised to 85/100 for no-trade

Notes that the quant, starting from a friendlier prior (90% completion),
still arrives at "no trade" via pure arithmetic — independent convergence
from a different starting point is stronger evidence than either panelist's
case alone. Highlights the nonlinearity of breakeven spread in `p`:
`p=0.90→s*≈4.1%`, `p=0.85→~6.2%`, `p=0.80→~8.6%`, `p=0.75→~11.3%` — a modest
haircut to the most contestable, least-observable input roughly doubles the
required breakeven. Argues "wait for a clean quote, then enter" doesn't
resolve the objection: a well-covered, fast-arbed cash deal typically
re-rates to within a few percent of terms almost immediately, so the likely
realized spread is thin regardless of data cleanup — probably at or below
breakeven either way. Revises p(completion) down to 0.75-0.85 (vs. the
quant's 0.90), citing MBO process/fairness-challenge risk, unconfirmed
financing, unconfirmed voting/support agreements, and the unresolved Taiwan
cross-border regulatory gate.

**Steelmans the bull:** the insider buyer has already done full diligence and
has no informational surprises to discover — real, and it reduces the
already-rare strategic-buyer-walk-away failure mode. But this doesn't fix the
entry-price/adequate-compensation problem; it tempers concern about
catastrophic break, not concern about being paid enough for the risk taken.

### Quant rebuttal — confidence 88/100 in no-trade (final numbers)

Explicitly reconciles the panel: the bear's "no trade" is driven by elevated
risk + a structurally thin spread; the quant's is driven by a non-computable
EV (missing `D`, broken `M`) — two independent, orthogonal screens agreeing
is stronger than either alone. Revises `p(completion)` down from 0.90 to
**0.82** (range 0.80-0.85) after folding in incremental, non-double-counted
risk: MBO litigation stays mostly a carry/delay risk already inside the
original 10% (no further markdown); conflict-of-interest/fairness-challenge
risk (-3 to -4 pts), financing-visibility gap (-1 to -2 pts), Taiwan
cross-border regulatory gate (-2 to -3 pts), and majority-of-minority
shareholder-vote risk (-1 to -2 pts) are genuine incremental hazards — net
markdown -7 to -11 pts. Notably converges with the bear's independent 82
number from a completely different calculation.

States the insider-buyer completion **edge** (no strategic walk-away/MAC
surprise) and the conflict-of-interest **penalty** (fairness litigation,
vote risk, delay) do not simply cancel: the edge shaves an already-rare
break mode (marginal), while the penalty mainly loads onto time/carry — the
hold likely extends past 2026-10-15 toward ~0.45-0.55yr through a
committee/litigation process.

Re-runs the EV at `p=0.82`:

```
Breakeven spread s* ≈ 7.6%  (up from 4.1%)
Hurdle-clearing spread s* ≈ 13-14%  (accounting for the extended hold)
```

Given the deal is already 2-3 days stale and likely fast-arbed, the most
likely live spread sits in the **2-5% range — below breakeven even under the
revised numbers.** Final decision rule: `s < 7.5%` → no trade; `s` 7.5-12% →
marginal/token only (and itself a signal to re-examine `p` downward);
`s > 12%` → nominally clears the hurdle but is a red flag. Modal expectation:
no trade even after clean data arrives. Concedes a ~15-20% (~1-in-6) joint
probability that clean data reveals `p≈0.88` and a genuinely wide (>8%)
liquidity/technical-driven (not break-priced) spread, which would flip to a
small positive-EV long — sizes the bull case at "a ~1-in-6 option, not a
62%-conviction long."

---

## Round 3 — Synthesis

**Hypothesis:** PERF is a signed, definitive, all-cash MBO (founder/CEO
Alice Chang via ProjectNY) at a ~48% premium, targeting a Q4 2026 close
subject to a shareholder vote. The deal-*direction* (converges to terms) is
high-probability — panel-blended p(completion) ≈ 0.82. But this is a
merger-arb spread trade, not a directional bet, and its executability is
fully gated by two independently broken inputs: the corrupted per-share deal
price and the incoherent, non-monotonic price feed. Even after clean data,
the modal expectation is that a 2-3-day-stale, fast-arbed cash deal has
already re-rated to a thin spread (est. 2-5%), below the p=0.82 breakeven of
~7.6% and far below the extended-hold hurdle of ~13-14%.

**Direction:** no_trade. **Confidence:** 84/100 (in the no-trade-now call).

**Plan:** No position now. Re-open only if ALL hold simultaneously: (1) the
actual per-share deal price `D` is confirmed from the executed merger
agreement/proxy, not the corrupted dossier field; (2) a cross-checked live
quote `M` from a real venue is available (the broken internal feed is
disqualified); (3) the computed spread `s = (D-M)/M > 8%` and is attributable
to liquidity/technical dislocation rather than a priced-in break signal; (4)
no active break trigger is present (no litigation escalation past routine
disclosure settlement, no competing/go-shop bid, no opened Taiwan FSC/FTC
review, no vote-delay or financing-failure headline). If opened, size small
(~1/4 unit), model an extended hold (~0.45-0.55yr, not the naive 0.29yr) to
account for MBO-driven delay, use event-based stops (not price stops), and
converge to `D` on a clean close. Expected profit: ~0% (modal EV is
approximately zero — likely spread sits below breakeven; the quant's ~1-in-6
tail case of a wide, technical-driven spread is the only path to a small
positive-EV long).

**Dissent (preserved for post-mortem):** Whether the post-cleanup spread
would actually clear ~8%. Bull holds that the no-trade call is an artifact of
*bad data*, not a bad trade — once a real deal price and clean quote arrive, a
defensible small long exists at the true convergence spread. Bear/quant hold
that a well-covered, fast-arbed cash deal re-rates to within a few percent of
terms almost immediately, so the likely spread is structurally thin and sits
at or below breakeven *regardless* of data quality — i.e. the no-trade
survives clean data. This is the exact quantity the post-mortem should
measure first: if clean data later shows `s > 8%` on liquidity grounds, the
bull was right and the panel left EV on the table; if `s < 5%`, the bear and
quant were right. Secondary unresolved fork: `p(completion)` itself — bull
~0.88 (no case-specific evidence of break risk in the record) vs. bear/quant
~0.80-0.85 (MBO conflict-of-interest + unconfirmed financing/support
agreements + Taiwan cross-border gate as genuine incremental hazards).

**Rationale:** Three rounds produced a rare near-unanimous convergence from
three different starting points. The bull never disputed the deal structure
(signed, definitive, all-cash, insider sponsor who has already diligenced the
asset), only conceded that sizing any position off a corrupted deal price and
an incoherent feed is indefensible, cutting confidence to 58. The bear and
quant reached "no trade" via two orthogonal screens that reinforce rather
than merely echo each other: elevated MBO/regulatory/vote risk plus a
structurally thin post-announcement spread (bear), and a non-computable EV
that independently converges on p≈0.82 and a breakeven of ~7.6% against a
likely live spread of only 2-5% (quant). Two independently broken inputs plus
a modal sub-breakeven spread mean the disciplined action is: no directional
or arb position now, with a specific, measurable re-entry gate handed forward
to the next research cycle and the post-mortem.
