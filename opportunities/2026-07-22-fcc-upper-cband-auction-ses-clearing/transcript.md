# Debate transcript: 2026-07-22-fcc-upper-cband-auction-ses-clearing

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `debate-three-round-panel`. Personas: bull (sonnet), bear (sonnet), quant
(opus). Synthesizer: opus. Run at 2026-07-23T15:41:59Z.

Pre-debate check (orchestrator, cited): the dossier ticker SGBAF, plus the two obvious
alternates SESG.PA (Euronext Paris) and SESGY, were each queried against the real price
provider (`toa price <ticker> <ts> --provider twelvedata`). All three returned an error
(SGBAF: HTTP 400, SESG.PA: HTTP 404, SESGY: HTTP 404) — no SES instrument is currently
priceable/simulatable in this system. This constraint was injected into every persona's
Round 1 brief per the institutional lesson from `2026-07-12-nayax-cyber-breach-ultimatum`
("test-query the real price provider before finalizing a plan — an unpriceable plan
resolves as an uninformative neutral").

Lessons injected (regulatory-event class, via `toa lessons-relevant`):
- Never map a corporate/legal calendar date directly onto an execution timestamp —
  derive fill time from the nearest valid trading session (source:
  `2026-07-08-caesars-icahn-fertitta-bidding-war`).
- Test-query the real price provider for exact timestamps before finalizing a plan
  (source: `2026-07-12-nayax-cyber-breach-ultimatum`).
- A signal-to-noise ratio below ~0.15 on a linear-EV fade is not a durable edge; the
  simulator has no path-dependent stop-loss enforcement (source:
  `2026-07-10-prologis-segro-bid-deadline`).
- An entry fill outside the planned entry band is an early falsification signal
  (source: `2026-07-10-prologis-segro-bid-deadline`).

---

## Round 1 — Independent research

### Bull (sonnet), confidence 30/100
FCC's Jul 22, 2026 vote to auction 160 MHz of upper C-band is a structural positive for
SES, not a cost story alone. SES faces ~USD 3.6B in clearing costs, but the mechanism
exists because incumbents get compensated — same playbook as the 2020 lower C-band
auction, where SES (with Intelsat) received large accelerated-relocation payments
(general knowledge, labeled). The dossier's own framing — SES is "negotiating"
incentive/reimbursement payments — means the USD 3.6B is a gross figure, not a net
loss; the offsetting payment is the real swing factor and likely isn't priced yet.

Evidence cited: FCC vote date Jul 22 2026 (newscaststudio.com); 160 MHz "super-band"
auction; clearing deadline Jul 2027 (~12-month impact window); SES's own USD 3.6B
clearing-cost estimate.

Tradeability: confirmed SGBAF/SESG.PA/SESGY all fail on twelvedata (404/400) — kills
any direct SES trade in this system today. No confirmed liquid, priceable proxy exists.
Proposed action: flag as directionally bullish but **NOT ACTIONABLE** pending a
priceable instrument. If forced, tentatively nominate a low-conviction EchoStar/Viasat
sector-sentiment proxy only — not a clean expression of this specific catalyst.

### Bear (sonnet), confidence 6/100
This is a 12-month-out clearing deadline (Jul 2027), not a binary event. The dossier
itself says SES is still "negotiating" incentive payments — the net cost is unknown
and unresolved as of the vote. A thesis built on the gross USD 3.6B figure without the
net figure is noise, not signal.

Risks to the bull thesis: (1) incentive payments could largely/fully offset the 3.6B
(2020 C-band precedent reimbursed incumbents substantially — general knowledge — no
evidence this auction breaks that pattern, but no evidence it doesn't either); (2) FCC
auction/clearing timelines routinely slip (general knowledge) — "Jul 2027" is a target,
not a hard catalyst date; (3) this is one line item for a diversified multi-orbit
operator (GEO, MEO/O3b, post-Intelsat-merger scale) — likely immaterial until the net
cost is known; (4) no dossier evidence on how SES-related equity already moved on
Jul 22 — can't claim unpriced alpha without that.

Untradeable ticker: "close to fatal" — per lessons, an unpriceable plan resolves as an
uninformative neutral and wastes the debate. Unless a provider-resolvable proxy exists
with a real quote, there's no instrument to express this view.

### Quant (opus), confidence 88/100 (in the no-trade verdict)
Assumed probabilities: P(incentive payments materially offset USD 3.6B) = 0.55 (2020
mid-band clearing precedent reimbursed incumbents' relocation costs in full plus
accelerated-clearing bonuses — base rate favors substantial offset, but "material" ≠
"full," negotiation risk live). P(clearing/auction timeline slips past Jul 2027) = 0.65
(spectrum deadlines slip more often than not). P(already priced into SES ordinary
shares) = 0.80 (clearing framework telegraphed for quarters; Jul-22 confirmatory vote
is low-surprise; semi-strong efficiency implies small residual).

EV sketch: unpriced residual ≈ 20% of a plausible ±8-12% terminal repricing over 12
months ≈ ~2% of gross expected move available to capture. Signal-to-noise: ~2% drift
against SES's ~30-35% annualized vol ≈ S/N 0.06 — below the 0.15 durability floor
(institutional lesson). Costs: OTC ADR spread + a full year of opportunity cost
(~4-5% risk-free forgone) swamps the ~2% gross. Net EV negative before direction.

Infrastructure gate (dispositive, leads over thesis): SGBAF/SESG.PA/SESGY all fail on
twelvedata — no valid trading session to derive a fill from, so the Jul-2027 calendar
date can't even be mapped to an execution timestamp. **NO TRADE regardless of thesis
quality** — two independent kill-switches (infra + negative EV), either sufficient
alone. Burden on bull to produce a resolvable proxy AND S/N > 0.15 after costs, absent
which quant fades to flat.

---

## Round 2 — Rebuttal

### Bull
Concedes the trade, not the thesis: "no priceable SGBAF/SESG.PA/SESGY resolution means
there's no instrument to express this view in, full stop." Pushes back partially on
"already priced in" (P=0.80) — 2020 precedent (Verizon/AT&T mid-band clearing) shows
incentive-payment terms are where the real value transfer happens, and that detail
genuinely isn't baked into consensus because it hasn't been negotiated yet — so
informational edge may exist. But edge without a tradeable vehicle is moot. No rebuttal
to the quant's EV math that survives scrutiny — even nudging P(offset) to 0.65
optimistically, the durability-floor problem is structural (12-month runway + missing
ticker), not a probability quibble.

What would change bull's mind: (1) a confirmed incentive-payment figure from FCC/SES
disclosure; (2) any single resolvable proxy (ADR variant, options chain, sector ETF
with real SES weight) the price provider can quote; (3) evidence the clearing deadline
is locked (no extension filed).

Verdict: **NO TRADE**. 30/100 directional, 0/100 actionable.

### Bear
The bull's "2020 precedent" cuts both ways: those payments were structured around a
hard, enforced FCC deadline with real clawback risk for missing it — which is exactly
why timeline slippage (quant's 65%) is so damaging, not reassuring. Adds a risk neither
other persona engaged: SES is one of only two incumbents being cleared, so any
FCC-SES friction becomes bilateral/idiosyncratic, not diversifiable the way
"sector sentiment" framing implies. Fully agrees with the no-trade verdict, raises own
confidence in it to 90/100 — "directionally bullish but not actionable" is doing a lot
of work to salvage a trade with no clean instrument, no binary catalyst, and a
cost/benefit that nets to "maybe roughly neutral in 12+ months." Calls the EchoStar/
Viasat proxy noise, not signal — idiosyncratic catalysts unrelated to SES's C-band
economics risk manufacturing a false signal.

### Quant
Nothing moves the math. Explicitly ran S/N through the bull's proposed EchoStar/Viasat
proxy: those names carry ~50-70% annualized vol (higher than SES) and near-zero beta to
SES-specific incentive-payment news, so the already-sub-floor residual (~2% of
expected move, S/N≈0.06) gets diluted further by proxy tracking error — effective
S/N falls to ~0.02-0.03, worse, not better. Base rates reinforced, not undercut, by
precedent: the 2020 C-band precedent was already the market's anchor for pricing this
(supports P(priced in)=0.80). Two independent gates fail (infrastructure + EV), either
alone sufficient. Final confidence in NO-TRADE verdict: **92/100** (up from 88 — both
opponents corroborated the fatal infrastructure gate).

---

## Round 3 — Synthesis (opus)

**Verdict: unanimous no-trade.** All three personas converge; confidence in the
no-trade call rises 88 → 90 → 92 across rounds with zero dissent on the core
conclusion. Two independent kill-switches, either fatal alone: (1) infrastructure gate
— no priceable instrument (SGBAF/SESG.PA/SESGY all fail on twelvedata); (2) EV gate —
S/N ~0.06 direct (~0.02-0.03 through the best proposed proxy), well below the 0.15
durability floor. The directional read on SES is mildly bullish (unpriced incentive-
payment offset to the USD 3.6B clearing cost, per 2020 precedent) but inert — there is
no vehicle to express it.

**hypothesis**: statement as above; direction `none`; confidence 92 (confidence is in
the no-trade conclusion, the operative output — the residual directional lean,
decoupled from actionability, is ~30/100 long and 0/100 actionable).

**plan**: no ticker, no action, no entry/exit, no size — nothing to schedule or
simulate.

**dissent** (strongest unresolved disagreements, worth carrying into post-mortem /
re-scout triggers):
1. Bull: an informational edge may genuinely exist — incentive-payment terms are not
   yet fully priced in. Conceded only the trade (no vehicle), not the thesis. If a
   priceable SES instrument becomes available before the Jul 2027 clearing deadline,
   this should be re-scouted rather than treated as permanently dead.
2. Bear: idiosyncratic-counterparty risk — SES is one of only two incumbents being
   cleared, exposing it to bilateral FCC-SES friction and clawback risk that is not
   diversifiable and cuts against the bullish offset. Bull and quant did not fully
   engage this; quant folded it into general vol/base-rate terms rather than pricing it
   as a directional downside skew on the thesis itself. This is the strongest
   unaddressed counter to the bull's mildly-bullish direction, should the trade ever
   become actionable.
