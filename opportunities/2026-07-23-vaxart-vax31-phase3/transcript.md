# Research Debate Transcript — 2026-07-23-vaxart-vax31-phase3 (VXRT)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.
Debate run: 2026-07-26.

## Pre-debate data verification

- Dossier event: Vaxart Phase 3 VAX-31 (oral vaccine) vs Pfizer Prevnar 20 and Merck Capvaxive. Source: "10 clinical trials to watch in the second half of 2026" — BioPharma Dive, https://www.biopharmadive.com/news/biotech-pharma-clinical-trials-watch-2026/808255/ (accessed 2026-07-23T04:24:42Z). Impact window: 2026-09-30.
- Live price check (twelvedata): VXRT $0.487 at 2026-07-23T13:30:00Z; $0.490 at 2026-07-24T13:30:00Z.
- Coverage probe: 6 additional minute timestamps on 2026-07-24 (13:35, 14:00, 15:00, 16:00, 17:00, 19:00 UTC) all returned `KeyError: no 1min bar` — only 13:30 UTC resolved on that day. Coverage ≈ 1/7 (14%) of probed timestamps.
- Institutional memory (`toa lessons-relevant --type product --tickers VXRT`): SPCX lesson (2026-07-22 post-mortem) — freshly-thin-coverage tickers are a distinct data-risk category; verify exact planned entry/exit timestamps price cleanly before scheduling, not just a stale reference print.

## Round 1 — Independent research

### Bull
The Catalyst: Vaxart's Phase 3 VAX-31 trial (oral vaccine, head-to-head vs. Pfizer's Prevnar 20 and Merck's Capvaxive) is flagged by BioPharma Dive as one of the sector's most closely watched H2-2026 readouts. Being named alongside two blockbuster-franchise incumbents is itself a signal. Impact window 2026-09-30, ~65 days from 2026-07-26.

Why it moves the stock: VXRT is a sub-$1 clinical-stage name ($0.487→$0.490). A positive readout would be the first real de-risking event for the oral-vaccine thesis at pivotal scale; binary biotech catalysts on thinly-floated penny names routinely produce multi-fold moves, not incremental ones.

Proposed action: Long VXRT, small size, entered now-to-mid-September, exit as a post-readout event trade (scale out into a pre-catalyst run-up, or hold a small residual through the print).

Data-quality caveat: 6 of 7 probed minute timestamps had no bar; per the SPCX lesson, must pin exact tradable entry/exit timestamps and confirm they price before scheduling; use daily/session-level fills rather than intraday timing, keep size small to survive slippage.

### Bear
Thesis risk: binary readout with no informational edge over the rest of the market (same public BioPharma Dive article since 2026-07-23).

What's priced in: $0.48-0.49 for a company running Phase 3 against two entrenched, already-approved vaccines signals the market expects a negative/ambiguous readout and/or dilution — no partnership premium, trades below $1.

Named risks: (1) binary outcome risk / hard immunogenicity bar vs. Prevnar 20/Capvaxive; (2) dilution/cash-runway risk typical of clinical-stage microcaps funding trials via ATM/registered-direct raises around catalysts; (3) competitive positioning — even a win doesn't guarantee commercial uptake given Pfizer/Merck's entrenched payer contracts and sales forces; (4) data-coverage/liquidity risk — only 1/7 probed timestamps resolved, unreliable fills/slippage.

Recommendation: NO-TRADE or defined-risk sized for total loss. Would change mind: disclosed interim/DSMB data, dilution-light financing, confirmed deeper liquidity.

### Quant
Base rates: vaccine Phase 3 ~70-80% success generally, but haircut for non-inferiority vs. entrenched marketed comparators and no approved oral-adenoviral precedent. Assumed P(clean win)=35%, P(mixed)=25%, P(miss)=30%, P(delay)=10%.

EV on USD 10,000 notional: gross EV +USD 3,750 (+37.5%); after 6% round-trip costs/slippage: net EV +USD 3,150 (+31%); after -15% expected dilution drift (0.7 prob × ~-22%): net EV ≈ +USD 1,650 (+16.5%).

Breakeven P(win) after costs+dilution ≈ 24-26%; a 10-point error in the 35% prior erases the edge — an unfalsifiable prior, not a proprietary edge.

Tradability: only 1 of 7 probed minute timestamps resolved (14% coverage) — an entry/exit that cannot be priced has undefined EV. Any plan must use 13:30 UTC prints only.

Bottom line: SKIP. If overridden: max 0.25% of capital, entry/exit hard-pinned to 13:30 UTC, no trade unless both timestamps price cleanly in advance.

## Round 2 — Rebuttal

### Bull rebuttal
Concedes: the dilution point and the coverage-quality gate both land — a microcap running Phase 3 will very likely tap the ATM around the readout; the liquidity picture (1-of-7 resolving) is close to disqualifying per the SPCX precedent; P(clean win)=35% is a prior, not an edge.

Pushes back: Bear's "$0.48 = market expects negative readout" is an assumption, not evidence — no short interest, options skew, or analyst commentary was cited. A sub-$1 clinical-stage biotech trades there for structural reasons (float, cash runway, sector sentiment) as often as for informational reasons. Quant's own Round-1 math still showed positive EV (+16.5%) — the disagreement at that point was about sizing/tradability, not sign.

Revised position: no longer defends "small size, flexible entry"; concurs that absent two clean pinned tradable prints, the position should be SKIP; if priceable, max 0.25% notional only, no discretionary sizing up.

### Bear rebuttal
Quant's EV framing is too generous because the prior is unfalsifiable — nothing justifies pinning P(clean win) at 35% rather than 20% or 15%. EV already collapsed from +37.5% to +16.5% before any downward stress-test of the success prior itself.

Bull's "small size + pin timestamps" mitigation is a liquidity fix, not a thesis fix — it addresses fill risk but does nothing about informational-edge risk, dilution risk, or commercial-uptake risk. Coverage (1/7, 14%) is independently disqualifying — a data desert, not just a caveat.

Would change mind: disclosed interim/DSMB signal, non-dilutive financing, confirmed multi-timestamp liquidity depth. Stays NO-TRADE.

### Quant rebuttal
Rejects Bear's "price = probability" framing as sloppy — price reflects share count/dilution history/cash runway, not readout odds directly — but accepts a modest downward adjustment since an efficient-ish market with 65 days to a scheduled binary should already price consensus base rates.

Revises: P(clean win) 35%→28%, P(mixed)=25%, P(miss) 30%→37%, P(delay)=10%.

Recomputed EV on USD 10,000: gross EV +20.5% (+USD 2,045, down from +USD 3,750); after 6% costs: +14.5% (+USD 1,445); after 15% dilution drift: ≈ -0.6% (≈ -USD 55). Breakeven P(win) after costs+dilution ≈ 29-30%; the revised prior (28%) is now below breakeven — EV flipped negative on a 7-point, largely indefensible prior adjustment. States explicitly: "the EV sign is a free parameter."

Final position: SKIP, strengthened. Both entry and exit timestamps must independently price cleanly before any commitment.

## Round 3 — Synthesis

```json
{
  "hypothesis": {
    "statement": "VXRT's VAX-31 Phase 3 readout (impact window 2026-09-30) is a publicly known, fully-priced binary event on a sub-USD 1 microcap where no persona identified an informational edge; the expected value is indistinguishable from zero once round-trip costs (6%) and expected dilution drift (-15%) are applied, and the name fails an independent tradability gate at 14% minute-bar coverage.",
    "direction": "none",
    "confidence": 82
  },
  "plan": {
    "ticker": "VXRT",
    "action": "no-trade",
    "entry": null,
    "exit": null,
    "expected_profit_pct": null,
    "reason": "Negative-to-zero EV under a defensible prior, plus only 1 of 7 probed minute timestamps priced (14% coverage) — no reliably fillable entry/exit pair can be pinned."
  },
  "dissent": {
    "unresolved": "Whether the sub-USD 1 price carries information about readout odds. Bear treated USD 0.48-0.49 as the market pricing a negative/ambiguous outcome; Quant explicitly rejected price-as-probability yet still cut P(win) 35%->28% on an efficient-market argument — the same reasoning he called sloppy. That 7-point cut is what flipped EV from +14.5% to -0.6%. Bull's objection stands unrebutted: no short interest, options skew, or analyst data was ever cited to anchor any prior. The panel converged on the verdict while the number driving the verdict remains unfalsifiable.",
    "for_post_mortem": "If VXRT rallies hard on a clean win, the miss was not the process — it was that no persona could source a defensible prior. Log whether a tradable prior was ever obtainable, or whether this class of opportunity should be gated out at scout time on coverage alone, before rounds are spent."
  }
}
```

### Prose synthesis

All three personas ended at SKIP / NO-TRADE, and the convergence was driven by the bull-side advocate conceding rather than the bear winning an argument. Bull dropped "small size, flexible entry" in Round 2, accepted the coverage gate, and conceded that P(clean win)=35% was an unverifiable prior rather than an edge. That leaves no live advocate for the position.

The decisive fact is that the Quant's own EV calculation flipped sign under a modest, self-proposed prior revision: 35%→28% P(clean win) took gross EV from +37.5% to +20.5%, +14.5% after costs, and ≈ -0.6% (-USD 55 on USD 10,000) after the 15% dilution drift — below a 29-30% breakeven. A 7-point move on an unanchored prior reverses the trade's sign. The Quant's own words, "the EV sign is a free parameter," are the finding here: this is not a thin-edge trade, it is a calculation with no load-bearing input.

Independently, and sufficient on its own, the tradability gate fails. Only 1 of 7 probed minute timestamps resolved (14% coverage). Per the SPCX institutional-memory lesson, both entry AND exit timestamps must price cleanly in advance before any commitment. One resolving timestamp cannot supply a pinned entry-exit pair, so the EV is not merely negative — it is undefined, because the position is not reliably fillable.

Confidence 82 reflects strong three-way agreement on the verdict alongside genuine fragility in the reasoning that produced the EV number.
