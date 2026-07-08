# Research Debate Transcript — Union Pacific (UNP) Q2 FY26 Earnings

- Opportunity: `2026-07-23-union-pacific-q2-fy26`
- Event: Union Pacific reports Q2 2026 earnings on 2026-07-23; volumes and merger-narrative commentary drive rails.
- Strategy: `debate-three-round-panel`
- Personas / models: bull (sonnet), bear (sonnet), quant (opus), synthesizer (opus)
- Anchor price: UNP $31.23 @ 2026-07-08T15:00Z (source: stub:deterministic paper-trading price feed)
- Institutional lessons injected (via `toa lessons-relevant --type earnings --tickers UNP`):
  1. [NKE, earnings] Confidence ≤~45 with an un-hedgeable positive tail and net EV <~2% against a ~7-8x adverse-tail-to-edge ratio is a no-trade filter, not a size-down; express such earnings gap-shorts via defined-risk options, never a naked short.
  2. [NKE, earnings] Discount post-earnings negative base rates when the name is already at/near its 52-week low.
  3. [TSLA, earnings] Set intraday exits at least one minute inside the session boundary (19:59:00Z, not 20:00:00Z).
  4. [TSLA, earnings] Add a pre-simulation timestamp guard validating both legs map to available US-equity bars, snapping to the nearest valid bar instead of voiding to NEUTRAL.

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

**Note on process:** during Round 2, a orchestration labeling error briefly swapped the "you are the quant" / "you are the bear" instructions between the two agents. Each agent's first Round-2 output under the wrong persona label was discarded and is omitted below; each was corrected and re-run under its actual persona (the same agent that wrote the corresponding Round 1 position). Only the corrected, final Round 2 outputs are recorded.

---

## Round 1 — Independent Opening Positions

### Bull (confidence 62/100)

BULL POSITION — Union Pacific (UNP) Q2 FY26 Earnings, July 23, 2026

**Why this moves the stock, and which way.** Bullish into this print. UNP heads into Q2 FY26 earnings with real operational momentum and a merger overhang entering a news-dense window right around the report date — both catalysts that skew upside if management simply keeps executing.

**Concrete evidence.** Q1 FY26 results (reported late April 2026): freight revenue grew 4% (a first-quarter record); Bulk segment revenue rose 10% on 12% volume growth driven by utility coal demand, favorable gas pricing, the LCRA contract, and a rebound in grain exports to China/Mexico; Industrial segment revenue rose 5% on LNG-terminal and data-center-driven demand; domestic intermodal hit its third consecutive record quarter. Operationally: freight car velocity +9% to 235 miles/day, terminal dwell improved 11% to 19.7 hours, locomotive productivity +6% with a 4% smaller active fleet. The Q1 EPS beat drove roughly a 7% rally (per Tickeron's earnings recap). On the merger side, the Surface Transportation Board accepted UP and Norfolk Southern's revised major-merger application on May 28, 2026, holding the proceeding in abeyance and ordering supplemental information by July 27, 2026 — four days after this earnings call. Expected deal close still guided to early 2027. Flagged clearly: no Q2-specific volume or guidance data — the "beat continues" assumption is informed extrapolation, not sourced fact.

**Catalyst timing and positioning.** Print is July 23, 2026, historically before market open; real price discovery expected in the first 30-60 minutes of the regular session. Plan: build position into July 22 close / July 23 pre-market, manage exit intraday July 23 rather than hold overnight into unknown fresh merger headlines. Per the TSLA lessons, hard time-boxed exit at 19:59:00Z, not 20:00:00Z.

**Proposed action.** Prefer a defined-risk long call (front-week, slightly OTM) if listed options are available and reasonably priced; otherwise long equity. Entry: EOD July 22 / pre-market July 23. Exit: intraday July 23 by 19:59Z. Sizing: moderate, ~2-3% of book notional — not full conviction, because the merger outcome itself is a binary, multi-quarter risk not being bet on directly, only the near-term reaction to the print and management tone.

**Confidence: 62/100.** Momentum, margins, and operating metrics point the right way off a real Q1 beat-and-rally precedent, and the merger calendar creates legitimate reason for outsized attention on this print. Not higher because of zero visibility into actual Q2 volumes/guidance and because STB's abeyance-plus-supplemental-info posture could make merger commentary neutral-to-cautious rather than triumphant.

Sources: Businesswire UNP Q2 2026 earnings-date release; Tickeron UNP Q1 2026 earnings recap; Investing.com UNP Q1 2026 slides recap; FreightWaves UNP Q1 earnings first look; STB press release PR-26-13 (UP-NS merger application accepted, held in abeyance); Wikipedia — Proposed merger between Union Pacific and Norfolk Southern.

### Bear (confidence 25/100)

BEAR POSITION — UNP Q2 FY26 Earnings (2026-07-23)

**1. The directional-earnings thesis is likely overstated.** Class I rail earnings are structurally low-information events. UP runs on multi-quarter volume trends, fuel-surcharge pass-throughs, and a well-worn PSR cost narrative reinforced every call since Jim Vena took over in 2023. Analysts model volumes off weekly AAR carload/intermodal data public well before the print, and UP typically reiterates full-year operating-ratio and volume guidance rather than resetting it sharply at Q2 — most of the print's informational content is already in consensus. Historically UP's post-earnings absolute moves cluster in the low single digits.

**2. What's already priced in.** Three things dominate the UNP narrative, none of which is "will Q2 EPS beat by a few cents": (a) the pending UP–Norfolk Southern merger and STB review timeline — the stock trades on regulatory-process headlines, not quarterly fundamentals; (b) a multi-year freight-volume soft patch (intermodal vs. cheap trucking, coal's secular decline, mixed industrial carloads) already discounted into muted expectations; (c) UP's familiar playbook of defending margins/operating ratio through cost control even with flattish top-line, now the expected "base case." Confirmed fact: Businesswire's July 23, 2026 report date. Everything else is inference from well-established public themes, with a flagged limit: visibility past a Jan 2026 knowledge cutoff, no independent verification of current STB docket status or Q1 FY26 commentary.

**3. Specific blow-up risks.** Dominant tail risk is binary and exogenous to earnings: an STB ruling, merger-condition announcement, or competing-bid/regulatory pushback landing near July 23 would swamp any volume/EPS reaction — an un-hedgeable event structure (echoing the NKE lesson). Low realized post-earnings volatility in rails may mean options already price a wide-enough implied move, giving a naked directional trade poor edge-to-cost economics. Event-timing/session-boundary execution risk applies mechanically per the TSLA lessons.

**4. What the bull likely overweights.** "Cost discipline keeps beating estimates" / "volumes inflect positively" as guaranteed tradeable pop — ignoring that beat-and-raise on operating ratio is now the expected outcome, not a surprise, and that merger-process news can override fundamentals same-day or same-week regardless of print quality.

**5. Confidence a directional trade is justified: 25/100.**

### Quant (no-trade confidence 78/100, directional confidence 22/100)

**Base rates (all estimates, not a verified backtest):** assumed UNP earnings-day |move| distribution: ~55-60% of prints ≤3%, ~30% 3-6%, ~10-15% >6% tail; mean |move| ≈3.25%. No directional edge assumed — P(up) ≈ P(down) ≈ 50%; the merger-narrative driver treated as a two-sided, un-forecastable tail, not a directional signal.

**Instrument availability:** per institutional lessons 1/3/4 and the stub-feed nature of this simulation, assumes ONLY US-equity 1-minute bars (13:30Z–19:59Z) are executable — no options chain on the synthetic single-price stub series. Any directional bet is therefore NAKED equity; the un-hedgeable tail cannot be capped.

**EV calculation:** Gross EV = 0.50×(+3.25%) + 0.50×(-3.25%) = 0.00%. Net EV after ~0.15% costs/slippage ≈ -0.15%. Even at a generous 55/45 directional lean: Gross EV = +0.325%, Net EV ≈ +0.175% — still far under a 2% threshold. Adverse-tail-to-edge ratio: an ~8% tail move (10-15% probability) against a ~0.18% best-case edge ≈ 40:1+, worse than the ~7-8x no-trade precedent from the NKE lesson.

**No-trade filter (institutional lesson 1):** confidence ≤45 (met — directional confidence 22), un-hedgeable tail (met), net EV <~2% (met), large adverse-tail-to-edge ratio (met). All four conditions satisfied → NO-TRADE, not size-down.

**Recommended action:** NO-TRADE / NEUTRAL. Position size = 0 (zero/negative EV with an unbounded naked tail means no size is optimal; Kelly = 0). If a trade were forced (it is not): entry 2026-07-23T13:31:00Z, exit 2026-07-23T19:59:00Z, both timestamp-guarded per lessons 3/4.

**Confidence:** no-trade call 78/100; any directional thesis 22/100.

---

## Round 2 — Rebuttals (corrected)

### Bull rebuttal (revised confidence 33/100, down from 62)

Partially concedes the bear's "already priced in" point but notes Q1's ~7% move happened despite being a "no surprise" PSR-execution quarter — suggesting either more informational content in prints than public carload data captures, or Q1 was an outlier; can't fully rule out the latter, a real concession.

On the STB timing: concedes the July 27 supplemental-information deadline is a company filing obligation, not a ruling date — nothing forces a market-moving regulatory decision to land inside the July 23 window, so the bull was overstating the timing coupling in Round 1. On reflection, the quant's symmetric/un-forecastable-tail treatment of the merger variable is more defensible than the bull's original framing.

On the quant's EV math: pushes back narrowly — the 3.25% mean/symmetric assumption reads like an unconditional rail-sector prior, not this name's actual recent behavior, given the one hard Q1 data point sits well outside it. But concedes one data point doesn't overturn a distributional assumption; would want quant to check actual multi-quarter UNP move history before fully accepting 3.25%/symmetric — if confirmed, concedes the base rate and EV math holds and kills the trade.

On the naked-equity constraint: concedes this is decisive. The Round 1 preference for a defined-risk call was explicitly built on the NKE lesson (cap the un-hedgeable tail, don't take it naked); if no options exist on this feed, any directional bet is naked equity exposed to exactly the un-hedgeable merger-headline tail the bear flagged, and the quant's ~40:1 adverse-tail-to-edge ratio is the correct lens. Per the NKE lesson, this is a no-trade scenario, not a size-down scenario, at this confidence level.

What would flip to no-trade (and largely already has): confirmation options are unavailable, plus a multi-quarter check showing symmetric/low-single-digit reactions rather than a repeatable positive-skew pattern — both currently unconfirmed/unfavorable.

**Revised confidence: 33/100.** Not fully down to the quant's 22 because the Q1 reaction is genuine evidence the name can move more than a generic rail base rate suggests, but sharply down from 62 without options to cap the tail and without evidence Q1's move was a pattern rather than an outlier.

### Bear rebuttal (revised confidence 20/100, down from 25)

The bull's Q1 data doesn't overturn the bear's thesis — a single observation being asked to carry too much weight. A ~7% one-day rally on a Q1 beat is exactly the kind of low-base-rate tail event the bear's Round 1 distribution already accounted for (quant's own prior: >6% move at only 10-15% probability); one observation in that tail doesn't mean the tail got fatter, it means one of the expected low-probability outcomes fired. Letting a single favorable print override "historically low single digit moves" would be recency-driven overfitting (echoing the NKE lesson on discounting single-print anomalies). Notes an asymmetry the bull doesn't address: Q1's beat had simultaneous multi-metric confirmation (velocity, dwell, productivity, fleet efficiency, multiple segment beats) — a high bar to repeat; a merely-continued-improvement Q2 print is more likely to get a shrug.

On STB timing: takes it more seriously than the bull, but moves toward MORE caution. A supplemental-information order due July 27, four days after the print, doesn't make the July 23 call a clean read on merger progress — it makes it the moment management is most likely to hedge/soften tone precisely because regulators are still asking questions and a filing deadline is imminent. Market attention splits between "how were the numbers" and "what did management just imply about the merger" — the second channel can move the stock hardest, in either direction, unrelated to freight fundamentals, and can't be hedged with any instrument available in this sim. This makes the July 23 print MORE dangerous to trade directionally, not more attractive.

What would change the bear's mind: (a) sourced evidence Q2 volumes/margins are tracking meaningfully above the Q1 run rate specifically; (b) a signal the STB abeyance is resolving low-drama before July 23; (c) confirmed real, liquid, listed options capping downside to a known premium. All three together might justify a small, defined-risk, single-direction bet; none are established.

**Revised confidence: 20/100.** The bull's new evidence sharpens the story but adds a second, unhedgeable, date-specific risk channel on top of an already low-information print — an argument for staying out, not for sizing up.

### Quant rebuttal (no-trade confidence 82/100 up from 78, directional confidence 20/100 down from 22)

One data point (Q1's 7% move) can't move the central mean much — n=1 is not a distribution — but legitimately informs revising the tail-probability upward: ~12%→20% for a >6% move, with the central mean |move| nudged slightly from 3.25% to ~3.75%, reflecting that this name may be running hotter than a generic Class-I-rail base rate, without fully capitulating to "one print defines the new normal" (would share the bear's skepticism about that).

Revised EV: direction held at 50/50 — the fundamentals story is real but is largely visible pre-print via weekly AAR carload data and is not a demonstrated forecasting edge. Gross EV = 0.50×3.75% + 0.50×(-3.75%) = 0.00%; Net EV = -0.15%. Even at a generous 55/45 lean: Gross EV = +0.375%, Net EV = +0.225% — still far below the ~2% threshold, and now measured against a WORSE adverse-tail-to-edge ratio (still ~40:1+) because the tail widened without adding edge — the textbook signature of a fluke-prone, no-edge trade.

On the STB deadline: reinforces the un-hedgeable-tail case, doesn't provide directional edge — a second variance-increasing, non-edge-generating fact this round.

On options: declares this "decisive independent of everything else" — no evidence from the dossier, the price feed, or the institutional lessons in scope that a listed/liquid options chain is executable on this sim's stub series. Absent that confirmation, the bull's preferred structure resolves to unavailable by default, collapsing any directional bet to naked equity — exactly the configuration the NKE lesson says must be filtered to no-trade rather than sized down, regardless of the base-rate math.

**Revised confidence:** no-trade call 82/100 (up from 78); directional thesis 20/100 (down from 22). New evidence widened the assumed distribution and confirmed a fatter-tailed, un-hedgeable, no-options event than first modeled — reinforcing, not weakening, the no-trade conclusion.

---

## Round 3 — Synthesis

**Hypothesis:**
- statement: "UNP Q2 FY26 (reporting 2026-07-23) is a low-information, already-priced-in Class I rail print. Weekly AAR carload data makes volumes visible pre-release and guidance is typically reiterated, not reset, so there is no demonstrated directional forecasting edge (50/50). The distribution carries a fat, un-hedgeable tail — widened by the July 27 STB supplemental-filing deadline four days out, which layers merger-tone/regulatory-parsing risk on top of the earnings distribution — that cannot be capped because the sim surface offers naked equity only (no executable options). Net EV sits far below the action threshold."
- direction: none
- confidence: 20/100 (directional conviction); ~80/100 conviction in the no-trade decision itself.

**Plan:**
- ticker: UNP
- action: no-trade
- entry: null / null
- exit: null / null
- expected_profit_pct: 0

**Dissent (logged for post-mortem):** The sharpest unresolved tension is the epistemic status of Q1 FY26's ~7% one-day move. Bull reads it as possible evidence rail prints carry more information than public AAR carload data captures (a repeatable positive skew), while conceding it might be a one-off outlier. Bear/Quant read the same data point as a single draw from an already-assumed 10-15% tail — recency/small-sample overfitting, echoing the NKE single-print-anomaly lesson. Nobody produced the multi-quarter post-earnings move distribution for UNP that would adjudicate this; the quant's tail-probability revision (12%→20%, mean 3.25%→3.75%) is an unfalsified judgment call, not a measured update. A subtler split: bear implies the July 27 STB deadline makes management's July 23 tone structurally cautious (a mild negative skew), while quant insists direction stays a strict 50/50 and the deadline only widens variance — that latent short-lean was never tested. Also worth logging: the entire no-trade outcome is contingent on one unverified structural assumption — that no options are executable on this stub feed. If that assumption is ever falsified, the analysis does not merely re-size, it reopens, because a defined-risk long-call structure would neutralize the single decisive filter (the un-hedgeable tail).

**Synthesis reasoning:** All three personas converged on no-trade, and the convergence strengthened across rounds rather than being a soft compromise: directional confidence decayed monotonically (bull 62→33, bear 25→20, quant 22→20) while the quant's no-trade confidence rose (78→82). The convergence rests on all four institutional-lesson filters being met simultaneously, more firmly in Round 2 than Round 1: (1) confidence ≤45 — every persona's terminal directional confidence sits at or below 33; (2) un-hedgeable tail — the sim's naked-equity-only surface can't cap the ~10-20% tail, and the July 27 STB deadline (a company filing obligation, not a ruling — a point the bull explicitly retracted) adds a second, orthogonal, un-hedgeable regulatory-tone risk channel; (3) net EV <2% — even under a generous 55/45 skew, net EV is ≈+0.18-0.23% after ~0.15% costs, an order of magnitude below the 2% action threshold, with gross EV at true 50/50 sitting at 0%; (4) adverse-tail-to-edge ratio ~40:1+ — the Round 2 tail-widening (legitimately motivated by the real, sourced Q1 ~7% move) made this ratio worse, not better, since variance rose without any accompanying directional edge. New information that widens variance without generating edge argues against action, not for it. With no options vehicle to convert an un-hedgeable naked-equity bet into a bounded-risk expression, there is no admissible way to take the print. **Final: NO-TRADE on UNP.** No entry/exit window opened.
