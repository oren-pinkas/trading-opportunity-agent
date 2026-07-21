# Debate transcript: 2026-07-14-lufthansa-pilot-strike-threat (DLAKY)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. Run restricted to this opportunity alone, no cross-opportunity
comparison.

## Key facts

- Ticker: DLAKY, an OTC pink-sheet ADR of Deutsche Lufthansa AG, extremely thin
  (only 9-20 one-minute bars per session on twelvedata).
- Event: Vereinigung Cockpit (VC) pilots authorized a 96 percent strike mandate,
  valid through 2026-10-26, allowing a 48-hour strike notice at any time. No
  strike date has been set.
- Dossier impact_window: 2026-08-15 (vague; not a discrete dated event).
- Price action (twelvedata bars): roughly USD 11.30-11.50 pre-mandate high in
  early July, to about USD 10.35 on mandate day (2026-07-14), to USD 10.02-10.16
  by 2026-07-20 — one continuous drawdown of about 10-13 percent, not a panic
  spike.
- Prior context: two strike waves already in 2026 (April, May) cost roughly
  EUR 150 million against a multi-billion-euro EBIT base; the market has treated
  these as noise.
- The only near-term dated catalyst is Q2 earnings (before 2026-08-15), which is
  unrelated to the strike narrative.

## Round 1 — Independent research (parallel, no cross-visibility)

### Bull (opening) — confidence 28/100

Long DLAKY at about USD 10.00-10.15, target USD 10.80-11.00 (mean reversion to
the pre-mandate level), stop about USD 9.50. Cited twelvedata bars: USD 10.81-10.85
(07-10) to USD 10.35-10.38 (07-14, mandate day) to USD 10.02-10.16 (07-20), about
an 8 percent decline over 10 days. Thesis: the market overreacted to strike-mandate
fear, no strike is actually dated, and the price will mean-revert.

### Bear (opening) — confidence 15/100, no-trade

Could not retrieve twelvedata quotes at all (400/404 across DLAKY/LHA/DLAKF).
Argued from secondary sources that DLAKY hit 52-week highs around USD 11.29-11.46
in early July, suggesting the strike is priced-in noise. Flagged Q2 earnings
(before 2026-08-15) as the real, unrelated catalyst. Noted that the Q1/Q2 2026
strikes cost roughly EUR 150 million against multi-billion EBIT — treated as noise.

### Quant (opening) — confidence 12/100, no-trade, negative EV

Independently retrieved twelvedata bars confirming the decline. Found DLAKY
illiquidity disqualifying: only 9-20 one-minute bars per session, implying a
1.5-3 percent round-trip friction. Computed net EV on any directional trade as
-1.5 percent to -2.5 percent after costs. No discrete dated catalyst at the vague
2026-08-15 impact window.

## Round 2 — Rebuttal (parallel)

### Bull (revised to 10/100, WITHDRAWING)

Conceded the price move is a grind/decline, not a panic spike — which kills the
mean-reversion premise. Conceded that liquidity friction (1.5-3 percent) is fatal
given the target is only 7-9 percent away. Fully withdrew and converged to no-trade.

### Bear (revised to 8/100)

Retracted the "priced-in-at-highs" claim. Recognized that the twelvedata series
(from bull and quant) shows the highs were pre-mandate and that the decline
predates AND continues after the mandate news, meaning the high was a stale anchor,
not evidence of priced-in noise. Fully converged with quant on illiquidity as the
dominant, fatal factor. Confirmed no dated catalyst before 2026-08-15 tied to the
strike story (Q2 earnings is separate).

### Quant (revised to 10/100, most rigorous)

Reconciled the price series: the bear's high and the bull/quant declining bars
describe ONE continuous drawdown (about 11.30 peak pre-mandate to about 10.00 by
07-20), not a contradiction, and the EV conclusion is invariant to which anchor is
used. Quantified the bull's own trade geometry: entry USD 10.02, target +8.8 percent
midpoint, stop -5.2 percent, friction about 2.25 percent round-trip. Driftless
barrier-hit probability: 37.1 percent target-first versus 62.9 percent stop-first.
EV = -2.26 percent even under a charitable no-drift assumption; realistically
-3 percent to -4 percent once ADR stop-slippage (illiquid, gappy fills) is included.
The bull needed about 53 percent win probability to break even but only had 37 percent.

## Round 3 — Convergence (synthesizer)

All three personas converged to NO-TRADE by the end of Round 2 (confidence 8-10/100).
See the dossier frontmatter for the final hypothesis, plan, confidence, and dissent.
Verdict: NO-TRADE (not scheduled, not simulated). The trade fails on two independent
grounds, either sufficient on its own: (1) structural illiquidity — a 1.5-3 percent
round-trip friction on an OTC ADR trading 9-20 bars per session, and (2) negative
expected value — the quant's driftless barrier math gives a 37 percent win rate
against a 53 percent breakeven requirement, an EV of about -2.26 percent before
slippage. The original mean-reversion thesis was invalidated when the "overreaction
spike" turned out to be a continuous multi-day grind lower with no dated catalyst.
