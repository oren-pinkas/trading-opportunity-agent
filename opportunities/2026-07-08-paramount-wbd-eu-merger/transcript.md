# Research debate transcript — 2026-07-08-paramount-wbd-eu-merger

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `three-round-panel` | Personas: bull (sonnet), bear (sonnet), quant (opus) | Synthesizer: opus
Debate run: 2026-07-10T15:03:42Z

Dossier facts used: EC's July 7, 2026 deadline to rule on Paramount Skydance's $111B
acquisition of Warner Bros Discovery has passed as of dossier creation (2026-07-08);
decision "imminent"; deal already cleared other (unnamed) jurisdictions. Source:
Bloomberg, "Paramount-Warner Bros. Discovery Merger Faces EU Decision by July 7,"
https://www.bloomberg.com/news/articles/2026-06-02/paramount-seeks-eu-green-light-for-110-billion-warner-deal,
accessed 2026-07-08T15:21:00Z. Tickers: PSKY, WBD.

Reference prices (via `toa price`, deterministic stub source, not live market data):
PSKY $34.81, WBD $317.58, both as of 2026-07-10T15:00Z.

Institutional lessons (`toa lessons-relevant --type regulatory --tickers PSKY,WBD`): none found.

---

## Round 1 — Independent research

### Bull (Catalyst-hunter, sonnet)

Binary regulatory catalyst sitting right on top of the trade. The EC's July 7 deadline
has passed, decision imminent, and the deal has already cleared other jurisdictions
(dossier, Bloomberg-sourced) — the textbook setup for a merger-arb catalyst: when the
last major regulator is the outstanding condition and every other approval is in hand,
the base rate strongly favors clearance (with or without remedies) rather than a
blocking decision, since Brussels rarely kills a deal this advanced without earlier
Phase II signaling.

Mechanism: WBD (target) arb spread should mostly collapse on clean clearance —
smaller, faster, higher-probability move. PSKY (acquirer) move is about removing
overhang/uncertainty and re-rating, with more upside if the market had been pricing
meaningful EU-block risk.

Proposed action: primary long WBD (small-moderate size, common stock or near-dated
calls — flagging IV crush risk on "event resolved" news makes the underlying cleaner
than options); secondary long PSKY (smaller, higher-beta, more idiosyncratic
integration/leverage risk). Enter before/at confirmation of clearance headlines, exit
on the pop — fast event trade (hours to days), cut fast if heavy remedies/divestitures
or further delay.

Known unknowns / assumptions flagged: "other jurisdictions cleared implies favorable
base rates" is inferred, not cited — dossier doesn't specify EC's Phase I vs Phase II
posture. Betting on relief rally vs. sell-the-news, but flags the move could be muted
especially on WBD if the arb spread is already tight. No information on the actual WBD
arb spread vs. deal terms (cash/stock mix, exchange ratio) — material gap. No
information on possible EC remedies (forced divestiture of channels/assets). Exact
ruling timing vague ("imminent"). No institutional lessons available.

### Bear (Skeptic, sonnet)

The EC's self-imposed July 7 deadline has passed with no decision recorded, and today
is July 10 — three days later. The bull case ("other jurisdictions cleared it, so the
EU will too") is weaker than it looks for two reasons: (a) plain-vanilla approval is
very likely already priced in given the deal has been public since at least the
June 2 Bloomberg piece and has cleared other regimes; (b) the deadline slipping is a
data point, not noise — a missed Phase I deadline typically means either a remedies
negotiation is underway or a Phase II in-depth referral is being teed up, both
bearish-to-neutral, not confirmatory, signals.

Evidence cited: dossier EC deadline (Jul 7, passed), Bloomberg source; dossier states
other jurisdictions cleared but names none. Reference prices (toa stub) with no
baseline pre-deal price to judge embedded premium — flagged as a known unknown.
Assumption (not confirmed for this deal): WBD's EU footprint (Eurosport, HBO Max
Europe, Discovery linear channels, TVN Poland) is large enough to draw sports-rights/
bundling scrutiny, by analogy to Fox/Sky, Comcast/Sky, Disney/Fox — not confirmed here.

What's priced in / blow-up scenarios: likely priced in — >85-90% implied clearance
probability already, meaning a bare "EU approves" headline may produce a muted or
negative "sell the news" reaction. Blow-up scenarios: conditional approval with
material divestitures reducing synergies; Phase II referral/extended timeline (biggest
risk given the deadline already slipped); outright block (low probability, severe
surprise given "decision imminent" framing); arb-spread compression already done,
meaning a fresh long has poor risk-reward.

Known unknowns: whether the EU has actually ruled July 7–10 and what the ruling was;
which jurisdictions cleared and on what terms; actual deal consideration/exchange
ratio (needed for a real arb spread); whether DG COMP has flagged specific concerns.
Verdict: would NOT initiate a long on current information.

### Quant (Pragmatist, opus)

Base rates (assumed, from general knowledge): EC clears >90%+ of notified mergers in
Phase I typically; outright blocks are historically <1% of EU merger reviews; for
large media deals, behavioral remedies/divestitures are the common friction, not
blocks. Sequencing signal: when a deal has already cleared other jurisdictions and
only the EC remains at a passed deadline, the market has typically de-risked most of
the arb spread already — "pennies in front of the steamroller."

Assumed outcome distribution: clean unconditional approval 55% (WBD +2-3%, PSKY
+1-3%); approval with conditions/remedies 33% (WBD +1-2%, PSKY 0-2%); delay/extended
review/referral 9% (WBD -2-4%, PSKY -1-3%); outright block 3% (WBD -20-35%, PSKY +2 to
-5%). Combined approval probability ≈ 88%.

Proposed trade: long WBD only, capturing residual merger-arb spread, assumed ~3%
residual upside (no deal terms known to compute the true spread). EV:
0.88×(+3%) + 0.09×(-2.5%) + 0.03×(-27%) = gross ≈ +1.60%; net of costs (~0.25-0.40%)
≈ +1.2-1.35%. Critical sensitivity: if the true spread is only ~1% (plausible since
peers already cleared), EV turns roughly flat-to-negative once the block tail is
weighted (≈ -0.05%) — "the edge lives or dies on an input I cannot see." Sizing:
negatively skewed n=1 binary event, caps at ≤1-2% of book, no leverage, prefers a
put-hedged structure to cap the tail. PSKY avoided as a directional trade — ambiguous,
no synergy/financing data. Verdict: small long-WBD tilt (≤1-2%, ideally put-hedged)
ONLY IF the observable residual spread is ≥~2%; otherwise NO TRADE.

---

## Round 2 — Rebuttal

### Bull rebuttal

Disagrees with bear: reading the deadline slip as itself bearish over-reads a data
gap — it may simply be routine administrative friction (translation, documentation
requests, case-team bandwidth), common even for eventually-clean clearances. Bear's UK
CMA comparables (Fox/Sky, Comcast/Sky, Disney/Fox) aren't close analogues to an EU
Phase I review of a US media combination with comparatively thin EU overlap (WBD skews
linear/kids/factual/Max streaming; Paramount's EU presence is thin). Six weeks of
silence on market-testing complaints, second requests, or remedies chatter since the
Bloomberg piece is itself informative and bear doesn't weight it.

Disagrees with quant: the 9%/3% delay/block priors look like generic base rates, not
conditioned on the one fact available — that other jurisdictions already cleared,
which is evidence of no smoking-gun overlap and should push tails below generic base
rate, not leave them at it. Quant's own math still nets positive (+1.2-1.35%) — "a
yes, trade it, small answer dressed up as no trade."

What bear/quant missed: time-decay on an unresolved binary favors entering now, since
resolution collapses uncertainty and captures the reaction quant's own model prices at
+2-3%.

Would change bull's mind: confirmed Phase II opening or a formal Statement of
Objections; confirmed remedies negotiations naming specific EU assets (Eurosport, HBO
Max carriage terms, TVN); real-time price action showing the market already reacting
to bad news not yet visible in the dossier.

### Bear rebuttal

Quant's 88% combined-approval figure is an unconditional base rate that silently
discards the one hard fact available — the EC's own deadline passed with no ruling.
Statutory EU deadlines don't usually slip without reason: a late request for
commitments typically precedes a with-remedies clearance (not a clean one); a referral
risk; or something in the file not fitting the rubber-stamp pattern. Proposes revised
weights: clean approval ~35-40%, remedies ~40-45%, delay/referral 15-20%, block ~3%.

Bull's "other jurisdictions cleared" is unsourced — no named jurisdictions, dates, or
conditions. Sequencing through easier jurisdictions first is standard deal-counsel
practice and doesn't imply the EU, historically the toughest venue on US media
consolidation and cross-border bundling, will be equally easy.

Quant's own admission — that EV flips negative if the true spread is only ~1%, an
unobserved input — means the trade rests on a placeholder, not a real number; sizing
down or using the underlying instead of options doesn't fix the missing-input problem.

Missed asymmetry: PSKY (acquirer) carries $111B of leverage/integration risk —
divestitures would hurt PSKY's post-deal economics even in the "approval" bucket, while
WBD is comparatively insulated as long as the deal survives at all; quant's "ambiguous"
on PSKY should be "bearish-skewed."

Position: NO TRADE, more skeptical than quant's already-cautious take; wants
confirmation of *why* the deadline slipped before treating "imminent" as a green
light. Would change bear's mind: confirmation the slip was purely
administrative/procedural; actual WBD deal terms to compute the real spread; named
jurisdictions/dates/conditions for the "already cleared" claim; any Phase II signal
(would flip bear to actively bearish WBD short-dated).

### Quant rebuttal

Grants bear's point is a real but bounded Bayesian update: an EU Phase I clock doesn't
casually "slip" — it clears, opens Phase II, or stops (a "stop-the-clock" when parties
owe information) — so the miss is consistent with administrative lag, last-minute
remedy fine-tuning, or a stop-the-clock, not only the bearish branch. Revises: 83%
approval (was 88%), 12% delay/Phase II (was 9%), 5% block/heavy-remedies (was 3%) — "a
nudge, not a regime change."

Reframes the fight: neither bull nor bear sourced the deal consideration or WBD arb
spread — the load-bearing input, absent from the dossier. Illustrative math (invented
$330 takeout vs. WBD $317.58 ≈ 3.9% spread): original 88/9/3 priors → EV ≈ +2.17%;
revised 83/12/5 priors → EV ≈ +1.26%. Bear's update roughly halves the edge — material
— but the whole calculation rests on an invented spread; if the real spread is ~1%, EV
is negative under both prior sets. "Without the actual spread, EV is unsigned."

On PSKY: bull's re-rating narrative has no coefficient or historical distribution;
acquirer reactions to expected clearance are empirically small and sign-ambiguous —
still avoid, or size as a pure lottery ticket, not a thesis leg.

Would change quant's mind (priority order): (1) actual deal consideration + live WBD
spread — decisive; spread >5% supports a buy, <2% is a pass; (2) EU procedural posture
confirmation (Phase I-clean vs. Phase II vs. stop-the-clock) — Phase II confirmation
flips negative; (3) whether other-jurisdiction clearances were conditional — raises EU
remedy odds.

Bottom line: bear earns a real but bounded revision (88/9/3 → 83/12/5); bull earns
nothing on the PSKY leg. Structure unchanged — WBD-long is the only defensible
expression — but no size committed until the spread is known: "we are all pricing a
coin flip while refusing to look at the payout."

---

## Round 3 — Synthesis (opus, neutral)

**Hypothesis:** A long-WBD merger-arbitrage tilt into the imminent EC ruling is
directionally the only defensible expression the panel identified (approval remains
the modal outcome, ~83% combined per quant's revised distribution), but the trade's EV
cannot be signed without the actual deal consideration and live WBD arb spread — the
single load-bearing input, which no persona could observe and which quant explicitly
admitted inventing for illustrative math. With that input unobserved, and the EC
deadline already three days stale (a genuine, bounded bearish signal), there is
insufficient information to responsibly initiate now. Direction: **no-trade**.
Confidence: **72/100** (confidence in the no-trade/insufficient-information verdict,
not in a directional bet).

**Plan:** No trade initiated on WBD or PSKY. PSKY rejected as a thesis leg entirely
(acquirer reaction to expected clearance is empirically small and sign-ambiguous).
Triggers that would convert this into an actionable plan, in priority order:

1. Actual deal consideration + live WBD arb spread (decisive). Spread ≥~5%: buy WBD
   (common or near-dated calls, flag IV crush), size ≤1-2% of book, ideally
   put-hedged; entry at/just before the clearance headline, exit on the post-clearance
   pop/spread collapse. Spread ~2-5%: smaller tilt, only if procedural posture (below)
   is benign. Spread <~2%: pass — the block tail alone turns EV flat-to-negative.
2. EU procedural posture confirmation. Phase I-clean or confirmed
   administrative/stop-the-clock lag supports the long; a confirmed Phase II
   opening/Statement of Objections flips the thesis negative (bear would go actively
   short-dated WBD).
3. Whether the other-jurisdiction clearances were conditional or unconditional.
   Conditional peer clearances raise the odds of EU remedies and argue against a
   clean-approval-priced long.

**Dissent (strongest unresolved disagreement):** Bear vs. bull on the meaning of the
passed/stale EC deadline, with quant mediating but not resolving it. Bear holds the
slip is substantive evidence of remedies negotiation, stop-the-clock, or a Phase II
being teed up (proposed weights ~35-40% clean / ~40-45% remedies / ~15-20% delay).
Bull holds the slip is likely routine administrative friction, common even in
eventually-clean clearances, and that sequential peer clearance is affirmative
evidence against a smoking-gun overlap. Quant split the difference with a bounded
revision (88/9/3 → 83/12/5), calling it "a nudge, not a regime change." This is
unresolved because it requires external facts none of the personas could access — the
actual EU procedural posture and the reason for the deadline miss — the same class of
missing data as the unresolved WBD/PSKY deal consideration and live arb spread that
quant admitted inventing ($330 illustrative takeout) to make the EV math run. A future
post-mortem should score both: which deadline-slip interpretation reality vindicated,
and what the true arb spread actually was versus quant's placeholder.

---

**Result: no-trade.** Status set to `researched`. Convert to a live plan only when deal
terms/arb spread and EU procedural posture become observable.
