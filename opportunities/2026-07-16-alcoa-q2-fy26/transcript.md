# Research debate transcript — Alcoa (AA) Q2 FY26 earnings

Strategy: three-round-panel (bull/bear on sonnet, quant on opus, synthesizer on opus).
PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Event: Alcoa reported Q2 2026 results 2026-07-16 after the close. Research run date:
2026-07-22 — the catalyst has already fired and priced by the time this debate ran.

Relevant institutional lessons injected (via `toa lessons-relevant --type earnings --tickers AA`):
- NKE: confidence <=~45 with an un-hedgeable positive tail and net EV <~2% against a
  ~7-8x adverse-tail-to-edge ratio is a no-trade filter, not a size-down; express via
  defined-risk options, never a naked short.
- NKE: discount post-earnings negative base rates when the name is already near its
  52-week low — most of the drawdown may already be priced in.
- DAL: a catalyst that already drove a large run to a level above Street target is
  priced in; don't re-bet the same fundamental as a fresh gap trigger.
- DAL: when the strongest unrebutted dissent aligns with the quant's own EV math,
  synthesize to NO-TRADE rather than a quarter-size directional position.
- LEVI: when the quant says directional EV is ~0 and the only positive-EV structure
  is out of mandate, log NO TRADE — don't manufacture a position "for the learning loop."
- LEVI: anchor entry prices to a live quote at the actual entry timestamp.

---

## Round 1 — Independent research

### BULL

Earnings already fired July 16. EPS miss: USD 2.12 actual vs ~USD 2.24 consensus.
Alumina guidance cut (Pinjarra refinery). South32 acquisition overhang. Revenue
possibly a beat (~USD 3.97B, highest in Alcoa's independent-company history —
disputed across sources). Stock down ~9-10% peak-to-trough to USD 44.22 by 7/21.
RSI ~28 (oversold) on 7/17. All post-cut analyst targets remain above spot
(USD 51-80 vs ~USD 44.22 spot): Wells Fargo USD 72, B. Riley USD 80, Morgan Stanley
USD 53, BofA USD 51. Section 232 tariff cost guided to *decrease* ~USD 10M in Q3 — a
tailwind, not a drag. Aluminum market in structural deficit through 2026; Midwest
duty-paid premium elevated (~USD 2,500-3,000/mt).

Confidence: 42/100. Recommended: small long / call debit spread (USD 44 → USD 50-52
strikes), 2-4 week horizon, not a full-size naked long. Flagged that if the debate
synthesizes to "stale, already-priced catalyst," default to NO TRADE rather than
force a position.

Sources: Benzinga (Q2 miss detail, AH reaction), Investing.com transcript (revenue
beat framing), Alphastreet (EPS preview), Blockonomi / Barchart (alumina guidance
cut, Pinjarra), TipRanks / Barchart (South32 deal terms), Cryptonomist (RSI 28),
Benzinga (post-cut analyst targets), Seeking Alpha (Section 232 Q3 guidance).

### BEAR

Built deliberately pre-print, without post-print facts, to avoid look-ahead bias.
AA fell ~40% from its June 52-week high (USD 84.38) to ~USD 48.57 by 7/15, driven by
a company-initiated June 10 pre-announcement cutting Q2 EBITDA guidance: ~USD 60M
negative Alumina-segment hit, ~USD 35M incremental Section 232 tariff cost, and a
200-300kt cut to 2026 alumina production guidance (Pinjarra). LME 3-month aluminum
fell ~17% in the month into the print (USD 3,723/t on 6/3 to USD 3,087/t on 7/3).
Section 232 tariffs were restructured (effective April 6, modified June 8, 2026) to
apply to full customs value rather than just metal content — a structural, not
one-quarter, cost increase. Zacks consensus EPS cut ~5.5% into the print
(USD 2.37 → USD 2.24). Median analyst target ~USD 70 vs ~USD 48 pre-print spot — a
>40% gap that, per NKE/DAL lessons, could fuel a relief-rally squeeze against a
fresh short (AA beta 1.63).

Confidence: 42/100 for a fresh short. Recommended: if any position, a small
defined-risk put or put debit spread only, not a naked short — flagged as close to
NO-TRADE territory given squeeze/tail risk.

Sources: Gurufocus / Alcoa June 2026 investor presentation (pre-announcement
detail), Discovery Alert (LME aluminum move), White & Case / BDO (Section 232
restructuring), Tickeron / stockinvest.us (52-week range, 30-day decline),
Alphastreet / Yahoo-Zacks (EPS consensus cut), Marketbeat (analyst targets).

### QUANT

Pre-event reference price USD 48.62 (7/15 close). Day-of-print close USD 46.925.
Next-day reaction -6.55% to USD 43.85 — roughly in line with the ~4.9-5.5%
options-implied move and the ~5.2% 8-quarter average realized move, i.e. not a
blowout surprise; volatility was fairly priced. Estimate momentum negative (EPS
consensus cut ~5.5% into the print). Forward P/E ~10x vs ~11x metals/mining peer
average — not stretched. UBS bull price target of USD 80 vs ~USD 48 pre-print spot
indicates a depressed, not euphoric, setup (the DAL "priced-in run to highs" hazard
does not apply here).

EV math for a directional short at the pre-print reference: P(down)=0.52,
P(up)=0.48, ~5% symmetric magnitude → gross EV +0.20%; net EV ~0.0-0.1% after
slippage. Adverse-tail-to-edge ratio ≈ 50x — grossly fails the NKE 7-8x no-trade
filter. The only arguably positive-EV structure (long-vol straddle) is out of the
directional mandate.

Conclusion: NO TRADE. Directional-edge confidence ~38/100; confidence in the
NO-TRADE call itself ~70/100.

Sources: `toa price --provider twelvedata` (AA time series), Investing.com /
TipRanks (implied move), MarketChameleon (earnings IV history), Alphastreet (EPS
preview), Seeking Alpha (valuation, Section 232), StockTitan (Q2 2026 results).

---

## Round 2 — Rebuttal

### BULL rebuttal

Quant's ~50x adverse-tail-to-edge ratio was computed for a naked directional 1-day
bet, not the proposed call debit spread, whose max loss is the premium paid — the
NO-TRADE conclusion answers a different question than the one asked. Fwd P/E ~10x
vs ~11x peer average is read as a rerating floor forming, not fair value. Bear's
tariff-structure concern (full-customs-value restructuring) is contradicted by
Alcoa's own Q3 guidance for a ~USD 10M tariff cost decrease — new information Bear's
pre-print-only research couldn't have used. Bear's squeeze-risk point (beta 1.63)
is read as cutting in favor of the long thesis too (a squeeze up, not just down).

Confidence held at 42/100. Recommendation unchanged, but would narrow the spread's
near strike toward USD 46-48 to reduce cost basis given quant's point that the
initial move was in-line with implied vol, not a dislocation to chase.

### BEAR rebuttal

Disputes quant's "in-line-with-implied ⇒ no signal" framing: post-earnings-
announcement drift (PEAD) is a robust, well-documented anomaly where miss-plus-
guide-down stocks tend to keep drifting in the direction of the surprise, not
mean-revert — the quant's symmetric ~5% assumption forces EV toward zero without a
skew term for negative PEAD. Accepts the quant's ~50x tail-ratio math as an argument
against a *large* naked position, not against a small defined-risk short given the
trend is now confirmed. Pushes back on bull's tariff point: a ~USD 10M Q3 give-back
is small against the ~USD 35M Q2 hit and doesn't offset a permanent structural
cost-base step-up. Pushes back on RSI ~28 as stale/non-predictive since AA kept
falling after 7/17, and notes analyst targets remaining above spot both before and
after the print is evidence targets lag price discovery, not a buy signal. Concedes
the revenue-beat point weakens the "everything is broken" framing.

Confidence revised up slightly, 42 → 48/100, for directional correctness — but NOT
for risk-adjusted trade attractiveness. Recommendation unchanged: small defined-risk
put debit spread only, or NO TRADE, given beta-1.63 squeeze risk.

### QUANT rebuttal

Re-pulled the actual tape via `toa price --provider twelvedata`: 7/15 USD 48.57 →
7/16 (day-of) USD 46.87 → 7/17 USD 44.34 → **trough 7/20 USD 43.655** (a lower low,
below both bull's and quant's own Round 1 figures) → 7/21 bounce to USD 44.28
(+1.4%, one day). This corrects the record: the price action was NOT stabilization
from 7/17 onward — it was continued drift to a fresh low on 7/20, then a single-day
bounce. The RSI-28 signal (7/17) demonstrably failed to mark the bottom, since AA
made a lower low three days later; that undercuts the bull's mean-reversion timing.
Bear's "already priced in" argument is read as supporting *not being long*, not as a
quantified fresh-short edge.

For a NEW position entered 2026-07-22 at ~USD 44.28: PEAD-driven continued weakness
(~-1% to -2%) and oversold-bounce (~+1% to +2%) roughly cancel → net EV ≈ -0.1% to
-0.3% after costs. The original ~50x tail-ratio objection is moot (the binary event
has already resolved), but is replaced by a genuine near-zero-EV problem with an
unhedged fundamental left tail (South32 financing, further alumina/LME weakness).

Conclusion: NO TRADE, unchanged. Directional-edge confidence ~35/100 (down slightly
from 38 — the PEAD-vs-reversion cancellation makes the two-sidedness cleaner);
confidence in the NO-TRADE call itself ~78/100 (up from 70).

---

## Round 3 — Synthesis

**Hypothesis:** By the research date (2026-07-22) the scouted July 16 catalyst has
already fired and fully priced. AA fell from USD 48.57 (7/15) to a trough of
USD 43.655 (7/20) on a confirmed EPS miss and alumina guidance cut, then bounced one
day to USD 44.28 (7/21). Any position entered now is a new post-event bet, not the
pre-event trade the dossier scouted. The two live directional leans — PEAD-driven
continued weakness (~-1% to -2%) and an oversold-bounce case (~+1% to +2%, resting
on a stale RSI signal that already failed once) — roughly cancel. Net EV computes to
roughly -0.1% to -0.3% after round-trip costs, against an unhedged fundamental left
tail (South32 acquisition financing, further alumina/LME weakness) on a beta-1.63
name. Direction: none. Confidence: 20/100 (in the "there is no trade" call itself
being correct — this maps to the earlier per-persona confidences bull 42 / bear 48
/ quant 78-in-NO-TRADE, synthesized to a low-confidence *directional* verdict of
none, i.e. a firm NO-TRADE).

**Plan:** NO-TRADE. No ticker, entry, exit, or expected profit — the catalyst is
stale and priced, and a fresh position carries ~0 (slightly negative) expected value
with an un-hedged fundamental tail. This honors the bull's own Round 1
pre-commitment ("if debate synthesizes to a stale, already-priced catalyst, default
to NO TRADE") and the standing NKE/LEVI lessons against manufacturing a coin-flip
directional position for the learning loop.

**Dissent (strongest unresolved disagreement, for the post-mortem):** By Round 2,
bear and quant agree on *direction* — PEAD says the confirmed miss-plus-guide-down
should keep AA drifting down, and bear raised its directional-correctness confidence
from 42 to 48 on exactly this basis. Yet both decline to short, citing squeeze risk
on a beta-1.63 name and a net EV near zero. The bull reads the identical tape (lower
low on 7/20, then a one-day bounce) as an oversold mean-reversion setup with every
analyst target above spot. Unresolved: does the PEAD down-drift constitute a
tradable defined-risk short edge (small put spread), or is it genuinely neutralized
by the oversold-bounce/relief-rally pull and squeeze risk down to ~0 EV? Neither
side disproved the other; the down-drift lean was never quantified above the trade
bar, and the mean-reversion lean rests on a stale RSI signal that already failed
once. Testable post-mortem: does the 7/21 bounce extend or fade over the following
weeks, and does AA's realized drift match PEAD (down) or mean-reversion (up)?
