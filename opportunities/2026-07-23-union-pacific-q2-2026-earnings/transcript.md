# Research Debate Transcript: UNP Q2 2026 Earnings

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. Run at 2026-07-26T05:30:02Z, isolated to this opportunity only
(`2026-07-23-union-pacific-q2-2026-earnings`) — no other opportunity's dossier was
read or referenced during persona rounds.

## Ground truth used

Dossier event summary: "UNP reports Q2 2026 results today with analysts expecting
EPS growth on freight pricing and volume mix strength." Source: BusinessWire,
"Union Pacific Corporation Announces Second Quarter 2026 Earnings Release Date"
(accessed 2026-07-23T05:29:18Z) — a date announcement only; no EPS/revenue/guidance
figures were ever in the dossier.

Verified prices (`toa price UNP <ts> --provider twelvedata`):
- 2026-07-23T13:30Z (open): USD 309.900
- 2026-07-23T19:59Z (earnings-day close): USD 304.365 (-1.79% intraday)
- 2026-07-24T19:59Z (next-session close): USD 307.460 (+1.02%; still -0.79% vs the
  2026-07-23 open)
- 2026-07-25: no data — Saturday, market closed

## Round 1 — Independent research

### Bull (sonnet)
Read the -1.79%/+1.02% sequence as sell-the-news-dip-then-buy-the-recovery. Proposed
LONG UNP common equity, entry zone sub-$308, target retracement to $309.90, exit
timed ≥1 minute inside the session boundary per the TSLA lesson. Confidence 55/100 —
flagged as moderate given only two post-earnings closes and no EPS/guidance data to
confirm the beat narrative.

### Bear (sonnet)
Noted the dossier is a calendar reminder, not a research thesis — zero EPS, revenue,
or guidance figures, no analyst name or estimate attached to "EPS growth expected."
Argued the -1.79%/+1.02% pattern is consistent with either a real miss partially
bought back or noise on an in-line/beat print, and cannot be disambiguated without
the missing data. Any bull entry today is chasing a 3-day-stale, partially-reversed
move with no fresh informational edge. Recommended NO-TRADE, confidence 75/100; any
position taken must be defined-risk (options), never naked directional (NKE lesson).

### Quant (opus)
Framed any new entry as a fresh continuation/mean-reversion bet, not the original
earnings-surprise bet, since the event is 3 days stale (DAL lesson: don't re-bet an
already-priced fundamental). Direction is ambiguous even in sign — the drop argues
down-drift, the bounce argues absorption; treated as canceling. EV calc: P(down)=0.51,
P(up)=0.49, magnitude ±1.3%, gross EV=+2.6bps, round-trip costs ~7bps, net EV≈-4.4bps
— negative and an order of magnitude smaller than costs. NO TRADE. Confidence 22/100
on direction, ~85/100 that no-trade is correct (LEVI lesson: don't manufacture a
token directional position for the learning loop).

## Round 2 — Rebuttal

### Bull
Conceded the quant's EV math and the bear's data-vacuum argument are sound; the
"dip-buyers" narrative was inferred from price action alone, which is circular
without the actual print. Withdrew the immediate long entry. Would only re-raise
given a confirmed EPS/revenue beat, unchanged-or-raised guidance, and volume
confirmation on the recovery day — none of which exist in the record. Updated
confidence 25/100 (down from 55), effectively concedes to NO-TRADE.

### Bear
Argued the bull's "market voting with money" over-reads a 2-point sample — a single
session's +1.02% bounce is exactly what noise produces absent a fundamental anchor,
and is equally consistent with a dead-cat bounce inside a real selloff. The quant's
EV math (net -4.4bps against ~7bps cost) corroborates and strengthens, rather than
merely confirms, the no-trade case. Updated confidence 82/100 (up from 75).

### Quant
Neither rebuttal moves the point estimate. The bull's own "half the move already
reversed" claim actually shrinks the residual magnitude available to trade, which
would require P(up) confidently above ~52-53% to clear costs — a number the bull
never had beyond the pattern label itself. The bear's missing-data argument is
symmetric ignorance: it doesn't shift P(down) off 0.51, it only widens the error
bars, and wider error bars around a negative mean make standing aside *more*
correct (cost is deterministic, payoff is not). Updated: direction confidence
20/100 (down from 22), confidence NO-TRADE is correct 88/100 (up from 85).

## Round 3 — Convergence (synthesis)

**Verdict: NO-TRADE.** Direction: none. Confidence: 88/100 that standing aside is
correct; 20/100 in any directional view.

All three personas converged, and conviction strengthened rather than softened
across rounds (bull 55→25 and withdrew the long; bear 75→82; quant 85→88 on
no-trade while directional confidence decayed 22→20). Three independent legs point
the same way: (1) **information** — the dossier is a date-announcement press
release with no EPS/revenue/guidance figures, so the panel never knew what UNP
actually reported, only how price moved around the print; (2) **identification** —
the -1.79%-then-+1.02% sequence is a 2-point sample that cannot distinguish a real
miss being partially bought back from noise on an in-line/beat print, so the bull's
"market voting with money" reading over-extracts from too little data; (3)
**arithmetic**, which is decisive on its own — at P(down)=0.51/P(up)=0.49 with
±1.3% magnitude, gross EV is +2.6bps against ~7bps round-trip cost, for net EV of
about -4.4bps: the edge isn't merely negative, it's smaller than the frictions,
so realized sign would be set by slippage rather than by any thesis. The missing
fundamentals do not rescue this — they are symmetric ignorance that widens the
error bars around an already sub-cost expected value, which makes standing aside
more correct, not less.

**Plan:** ticker UNP, action no-trade, no entry/exit window, expected profit 0%.

**Dissent (for post-mortem):** Nobody sourced the actual Q2 2026 EPS/revenue/
guidance — convergence happened under a fundamental-data blackout, which is weaker
corroboration than agreement reached against verified facts. The open question is
whether this dossier should have reached a research round at all with only a
date-announcement as its content, not whether NO-TRADE was correct. Narrower
dissent: the bull's overreaction-then-absorption read was withdrawn on EV grounds,
never falsified on pattern grounds — log as an untested hypothesis for a future
post-earnings-drift study on Class I rail names, not as a live edge; even if true,
the ~0.79% residual retracement would not have cleared round-trip costs.
