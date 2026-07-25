# Research debate transcript — 2026-07-23-mirum-volixibat-pfic-data (MIRM)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `debate-three-round-panel`. Personas: bull (sonnet), bear (sonnet), quant
(opus). Synthesizer: opus. Run at 2026-07-25T17:30:06Z.

Dossier event: Mirum Pharmaceuticals volixibat Phase 3 data in PFIC (progressive
familial intrahepatic cholestasis), impact window 2026-08-15. Source: "10 clinical
trials to watch in the second half of 2026," BioPharma Dive,
https://www.biopharmadive.com/news/biotech-pharma-clinical-trials-watch-2026/808255/
(accessed 2026-07-23).

Institutional lessons injected (via `toa lessons-relevant --type regulatory --tickers MIRM`):
- Never map a corporate/legal calendar date directly onto an execution timestamp;
  treat it as a catalyst and derive the fill time from the nearest valid trading
  session. (source: 2026-07-08-caesars-icahn-fertitta-bidding-war)
- Test-query the real price provider for exact entry/exit timestamps during
  research; a plan that can't be priced resolves as an uninformative neutral.
  (source: 2026-07-12-nayax-cyber-breach-ultimatum)
- Never treat a single missing minute-bar as terminal — exhaust a fallback ladder
  before recording market-data-unavailable. (source: 2026-07-13-tariff-section122-expiry)
- Size fill-precision to the size of the edge: low-conviction/low-profit trades
  should use tolerance windows, not exact-minute targets. (source: 2026-07-13-tariff-section122-expiry)
- A signal-to-noise ratio below ~0.15 on a linear-EV fade is not a durable edge.
  (source: 2026-07-10-prologis-segro-bid-deadline)

---

## Round 1 — Independent research

### BULL (sonnet)

Mirum already has one approved rare pediatric cholestasis drug (Livmarli/
maralixibat). Volixibat is framed as a second IBAT inhibitor in the same class,
being tested in PFIC — a "prove out asset #2 in a validated mechanism, validated
indication, validated commercial team" setup, analogous to Albireo's Bylvay/
odevixibat (also IBAT, also approved in PFIC). Positive Phase 3 PFIC data would be
a credible path to a second NDA filing, expanding Mirum's addressable market and
de-risking the "one-drug story." Single-asset rare-disease biotechs commonly see
double-digit-to-50%+ moves on binary pivotal readouts given thin float.

Proposed action: long MIRM (common stock or short-dated calls if a liquid options
chain exists), position ahead of 2026-08-15 with fill pinned to the nearest valid
trading session (per institutional lesson), hold through the print, exit within 1-2
sessions of the reaction.

Flagged uncertainties: date firmness (a listicle, not a company-issued date); what
"positive" data looks like (endpoint/powering unknown); current MIRM market cap /
options liquidity unknown; real-provider price test not yet run; whether the
market already prices in a clean readout given the de-risked mechanism.

### BEAR (sonnet)

No informational edge exists pre-readout: the dossier contains zero efficacy or
safety data — it is a trade-press "trials to watch" mention, not a data
disclosure. The 2026-08-15 date is soft: sourced from a roundup that only scopes to
"the second half of 2026," not company IR, an SEC filing, or a ClinicalTrials.gov
primary-completion date; topline delays are the norm, not the exception, in rare-
pediatric trials with small enrollment pools.

What's already priced in: MIRM is a commercial-stage rare-liver name with an
approved IBAT inhibitor (Livmarli) for Alagille and PFIC; the market has had years
to price the mechanism and pipeline optionality. The available "surprise" is only
the delta versus an unknowable consensus probability of success.

Binary-readout payoff: positive/clean → plausible double-digit pop; negative/mixed
→ sharp drawdown with gap risk, often illiquid on the print day. PFIC IBAT-inhibitor
programs have genotype-dependent efficacy history (PFIC1 has shown blunted or
paradoxical response in prior datasets), so a "positive" topline could still hide a
subgroup miss. Direction is close to unknowable absent DSMB signals, interim peeks,
or KOL channel checks, none of which are available here.

Bottom line: not-yet-tradeable. Needs (a) primary-source date confirmation, (b) a
scan of prior PFIC IBAT-inhibitor efficacy data, (c) an options-implied-move check
against a rational outcome distribution.

### QUANT (opus)

Verdict up front: PASS on any pre-readout directional bet.

Base rate: unselected Phase 3 success ~50-60%; grant a higher prior for a
mechanistically de-risked IBAT-class asset, PoS ~60-70% on the trial's own primary
endpoint. But trial success ≠ stock up — modeled outcome distribution for a
secondary-asset readout at a commercial-stage mid-cap: clean win +8% to +20%
(median +12%, p=0.45); mixed/ambiguous -3% to +3% (median +0.5%, p=0.25); clean miss
-12% to -30% (median -18%, p=0.30). The shape is asymmetric against the long.

Information edge: none. The dossier supplies no interim efficacy readthrough, no
DSMB/early-stop signal, no analyst consensus PoS, no options-implied move, no
positioning data — just a listicle mention.

**Integrity flag:** the dossier states volixibat is in "Phase 3 in PFIC," but
recollection is that volixibat's disclosed late-stage programs are PSC (VISTAS)
and PBC (VANTAGE) — cholestatic pruritus indications — while Livmarli
(maralixibat) is the drug with PFIC/Alagille approvals, competing with Albireo's
Bylvay (odevixibat) in PFIC specifically. Cannot verify online this round; applies
p ≈ 0.4 that the dossier's drug/indication pairing is correct as written.

Date: 2026-08-15 is a Saturday — not a trading session — and the source only
scopes to "the second half of 2026." P(readout on/before 2026-08-15) ≈ 0.18;
P(the stated window is pure noise, no real catalyst) ≈ 0.82.

EV: `EV_gross(conditional) = 0.45(+12%) + 0.25(+0.5%) + 0.30(-18%) = +0.125%`.
Net of ~40bp round-trip slippage/spread for a mid-cap biotech: `EV_net(conditional)
= -0.28%`. Unconditional on date risk: `EV_net = 0.18(+0.125%) + 0.82(0%) - 0.40%
= -0.38%`. Breakeven requires p(win) > 0.459 ignoring date risk, > 0.52 including
it — no evidence supports this. Short side worse (-0.8% to -1.4% EV incl. borrow,
unbounded gap-up risk). Long-premium/straddle: paying for event vol on a date 82%
likely to be wrong — pass.

SNR: conditional 0.125/11.3 ≈ 0.011; unconditional 0.02/11.6 ≈ 0.002 — one to two
orders of magnitude below the ~0.15 durability floor.

Execution: test-queried the real provider per institutional lesson —
`toa price MIRM ... --provider twelvedata` returned HTTP 429 on all timestamps
tried; SPY control also 429'd, confirming global provider quota exhaustion rather
than a MIRM-specific coverage gap. Price remains unverified this round.

Position: PASS pre-readout, long or short. Best alternative is post-readout
momentum only (base rate ~55-60% continuation over 5-10 days, EV_net ≈ +0.05%,
SNR ≈ 0.1) — still under the durability floor; "watch, don't fund." Preconditions
to reconsider: company-confirmed date, resolved indication inconsistency, a
successful priced probe on the exact entry/exit minutes.

---

## Round 2 — Rebuttal

### BULL rebuttal

Concedes the indication-mismatch flag is disqualifying until resolved — withdraws
the "volixibat PFIC" thesis as stated; if the real trial is VISTAS/VANTAGE, it's
effectively a different dossier, not a rebuttal point winnable here. Concedes the
quant's EV math and asymmetric payoff shape stand — Round 1 was "the setup is
interesting," not an EV calculation, and no counter-model exists. Concedes the date
risk (soft sourcing + Saturday date) breaks the "position ahead of 8/15" plan and
retracts the pre-positioning instruction entirely.

What would change my mind: (a) ClinicalTrials.gov/Mirum-IR confirmation of the
actual drug/indication/date, (b) a scan of prior PFIC (or PSC/PBC) IBAT-inhibitor
efficacy data to re-weight the outcome distribution with evidence, (c) an
options-implied-move check against that distribution. What still stands, weakly:
the general category (commercial-stage rare-disease name + binary pipeline
catalyst) is a legitimate trade shape *if* the facts check out — but that's a
process point, not a claim on this dossier as currently specified. On the facts in
front of the panel: agrees with quant, PASS.

### BEAR rebuttal

The quant's EV math corroborates and sharpens the skepticism — EV_net is negative
even conditional on the dossier being accurate, and SNR is over an order of
magnitude short of the durability floor; Round 1's "not-yet-tradeable" was too
generous. The indication-mismatch flag is now the load-bearing objection: a soft
date means the edge might arrive later; a wrong drug/indication pairing means the
event described may not exist at all, and every downstream number in the debate
(PoS, outcome distribution, the bull case) is scaffolding on an unchecked premise
sourced only from a listicle.

The bull's "de-risked mechanism, second NDA path" framing breaks two ways: if the
mismatch is confirmed, there is no PFIC readout from volixibat to de-risk; and even
taking the framing at face value, the quant's EV math already kills it — de-risked
biology does not imply de-risked stock economics on an asymmetric binary print.

Escalates from "not-yet-tradeable, needs verification" to recommending the dossier
be excluded from the active plan entirely: two independent failure modes now stack
(EV math fails even under generous assumptions, and the core factual premise may
not exist). What would change this: primary-source confirmation of the drug/
indication/date, a resolved options-implied-move check, and genotype/subgroup
detail on PFIC response history.

### QUANT rebuttal

Restates the objection numerically for the bull: unconditional EV_net ≈ -0.38%,
SNR 0.002-0.011 vs the 0.15 floor (14-75x short), Kelly f* ≤ 0 on a negative-edge
bet. To merely break even, conditional-on-event p(win) must exceed ~0.53 (symmetric
±30%) or ~0.57-0.58 under a realistic asymmetric payoff for an illiquid single-
asset-story smallcap — asks the bull directly to defend an evidenced p(win) at
that level; none is offered, so the bull's own framework concedes PASS. Notes
"de-risked mechanism" is a prior on PoS, not an edge — an edge requires a delta
versus consensus PoS, which nobody has identified.

Sharpens the bear's epistemic argument into a structural one: even granting the
bull's best-case premises in full (trial exists, date real, class read-through
genuine, PoS above naive base rate), payoff shape alone still makes the long
negative-EV, because a pre-priced high prior converts into a modest pop against a
full-size gap-down tail. This makes the PASS over-determined — bear's and quant's
arguments point the same way via independent routes, warranting higher combined
confidence than either alone. Extends the bear's genotype point: the outcome space
is really three-branch (clean win / headline-positive-with-subgroup-miss / miss),
and the modal middle branch resolves ambiguously-to-negatively for a leveraged
long, pushing EV further down, not rescuing it.

On the indication-mismatch flag: cannot verify online, holds at p ≈ 0.4. Notes a
sharp interaction — the bull's central analogy (Bylvay/odevixibat) is actually the
PFIC comparator to *Livmarli*, not to volixibat, per the quant's recollection; if
so the bull's analogy is evidence for a different asset than the one being traded.
Recommends NOT folding this into the EV math (PASS already stands without it) but
logging it as a separate, unresolved fact-check that independently caps any future
trade confidence at a ~0.4 multiplier ("low confidence, ever, until cleared"), and
flags it as a possible scout-time data-integrity defect worth logging alongside
existing venue-coverage gates, not merely a research gap.

Final verdict: PASS — no position, long or short, into 2026-08-15. Confidence in
the PASS itself: 0.78-0.85 (high, over-determined across EV math, SNR, date
softness, and the information argument independently). Confidence a directional
long has positive EV: <0.15. Confidence in the dossier's factual premise: ~0.4.
Four preconditions to ever reconsider, all required: (1) primary-source-confirmed
date on a real trading session, (2) indication fact-check cleared, (3) a working,
liquidity-gated price provider, (4) an options chain showing implied move
underpricing realized readout moves — which would indicate a long-volatility,
non-directional structure, not a directional bet.

---

## Round 3 — Synthesis (opus)

**hypothesis:**
- statement: The dossier's core premise (a volixibat Phase 3 PFIC readout at MIRM
  on 2026-08-15) is not established — volixibat's known late-stage programs are
  PSC (VISTAS) and PBC (VANTAGE); PFIC/Alagille is Livmarli's indication, making
  the drug/indication pairing a probable scout-time data-integrity defect
  (P(premise correct) ~0.4). Independently, the date is soft (trade-press listicle,
  not IR/SEC/CT.gov) and 2026-08-15 is a Saturday — not a trading session. Even
  granting the bull's mechanistic de-risking argument in full, the payoff shape of
  a directional pre-readout long is negative-EV under the panel's own generous
  assumptions (EV_net ≈ -0.28% conditional, ≈ -0.38% unconditional; breakeven needs
  an undefended p(win) > ~0.52-0.58). SNR (0.002-0.011) sits one to two orders of
  magnitude below the ~0.15 durability floor, with zero efficacy/safety/DSMB/
  consensus-PoS data in the dossier to supply an edge.
- direction: none
- confidence: 18 (in a directional trade being right; confidence in the no-trade
  verdict itself is 78-85, over-determined across EV math, SNR, date softness, and
  the unresolved factual premise, each independently sufficient for PASS)

**plan:** no-trade / watch-only. No position taken, long or short, into MIRM.
Preconditions for re-evaluation (all four required): (a) primary-source
(IR/SEC/ClinicalTrials.gov) confirmation of the drug, indication, and trial
identity; (b) a confirmed readout date landing on a real trading session; (c) a
working, liquidity-gated price provider for MIRM (twelvedata hit a global HTTP 429
this round — price unverified); (d) an options chain showing implied move
underpricing realized readout moves for comparable rare-disease Phase 3 toplines —
which would indicate a long-volatility structure is the correct trade, not a
directional long.

**dissent:** Exclude-outright (bear) vs keep-as-capped-watch (quant) — the
synthesis sided with bear on disposition (no position, effectively shelved) but
with quant on bookkeeping (log the drug/indication mismatch separately rather than
folding it into the EV math). Secondary dissent: the bull conceded on every axis by
Round 2 without ever producing a counter-model or a defended p(win) estimate, so
the panel's convergence may be softer than its stated confidence — the strongest
possible long case (options-implied-move underpricing, thin-float squeeze
mechanics) was never actually argued. Post-mortem test: if a real MIRM binary print
occurs near the window and moves >20%, check whether a long-volatility structure
would have been profitable even though the directional long was correctly
rejected; also check whether a pre-debate primary-source verification gate at
scout time would have caught the indication mismatch before three rounds of debate
were spent on it.
