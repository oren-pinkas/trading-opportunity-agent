# Research Debate Transcript — LVMH Q2 2026 Earnings (LVMUY)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. Processed as a single, isolated opportunity — no comparison to
any other dossier in this repo.

## Round 1 — Independent Research

### Bull (confidence 40/100)

"Less bad than feared" sentiment-reset bellwether thesis: LVMH's July 28 print
resolves two overhangs at once — durability of the Europe/Asia luxury demand
recovery and how much US tariff exposure is biting margins. As the sector
bellwether, its print has read-through to Kering/Richemont/Burberry/Hermès,
which historically amplifies the move. Luxury names have traded on sentiment
and multiple compression for two years; any "less bad" signal could trigger a
sharp re-rating off a low reset base.

Evidence: LVMUY = USD 111.82 at 2026-07-13T15:30Z (toa price, twelvedata).
Event date and framing confirmed via MarketScreener LVMH calendar (accessed
2026-07-14). Follow-up price pulls were rate-limited (HTTP 429).

Proposed action: long LVMUY equity or, if liquid, a defined-risk call spread
into 2026-07-28; entry 1-2 sessions before the print anchored to a live quote;
exit into the post-earnings reaction on 7/28-7/29, hard exit by 7/29 close if
thesis unconfirmed; intraday exit orders set at 19:59:00Z per institutional
lesson on session-boundary fills.

Flagged gaps: no current Street consensus estimates, no confirmed live
pre-print price, tariff margin impact unsized.

### Bear (confidence 35/100, leaning NO TRADE)

The "recovery" narrative has run and failed repeatedly for multiple quarters —
a long bet here re-bets an already-failed trade rather than a fresh catalyst.
Proximity to the 52-week low cuts both ways: it caps clean downside conviction
but also caps clean upside conviction, producing a muddled two-sided setup
rather than a clean directional trade. Tariff commentary on Cognac and
Fashion & Leather Goods margins could break the 103.00 floor and accelerate
momentum selling through a multi-year level.

Evidence (toa price, twelvedata, queried 2026-07-21): LVMUY close 114.66 on
2026-07-16 vs. 110.47 on 2026-07-20 (-3.7% over four sessions, negative drift
into the print). 52-week range: high 152.95 / low 103.00 (260-day daily bars).
Current price ~110.5 is -27.7% off the high and only +7.3% above the low.

Flagged gap: no working web-search tool this round, so no verified sell-side
consensus EPS/organic-growth numbers or confirmed current tariff-policy status
— explicitly not fabricated.

### Quant (confidence 22/100, NO TRADE)

LVMUY is a thinly-traded OTC ADR: the twelvedata provider returned no 1-minute
bar for most queried timestamps (only top-of-hour prints filled), implying
wide bid/ask and real fill uncertainty — a cost, not a story.

Evidence: LVMUY = USD 110.17 at 2026-07-14T17:00Z, USD 114.63 at
2026-07-16T17:00Z (+4% over two sessions — some recovery optimism already
being paid for).

Assumed earnings-day move distribution (explicitly flagged as an assumption,
no web-search available): 20% chance of a >+6% move (avg +8%), 30% chance of a
0/+6% move (avg +3%), 30% chance of a 0/-6% move (avg -3%), 20% chance of a
>-6% move (avg -8%) — roughly symmetric because the two named swing factors
(demand recovery vs. tariff drag) push in opposite directions with no clear
edge to either. Expected directional move ≈ 0%; expected absolute move ≈ 5%.

EV: gross directional EV ≈ 0%, less ~1.2% round-trip costs/slippage (wide
OTC-ADR spread) ≈ **-1.2% net**. Negative — no directional trade clears. The
only structure that could monetize the ~5% expected absolute move is long
volatility (straddle), but LVMUY ADR options are effectively illiquid or
non-existent — an out-of-mandate positive-EV structure is NO TRADE, not a
manufactured minimal position, per institutional lesson. Needs net EV
materially above +2% to justify a trade; nothing in the current data clears
that bar.

## Round 2 — Rebuttal

### Bull (revised confidence 40 → 22/100)

Concedes substantially to bear's drift data and "failed narrative" point — no
new evidence exists that this cycle is different from prior failed recovery
calls. Concedes quant's illiquidity finding kills the call-spread fallback
entirely; won't assert options liquidity that hasn't been confirmed. Concedes
the near-52-week-low argument is a magnitude point (smaller realized downside
room), not a directional edge, and that this was conflated in Round 1.
Floats MC.PA (Paris-listed ordinary shares) options as a *possible* unverified
avenue for a defined-risk structure, explicitly flagged as unconfirmed, not a
rebuttal. Still argues a small, stop-defined long-equity position (hard stop
below 103.00) remains mechanically available even without options, but
acknowledges this is a weaker, higher-friction version of the original thesis.

### Bear (revised confidence 35 → 22/100)

Quant's illiquidity finding hardens the NO TRADE lean: it closes the one path
(vol-arb) that could have turned bear's own "muddled two-sided setup"
observation into a positive-EV trade. Rejects bull's sentiment-reset thesis
directly as a plausible mechanism without supporting data — no consensus
revision data, no implied-vol/skew data, no positioning data produced by
anyone across two rounds. Reconciles the full price path (quant's +4% then
bear's own -3.7%, netting to roughly flat over two weeks) as noisy chop, not a
coiled-spring signal. Declines to assert the 103.00 floor break is "cleaner"
than a bounce without fresh evidence — flags it as a risk to monitor, not a
trade to size.

### Quant (revised confidence 22 → 15/100)

Runs a significance test on bear's four-session -3.7% drift: at ~1.8% daily
vol, four-session one-sigma ≈ 3.6%; observed -3.7% ≈ -1.03σ — statistically
indistinguishable from noise, and does not overturn the symmetric prior.
Reconciles the full two-week path (+4% then -3.7%) as a round trip to flat,
confirming no directional conviction exists in the tape.

Computes the probability bar required to trade: clearing +2% net EV against a
~1.2% cost drag requires gross directional EV > +3.2%, which at an assumed 5%
expected absolute move requires **p_up = 0.82** — unsupported by anything
produced at the table (bull self-rates 40/100 with no Street estimates; an
unattributed drift is not evidence of a lowered bar).

Shows the 103.00 floor offers no asymmetric protection: an -8% tail move from
110.47 lands near 101.6, breaching the floor — the exact scenario bear fears
is not stopped by the "support level," and if anything implies a fatter left
tail. Recomputed EV unchanged: -1.2% net. The round-trip path does confirm
realized vol (~5% expected absolute move) is real, meaning the theoretically
correct expression is long volatility — but that instrument doesn't exist in
liquid form for this name, so per institutional lesson, no substitute
directional position is manufactured. Final lean: NO TRADE.

## Round 3 — Synthesis (opus)

All three personas converged to NO TRADE by end of Round 2 (confidences
22/22/15).

**Hypothesis:** LVMH's Q2 2026 print offers no tradable edge. All three
personas independently converged on a symmetric, roughly zero-drift
distribution around 110-111 into the 2026-07-28 report. The -3.7% four-session
drift tests as ~-1.03σ noise on ~1.8% daily vol, and the full two-week path is
a round trip to flat (+4% then -3.7%), so no directional conviction exists.
The only positive-EV structure (long volatility) is unreachable because the
sole in-mandate instrument, the LVMUY OTC ADR, is thinly traded with wide
spreads and no liquid options. Direction: none. Confidence: 18/100.

**Plan:** Ticker LVMUY. Action: no-trade. No entry/exit taken. Modeled net EV
of a forced directional trade after ~1.2% round-trip costs: -1.2%.

**Dissent (for post-mortem):** Residual uncertainty is entirely about missing
inputs, not flawed reasoning — all three personas were internally consistent.
No one produced Street consensus estimates, revision breadth, implied
volatility, skew, or positioning data. The symmetric prior is an assumption of
ignorance, not a measured distribution. Bull's sentiment-reset thesis (less
bad than feared) remains plausible but unfalsifiable without consensus
revision data. The 103.00 52-week floor gives no protection against the feared
-8% tail (which breaches to ~101.6), so it neither creates asymmetry nor caps
downside. **Revisit only if** (1) real Street estimates plus implied vol/skew
become available and imply p_up materially above 0.82 or a mispriced vol
surface, or (2) a liquid, in-mandate instrument for the volatility view is
confirmed — e.g., verified MC.PA Paris-ordinary options with real depth.
Absent both, NO TRADE stands.

## Sources

- LVMH Company Events, Publications and Financial Calendar — MarketScreener,
  https://www.marketscreener.com/quote/stock/LVMH-4669/calendar/ (accessed
  2026-07-14)
- LVMUY price series — twelvedata via `toa price LVMUY <ts> --provider
  twelvedata`: 111.82 @ 2026-07-13T15:30Z; 110.17 @ 2026-07-14T17:00Z; 114.63 @
  2026-07-16T17:00Z; 114.66 close 2026-07-16; 110.47 close 2026-07-20; 260-day
  range high 152.95 / low 103.00 (queried 2026-07-21)
