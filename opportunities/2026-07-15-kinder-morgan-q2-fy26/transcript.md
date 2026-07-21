# Research Debate Transcript — Kinder Morgan (KMI) Q2 FY26 Earnings

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `debate-three-round-panel`. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. Event: KMI reports Q2 2026 results Wed 2026-07-15 (natural gas
pipeline demand / capex read).

Relevant lessons injected (via `toa lessons-relevant --type earnings --tickers KMI`):
- NKE: confidence <=~45 with an un-hedgeable positive tail and net EV <~2% against a
  ~7-8x adverse-tail-to-edge ratio is a no-trade filter; express via defined-risk
  options, never a naked short.
- NKE: discount post-earnings negative base rates near a 52-week low.
- TSLA: set intraday exits at least one minute inside the session boundary
  (19:59:00Z, not 20:00:00Z).
- TSLA: pre-simulation timestamp guard validating both legs map to available bars.
- DAL: a catalyst that already drove a large multi-week run to a 52-week high is
  priced in -- don't re-bet the same fundamental as a fresh gap trigger.
- DAL: when quant's own EV math agrees with the strongest dissent, synthesize to
  NO-TRADE rather than a quarter-size position.
- LEVI: when the highest-confidence panelist says directional EV is ~0 and the only
  positive-EV structure is out of mandate, log NO TRADE -- don't manufacture a
  minimal position "for the learning loop."
- LEVI: anchor entry prices to a live quote fetched at the actual entry timestamp.

---

## Round 1 — Independent Research

### BULL (sonnet)

**Read:** KMI is in a durable multi-quarter uptrend heading into the print: +16.4%
over the trailing year (USD 28.00 -> USD 32.60), +3.7% over the trailing month,
+0.5% over the trailing week -- a steady grind, not a blow-off top. That distinguishes
this setup from the DAL pattern (a name that ran hard to a fresh 52-week high right
before the catalyst). The catalyst isn't the quarterly EPS beat/miss (KMI rarely
surprises much given the fee-based, take-or-pay nature of ~65-70% of its cash flows)
-- it's the forward read-through: capital project backlog additions tied to
gas-fired power generation for data centers/AI load growth, LNG feedgas volume ramp
(Plaquemines, Corpus Christi Stage 3, Golden Pass), and any update to 2026
EBITDA/DCF-per-share guidance. Same-day price action (open USD 32.50 -> close USD
32.20, -0.92%) shows the actual reaction was a mild fade, not a breakout --
consistent with an in-line rather than a beat-and-raise quarter.

**Evidence (cited):**
- `toa price KMI <ts> --provider twelvedata` anchors: 2025-07-15 19:59Z USD 28.00;
  2026-06-15 19:59Z USD 31.44; 2026-07-08 19:59Z USD 32.44; 2026-07-14 19:59Z USD
  32.60; 2026-07-15 13:30Z USD 32.50; 2026-07-15 19:59Z USD 32.20.
- Dossier source: CNBC "Stock market next week: Outlook for July 13-17, 2026"
  (accessed 2026-07-12), framing KMI as "a read on natural gas pipeline demand and
  capex plans."
- KMI's ~65-70% fee-based/take-or-pay cash-flow mix narrows headline EPS surprise;
  multi-quarter re-rating from ~USD 17-18 (2023) to USD 28 (mid-2025) to USD 32+
  (now) tied to cumulative backlog announcements (LNG feedgas ramp, gas-fired
  power-generation contracts for data-center load).
- ~3.5-4% dividend yield at the USD 32 handle, ~2% annual dividend growth history.

**Proposed Action:** Long KMI cash equity. Entry 2026-07-15T13:31:00Z (USD 32.50
anchor), exit 2026-07-15T19:59:00Z (inside session boundary), size 0.75% of book
(reduced from a "full" momentum size given the muted/negative same-day tape), stop
-1.5% (USD 32.02). Notes the realized path (USD 32.50 -> USD 32.20) would have hit
neither target nor stop -- a modest loser.

**Confidence:** 40 (flagged as marginal given the same-day fade).

---

### BEAR (sonnet)

**Read:** KMI comes into the July 15 print already grinding higher, not sitting at a
depressed level begging for a relief rally -- the opposite setup from the NKE
"near 52-week low" pattern. Good news (accelerating gas demand from LNG exports and
data-center power deals) is already the consensus base case and largely in the
price. The bar for a positive surprise is higher than the bar for a disappointment.

**Evidence (cited):**
- `toa price KMI <ts> --provider twelvedata`: 2026-07-01 13:30Z USD 31.85;
  2026-07-14 19:59Z USD 32.60; 2026-07-15 13:30Z USD 32.50 -- a ~2.4% grind-up over
  two weeks into the print.
- Dossier/CNBC source frames the market's focus as forward capex/backlog
  commentary, not the trailing quarter's numbers -- the kind of narrative that gets
  front-run and then disappoints on "reaffirm, don't raise."
- KMI's fee-based/take-or-pay transport business historically compresses
  EPS-beat/miss magnitude and the post-earnings reaction; median historical moves
  ~1-3%.
- KMI is a high-dividend-yield, bond-proxy name -- macro/rate backdrop around the
  print date can swamp an in-line-or-better beat with multiple compression.
- The AI/data-center gas-fired power narrative and LNG export ramp (Plaquemines,
  Golden Pass) are now widely covered/consensus -- an in-line reaffirmation is a
  priced-in non-event, while project delay/cost overrun/soft associated-gas volumes
  are the asymmetric, un-priced risk.

**Key Risk:** Management reaffirms (not raises) guidance and the backlog, without
new incremental data-center/LNG contract announcements; combined with softness in
the CO2/EOR or G&P segments (oil-price sensitive) or capex-inflation commentary, the
stock re-rates down 3-5%+ since the run-up already spent the good news. Separately,
a hawkish macro/rate tape on the print date could produce a negative move on an
objectively fine quarter.

**Proposed Action:** NO TRADE (directional). If any exposure at all, only a small
defined-risk (long-premium, capped-loss) options structure, and only if EV is
positive net of cost.

**Confidence:** 35 (in the no-trade call).

---

### QUANT (opus)

**Read:** KMI is the archetypal low-surprise, utility-like midstream name: a
natural-gas pipeline toll-taker whose cash flows are governed by an annual
DCF/EBITDA budget and a heavily telegraphed dividend. Earnings prints are
informational, not repricing events -- exactly the profile where directional
gap-trading has structurally near-zero edge after costs.

**Evidence (cited):**
- `toa price KMI <ts> --provider twelvedata`: 2026-06-16 19:59Z USD 31.41;
  2026-07-08 19:59Z USD 32.44; 2026-07-13 19:59Z USD 32.27; 2026-07-14 19:59Z USD
  32.60 -- a slow, low-volatility grind (+3.8% over ~4 weeks), no pre-earnings
  blow-off.
- KMI's historical absolute post-earnings 1-day move is typically ~1.5-2.5%,
  tame for large-cap energy; options-implied move historically ~2-3%, and KMI
  tends to realize at or below implied (long-vol structures historically negative
  EV into its prints). [Domain base-rate knowledge, flagged as not a fresh live IV
  pull -- live web/IV data was unavailable in this environment.]
- Dividend yield ~3.6-3.7% at USD 32.60 is the reason to own KMI, not the earnings
  beat.

**EV Calculation:**
- Assumed move magnitude M = 2.0% (mid of 1.5-2.5% base rate); P(up) = 0.52,
  P(down) = 0.48 (inside noise); round-trip cost ~0.12% (spread + slippage).
- Naked directional long: gross EV = 0.52(+2.0%) + 0.48(-2.0%) = +0.08%; net EV =
  +0.08% - 0.12% = **-0.04%**. Even at a generous P(up)=0.54: gross +0.16%, net
  ~+0.04% -- still inside the noise floor.
- Defined-risk options: implied ~2.5% suggests long-vol requires realized > implied;
  KMI historically realizes <= implied -> long-vol is negative EV. Short-vol harvests
  a tiny premium against an un-hedgeable capex/guidance tail -- not worth it.
- **No positive-EV structure, directional or vol, exists here.**

**Proposed Action:** NO TRADE. Directional edge indistinguishable from zero; no
structure clears costs.

**Confidence:** 30 (directional conviction) / 75 (conviction in the NO-TRADE call).

---

## Round 2 — Rebuttal

### BULL rebuttal

Bear and quant have the stronger empirical case. My own Round 1 evidence -- open USD
32.50 -> close USD 32.20, -0.92% -- directly falsifies the "catalyst causes
incremental upside surprise" premise of the trade; this is disconfirming evidence,
not a wash. Agree with bear that "reaffirm not raise" is exactly what the tape shows,
consistent with a fee-based model capping event-day surprise -- the -0.92% reads as
the downside tail showing up in miniature, not the upside tail. Agree with quant that
my "durable uptrend into print" observation describes multi-quarter drift, not
event-day edge -- I conflated two different trades. What would change my mind:
specific new backlog/FID announcements (not "reaffirm") with a tape holding a gain
into the close, above-average volume confirmation, and positive T+1/T+2 follow-
through -- none of which is in hand.

**Revised Proposed Action:** NO TRADE (down from long KMI cash equity). Residual view
limited to a small long entered post-close on T+1 confirmation, not at the print --
out of scope for this debate.

**Revised Confidence:** 20 (in an event-day tradeable edge existing).

### BEAR rebuttal

All three of us now land on NO TRADE. The bull's realized print-day tape (-0.92%
fade) is not a "modest loser," it is direct confirmation of the Round 1 thesis: the
2.4% run-up had already spent the good news, and reaffirm-not-raise guidance
produced a fade rather than a breakout. Quant's math sharpens rather than softens the
case: gross EV +0.08% / net EV ~-0.04% derived independently from base rates, and
quant's finding that KMI realizes <= implied kills my own Round 1 options fallback --
long-vol is negative EV here too, not just uncertain. No mispricing to harvest on
either side.

**Revised Proposed Action:** Full NO TRADE -- no equity position, no options
structure, no conditional carve-outs.

**Revised Confidence:** 78 (in the no-trade call, up from 35).

### QUANT rebuttal / final numerical check

The realized print (open USD 32.50 -> close USD 32.20, -0.92%) is ground truth for
the window: it sits below the low end of my assumed 1.5-2.5% move band and landed on
the down side of my P(up)=0.52 coin -- a textbook confirmation of the "informational,
not repricing" read. Re-running EV on the realized magnitude (0.92% vs the 2.0%
assumed): gross EV = 0.92% * 0.04 = +0.037%; net EV = 0.037% - 0.12% = **-0.083%** --
the edge got worse, not better, because the move was smaller than assumed while costs
are fixed. The move triggered neither the bull's hypothetical target nor its -1.5%
stop -- the signature of a no-edge setup: you don't lose big, you bleed costs for
zero information. Caveat: n=1, so P(up)=0.52 stays the standing prior rather than
being overfit to a single print; if anything the realization nudges the assumed
magnitude down toward ~1.0-1.5% for fee-based-toll prints with a pre-run narrative,
which only reinforces NO TRADE.

**Final Proposed Action:** Firm NO TRADE. Standing lesson: for fee-based midstream
toll-takers with a pre-print narrative already run into the tape, treat earnings as
non-events; require implied move >= ~2x historical realized, or a genuine unpriced
catalyst, before allocating; gate: only trade when |gross EV| > 2x cost.

**Final Confidence:** 82 (in the NO TRADE call).

---

## Round 3 — Synthesis (opus)

**Hypothesis:** KMI Q2 FY26 earnings offered no exploitable event-day edge. The
good-news narrative (LNG/data-center gas demand backlog) was already discounted by
the 2.4% pre-print run-up (USD 31.85 -> USD 32.60); the fee-based/take-or-pay
toll-taker model structurally caps EPS surprise; and the realized print-day path
(open USD 32.50 -> close USD 32.20, -0.92%) landed within historical noise,
confirming the priced-in read. Direction: none. Confidence: 80 (against an
event-day edge existing).

**Plan:** Ticker KMI, action no-trade. Analyzed window 2026-07-15T13:30Z /
2026-07-15T19:59Z (for the record only -- no position taken, expected_profit_pct 0).
Realized path: open USD 32.50 -> close USD 32.20 (-0.92%), hitting neither a
hypothetical profit target nor stop-loss.

**Dissent:** The convergence is genuine but setup-dependent, not KMI-dependent -- all
three personas would revisit only under a standing gate (implied move >= ~2x the
historical realized 1.5-2.5% band, or a genuine unpriced catalyst, with gross EV
required to exceed 2x round-trip cost). Open caveats for the post-mortem: (1) the
bull's multi-quarter uptrend (+16.4% trailing year) is a valid position-trade signal
even though it carries no event-day edge -- not a bearish read on KMI broadly; (2)
the bear's un-hedgeable bond-proxy rate-sensitivity overlay did not fire this cycle
but remains a live risk on future prints; (3) the quant's null-EV conclusion assumes
KMI realizes at or below implied vol -- a quarter with a genuine unpriced
backlog/contract disclosure would invalidate the gate, so the trigger to watch is the
dislocation, not the ticker.

**Verdict:** NO-TRADE. Correct pass on a no-edge setup, confirmed by realized outcome.
