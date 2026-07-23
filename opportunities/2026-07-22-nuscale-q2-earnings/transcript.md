# Research debate transcript: 2026-07-22-nuscale-q2-earnings

Strategy: debate-three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.
PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Relevant lessons injected (generic earnings lessons; no SMR-specific post-mortem history exists yet):
- (NKE) Confidence <=~45 with an un-hedgeable positive tail and net EV <~2% against a ~7-8x adverse-tail-to-edge ratio is a no-trade filter, not a size-down; express such earnings gap-shorts via defined-risk options, never a naked short.
- (NKE) Discount post-earnings negative base rates when the name is already at/near its 52-week low.
- (TSLA) Set intraday exits at least one minute inside the session boundary (19:59:00Z, not 20:00:00Z).
- (TSLA) Add a pre-simulation timestamp guard validating both legs map to available US-equity bars.
- (DAL) A catalyst that already drove a large multi-week run to a 52-week high is priced in.
- (DAL) When strongest unrebutted dissent aligns with quant's own EV math, synthesize to NO-TRADE rather than a quarter-size position.
- (LEVI) When quant's directional EV is ~0, log NO TRADE — don't manufacture a minimal directional position "for the learning loop."
- (LEVI) Anchor entry prices to a live quote at the actual entry timestamp; re-price or abort if the stock has run away from the modeled entry.

## Round 1 — Independent research

### Bull
Price check: `toa price SMR 2026-07-22T19:59:00Z --provider twelvedata` → USD 8.67.

Sees SMR as range-bound pre-catalyst, not at a 52-week high or low. SMR's 2026 price action has been almost entirely binary-news-flow driven (utility agreements, DOE funding, state policy) with historically outsized realized moves on earnings. Three levers for the Aug 5 print: contracted MW backlog additions, cash runway/dilution risk, DOE/utility MOU converting to binding contract.

Proposed action: defined-risk call debit spread (buy ATM call, sell ~15% OTM call) expiring Aug 7 2026, entered Aug 3-4 (pre-earnings IV expansion), exit within first 30-60min of the Aug 6 session, ~50% premium stop-loss, re-anchor entry to a live quote before sizing.

### Bear
Price check: `toa price SMR 2026-07-22T15:30:00Z --provider twelvedata` → USD 8.84.

NuScale has essentially no revenue; valuation is 100% narrative. Core risks: dilution via ATM raises, timeline slippage (RoPower/ENTRA1 permitting/NRC delays), guidance walk-back or no guidance at all, no confirmed sell-side consensus figures anywhere. Stock is mid-range, not at a 52-week low, so there is no "priced-in disaster" floor to lean on.

Recommendation: NO TRADE outright, or if a directional view must be expressed, only a small long-dated put, never a naked short. Demands the bull identify at least one binding, capital-backed commercial commitment before conceding any long edge.

### Quant
Price check: `toa price SMR 2026-07-21T19:59:00Z --provider twelvedata` → USD 8.72.

Base rate: 12-20% one-day move for a speculative pre-revenue small-cap earnings print; uses 15%. P(up)=0.47, P(down)=0.48, P(muted)=0.05. Gross EV ≈ -0.15%; net EV after IV crush/slippage ≈ -0.4% to -0.6%. Symmetric fat tail, no informational edge.

Recommendation: NO TRADE, sizing 0. If forced, only a defined-risk straddle <=0.5R and only if breakevens sit inside the historical move (does not currently see that edge).

## Round 2 — Rebuttal

### Bull rebuttal
Concedes dilution is the single biggest tail risk, but argues the debit spread already accounts for it (defined risk, not naked). Argues the bear can't have it both ways (no floor for a contrarian long, yet no ceiling either / no edge per the quant). Argues thin SMR options coverage means IV crush may be less efficiently priced than the quant assumes, so a capped-risk spread can carry asymmetric payoff even near coin-flip odds. Concedes "no edge on direction" but argues the payoff asymmetry of a capped-risk structure survives a negative/flat EV assumption in ways a straddle or naked short do not. Lists falsifiable kill conditions: a pre-earnings dilutive 8-K, confirmed negative permitting news, options bid-ask too wide to clear breakevens, or SMR running >8-10% pre-entry on no news. Asks bear/quant what implied-move threshold would flip them off NO TRADE.

### Bear rebuttal
Grants the debit spread caps loss magnitude, but argues defined-risk ≠ positive-expectancy — the catalyst mix still skews toward disappointment. Flags unverified options liquidity/bid-ask risk on the proposed exit mechanics. Reiterates that "MOU converting to binding" is exactly the unresolved hope being repackaged as a reason to buy calls, not new evidence. Pushes back on the quant's symmetric-tail assumption, arguing downside is fatter (dilution/ATM raises at depressed prices compound down-moves) while upside is more often an underwhelming "in-line MOU." Would only accept the bull's trade if strikes/premium/bid-ask are verified and breakeven sits inside a realistic upside scenario — otherwise NO TRADE holds.

### Quant rebuttal
Notes a debit spread is still net long vega (buys ATM vega, sells smaller OTM vega), so it still bleeds in a 30-50% earnings IV crush; capping max loss doesn't fix the EV sign — net EV drifts to roughly -0.5% to -0.8% after four-leg round-trip slippage and theta/vega drag. On the bear's "binding commitment" demand: reframes the real tell as the total absence of ANY published sell-side consensus (revenue, EPS, backlog MW) from either side — no consensus means no defined "surprise" axis, so the reaction function is genuinely undefined, which is neutral evidence, not directional evidence for either side. Holds probabilities unchanged (P(up)~0.47/P(down)~0.48/P(muted)~0.05). Verdict: NO TRADE holds, sizing 0.

## Round 3 — Convergence (synthesizer, opus)

**Hypothesis:** NuScale's Q2 print is a binary, narrative-driven event with no published sell-side consensus (revenue, EPS, or backlog MW) on either side, so there is no defined "surprise axis" and no informational edge. Realized moves are historically large (~15%) but directionally symmetric-to-negatively-skewed, and an earnings IV crush (30-50%) bleeds any net-long-vega structure — including the bull's debit spread. No participant supplied a quantitative directional edge.
Direction: neutral. Confidence: 40/100.

**Plan:** SMR, no_trade. No entry/exit/target. Expected profit ≈ 0%.

Rationale: two of three personas (bear, quant) land on NO TRADE outright; the quant's net EV is negative across every structure considered (-0.4% to -0.8% after IV crush and round-trip slippage). The bull explicitly conceded "no edge on direction" and rested the case on the payoff *asymmetry* of a capped-risk spread — but the quant showed that spread is still net long vega and still negative-EV, and the bear showed the catalyst mix and fatter downside tail undercut the "breakeven inside a realistic upside scenario" requirement. Per the panel's own institutional filter — confidence <=~45 with EV <2% against an adverse-tail-to-edge ratio is a no-trade filter, not a size-down — this converges to a flat no-trade. No minimal "learning-loop" position is manufactured.

**Dissent (strongest unresolved disagreement):** Whether a capped-risk debit spread's payoff asymmetry can survive negative/flat EV. The bull argues thin/inefficiently-priced options coverage may leave IV crush mispriced, giving the spread asymmetric upside even at coin-flip odds. The quant counters that the spread is still net long vega and negative-EV after four-leg slippage, so capping loss magnitude never fixes the EV sign. Never resolved empirically — no one verified actual strikes, premium, or bid-ask. Adjacent unresolved thread: the bear's fatter-downside-tail claim (dilution compounds down-moves) vs. the quant's symmetric-tail model — a skew that, if the bear is right, would only strengthen the no-trade verdict but was held at neutral for lack of quantitative support.

Post-mortem watch-flags: (a) a pre-earnings dilutive 8-K or ATM raise; (b) confirmed RoPower/ENTRA1 permitting/NRC news; (c) any published sell-side consensus emerging (would restore a surprise axis); (d) SMR running >8-10% pre-print on no news.
