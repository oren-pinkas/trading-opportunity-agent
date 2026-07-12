# Debate transcript — 2026-07-10-meta-broadcom-ai-chip-production

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `debate-three-round-panel` (three-round-panel). Personas/models: bull/sonnet,
bear/sonnet, quant/opus, synthesizer/opus. Run at 2026-07-12T12:53:00Z.

Event: Meta will begin production of its in-house Iris (MTIA) AI chip, co-developed
with Broadcom and fabbed by TSMC, starting September 2026, targeting 14GW of compute
by 2027. Ticker in scope: AVGO. Source: Reuters via CNBC (2026-07-09/10),
https://www.cnbc.com/2026/07/09/meta-to-put-ai-chip-into-production-in-september-report.html.
Impact window: 2026-09-01. Dossier created 2026-07-10T15:17:34Z (status: scouted, no
prior research).

Institutional lessons checked (`toa lessons-relevant --type product --tickers AVGO`):
none on file.

**Data-quality note (applies throughout):** the internal `toa price AVGO <timestamp>`
feed in this environment is a deterministic stub and returned incoherent values —
$64.01 at 2026-07-10T15:17Z, $341.77 at 2026-07-09T15:00Z, $174.64 at
2026-07-12T12:37Z — a >5x swing across ~48 hours with no news to explain it. No
persona treated these as real price levels. No WebSearch/WebFetch tool access was
available to any persona in this run.

---

## Round 1 — Independent research (parallel, blind to each other)

### Bull (sonnet) — confidence 62

**Read:** Confirmation-of-ramp event, not a rumor — Reuters reports Meta's in-house
"Iris" MTIA accelerator, co-developed with Broadcom, fabbed at TSMC, moves from
development to production in September 2026, targeting 14GW of compute by 2027. For
AVGO this is the inflection where design/NRE revenue converts into high-volume unit
economics for Broadcom's AI ASIC line, reinforcing Broadcom's position as preferred
co-design partner vs. Marvell and Nvidia's merchant GPU franchise. Networking attach
(Tomahawk/Jericho switches, co-packaged optics) tends to scale with custom-accelerator
cluster buildouts, so a 14GW multi-year buildout implies a trackable, near-term ramp
curve rather than a distant 2027 promise.

**Evidence:** Reuters/CNBC dossier source (2026-07-09/10); dossier's own
`impact_window` flags 2026-09-01 as a dated, tradeable catalyst; general knowledge
that Broadcom's AI semiconductor segment is built substantially on hyperscaler custom
XPU programs (Meta, Google as anchor customers) — flagged as lower-confidence
background, not a sourced fact for this specific event. No working web access; price
feed confirmed broken and not used for price levels.

**Proposed action:** Long AVGO (equity or dated calls expiring after September 2026).
Enter now or on near-term weakness between now and late August. First checkpoint:
Broadcom's next earnings call following the September production start — reassess/trim
if that call doesn't show accelerated AI-segment guidance tied to this program. No
specific entry/stop/target price levels proposed, given the broken price feed.

**Confidence: 62** — docked for inability to verify whether this is already priced in,
for "production start" being somewhat expected news given the pre-existing
relationship, and for not yet having seen bear/quant downside risks.

### Bear (sonnet) — confidence 62

**Read:** This is a confirmation event, not new information — the Meta-Broadcom MTIA
relationship has been public since ~2023 (MTIA v1) and reiterated on Broadcom's own
earnings calls. A confirmatory production-start headline for an already-known
relationship, with no new financial detail, is a textbook sell-the-news setup rather
than a fresh entry point. The bull framing has the causality backwards: Meta's
explicit long-term strategy is to reduce dependence on external silicon vendors,
including eventually Broadcom's IP/design services, as it internalizes more design
work over successive chip generations. Broadcom's economics here are custom
ASIC-design/IP-licensing plus networking fee — lower-margin and more
customer-concentrated than the market's current multiple may assume. The "14GW by
2027" figure is Meta's compute target, not a disclosed Broadcom order book.

**Evidence:** Single-sourced Reuters report (not a Meta/Broadcom filing or press
release) — no dollar figures, unit volumes, margin data, or exclusivity/contract-
duration disclosed. Relationship public since 2023 MTIA v1 and reiterated on Broadcom
earnings calls. Dossier itself has no prior research, price target, or analyst
reaction captured. Price feed confirmed broken/incoherent.

**Key risks:** sell-the-news/already-priced-in; in-house substitution risk (Meta
reducing reliance on Broadcom over successive chip generations, per the Google
TPU/Amazon Trainium-Inferentia precedent of hyperscalers internalizing more of the
stack over time); single-customer concentration risk; execution/timeline slip risk
(AI datacenter buildouts have a documented history of slipping); macro AI-capex-bubble
sentiment overhang affecting the whole custom-silicon group regardless of
Meta-specific fundamentals.

**Proposed action:** No new long entry off this headline. If AVGO gaps up meaningfully
on this specific news, that is a fade/no-chase signal rather than an entry signal.
Would not recommend an outright short, given the underlying custom-silicon growth
story is real.

**Confidence: 62** — moderately confident this news is low-information/already priced
in and a poor standalone catalyst for a fresh long; not high-confidence on an outright
short given the strength of the underlying multi-year growth trend.

### Quant (opus) — confidence 35/100 on point estimates, 72/100 on direction

**Read:** Low-information event dressed as news. The relationship (public since ~2023)
is consensus; this is a second-hand, non-quantified media report, and it is already
2-3 days stale relative to "now" (2026-07-12) — the efficient-market first reaction, if
any, has already occurred. Base rates: company-issued, quantified disclosures
(dollar figures, unit volumes) tend to move a partner stock ~+8-15%; second-hand,
non-quantified reports about an already-known relationship tend to produce muted,
short-lived low-single-digit pops that mean-revert within days.

**Evidence and assumed probabilities:** Source is Reuters/CNBC secondary reporting,
non-quantified for AVGO. Relationship pre-existing and consensus. News is 2 days
stale. Price feed confirmed broken/incoherent — no reliable price level, no real
return-distribution measurement possible, no web access to backfill. Assumed priors:
P(positive drift)=35% at +4%, P(noise/flat)=40% at 0%, P(negative/fade)=25% at -5%.

**EV calculation:** Gross EV = (0.35×4.0%) + (0.40×0%) + (0.25×-5.0%) = 1.40% + 0% -
1.25% = **+0.15%**. Round-trip cost/slippage for a mega-cap liquid name ≈ 8bps. **Net EV
≈ +0.07%** — positive but indistinguishable from zero/estimation error, before even
charging for ~7 weeks of carry/gap risk into September or for Broadcom's own September
earnings (the real, quantified catalyst) landing in the same window and swamping this
signal. Sensitivity check: even a generous reweight (45%@+4%/20%@-4%) only reaches net
~+0.9%.

**Proposed action:** No trade / stand aside. If forced to express anything: a tiny long
biased toward the September earnings print (not this news), sized at a fraction of a
normal unit, explicitly as an earnings bet rather than an Iris-production bet.

**Confidence:** 35/100 on point estimates (deliberately low — price feed unusable, no
live analyst-reaction data); 72/100 on the directional no-trade conclusion, which is
robust to the data gap because it rests on structural facts (stale, known,
non-quantified, already-priced) rather than exact price levels.

---

## Round 2 — Rebuttal (parallel, each shown the other two Round 1 positions)

### Bull rebuttal — confidence revised 62 → 56

Argues quant's EV model prices a different trade (headline-day reaction) than the one
actually proposed (hold into and past the September production start, checkpointed at
Broadcom's next earnings call — the same event quant identifies as "the real
catalyst"). Concedes bear's in-house-substitution risk is real but mistimed: Google's
TPU trajectory is the right precedent for a *mature* program, but Iris/MTIA is only
now hitting first production, so substitution risk is a multi-year overhang on the
relationship, not an argument against this specific ramp. Concedes the sell-the-news
framing for the headline itself — agrees a pure gap-up on this Reuters report would be
a fade/wait signal, not an entry signal. Flags an point neither bear nor quant
addressed: networking attach (Tomahawk/Jericho, co-packaged optics) as a second,
less-crowded revenue line riding the same buildout, less subject to the "known since
2023" staleness argument.

**Revised action:** scale in on weakness only, do not chase any headline-driven pop,
size to survive a sell-the-news fade, treat the September earnings call as the primary
confirm/kill checkpoint (not secondary). **Falsifiers:** no AI-segment guidance step-up
at Sept earnings tied to the Meta ramp; credible (non-rumor) reporting that Meta is
shifting next-gen MTIA design in-house or to a different partner; the 14GW/2027 figure
being walked back before September.

**Confidence: 56** (down from 62) — reflecting legitimate stale-news risk previously
underweighted, the bear's substitution-risk point being real even if long-dated, and
an unresolved blind spot: no way to verify whether the move is already priced in given
the broken feed.

### Bear rebuttal — confidence revised 62 → 66

Notes near-total convergence with quant (both land on stand-aside) — the only
disagreement in degree is that bear would widen quant's left tail slightly, since
"confirmation of a known relationship" events sometimes trigger sell-the-news
precisely because buy-side had already priced the ramp on rumor. Pushes back on
quant's framing that Broadcom's September earnings is a clean bullish catalyst
in waiting — argues even that catalyst is contaminated by the same
in-house-substitution overhang. Engages the bull's strongest point (backlog
conversion/networking attach) directly: doesn't dispute the mechanism exists, disputes
that *this specific headline* (a schedule confirmation, not a unit/dollar/margin
disclosure) is evidence of it — the networking/switching attach-rate story is the more
durable thesis and doesn't actually need this Reuters report to be true. Partially
concedes the bull's implicit counter (a production ramp announcement is evidence
against *near-term* abandonment of the partnership) but maintains this only
retimes, not retires, the substitution risk (3-5 year horizon, per the Google
TPU/Amazon Trainium pattern) — and notes bull never engaged with the multi-generation
revenue-share-erosion question at all.

**Action unchanged:** no new long entry; gap-up on this news remains a fade/no-chase
signal; would not short outright given the real underlying attach-rate growth story.
**Mind-changers:** a follow-up disclosure with actual unit volumes/dollar
content-per-system/ASIC-line gross margin; any exclusivity or multi-generation
contractual commitment disclosed; evidence the price reaction does NOT mean-revert
within 3-5 sessions post-print; explicit Meta/Broadcom commentary quantifying
Broadcom's expected multi-year revenue share under substitution pressure.

**Confidence: 66** (up from 62) — quant convergence and bull's non-engagement with the
substitution question both reinforce the no-trade priors; not raised further because
the backlog-conversion point is directionally real and worth revisiting at the actual
earnings print.

### Quant rebuttal — confidence 38/100 on estimates, 74/100 on direction

Grants the bull's backlog-conversion/networking-attach argument a small, quantified
right-tail bump — raises P(positive drift) from 35% to 38% and its magnitude from +4%
to +4.5%, crediting genuine ramp momentum and likely analyst-note flow, while
explicitly rejecting the bull's implicit use of the +8-15% "quantified disclosure" base
rate, since this report contains no $/unit/margin figures (siding with the bear here on
source quality). Grants the bear's fade-mechanic point (not the insourcing thesis) —
raises P(negative/fade) from 25% to 30%, holding magnitude at -5%; treats
in-house-substitution as a 2-4 year secular/terminal-value risk that doesn't resolve on
a September production-start headline, and notes the headline is arguably near-term
evidence the *current* generation is still on Broadcom silicon.

**Updated EV:** 38%@+4.5% + 32%@0% + 30%@-5% = gross **+0.21%**; net of ~8bps
round-trip cost = **+0.13%** — still statistically indistinguishable from zero. Notes
the reweighting raised both tails (bull's right, bear's left) while the noise bucket
shrank (40%→32%): variance went up (a more binary event than first modeled) but the
mean stayed pinned near zero — exactly what the symmetric 62/62 Round-1 confidence
scores predicted. Information ratio (≈+13bps edge against ~3-4% per-leg dispersion) is
far below anything worth committing discretionary risk capital to.

**Falsifiers (concrete):** a quantified $/unit/margin/exclusivity disclosure from
Broadcom or Meta (single most important trigger — flips the base rate regime); a
working price feed showing the actual cumulative gap size since the report (<~1.5%
implies no efficient pre-reaction and reopens a real drift trade; ≥+4% confirms the
bear's fade thesis); a cluster of 3+ analyst estimate revisions explicitly citing this
event; options IV term structure into Broadcom's September earnings showing cheap
front-month IV relative to realized.

**Final action:** no trade on the headline itself. Conditional carve-outs, each gated
on a working price feed: if minimal pre-reaction, small conditional long biased toward
the September earnings catalyst (not the news), fractional size; if already gapped
≥+4%, a small defined-risk short-the-pop (not an outright short, agreeing with bear's
own instinct there).

**Confidence:** 38/100 on point estimates (data gap unchanged); 74/100 on the
directional no-trade-on-headline conclusion.

---

## Round 3 — Synthesis (neutral synthesizer, opus)

**Hypothesis**
- **Statement:** The Meta MTIA/Iris production-start report is a low-information
  confirmation of a publicly known (since ~2023) Broadcom co-design relationship, not
  a quantified disclosure of Broadcom-booked revenue. Bull upside (ramp momentum,
  networking attach) and bear downside (sell-the-news, multi-generation in-house
  substitution, customer concentration) approximately cancel over this
  headline-to-impact window, leaving expected value statistically indistinguishable
  from zero net of costs. The real tradable catalyst is Broadcom's own September 2026
  earnings call, not this news.
- **Direction:** no_trade
- **Confidence:** 68

Convergence rationale: all three personas independently landed at or near
"stand aside." Quant's reweighted EV was net +0.13% (flat mean, wider tails). Bear
moved 62→66, explicitly noting near-total convergence with quant. Bull moved 62→56,
abandoning any headline-chase and retreating to "scale in on weakness only, Sept
earnings as confirm/kill." No persona advocated an outright short.

**Plan: no trade.**

The debate did not converge on a deployable long or short over this specific
headline-to-impact window. **Blocking data gap:** the internal AVGO price feed is
confirmed broken/incoherent ($64.01/$341.77/$174.64 across three nearby timestamps),
and no WebSearch/WebFetch was available to any persona — no entry, exit, or
profit-target price levels can be responsibly stated. Any real deployment is gated on
first sourcing a working, verified price feed.

Conditional plans if a specific falsifier is met (each still requires working price
data first):
- **If a live feed shows AVGO has not already gapped materially** on this news: open a
  small, fractional-size conditional long biased toward Broadcom's September 2026
  earnings call (not the headline). Kill if that call shows no AI-segment guidance
  step-up tied to the Meta program.
- **If AVGO has already gapped ≥+4%** on the headline: consider a small, defined-risk
  short-the-pop (options-structured, not an outright short) — a fade of headline
  euphoria, not a directional bearish thesis.
- **Primary revisit trigger:** Broadcom's September 2026 earnings call. Go/no-go signal
  = accelerated AI-segment guidance explicitly tied to the Meta program.
- **Additional confirm signals:** a quantified $/unit/margin disclosure tied to this
  program; 3+ analyst estimate revisions citing this specific event; options IV term
  structure into September earnings.
- **Kill signals:** no AI-segment guidance step-up at Sept earnings; credible reports of
  Meta shifting next-gen design in-house or to a rival; the 14GW/2027 target being
  walked back.

**Dissent (retained for post-mortem, not resolved):** the strongest unresolved
disagreement is whether the September earnings catalyst is clean or contaminated —
i.e., the timing vs. permanence of in-house substitution risk. Bull holds substitution
risk applies to future chip generations, not this production ramp, so Sept earnings
should cleanly show the NRE-to-unit-revenue conversion. Bear holds substitution risk is
only retimed (pushed 3-5 years out, per the Google TPU/Amazon Trainium precedent), so
even Sept earnings is contaminated by the same long-run revenue-share-erosion overhang.
Bull never engaged with bear's multi-generation revenue-share-erosion question — this
crux is unresolved and should be re-examined at the Sept earnings call with actual
segment guidance and margin data. Secondary latent dissent: quant rejected the +8-15%
quantified-disclosure base rate that bull implicitly leaned on, since no $/unit/margin
figures exist in the report — unresolved until such figures are disclosed.

**Overall confidence: 68/100** in the no_trade hypothesis for this specific event
window — high confidence in "no trade on the headline," tempered by the unknown actual
pre-reaction/gap state (the confirmed-broken price feed) and the unresolved bull/bear
dissent on whether Sept earnings is a clean catalyst.
