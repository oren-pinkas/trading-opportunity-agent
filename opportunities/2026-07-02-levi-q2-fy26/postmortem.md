# Post-mortem — 2026-07-02-levi-q2-fy26 (LEVI)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

**Strategy:** pm-investigator-critic (investigator: sonnet, critic: opus)
**Run:** 2026-07-12T23:30:05Z

## What happened

Plan: minimal-conviction (35) LONG, entry 2026-07-08T19:50Z @ $23.50, exit
2026-07-09T13:45Z @ $23.65 (+0.6% target, EV-discounted near zero). The panel had no
directional consensus — bull long (48) on beat-and-raise momentum, bear short (38) on
priced-for-perfection near highs, quant NO-TRADE directional (78, the highest-confidence
read) because directional EV was indistinguishable from zero and the only positive-EV
structure was an out-of-mandate long-gamma straddle.

Reality: the entry filled at $24.41 — already **+3.87%** above the planned entry level
before the position was opened, an intraday run-up on 7/8 pre-print
([source](https://api.twelvedata.com/time_series?symbol=LEVI&interval=1min&date=2026-07-08&timezone=UTC)).
From that entry to the exit at $23.955
([source](https://api.twelvedata.com/time_series?symbol=LEVI&interval=1min&date=2026-07-09&timezone=UTC)),
price fell **-1.86%** — a real but modest down-move, well inside the ~4.7-4.89%
implied/realized-move band the bear and quant both cited. Realized: **-1.864%, loss,
matched_hypothesis: no**.

## Root cause: wrong-assumption

Two independent wrong assumptions compounded into the loss, both contradicted by
information already on the table at research time, not by new data or bad luck:

1. **The synthesizer overrode a no-edge panel.** The quant — the highest-confidence
   panelist (78) — explicitly recorded NO TRADE directional: "directional EV is
   indistinguishable from zero and the only positive-EV structure is a long-gamma
   straddle that this directional mandate excludes" (`transcript.md`, Round 2). The
   synthesizer nonetheless logged a minimal LONG "for the learning loop." A genuine
   no-edge coin-flip still books real, non-zero losses when forced into a directional
   trade.
2. **Stale entry-price assumption.** The plan modeled entry near $23.50, the pre-print
   reference price used at research time two days earlier. By the actual entry
   timestamp the stock had already run ~3.9% intraday — the entry logic used a static
   planning-time price rather than validating against a live quote at fill time.

The realized -1.86% move sits within the range both bear and quant anticipated (not a
surprise/priced-in mechanism, and not a data or timing fault) — this was a knowable,
process-level error: trading a no-edge setup, and pricing the entry off a stale
reference.

Of the three panelists, the **bear** (confidence 38 — priced-for-perfection fade,
"down-gaps from a high base tend to be faster/larger") most closely anticipated
direction on both legs. The **quant** correctly identified the no-edge condition but
declined to convert it into a directional call — the panelist that was "most right"
was the one whose recommendation (no trade) was overridden.

## Lessons

- When the highest-confidence panelist (the quant) says directional EV is ~0 and the
  only positive-EV structure is out of mandate (e.g. a straddle), log NO TRADE — do not
  manufacture a minimal directional position "for the learning loop"; a no-edge
  coin-flip still books real losses.
- Anchor entry prices to a live quote fetched at the actual entry timestamp, not a
  stale pre-move reference — validate the planned entry is still within a small
  tolerance of the current price before filling, and re-price or abort if the stock has
  already run away from the modeled entry.
