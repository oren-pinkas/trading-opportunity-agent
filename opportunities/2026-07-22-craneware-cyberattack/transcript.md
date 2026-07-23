# Research debate transcript — 2026-07-22-craneware-cyberattack

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Event: UK healthcare billing/RCM software firm Craneware disclosed on 2026-07-20
that attackers exfiltrated a significant volume of file names before being removed
from its systems; ongoing US/UK forensic investigation could reveal further scope
or customer-notification costs. Ticker: CRW.L (AIM). Impact window: 2026-08-20.
Source: TechRepublic, "Craneware Confirms Data Theft After Cyberattack"
(https://www.techrepublic.com/article/news-craneware-cyberattack-data-theft-2026/,
accessed 2026-07-22T11:19:27Z).

Institutional lessons injected (via `toa lessons-relevant --type regulatory
--tickers CRW.L`): trading-session/timestamp validation (CZR); don't map
calendar/legal dates directly to execution timestamps (CZR); low signal-to-noise
linear-EV fades are not durable edges and simulate-plans doesn't enforce
path-dependent stops (PLD); an entry fill outside the planned band is an early
falsification signal (PLD); and — most directly relevant — test-query the real
price provider before finalizing a plan, since an unpriceable instrument resolves
as an uninformative neutral (NYAX cyber-breach precedent).

Pre-debate check: `toa price CRW.L / CRW:LSE / CRW.LON / CRW --provider
twelvedata` all returned HTTP 404 — the ticker cannot currently be priced by the
real market-data provider. This constraint was given to every persona up front.

---

## Round 1 — Independent research

### Bull (sonnet)

File-names-only exfiltration is a mild disclosure category, not confirmed
PHI/content theft. Initial cyber-disclosure headlines are systematically
overpriced with fear; the pattern is a sharp initial drop followed by
partial-to-full recovery once no fine/no churn materializes. Craneware's sticky
hospital RCM customer base implies high switching costs and low churn risk even
post-breach. Proposed action: long CRW.L, buy the post-disclosure dip, exit
near/before the Aug 20 impact window, via direct equity (no meaningful AIM options
liquidity). Flagged the CRW.L pricing 404 directly and suggested either finding an
alternate data path or marking this opportunity observational-only rather than
silently proceeding.

### Bear (sonnet)

Skeptical of any confident directional call in either direction. "File names
only" could still be PHI-adjacent enough to trigger HIPAA/ICO notification
obligations (RCM systems commonly use patient-identifying file-naming
conventions); breach-scope estimates historically grow, not shrink, during
forensics. AIM-listed stocks gap violently with no real stop-loss enforcement in
`simulate-plans`. The Aug 20 impact_window is a soft, analyst-assigned date, not a
scheduled corporate/regulatory deadline — should not be mapped directly to an
execution timestamp. Sourcing is a single secondary tech-press article with no
primary RNS or ICO filing. Concurred that the CRW.L pricing 404 is disqualifying
per the NYAX lesson (unpriceable instrument resolves as an uninformative
neutral). Recommended no-trade, or at minimum explicit unverifiable-by-real-price
flagging if a plan is proposed anyway.

### Quant (opus)

Recommends 0% position size / stand aside. The pricing 404 is a hard EV cap:
unfillable data means simulated P/L is structurally 0 regardless of thesis
quality. Base rates for breach disclosures on small-cap software show average
abnormal returns of only -1% to -5%, typically recovering, and file-names-only
(no ransomware, no confirmed PHI) is one of the milder disclosure categories,
arguing against a large tail move. Explicit EV calc on a hypothetical short/fade:
probabilities 0.30 (further adverse finding, +6% to a short), 0.45 (drift, +1%),
0.25 (reassurance/recovery, -4%) → gross EV = +1.25%. AIM round-trip costs
(spread ~0.5-1.0%, commission/FX ~0.3-0.5%, slippage ~0.5-1.0%) ≈ 1.5-2.5% →
net EV ≈ -0.75%, negative. Signal-to-noise ≈ 0.12-0.15, at/below the ~0.15
durability floor from the PLD lesson. Notes `simulate-plans` won't enforce a
stated stop anyway. Bar to reconsider: a real priceable instrument/timestamp AND
an EV case beating the -1%/-5% base rate net of ~2% costs.

---

## Round 2 — Rebuttal

### Bull rebuttal

Conceded the 404 is dispositive — a "long position" here would have simulated P/L
of zero regardless of thesis; conceded Round 1 buried this blocker behind the
thesis and should have led with it. Pushed back that bear's "PHI-adjacent" read is
exactly as unconfirmed as bull's "contained" read absent a primary RNS/ICO
filing — bear is treating the worse-case interpretation as the base case.
Accepted quant's cost-structure math (a ~1.25% gross edge against 1.5-2.5% AIM
round-trip costs is a bad trade even before the pricing problem). Dropped the
"exit near/before Aug 20" framing as unsupported precision. Conceded to quant's 0%
position size. Final position: no real trade; at most a watchlist/observational
entry, explicitly flagged unverifiable-by-real-price and ineligible for simulated
execution.

### Bear rebuttal

Nothing raised by bull or quant changes the stand-aside conclusion; quant's EV
math independently corroborates bear's Round 1 instinct. Notes three-way
convergence on "no real tradeable edge." If the quant's "mild category" base-rate
assumption is wrong (scope grows rather than narrows, per typical forensic
patterns), the left tail gets fatter — reinforcing caution, not creating a bull
case. Unanswered across both rounds: no primary RNS/ICO filing cited by anyone; no
quantified PHI-adjacent exposure estimate; Aug 20 remains a soft, non-catalyst
date; AIM gap/no-stop-enforcement risk is independent of, and unaddressed
alongside, the pricing issue. Verdict: unanimous stand-aside/0% size, for three
distinct complementary reasons (bear = data-integrity/executability, quant =
EV-negative economics, bull = untestable directional thesis). Would only revisit
given (a) a working alternate price feed, (b) a primary RNS/ICO source on PHI
scope, (c) Aug 20 replaced by an actual scheduled event.

### Quant rebuttal

Neither opponent's argument moves the EV numbers — both are thesis-layer
(probability-weight) arguments that don't touch the two extra-thesis constraints:
(1) the unpriceable instrument, now unanimous across all three personas, is a hard
EV cap; (2) even granting the bull's most favorable distribution skew
(0.40×+6% + 0.40×+1% + 0.20×-4% = +2.0% gross), net EV after ~1.5-2.5% AIM costs
lands at roughly -0.5% to +0.5% — a coin-flip inside the noise band; signal-to-noise
stays ~0.12-0.15, at/below the durability floor. Full convergence on size (~0%),
but explicit residual dissent on hypothetical direction if the instrument were
suddenly priceable and properly sourced: bull would go long (fear overpricing +
sticky customers), quant leans weak-fade/short (base rate -1%/-5%) but flags the
edge isn't separable from noise, bear declines to take any directional side
(argues scope-growth risk is underweighted by both). This directional split is
moot this cycle since size = 0, but is logged as the dissent rather than papered
over.

---

## Round 3 — Synthesis (opus)

**Hypothesis:** Craneware's file-names-only exfiltration is one of the milder
cyber-disclosure categories (base-rate abnormal returns of -1% to -5% with typical
partial-to-full recovery), but the trade is not takeable on two extra-thesis
grounds all three personas converged on: (1) executability — CRW.L, CRW:LSE,
CRW.LON, and CRW all 404 on twelvedata, so the instrument is unpriceable via the
real provider and simulated P/L is structurally zero regardless of direction (the
NYAX unpriceable-resolves-neutral lesson); (2) economics — the quant's gross EV of
+1.25% is erased by AIM round-trip costs of 1.5-2.5% for a net EV near -0.75%, and
even the bull's most favorable skew nets only -0.5% to +0.5% — a coin-flip inside
the noise band at signal-to-noise 0.12-0.15, at/below the 0.15 durability floor.
Sourcing is single-source secondary press with no primary RNS/ICO filing, and the
Aug 20 impact window is a soft analyst date, not a scheduled catalyst.
Direction: none. Confidence: 18/100.

**Plan:** ticker CRW.L, action no-trade, entry/exit null (no valid execution
timestamp or fill price — the instrument cannot be priced), expected_profit_pct 0.

**Dissent (for the post-mortem):** the unresolved disagreement is hypothetical
direction if the instrument were suddenly priceable and properly sourced — moot
this cycle since size is 0, but logged rather than papered over. Bull would go
long (fear-overpricing + sticky customers + mild disclosure category). Quant
leans weak-fade/short on the -1%/-5% breach base rate but flags the edge isn't
separable from noise. Bear declines any directional side, arguing both bull and
quant underweight forensic-scope-growth risk. Testable trigger to revisit: (a) a
working alternate price feed for CRW.L, (b) a primary RNS/ICO source quantifying
PHI-adjacent exposure, and (c) the soft Aug 20 date replaced by an actual
scheduled event.

**Verdict: NO-TRADE** (not scheduled, not simulated).
