# Post-mortem — 2026-07-08-caesars-icahn-fertitta-bidding-war (CZR)

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

**Strategy:** pm-investigator-critic (investigator: sonnet, critic: opus)
**Run:** 2026-07-12T23:30:05Z

## What happened

Plan: token long, entry 2026-07-10T14:00Z @ $31.50, exit 2026-07-11T20:00Z @ $32.00
(+1.6% target), confidence 35, sized as a Kelly-near-zero token position because the
panel could not agree the available price series was usable signal for deal economics.

Reality: **no fills at all**. The exit timestamp, 2026-07-11T20:00Z, falls on a
**Saturday** — US equity markets are closed, so no trade/quote data exists for that
leg. The simulator correctly returned `market data unavailable: CZR 2026-07-11: HTTP
400` and recorded the plan as neutral (0.0% realized) rather than fabricate a fill.
The entry leg's own timestamp (Friday 7/10, market hours) was valid, but with no exit
price the pair could not be closed. `matched_hypothesis: no` — not because the thesis
was right or wrong, but because it was never tested against real prices.

## Root cause: wrong-assumption

The plan derived its exit timestamp directly from the go-shop deadline (2026-07-11) as
stated in the dossier, with no check that the date fell on a trading day. July 11,
2026 being a Saturday is derivable from the date alone — no external research was
needed, only a calendar lookup. This was not missing information (the deadline date
was already in the dossier), not a data-feed fault (`HTTP 400` correctly reflects a
closed market), and not a "priced-in" dynamic — the research notes' "signal vs. noise"
concern was about whether the price series reflected deal economics, not about
execution-calendar validity, and never touched trading-day validation.

The defect is structural: corporate/legal deadlines (go-shop windows, deal closes,
regulatory decisions) are not constrained to trading days, but market-order fills are.
The plan-generation logic mapped a legal calendar date verbatim onto an execution
timestamp with no trading-calendar-awareness step and no fallback rule to roll a
non-trading exit forward to the next open session.

This is a distinct, more basic failure mode than the pricing/signal debate the panel
actually had — the go-shop resolution itself may well have played out as hypothesized
in the real world, but this dossier cannot confirm or refute that, because the plan was
never executable as written.

## Lessons

- Before finalizing any plan, validate that every entry and exit timestamp falls
  within an open trading session (not a weekend or exchange holiday) for the specific
  instrument, and roll non-trading exit dates forward to the next open session.
- Never map a corporate/legal calendar date (go-shop, earnings, deal deadlines) directly
  onto an execution timestamp — treat such dates as catalysts and derive the fill time
  from the nearest valid trading session.
