# Debate transcript — 2026-07-14-citigroup-q2-fy26

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

- **Strategy:** three-round-panel
- **Personas / models:** bull (sonnet), bear (sonnet), quant (opus); synthesizer (opus)
- **Run:** 2026-07-07T20:13:30Z
- **Event:** Citigroup (C) Q2 FY26 earnings, before open 2026-07-14. Shares ~$145 at scout (2026-07-06).

**Note on prices:** the `toa price` provider is a deterministic stub returning
non-physical per-minute values (28 → 314 → 473 within days). Price *levels* carry no
signal, so the panel reasoned on the real-world thesis; no live price target was set
(no-trade outcome).

**Institutional lessons injected:**
1. Confidence ≤~45 + un-hedgeable positive tail + net EV <~2% against ~7-8x
   adverse-tail-to-edge = no-trade filter (not size-down); express earnings gaps via
   defined-risk options, never naked.
2. Discount negative base rates when the name is near its 52-week low.
3. Intraday exits ≥1 min inside the session boundary (19:59:00Z, not 20:00:00Z);
   US equity bars run 13:30Z–19:59Z.
4. Validate both legs map to available bars; snap to nearest valid bar.

---

## Round 1 — Independent research

### Bull (catalyst-hunter)
Beat-and-pop pattern intact. Consensus EPS ~$2.62–2.64 (+30–34% YoY) on revenue
~$23.37B (TipRanks / Yahoo Finance); Zacks Earnings ESP +7.82%, Rank #3 favors another
beat. Clean analogue: Q2 FY25 (2025-07-15) beat $1.96 vs $1.60 (+22.5%), stock +3.7%
same-day, markets revenue +16% YoY (CNBC). Momentum: fresh 52-week high, +44.3% YTD,
near $145–148 (top of $77.51–$147.96 range) — strength into the print, the opposite of
lesson #2's low-base-rate trap. Uniform pre-print target hikes: Morgan Stanley $154→$164
(6/29), Truist $147→$158 (6/26), Wells Fargo $162→$165 (6/18), KBW $140→$153 (5/8)
(Benzinga). **Trade:** defined-risk long weekly calls (~$150–152 strike, exp 2026-07-17),
entry 2026-07-13T19:59:00Z, exit 2026-07-14T19:59:00Z, target 3–5% underlying move.

### Bear (skeptic)
Directional long is crowded and priced-for-perfection. C near 52-week high ($147.96)
after an 82% trailing-year / +44% YTD run (Simply Wall St / Yahoo). Consensus already
expects a big beat (~$2.62–2.66, +34% YoY) and Zacks ESP +7.82% means the whisper is
already above consensus → an in-line beat risks a "sell-the-news" reaction. Claims Citi
blows through its options-implied move in ~4 of the last 8 prints (Apr 2026 implied 3.7%
vs realized 10.4%; Jan 2026 implied 4.1% vs −8.2% on decent numbers) (Investing.com /
Market Chameleon). Current options price a ~4% move. **Verdict:** no naked directional
trade; if forced, a defined-risk debit put spread / iron condor on post-earnings mean
reversion / vol crush.

### Quant (pragmatist)
Consensus EPS ~$2.65 (+35% YoY); Zacks ESP +4.74% → mild positive lean. Implied
earnings-day move ~4% (Bloomberg straddle) / 5.56% weekly (OptionSlam). Last print
(Q1, Apr 14): beat $3.06 vs $2.65; one-day move ~2.6% (max 3.7%) — realized < implied,
IV crush won (CNBC / OptionSlam). **Probabilities:** P(up)=0.52, P(down)=0.48,
conditional magnitude ≈4%. **EV (directional long equity):** gross = (0.52−0.48)×4% =
+0.16%; net ≈ −0.05% after ~0.15–0.20% round-trip + slippage. Adverse-tail-to-edge
≈25x, far past the ~7-8x filter. Long straddle: negative EV (pay ~4% implied vs
~3–3.5% expected realized → IV crush). Short vol: credit ~1–1.3% too thin vs a
season-opening left tail. **Verdict:** NO-TRADE, confidence ~45.

---

## Round 2 — Rebuttal

### Bull
Coin-flip framing ignores the asymmetry: consistent EPS beats, ESP +7.82%, and a
uniform pre-print upward-revision wave are a momentum tell, not noise. Bear's own
"shatters the implied move" data is a *fat right tail* — precisely the reason to buy
defined-risk calls (capped loss), not stock or a straddle; when the underlying moves
2–3x the implied, IV crush is a rounding error. Concedes naked is wrong (never proposed)
and that an in-line beat leaves calls worthless — a capped, known cost, a feature.
Would change mind if the whisper visibly runs several points above the +7.82% ESP, or
if C gaps up 4%+ in the two sessions before the report, gutting the entry edge.

### Bear
Q2 FY25's +3.7% pop came in the mid-$80s with room to re-rate; today at a 52-week high
the easy multiple expansion is done. Uniform target hikes + ESP +7.82% make the beat the
base case, not the catalyst. A day-before weekly $150–152 call pays peak IV and eats the
guaranteed post-print vol crush; Jan 2026 (decent numbers, −8.2%) shows OTM calls expire
worthless on a good-but-not-perfect quarter. Agrees with quant: ~25x adverse-tail-to-edge
is a screaming no-trade. Would change mind only if C sells off *into* the print (removing
priced-for-perfection) or implied is cheap vs realized. **Hold: NO-TRADE.**

### Quant
Resolves the volatility tension decisively: the Bear's "Apr 2026 moved 10.4%" is
contaminated — that is ~30-day post-earnings drift, not the earnings-day gap.
OptionSlam's clean Apr 14 print: pre-earnings close $126.28, one-day move 2.61%, max
intraday 3.72% vs 3.7% implied → realized ≈ implied. So the Bear's long-vol premise
fails on same-day data; long straddle remains negative-EV. On the Bull: ESP and target
revisions are real but already priced into a +44% YTD, 52-week-high tape; the Q2 FY25
+22.5% beat produced only +3.7% same-day. Long $150–152 calls need a >~4% up-gap just to
clear premium; P(finishes sufficiently ITM) ≈ 0.52 × 0.35 ≈ 0.18 — a lottery ticket.
Would change mind if P(up) > ~0.58 (a credible leak / sector read) or implied compresses
below ~3% vs ~3.5% realized. **Still NO-TRADE.**

---

## Round 3 — Convergence (synthesizer)

**Hypothesis:** Citigroup Q2 FY26 is a likely EPS beat (ESP +7.82%, uniform upward
target revisions), but the beat is already priced into a stock at fresh 52-week highs
after a +44% YTD run, and clean same-day earnings-move history (~2.6–3.7%) roughly
equals the ~4% implied move — no exploitable directional or volatility edge. A
priced-for-perfection setup where a good-but-not-perfect print can still sell off.
**Direction:** neutral. **Confidence:** 43.

**Plan:** C — action **none**. No entry/exit; expected_profit_pct 0. The setup fails the
institutional no-trade filter (confidence ≤~45, directional net EV ≈ −0.05%,
adverse-tail-to-edge ≈25x ≫ ~7-8x). Long calls are a ~0.18-probability lottery into peak
IV; long straddle is negative on crush; short vol carry too thin vs the season-opening
tail.

**Dissent (unresolved):** The Bull maintains that the fat right tail plus consistent
beats and momentum justify a small defined-risk long call (capped loss), arguing the
coin-flip framing understates the asymmetry. The Quant/Bear counter that
P(call finishes sufficiently ITM) is only ~0.18 — a lottery ticket paying peak IV before
crush — and that a ~25x adverse-tail-to-edge massively exceeds the 7-8x no-trade filter.
