# Research debate transcript — 2026-07-23-iberdrola-caruna-acquisition

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. Researched in isolation from all other opportunities.

Event: Iberdrola agreed to acquire an 80% stake in Finnish grid operator Caruna for
EUR 2 billion (USD 2.3 billion); close expected Q1 2027 pending regulatory approval.
Ticker: IBDRY (Iberdrola's US OTC ADR). Source: Bloomberg, "Iberdrola Agrees to Buy 80%
Stake in Caruna Group for EUR 2 Billion", 2026-07-21,
https://www.bloomberg.com/news/articles/2026-07-21/iberdrola-agrees-to-buy-80-stake-in-caruna-group-for-2-billion

Pre-debate data check: `toa price IBDRY 2026-07-23T19:57:39Z --provider twelvedata`
and `toa price IBDRY 2026-07-24T15:30:00Z --provider twelvedata` both raised
`KeyError: no 1min bar for <minute>`. A direct fetch of the full 2026-07-24 twelvedata
1-minute series for IBDRY returned only 15 bars for the entire US session (~09:30-16:00
ET), with gaps of 30-60+ minutes between prints, trade sizes as low as 9-18 shares
(largest 633 shares), and price ranging ~96.24-96.83. This structural illiquidity
finding was handed to all three personas as shared context before Round 1.

## Round 1 — Independent research

### Bull (sonnet)

Grid M&A at scale is a clean positive re-rating catalyst for Iberdrola's regulated-
networks pillar; deal durability is high since the deal is agreed, not rumored
(Bloomberg, 2026-07-21). Proposed: long IBDRY via plain equity (no options market
exists on this name). Entry as a swing position over the next 1-2 sessions in the
$96.25-96.83 band observed on 2026-07-24, using the nearest available print at the
next liquid session open. Exit: hold toward a 4-6 week checkpoint to reassess, well
short of the full impact window to 2027-03-31. Acknowledged the illiquidity (15
prints/session, 30-60min gaps, sizes as low as 18 shares) requires tolerance-window
pricing (not exact-minute targets), modest position sizing, and treating any fill
outside the observed band as an early falsification signal.

### Bear (sonnet)

The deal was announced 2026-07-21, two days before this dossier — any re-rating from
the announcement is already in the tape; no discrete near-term catalyst remains. The
Q1 2027 close is undated within the dossier, 8+ months out, and is a legal/regulatory
milestone, not a scheduled price event. EUR 2B is ~2% of Iberdrola's ~EUR 90B market
cap — immaterial to consolidated valuation. Between now and close, EUR/USD moves (the
ADR converts a EUR-denominated equity to USD), earnings, rate decisions, and utility-
sector rotation will dominate IBDRY's price far more than this single deal. On
liquidity: ~15 one-minute prints/session, gaps of 30-60+ minutes, sizes as low as 18
shares mean no reliable price exists at any given moment; a planned entry/exit at a
specific timestamp is highly likely to fall in a gap. Recommendation: NO TRADE.

### Quant (opus)

Base rate for bolt-on utility M&A at ~2-2.5% of acquirer cap: announcement-day
cumulative abnormal return (CAR) is centered near zero, cross-sectional SD ~2%; no
visible re-rating in the 2026-07-24 tape (session opened 96.82, closed 96.25). The
Q1 2027 close is a legal milestone with a >90% clearance base rate for grid-stake
approvals, carrying near-zero price information. EV calculation: P(favorable near-term
move) = 0.52, magnitude ±1.5% → gross EV = +0.06%. Test-queried the real provider
(`toa price`) at 14:00Z, 15:30Z, and 19:55Z on 2026-07-24 — **all three raised
MarketDataUnavailable** (only 15 of ~390 session minutes have prints, 3.8% coverage).
Round-trip transaction costs on this illiquid name estimated at ~0.9% (spread ~0.55% +
impact/scarcity slippage ~0.35%). Net EV = 0.06% − 0.9% = **−0.84%**. Signal-to-noise
≈ 0.06/0.61 ≈ 0.10, below the 0.15 durability floor established in prior lessons. A
tolerance window doesn't rescue this — it launders the noise rather than removing it.
Recommendation: **REJECT, 0% of book** — not a call against the deal, against the
instrument/setup.

## Round 2 — Rebuttals

### Bull (rebuttal) — concedes

The quant's 3-for-3 MarketDataUnavailable finding is worse than "wide gaps" — it means
the instrument frequently cannot be priced at all during ordinary session hours, so
the Round 1 entry/exit discipline has nothing reliable to execute against. No minimal
viable version survives: smaller size doesn't fix a broken pricing mechanism, it just
makes the failure cheaper. Combined with the bear's stale-catalyst point, there is no
honest edge left to size into. Withdraws the long. New recommendation: **NO TRADE, 0%
of book** — concurs with quant and bear on execution grounds, not on the merits of the
deal itself.

### Bear (rebuttal) — firm pass

The quant's EV/S-N math and the 3-for-3 unpriceable finding corroborate and sharpen the
qualitative liquidity case via an independent method: two methods converged on the same
verdict via different paths. The 3-for-3 finding is decisive on its own — a position
that can't be reliably marked intraday isn't "thinly traded but tradeable," it's
functionally unpriced. On the bull's tolerance-window/falsification framing: it
"manages a risk (adverse price) while ignoring the prior risk (no price) — it's not a
safety net, it's a description of hoped-for market behavior," since the plan assumes
timely fills to compare against the band that the 3.8% coverage rate doesn't guarantee.
No version of the trade is acceptable — a dated catalyst doesn't fix the pricing
problem; sizing down doesn't fix negative EV on a broken instrument. Firmly **PASS
ENTIRELY**.

### Quant (rebuttal) — verdict unchanged

Reworked the bull's tolerance-window plan explicitly: a tolerance window doesn't reduce
cost, it widens the fill distribution (uniform-ish realized entry across the 0.60%
band), raising adverse selection rather than lowering it. Rebuilt net EV under the
bull's plan: −0.84% to −1.14%, with S/N falling to ~0.02 once the 4-6 week hold's
EUR/USD and sector-beta variance (~3-4% over 30 sessions) is included. Agrees with the
bear on the conclusion, provides the numbers behind it: the deal thesis is not zero
edge in principle (small positive drift, P=0.52 above coinflip) — it's a cost problem,
not a thesis problem; the edge is "15x too small to clear this instrument's frictions."
No parameter change rescues it — even switching to Madrid ordinaries (IBE.MC, ~0.10-
0.15% round-trip) only gets net EV to ~−0.05% at best, and that venue is outside the
tradeable universe anyway. Verdict unchanged: **REJECT, 0% of book**.

## Round 3 — Synthesis (opus)

**Hypothesis** (direction: no-trade, confidence: 88): The Iberdrola/Caruna deal is real
but immaterial and already absorbed, and IBDRY is not reliably priceable, so no
tradeable edge exists. Three independent lines converge: (1) materiality — EUR 2B is
~2% of Iberdrola's ~EUR 90B cap, a bolt-on with announcement-day CAR centered near
zero; (2) timing — announced 2026-07-21, two days stale by dossier date, no visible
re-rating in the 2026-07-24 tape, and the only forward milestone is an undated,
>90%-clearance-probability Q1 2027 legal formality 8+ months out; (3) executability —
3-for-3 MarketDataUnavailable on toa price test queries (3.8% minute coverage), giving
net EV of −0.84% (−1.14% under the bull's tolerance-window fill distribution) against
a 0.15 signal-to-noise durability floor (actual: ~0.10, falling to ~0.02 over a 4-6
week hold). The panel is unanimous. The deal thesis is not judged wrong — the drift is
mildly positive — this is a cost-and-executability problem, with the edge roughly 15x
too small to clear this instrument's frictions. Confidence of 88 reflects conviction in
the no-trade determination, not a directional view; the residual 12 reflects that
P=0.52 is genuinely above a coin flip, so the conclusion rests on execution economics
rather than the thesis being falsified.

**Plan**: explicit no-trade determination. ticker IBDRY, action no-trade, no entry/exit
scheduled, expected_profit_pct 0, allocation 0% of book. Reducing size does not repair
a pricing mechanism unavailable for ~96% of session minutes — it only makes the
failure cheaper. Even the liquid venue (Madrid ordinaries, IBE.MC) does not rescue the
trade: net EV only reaches ~−0.05% at best, and that venue is outside the tradeable
universe regardless.

**Dissent** (unanimous conclusion, non-identical reasoning):
1. Cause of rejection differs: bull withdrew on execution grounds only and explicitly
   preserved the merits of the deal thesis; bear rejects on both materiality and
   liquidity, treating the thesis as immaterial regardless of venue; quant sits
   between, agreeing to a small positive expected drift (P=0.52) and framing rejection
   purely as a cost problem. If IBDRY drifts up over the next 4-6 weeks, the bear was
   wrong on materiality while quant/bull were right on executability — naive outcome
   scoring would misread this as a missed opportunity.
2. Whether tolerance-window pricing is risk management or hope: the bull's Round 1
   falsification-signal framing was conceded on the grounds that it presupposes a
   pricing mechanism this instrument lacks — not generalized into a blanket rule
   against tolerance windows elsewhere.
3. What would need to change for this to become tradeable (all three conditions must
   hold together): (a) priceability — toa price must resolve a majority of sampled
   session minutes, not 0 of 3, the binding constraint to re-test first if revisited;
   (b) a dated, discrete regulatory-decision catalyst rather than an undated "Q1 2027
   close"; (c) magnitude — an event on the order of 10% of acquirer cap, not 2%, so
   expected move exceeds round-trip friction by a multiple. Admitting liquid primary
   listings (IBE.MC) to the tradeable universe is a separate, universe-design fix — the
   quant's own numbers show even that only reaches ~−0.05% net EV on this specific deal.

Post-mortem test if revisited: was the IBDRY move from 2026-07-24 to late August inside
the ±1.5% band assumed (validating immateriality), and did toa price coverage for
IBDRY remain under 10% of session minutes (validating the executability read)? If
low coverage is structural across thin OTC ADRs generally, that is a universe-filter
fix at scout time, not a per-opportunity research finding — thin US OTC ADRs should be
screened for priceability before a dossier reaches a three-round debate at all.
