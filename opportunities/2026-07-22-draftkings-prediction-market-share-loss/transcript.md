# Debate Transcript — 2026-07-22-draftkings-prediction-market-share-loss

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.
Paper-trading simulation only. Not financial advice.

## Institutional lessons applied (from `toa lessons-relevant --type earnings --tickers DKNG`)

1. (NKE) Confidence <=~45 with an un-hedgeable positive tail and net EV <~2% against a ~7-8x adverse-tail-to-edge ratio is a no-trade filter, not a size-down; express such earnings gap-shorts via defined-risk options, never a naked short.
2. (NKE) Discount post-earnings negative base rates when the name is already at/near its 52-week low: most of the drawdown is priced in and a benign or one-time-beat print flips the reaction positive.
3. (DAL) A catalyst that already drove a large multi-week run to a 52-week high above the Street mean target is priced in — do not re-bet the same fundamental as a fresh gap trigger for the print.
4. (DAL) When the strongest unrebutted dissent aligns with the quant's own EV math, synthesize to NO-TRADE rather than a quarter-size directional position.
5. (LEVI) When the highest-confidence panelist (the quant) says directional EV is ~0 and the only positive-EV structure is out of mandate, log NO TRADE — do not manufacture a minimal directional position "for the learning loop."
6. (LEVI) Anchor entry prices to a live quote fetched at the actual entry timestamp, not a stale pre-move reference — validate the planned entry is still within a small tolerance of the current price before filling.

## Source

"Prediction markets swell to 27% of sports bets during World Cup" — Fortune, 2026-07-19.
https://fortune.com/2026/07/19/prediction-markets-sports-betting-world-cup-kalshi-polymarket-fan-duel-draftkings/

## Round 1 — Independent opening positions

### Bull

Thesis: negative sentiment (DAU -36% from June 15 peak, DKeX at ~0.01% notional share vs. Kalshi 38%/Polymarket 13% audience share during the World Cup) is overdone ahead of the Aug 6 print. Frames the DAU dip as World Cup-driven event rotation, not durable loss in DraftKings' core parlay/combo business. Proposed: long via defined-risk call debit spread into Aug 6, entering when put skew shows max pessimism priced in, exiting 1-2 sessions post-print. Flagged the `toa price` quote ($225.84) as unverified stub data, not a real market price.

### Bear

The DAU decline coinciding with prediction markets hitting 27% of sports bets share, plus DKeX's negligible 0.01% share, reads as structural share-shift (cheaper, CFTC-regulated national prediction markets undermining DKNG's state-licensing moat), not seasonal noise. But the narrative has been public since July 19 (3 sessions prior — partially priced in), and a naked short into Aug 6 carries fat right-tail risk if management reframes the dip as immaterial or offsets with iGaming/hold-rate strength. Proposed: NO TRADE, or at most a defined-risk put spread only if EV clears the adverse-tail hurdle.

### Quant

Narrative-rich, evidence-thin. DAU drop is peak-to-trough off a World Cup peak, not YoY/sequential — likely partly seasonal mean reversion. DKeX's 0.01% share is immaterial to Q2 revenue. One Fortune trend piece is one data point; real impact only visible at the print. Priors: P(down)≈42%, P(up/flat)≈58%. EV for a defined-risk short (put spread, 1.0 risk / 1.4 reward) = 0.42×1.4 − 0.58×1.0 = **+0.8%**, below the ~2% no-trade threshold (lesson 1). Proposed: NO TRADE, confidence low. Refused to anchor to the stub price (lesson 6).

## Round 2 — Rebuttals

### Bull

Conceded bear/quant's "stale narrative" point erodes the surprise premium — reframed the edge as mean-reversion off oversold sentiment rather than a fresh catalyst, sizing down accordingly. Argued quant's own bullish inputs (DAU peak-to-trough not YoY, DKeX immaterial) support a long, not just a "no short." Narrowed conviction: entry now conditional on verifying real (non-stub) IV skew genuinely stretched to the put side before acting.

### Bear

Pointed out the bull is borrowing the NKE lesson's conclusion (overshoot → relief rally) without its precondition (stock actually near a 52-week low / de-risked positioning) — the dossier establishes no such fact (lesson 2 misapplied). Also flagged DKeX's low share as a non-sequitur defense: the real risk is users leaving DraftKings' core book for Kalshi/Polymarket, not DraftKings' own exchange underperforming. Maintained NO TRADE; noted both bull and bear structures suffer from a lack of real options/positioning data.

### Quant

Conceded the trade is about vol, not direction. Revised priors marginally: P(down) 41%, P(up/flat) 59%. Recomputed EV for the defined-risk short = 0.41×1.4 − 0.59×1.0 = **−0.16%**, now net negative. Identified the structurally cleaner unexploited idea — short-vol / iron condor to harvest post-print IV crush — but noted it requires an options chain and IV-rank the panel does not have and cannot size. Recommendation unchanged: NO TRADE, confidence low.

## Round 3 — Synthesis (convergence)

**Hypothesis:** The DKNG "prediction-market share-loss" story is genuine but already-public since July 19, resting on a peak-to-trough DAU figure that is at least partly World Cup seasonality, plus a DKeX 0.01%-share data point that is immaterial to Q2 revenue and — per the bear's uncontested rebuttal — the wrong metric for the actual risk. Both a directional long and short are unsupported: quant's defined-risk short EV turned net-negative (−0.16%) by Round 2, the bull's "oversold → relief rally" pattern is missing its required precondition (no dossier fact placing DKNG near a 52-week low), and the one structurally clean idea (short-vol / IV-crush harvest) cannot be priced or sized absent verified options data.

- **Direction:** no-trade
- **Confidence:** 78/100 (high confidence in the no-trade decision itself, driven by data absence rather than disproof of the thesis)

**Plan:** No position taken. No ticker, entry, or exit specified — this is a deliberate, logged NO TRADE, not a placeholder (lesson 5). Applied lessons: quant's EV fell below the no-trade threshold and then went negative; both bull and bear agreed no verified options/positioning data exists to time entry; the `toa price` $225.84 quote was never anchored to (lesson 6).

**Dissent (strongest unresolved disagreement):** Bull vs. bear/quant on whether the share-shift is structural or seasonal, and conditionally, whether a verified stretched put skew would justify a long. The bull's Round 2 fallback — a vol/oversold mean-reversion play, live *if* real IV skew were confirmed stretched to the put side — was never resolved because the panel had no options data to confirm or refute it. The bear counters the core risk (users defecting to cheaper, CFTC-regulated Kalshi/Polymarket) is structural and the DAU dip may be an early signal, not noise. Gold for post-mortem: the abstention was forced by a missing IV/positioning data gap, not by settling the seasonal-vs-structural question. If the Aug 6 print produces a large move on a vol crush, revisit whether a verified options chain would have converted this into a tradeable short-vol setup.
