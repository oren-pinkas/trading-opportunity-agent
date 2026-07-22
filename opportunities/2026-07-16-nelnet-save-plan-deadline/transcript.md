# Research Debate Transcript — 2026-07-16-nelnet-save-plan-deadline (NNI)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: `debate-three-round-panel`. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.
Debate run: 2026-07-22.

## Institutional memory injected

- Before finalizing any plan, validate that every entry and exit timestamp falls within an open trading session (not a weekend or exchange holiday) for the specific instrument, and roll non-trading exit dates forward to the next open session. (source: 2026-07-08-caesars-icahn-fertitta-bidding-war)
- Never map a corporate/legal calendar date (go-shop, earnings, deal deadlines) directly onto an execution timestamp — treat such dates as catalysts and derive the fill time from the nearest valid trading session. (source: 2026-07-08-caesars-icahn-fertitta-bidding-war)

## Round 1 — Independent research

### Bull (opening)

Read: weak/indirect catalyst but a real trade in volatility around Q3 earnings when SAVE-surge volume flows through LSS segment revenue. ED is 21% of total company revenue, 68% of Loan Servicing & Systems (LSS) segment revenue. Stock has proven big post-earnings moves (-15.6% in May 2026 on Q1 miss).

Evidence: CNBC, 2026-07-06, "Student loan servicers SAVE plan exit notices" (~7M borrowers, 90-day exit notices starting July 1); LSS revenue USD 120.7M Q1'25 → USD 127.8M Q1'26 (+5.9% YoY); USDS is a per-borrower blended-rate federal contract; total FY2025 revenue ~USD 1.67B; NNI trading ~USD 132-134, 52wk high USD 144.38, YTD +4.9% (Simply Wall St).

Proposed action: Long NNI common, enter now (week of 2026-07-22), hold through Q3 2026 earnings (~early-mid Nov 2026), exit 1-2 sessions after print. Small-moderate size.

Confidence: 35-40%, framed as an earnings-volatility trade, not a clean deadline-catalyst trade.

### Bear (opening)

Thesis structurally weak: LSS segment net income only USD 15.0M of USD 71.1M total Q1 2026 net income (~21%); LSS revenue DOWN 16% YoY in Q4 2025 (USD 138.0M → USD 116.6M). Nelnet announced staff reductions due to contract changes — servicing book contracting, not surging.

Mechanism: federal student loan servicers are paid a **flat monthly fee per borrower account**, not per-transaction/per-call (The College Investor, Pew) — so processing 7M exit notices is a cost increase (labor, call centers), not incremental revenue. Sign of bull's thesis may be backwards (margin headwind, not tailwind).

Staleness: CNBC article dated 2026-07-06, notices began July 1; by 2026-07-22 the market has had 3+ weeks to digest it. Nelnet's own Q1 2026 earnings (2026-05-07) already discussed SAVE/forbearance wind-down. Q1 2026 miss (revenue USD 419.1M vs USD 448.3M consensus, stock -3.9%) was driven by loan loss provisions, unrelated to SAVE volume. Window is diffuse (90 days, no single resolution date).

Confidence: 75-80% this is NOT a tradeable edge.

### Quant (opening)

Base rate for "regulatory/administrative workload increase" stories translating into a statistically meaningful directional move: ~10-15%, catalyst alpha ≈ 0.

Price check (twelvedata, NYSE hours): NNI ≈ USD 133 (2026-07-17 / 2026-07-21 intraday bars), realized vol ~20% annualized, 2-month sigma ≈ 8%.

EV calc: symmetric distribution (30% up 6%, 40% flat, 30% down 6%) → EV_gross = 0%, minus ~28bps round-trip costs → EV_net ≈ -0.28%. Options strictly worse: thin chains (5-15% of premium spread), no single-day catalyst in a diffuse 90-day window (theta bleed).

Recommendation: NO POSITION, size 0. Confidence in a real tradeable edge: 8/100.

## Round 2 — Rebuttal

### Bull (rebuttal)

Concedes: the flat-fee-per-account structure directly undercuts the "volume = revenue" mechanism (did not verify the actual contract fee structure in Round 1); concedes LSS is only 21% of net income; concedes the Q4 2025 LSS revenue decline (-16% YoY) cuts against the thesis; concedes the staleness point.

Notes bear's own mechanism (cost inflation, no offsetting revenue) is itself a directional — bearish — thesis that bear underweights as actionable, rather than treating it as "no edge." Notes NNI's proven -15.6% earnings-day move means a vol-purchase EV is a distinct question from directional EV, contingent on implied vol underpricing realized-move history (unverified — flagged for quant to check with real options-chain data).

**Fully withdraws the long thesis.** Revised confidence in a bullish directional trade: 10-15% (down from 35-40%). Revised action: NO LONG POSITION.

### Bear (rebuttal)

Concedes quant's EV framing is more robust than bear's own qualitative cost narrative. Concedes bull's Q3-earnings reframe is a more coherent trade construction than the original diffuse-deadline framing.

Reconciles the LSS revenue discrepancy (Q4'25 -16% YoY vs Q1'26 +5.9% YoY): concedes the segment trend is noisier/lumpier than bear's Round 1 "contracting book" claim implied, and revises that specific claim down — but maintains this doesn't rescue the bull thesis, since neither figure isolates SAVE-specific volume, and the flat-fee mechanism concern stands regardless of segment revenue direction. Flags that nobody (bull, bear, or quant) obtained the actual USDS contract fee schedule — a genuine unresolved evidence gap.

Distinguishes quant's direction-agnostic "no edge" from bear's own bearish-if-anything lean; declines to upgrade to an actionable short given the contract-terms gap.

Final confidence: 80% not tradeable as a deadline/catalyst play; 65% no clean directional edge exists (down from near-certainty). Recommends NO POSITION on both the original catalyst and bull's earnings-vol reframe, but flags the reframe as worth a fresh dedicated look near the Q3 print IF the USDS fee schedule question is resolved.

### Quant (rebuttal)

Models bull's earnings-vol reframe explicitly:
- Long common through the Q3 print: EV_net ≈ -0.28% (same as Round 1) but at 2-3x variance — worse risk-adjusted than the original framing.
- Buying a straddle into the print: EV ≈ -3% to -8% of premium (post-earnings IV crush + 5-15% chain spread); the market already prices the expected jump into IV, and bull showed a large move happened once (May) but not that current IV underprices realized-move history.

Sizes bear's short thesis explicitly: needs P_down ≳ 54% to clear ~45bps friction (round-trip + borrow); estimates P_down ≈ 50-52% given contradictory LSS revenue signals and Nelnet's own staff-reduction offset to the cost thesis; EV_net ≈ -0.21% — still fails.

Synthesis across structures: long common, short common, and long-vol all fail the EV bar; flat is the only structure with EV=0 and no downside.

Final confidence in a tradeable edge in ANY direction: 9/100 (up 1pt from Round 1 — the Q3 print is a more legitimate object to trade than the original diffuse deadline, but once modeled it's priced). Recommendation unchanged: NO POSITION, size 0.

## Round 3 — Convergence (synthesizer)

**Hypothesis:** Nelnet (NNI) SAVE-plan deadline story does not translate into a tradeable edge. The purported catalyst — 90-day borrower exit notices affecting ~7M ED borrowers, flowing through Nelnet's LSS segment — fails on mechanism and materiality: federal servicers are paid a flat monthly fee per borrower account (not per transaction), so elevated SAVE workload is a cost input, not a revenue driver; LSS is only ~21% of both total net income and revenue; the segment's revenue trend is lumpy/contradictory (Q4'25 -16% YoY vs Q1'26 +5.9% YoY) and doesn't isolate SAVE volume; the news is 3+ weeks stale with a diffuse 90-day window and no single resolution date. No long, short, or volatility structure clears round-trip friction on the expected-value math.

- Direction: none
- Confidence (that no tradeable edge exists / no position is correct): 88

**Plan:** NO TRADE. No entry, no exit, size 0 — no long, short, or options structure. Every modeled structure fails the EV bar (long common EV_net ≈ -0.28%, worse risk-adjusted under the earnings-vol reframe; short needs P_down ≳ 54% but estimated only ~50-52%, EV_net ≈ -0.21%; straddle into the print EV ≈ -3% to -8% of premium).

NOT-NOW watch item (not a live plan): bull's earnings-volatility reframe into the Q3 2026 print (~early-to-mid Nov 2026) is the only residual structure with a coherent rationale, resting on NNI's demonstrated capacity for large earnings-day moves (-15.6% May 2026). Revisit only if BOTH: (1) the actual USDS/ED contract fee schedule is obtained and confirms a materially non-flat structure, AND (2) implied vol into the print is shown to underprice NNI's realized-move history. Absent (1), the mechanism is dead.

**Dissent (preserved for post-mortem):**
1. Primary — sign-vs-magnitude split (bear vs quant): quant's direction-agnostic "no edge" conclusion masks a real question bear surfaced — the flat-fee mechanism plus Nelnet's own staff reductions constitute a genuinely bearish-if-anything lean, which quant priced at P_down ≈ 50-52% (fails the 54% friction bar by a hair). Unresolved: is the down-tilt real but sub-threshold, or under-weighted because friction estimates are conservative? If NNI drifts/gaps down around the Q3 print, the post-mortem should ask whether a genuine-but-sub-threshold signal was wrongly rounded to zero.
2. Secondary / evidence gap: nobody obtained the actual USDS/ED contract fee schedule. The entire mechanism debate (volume→revenue vs flat-fee→cost) rests on an assumption none of the three personas verified.

**Rationale:** All three personas converged on NO POSITION via independent paths. Bull fully withdrew the long thesis after conceding the flat-fee structure kills the core mechanism. Bear held ~80% not-tradeable while honestly revising its "contracting book" overstatement down to "lumpy/noisy segment." Quant independently sized every structure (long, short, vol-long) and found each fails the EV bar, with only 9/100 confidence any tradeable edge exists in any direction. The convergence is robust because it survived each persona attacking the others' framing. Decision: NO TRADE, size 0.
