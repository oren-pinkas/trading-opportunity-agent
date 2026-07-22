# Post-mortem — 2026-07-12-spacex-starship-flight13

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

## Investigator (reconstruction)

Plan: default posture NO-TRADE; conditional short of SPCX only if a launch-day pop
printed. Entry window 2026-07-16T22:45:00Z, target $165; exit 2026-07-18T20:00:00Z,
target $151. Confidence 72 on the "no unconditional long, only a conditional fade"
read.

Simulation result: `fills: []`, `realized_profit_pct: 0.0`, `outcome: neutral`,
`matched_hypothesis: no`, note: **"market data unavailable: 'no 1min bar for
2026-07-16 22:45:00'"**. No trade was actually filled.

The transcript's own "Process note" (Round 2) already surfaced this exact risk class:
both bull and bear/quant independently hit `toa price SPCX ... --provider twelvedata`
HTTP 400 errors for same-day/near-real-time timestamps, because SPCX only IPO'd
2026-06-12 (about a month before this dossier) and TwelveData's coverage for very
recently-listed tickers lags. The panel worked around it during research by adopting
a slightly-stale $147.93 print as reference spot, but the plan's actual entry
timestamp (launch window, several days later) was never confirmed to be priceable.

## Critic (root cause)

Was it knowable at research time? Yes, more so than the Nayax case — the panel
*directly observed* twelvedata HTTP 400 errors for SPCX near-real-time queries during
Round 2 and noted it as a process caveat, but did not extend that observation to
question whether the planned future entry/exit timestamps (which are also
near-real-time relative to the debate date) would be priceable when the simulator
later ran. The data-coverage risk was seen and not connected to the plan's own
execution timestamps.

**Root cause: data** — compounded by a **missing-info** element: the panel had direct
evidence of TwelveData's coverage gap for this specific ticker and did not
generalize it to the plan's entry/exit design.

## Lessons

1. Freshly-IPO'd tickers (listed within the last ~1-2 months) are a distinct data-risk
   category for this system: TwelveData's near-real-time coverage lags for them. If a
   panel hits provider errors on `toa price <NEW_TICKER> ...` during research, that is
   a direct signal to flag the entire plan as data-coverage-at-risk, not just a
   research-time inconvenience to route around with a stale reference print.
2. Reuse the Nayax lesson: test-query the real provider for the plan's exact
   entry/exit timestamps before finalizing, especially when the ticker has already
   shown provider errors earlier in the same debate.
