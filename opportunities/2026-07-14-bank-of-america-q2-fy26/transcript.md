# Debate transcript — 2026-07-14-bank-of-america-q2-fy26

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

- **Strategy:** three-round-panel
- **Personas / models:** bull (sonnet), bear (sonnet), quant (opus); synthesizer (opus)
- **Run:** 2026-07-07T20:05:22Z
- **Event:** BAC Q2 FY26 earnings, reports 2026-07-14 pre-market (~10:45Z, confirmed
  via BofA newsroom), before the 13:30Z US equity-bar open.
- **Setup:** BAC ~$60.17, ~99% of 52-wk range ($44.75–$60.83), near its high.

## Institutional lessons injected

1. Confidence ≤~45 with an un-hedgeable positive tail and net EV <~2% against a
   ~7-8x adverse-tail-to-edge ratio is a NO-TRADE filter, not a size-down; express
   earnings gap moves via defined-risk options, never naked. (src: 2026-06-25-nike-q4-fy26)
2. Discount post-earnings negative base rates when the name is near its 52-week LOW.
   (Does not apply here — BAC is near its high.) (src: 2026-06-25-nike-q4-fy26)
3. Set intraday exits ≥1 minute inside the session boundary (19:59:00Z, not
   20:00:00Z). (src: 2026-07-02-tesla-deliveries)
4. Both trade legs must map to available US-equity bars (13:30Z–19:59Z). (src: 2026-07-02-tesla-deliveries)

---

## Round 1 — Independent openings

### Bull (catalyst-hunter)

Beat-and-raise setup into a same-morning bank cohort (JPM/WFC/C) print. Consensus
~$1.09–1.12 EPS on ~$30–30.7B revenue vs a Q1'26 baseline of $1.11 EPS / $30.3B /
16.0% ROTE; BAC has beaten 8 straight quarters, estimate revised +2.2% in the last
month. Real driver is NII: FY26 NII growth guide raised to 6-8% (from 5-7%) after Q1
NII printed $15.9B, +9% YoY, on a 5-yr fixed-rate asset repricing tailwind plus
rate-cut expectations being priced out. Credit clean: Q1 provision $1.3B (~$190M
below est.), consumer NCO improving, "very good and improving" per management. Likely
post-stress-test capital-return bump = stacked second catalyst. Stock near 52-wk high
→ momentum/trend-confirmation trade. **Action:** long via 7/17 slightly-OTM (~$61)
call, entry 2026-07-14T13:35:00Z, exit 19:55:00Z, target +2.5-4% intraday.
Sources: TradingView/Zacks bank preview; Seeking Alpha Q1 call coverage; autofinancenews.net,
ainvest.com (credit); top1markets.com (capital return).

### Bear (skeptic)

The pop is fighting what's already priced. (1) NII guide raised **June 27** — three
weeks before the print; a beat that merely confirms it is a "sell the news" setup
[sahmcapital.com, 2026-06-27]. (2) Expectations stretched after 8 straight beats;
options price only ~3.5% implied, though BAC exceeded implied in 6 of last 8 prints
(April +8.0% vs 3.3% implied) — realized vol hard to handicap either way, cutting
against any high-confidence directional bet [Investing.com; MarketBeat]. (3) Q1 showed
a rare net reserve **release** ($72MM); not repeatable — any reserve-build reversion
reads as a negative surprise, and NCOs ticked up sequentially ($1.3B→$1.4B Q4→Q1)
[SEC 10-Q/8-K]. (4) **Date risk:** some sources placed BAC + MS on July 15 vs
JPM/WFC/C on July 14 — if BAC lags, peers set the tape and mute its idiosyncratic
reaction. **Action:** NO-TRADE pending date confirmation; if forced, defined-risk
only (tight debit straddle/iron fly), entry 13:30:00Z, exit ≤19:59:00Z.

### Quant (pragmatist)

Implied move ~3.5% (weekly ~4.47% OptionSlam); actual exceeded implied in 6 of 8, but
April's *close* move was only 1.81% (the 8% was tariff tape). **Binding constraint:**
the gap fires ~10:45Z, ~2h45m before the 13:30Z open — the event move is
**un-capturable** with tradable bars. BAC at ~99% of 52-wk range (near high), so
Lesson #2 does not apply; priced-for-perfection carries negative asymmetry. EV table
for the only executable trade (intraday open→close): continuation 0.42×+1.30%, flat
0.20×0, reversal 0.38×−1.30% → gross **+0.05%**, minus 0.06–0.10% costs → net
**≈ −0.02%**. Lesson #1 filter: conf ~48, EV ~0, adverse-tail-to-edge ≫7-8x.
**Action:** NO-TRADE.
Sources: Investing.com (implied move); OptionSlam BAC; StockAnalysis (price/52-wk);
IG Q2 2026 bank preview; TradingView/Zacks preview.

---

## Round 2 — Rebuttals

### Bull

Concedes both load-bearing points. The 2026 capital-return bump follows the annual
CCAR/DFAST test (~late June) — a **separate calendar event**, not a 7/14 earnings
trigger; scratched. Concedes the pre-market gap captures the bulk. Holds that
broad-based bank beats (NII + credit + fees all clean) historically show intraday
**continuation** rather than fade — BAC's Q4-25/Q1-26 prints closed near session
highs — so the residual is conditional on gap quality, not pure noise. **Refined:**
no blind 13:35Z entry; wait for the first 15-30 min opening range and only enter if
price holds above the pre-market gap high on volume; drop the OTM call (concedes the
IV-crush/theta/spread critique) for a tight debit call spread or small underlying;
fully concede to no-trade if the open fades below the gap high.

### Bear

Confirms BAC reports **July 14 pre-market** [Stocktitan/BofA newsroom] — resolves the
date risk but reinforces no-trade (gap baked into the open before any 13:35Z entry).
Verified the capital-return bump followed the **2025** CCAR results announced early
July, decoupled from the earnings print — not a fresh same-day catalyst
[BofA newsroom, 2025-07]. Agrees with quant's structural point; argues confidence
belongs in the low-to-mid 40s (not high 40s) given the priced-for-perfection skew
(any blemish punished disproportionately). **Flips to a trade only** if the 2026
capital-return announcement is still pending same-day, or via a capped-premium
defined-risk structure.

### Quant (tie-breaker)

Numeric adjudication. PEAD event studies put ~70-80% of the reaction into the
pre-market/opening print → ~1.9% un-capturable, leaving ~0.5-0.6% intraday residual;
capturable drift = (0.42−0.58)×0.6% ≈ **−0.10%** before costs. Granting the
capital-return catalyst maximum benefit lifts continuation only 0.42→0.50 and widens
the residual to ±1.5% → EV ≈ **0%**; it cannot manufacture the +2.5-4% move because
that already gapped. The 7/17 OTM call fails harder (IV crush, ~3-day theta, ~4-5%
round-trip spread; needs ~1.5% intraday continuation the ~0.8% residual std rarely
delivers at P≈0.50). Date risk lowers unconditional EV and widens variance — never
rescues. **Verdict: NO-TRADE, confidence 51.**

---

## Round 3 — Synthesis (neutral, opus)

- **hypothesis:** {statement: "Fundamental lean mildly long (beat-and-raise base
  case) but NOT tradable — the gap fires pre-market before the 13:30Z open, ~70-80%
  of the reaction is un-capturable, and the executable intraday residual has EV ~0%
  to negative after costs, worsened by near-52-week-high negative asymmetry, a
  priced-in NII guide, and non-repeatable Q1 reserve dynamics.", direction: long,
  confidence: 38}
- **plan:** NO-TRADE. ticker BAC, action buy, entry null, exit null,
  expected_profit_pct 0. Status held at `researched` (never scheduled) so no fill is
  taken. Rationale: catalyst resolves in the pre-market gap; only intraday residual
  drift remains (net EV ≈ 0 to negative after 0.06-0.10% costs); bull conceded the
  capital-return catalyst and the blind entry; its surviving conditional continuation
  idea can't be a deterministic pre-committed entry/exit; near-high negative
  asymmetry + Lesson #1 → no-trade filter, not a size-down.
- **dissent:** Whether broad-based bank beats produce a persistent, tradable intraday
  CONTINUATION leg after the gap. Bull: BAC's Q4-25/Q1-26 closed near highs, implying
  the ~0.5-0.6% residual is directionally exploitable conditional on a high-volume
  gap-and-hold. Quant: even at maximum continuation weight (0.42→0.50) EV is ~0%, and
  the edge is discretionary/conditional — never survives costs or the
  deterministic-entry constraint. Post-mortem should check, on the actual 7/14 bars,
  whether a gap-hold continuation rule would have paid after costs.
