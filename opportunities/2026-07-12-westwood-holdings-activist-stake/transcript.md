# Research Debate Transcript — WHG (Westwood Holdings Group)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.

Event: Settian Capital disclosed a 5% stake in Westwood Holdings Group (WHG) via Schedule 13D, filed 2026-07-12, signaling potential activist campaign at the small-cap asset manager. Source: [StockTitan SEC filing summary](https://www.stocktitan.net/sec-filings/WHG/schedule-13d-westwood-holdings-group-inc-sec-filing-f4921b59dbe9.html) (accessed 2026-07-12T23:20:25Z). Dossier-stated impact window: 2026-08-01 (unsourced).

Modeling note: `toa price WHG ... --provider twelvedata` returned `MarketDataUnavailable` for this simulated 2026 timeframe (confirmed the API key itself works against real historical dates, e.g. AAPL 2024-07-11). No live or historical WHG quote could be obtained for this debate — flagged explicitly by all three personas and treated as a hard input gap, not ignored.

## Round 1 — Independent research

### Bull (sonnet)
A Schedule 13D (not 13G) filed 2026-07-12 by Settian Capital disclosing a 5% stake in WHG is the tell — 13D explicitly signals intent to influence management/board/strategy, unlike a passive 13G. Activist campaigns at small asset managers historically push for cost cuts, buybacks, strategic review, or an outright sale — any of which re-rates the stock on announcement, not on fundamentals realized. Evidence: StockTitan filing summary, 5% stake, 13D, 2026-07-12; no letter text, no board-seat demand, no prior 13D/A history for Settian cited — Day 1 of the campaign.

Proposed action: long WHG common stock (cleanest instrument for a thin-float small cap; options likely too illiquid). Entry as close to now as possible; treat 2026-08-01 as a checkpoint to reassess, not a hard exit.

Confidence: 55/100. Capped by single-source dossier, no confirmation of Settian's track record, and no price/volume reaction data available.

### Bear (sonnet)
Treat as a low-conviction, event-hype trade, not a fundamentally-driven activist campaign. A bare Schedule 13D at 5% is the regulatory floor — doesn't confirm activist intent (no Item 4 language, no board-seat demand, no strategic-alternatives push quoted in dossier). 5% is below the ~8-10%+ level that typically confers real leverage. Thin float cuts both ways — pops on a 13D headline can fully round-trip with no follow-through. The 2026-08-01 "impact window" is unsourced — no confirmed shareholder meeting, earnings date, or filing deadline cited; may be a scouting-model placeholder. Single-source dossier, no corroborating reporting.

What would change the read: a 13D/A showing the stake increasing toward 8-10%+ or adding co-investors; disclosed Item 4 intent language; confirmation 2026-08-01 maps to a real corporate event; independent corroborating reporting.

Confidence in skepticism: 70/100.

### Quant (opus)
Modeling limitation flagged first: no anchorable live/historical price — a hard input gap forcing size-down and re-verify-before-fill, not a rounding error.

Base rate (assumptions, general activist-13D event-study knowledge): announcement-day/first-days abnormal return for 13D filings ~+3% to +6%, but that pop is largely behind us by the 2026-08-01 entry date — what's being bet on is post-filing drift/continuation over ~3 weeks. Estimated P(sustained continuation) ≈ 35-45%; conditional magnitude ≈ +5-8% if it continues, ≈ -2-4% give-back if it fades.

EV: 0.40×(+6.5%) + 0.60×(-3.0%) = +2.60% - 1.80% = +0.80% gross. Costs/slippage for illiquid small-cap round-trip ≈ 1.0%. No-anchor haircut ≈ 0.5%+. Net EV ≈ **-0.7%**.

Sizing: no trade at market on an unverified quote; if forced, ≤0.25R conditional on (a) a live verified quote at entry and (b) confirmation the stock isn't already at/near its 52-week high. Per prior lessons, if the only positive-EV path requires an unfillable conditional, don't record the trade — flat is the trade.

Confidence: 25/100. Default STAND ASIDE.

## Round 2 — Rebuttal

### Bull rebuttal
Concedes: Bear's 5%-below-threshold point is correct and was underweighted in Round 1 — without Item 4 language, the "tell" is weaker than framed. Concedes Quant's -0.7% EV moves the needle; Round 1's 55/100 was narrative conviction, not calibrated, since no competing EV math was done.

Pushes back: 13D vs 13G is still a meaningful choice by the filer (didn't have to disclose intent to influence at 5%) — Bear discounts this to zero. Also notes 13D filers disproportionately follow up with public letters/amendments within weeks when they intend to act — a real, checkable signal not yet ruled in or out.

Revises confidence down to **35-40/100**, contingent on someone checking actual Item 4 language and Settian's filing history.

### Bear rebuttal
Takes Quant's negative EV as convergence, not disagreement, with the Round 1 skeptical read. Argues the 35-45% continuation base rate is generous given no stated intent — would bias lower, pushing EV more negative.

Concedes: Bull's point that the 13D filing itself creates a mechanical attention/momentum effect is fair and was underweighted — but that argues for a near-term trade framing, not a thesis held through the August checkpoint, which is itself a tell that even Bull's conviction doesn't extend that far.

Flags a gap neither Bull nor Quant addressed: why 2026-08-01 specifically — no earnings, shareholder meeting, or filing deadline cited. If nothing dated exists, the checkpoint is arbitrary and both the upside and give-back cases may be timed wrong.

Bumps confidence to **75/100** (skepticism).

### Quant rebuttal
Concedes: Bear's structural points land — 5% below the leverage threshold, no articulated intent, and critically the unsourced 2026-08-01 date is "a countdown to nothing" if untraceable to a real event. Without the anchor, the 35-45% base rate likely drifts toward 30-35%.

Concedes: Bull is right that 13D filings do carry a real empirical announcement-drift effect — but argues that drift is largely a filing-window (2026-07-12) phenomenon that may already be substantially priced in by any executable entry, and by an August checkpoint.

Core unchanged: still no live/historical quote. Net EV holds at ≈ **-0.7%**, still negative — a negative-EV trade doesn't become tradable because the story is interesting.

States three concrete facts that would flip to a small long (15-20% size, hard stop): (1) a real live/historical price quote to anchor risk and sizing, (2) a sourced catalyst tying 2026-08-01 to an actual event, (3) confirmed Item 4 intent language or Settian's activist track record.

Confidence: **30/100**. Holds STAND ASIDE.

## Round 3 — Synthesis (opus)

**Hypothesis**: Settian Capital's 5% Schedule 13D in WHG signals possible activist intent, but the thesis rests on three unverified facts — no anchorable price, an unsourced 2026-08-01 "impact window," and unconfirmed Item 4 intent/filer track record. Modeled expected value is negative (~-0.7%) after illiquid-small-cap costs and a no-live-price haircut. All three personas converged on caution.
- Direction: **no_trade**
- Confidence: **72/100** (confidence in the no-trade decision itself, not in a directional move)

**Plan**: NO TRADE / STAND ASIDE.
- Reason: negative modeled EV (gross ~+0.80% vs ~1.0% costs + ~0.5% no-price haircut ≈ net -0.7%); no live/historical price available to anchor entry, stop, or size; unsourced 2026-08-01 catalyst date, possibly a placeholder; unconfirmed activist intent (Item 4 language / Settian track record); 5% stake is below the ~10%+ level that typically confers real activist leverage.
- No price target set — no price data was available in this debate window.
- Revisit triggers (all three would need to be true): (1) a real live/historical WHG quote to anchor risk/sizing; (2) a sourced catalyst tying 2026-08-01 to an actual event (earnings, proxy/annual-meeting date, director-nomination deadline); (3) confirmed Item 4 activist-intent language or an established activist track record for Settian Capital. If met, flip to a small long (15-20% size, hard stop).

**Dissent**: Whether the 13D announcement drift is a tradable edge or already gone. Bull held (even at reduced 35-40 confidence) that 13D filings carry real, empirically documented short-term announcement drift that could be captured. Quant conceded the drift is real but argued it's likely already decaying or fully priced in by any executable entry — turning a genuine effect into a non-actionable one. This was never resolved with data since no live price series existed. If WHG continued drifting up after 2026-07-12, the miss was the no-price haircut/execution-lag assumption overriding a real edge; if it faded or gave back, the caution was vindicated.
