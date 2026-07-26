# Research Debate Transcript — 2026-07-23-transdigm-stellant-blocked

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. Run in isolation on this opportunity only — no other dossier was
read or referenced.

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

## Event

TransDigm Group (TDG) dropped its USD 960 million bid for Stellant Systems (a
radar-components supplier) after the DOJ said it would sue to block the deal.
Source: "TransDigm Calls Off Deal for Rival After DOJ Lawsuit Threat" - Bloomberg,
2026-07-13, https://www.bloomberg.com/news/articles/2026-07-13/transdigm-calls-off-deal-for-rival-after-doj-merger-scrutiny
(accessed 2026-07-23T04:24:42Z). Dossier scouted 2026-07-23T04:24:42Z, stated impact
window 2026-08-15.

Confirmed anchor price: TDG traded at 1223.44995 at 2026-07-23T15:00:00Z
(`toa price TDG 2026-07-23T15:00:00Z --provider twelvedata`).

## Institutional lessons injected (via `toa lessons-relevant --type regulatory --tickers TDG`)

1. Validate every entry/exit timestamp falls within an open trading session; roll
   non-trading exit dates forward to the next open session.
2. Never map a corporate/legal calendar date directly onto an execution timestamp —
   treat it as a catalyst, derive the fill time from the nearest valid trading session.
3. A signal-to-noise ratio below ~0.15 on a linear-EV fade is not a durable edge;
   simulate-plans does not enforce path-dependent stops.
4. When the actual entry fill prints outside the planned entry band, treat that as an
   early falsification signal.
5. Before finalizing a plan's entry/exit timestamps, test-query the real price
   provider for those exact timestamps during research.
6. Never treat a single missing minute-bar as a terminal skip — exhaust a fallback
   ladder before recording market-data-unavailable.
7. Size fill-precision to the size of the edge: sub-0.5%-edge, sub-30-confidence plans
   should use a tolerance window, not an exact-minute target.

---

## Round 1 — Independent research

### Bull (sonnet)

Long TDG, conviction 35/100. Thesis: dropping the deal removes overhang/litigation
risk, signals capital discipline, and frees balance sheet capacity for buybacks or the
next accretive bolt-on — consistent with TransDigm's serial-acquirer playbook. Cited
only two price points: ~1228.63 at 2026-07-13T14:30Z vs. ~1223.45 at
2026-07-23T15:00Z, read as roughly flat (~-0.4%), i.e. the catalyst mostly priced with
limited residual upside drift. Acknowledged but downweighted the bear case (lost
growth avenue, DOJ scrutiny hardening) as second-order and slower-moving than the
trade horizon. Proposed: long TDG equity, entry band 1215-1235 (tolerance per lesson
7), exit near the next open session after the 2026-08-15 impact window — rolled
forward to Monday 2026-08-17 since 08-15 is a Saturday (lessons 1-2). Confidence:
35/100.

### Bear (sonnet)

No-trade, confidence in any tradeable edge 12/100. Cited a fuller (but, as later
corrected, still incomplete) series: 2026-07-10 ~1288.33 -> 2026-07-13 ~1238.15 ->
2026-07-23 ~1223.45, read as a gradual ~-1.2% post-news drift, i.e. fully priced and
stale ten days after the news broke, with no mechanism (no earnings gate, no options
expiry, no index event) identified for a delayed reaction. Flagged the deal size
(USD 960 million) as immaterial to TDG's scale, and challenged the bull's directional
read: dropping a bolt-on after a DOJ threat could equally signal DOJ scrutiny
hardening toward TDG's core aftermarket-pricing business model — a read-through
negative for future M&A optionality, not a clean "overhang removed" positive. Noted
the price drifted down, not up, since the news — disconfirming a bullish
overhang-removal story on its face. What would change her mind: a peer-relative
decomposition isolating company-specific under-reaction, a dated catalyst still ahead
in the window, or confirmed news of DOJ escalating scrutiny of TDG's core business.
Recommended NO-TRADE, would fade a bull long directly.

### Quant (opus)

No-trade, confidence in the no-trade recommendation 76/100, confidence in any
exploitable edge under 10/100. Pulled a granular minute-bar series via
`toa price TDG <ts> --provider twelvedata`:

```
2026-07-09 15:00   1301.13    (pre-news)
2026-07-10 15:00   1288.33
2026-07-10 19:55   1292.34    (last pre-news close)
---- news breaks Mon 2026-07-13 ----
2026-07-13 13:31   1266.58    (open, gap -2.00% vs Fri close)
2026-07-13 13:45   1231.24    (-2.79% in 14 minutes)
2026-07-13 14:00   1238.86
2026-07-13 15:00   1238.15
2026-07-13 19:30   1230.42    (near close, -4.79% vs Fri close)
2026-07-14 15:00   1226.79
2026-07-15 15:00   1216.15
2026-07-16 15:00   1238.71
2026-07-17 19:55   1215.07
2026-07-20 15:00   1212.42
2026-07-21 15:00   1200.83
2026-07-22 15:00   1194.77
2026-07-23 15:00   1223.45    (confirmed reference print)
2026-07-23 19:55   1210.04    (close)
```

Event-day move: -4.79% (with -2.79% of it in the first 14 minutes) — a fast, complete
reaction, not a slow reveal. Peak-to-trough 7/10->7/22: -7.39% (approx.). Cumulative
7/10->7/23 close: -6.37%.

Materiality: TDG ~56M shares x ~1220 = ~USD 68B market cap, plus ~USD 25B net debt =
~USD 93B enterprise value. The abandoned Stellant bid (USD 960 million) is ~1.41% of
market cap / ~1.03% of EV. Base rate for an acquirer walking from a sub-5%-of-cap
bolt-on under antitrust pressure: acquirer-side abnormal return typically -1.0% to
+1.5%, centered near 0 to +0.5% (capital retained, no integration risk, no
self-inflicted break fee). The observed -4.79% is 3-8x too large to be explained by
the deal alone — the parsimonious read is that the market repriced TDG's entire
serial-acquisition/aftermarket-pricing franchise's regulatory risk (a multiple
compression event), not the specific deal (an EPS event). Multiple compression from a
regulatory-posture shift does not mean-revert on a 3-week horizon absent a new
catalyst (a DOJ walk-back, a successfully closed bolt-on, an Antitrust Division
leadership change) — none identified in the dossier.

Explicit EV calculation (horizon ~15-16 sessions to 2026-08-14/17, sigma_daily ~1.30%
observed, sigma_horizon ~5.20%):

```
P(reversion +2.0%)   = 0.30
P(flat 0.0%)         = 0.35
P(extend -3.0%)      = 0.35
Gross EV = 0.30(+2.0) + 0.35(0.0) + 0.35(-3.0) = -0.45%
Round-trip cost (spread+slippage+fees) ≈ 0.16%
Net EV = -0.61%
SNR = |EV_gross| / sigma_horizon = 0.45 / 5.20 = 0.087  (below the 0.15 threshold)
```

Critical structural finding: TDG's fiscal year ends 2026-09-30, so fiscal Q3 earnings
land in early August — inside the stated 2026-08-15 impact window (and any 08-14 to
08-17 exit). TDG earnings-day moves routinely run 4-8%. Holding a position to that
exit is predominantly an unhedged earnings bet, not a test of the Stellant
abandonment thesis — a category error that would make even a winning outcome
uninformative about the actual event studied. Recommended NO TRADE. Confidence in
no-trade: 76/100. Confidence in any exploitable residual edge: under 10/100. What
would change his mind: evidence the 7/13 move was sector/market-driven rather than
TDG-idiosyncratic (peer comparison not yet done); a shorter horizon that excludes the
earnings print; a concrete dated DOJ-posture catalyst inside the window (none found).

---

## Round 2 — Rebuttal

### Bull (sonnet)

Conceded the Round 1 price citation was incomplete and misleadingly mild — the fuller
series shows a sharp, front-loaded -4.79% single-day move, not a flat reaction.
Argued the first-14-minute violence (-2.79%) is consistent with an
overshoot-then-partial-reversion pattern, but conceded the subsequent path (continued
decline through 7/22 before the 7/23 bounce) is "overshoot-and-extend," not
"overshoot-and-recover" — a materially weaker claim than his Round 1 thesis needed.
Partially conceded the franchise-repricing read is more parsimonious than his
overhang-removal story, pushing back only that TDG survived prior antitrust
controversy (2019 congressional scrutiny) without a lasting de-rating once the matter
closed — an open durability question, not evidence in his favor. Fully conceded the
earnings-contamination point: no defense of the exit as constructed; the only way to
preserve any version of the trade is an exit strictly before the confirmed earnings
date, which he could not verify with confidence. Revised confidence: 15/100. Revised
action: no-trade as constructed; would only reconsider a small starter long if the
bounce showed one more confirming session and a safely pre-earnings exit could be
confirmed.

### Bear (sonnet)

Confirmed the corrected, sharper price data strengthens rather than weakens the
staleness argument — a faster, more complete, front-loaded reaction is the textbook
signature of efficient real-time absorption, not a sign of information still being
digested. Fully adopted Quant's franchise-repricing read, resolving her own Round 1
directional ambiguity toward bearish/neutral: a move 3-8x larger than the deal's
economic weight cannot be a verdict on the deal alone. Argued the earnings
contamination is independently sufficient to kill the trade even setting aside
staleness and materiality. Noted Bull's revised position still rests on the same
understated numbers and never addressed materiality or the earnings window before
Round 2. Revised confidence: 6/100 in any exploitable edge (down from 12/100).
Revised action: NO-TRADE, on three independent grounds — full information absorption
before scout date, franchise-level (not deal-level) repricing that does not
mean-revert on this horizon, and earnings contamination of any window reaching the
stated exit.

### Quant (opus)

Re-pulled a consistent 19:55Z-close series to correct both counterparts, who had each
anchored on a milder two-point read:

```
2026-07-10 (pre-news) 1292.34
2026-07-13 (news day)  1233.81
2026-07-14             1217.39
2026-07-16             1231.30
2026-07-20             1206.54
2026-07-22             1196.86
2026-07-23 (scout)     1210.04
```

Event-day move 7/10->7/13: -4.53%. Peak-to-trough 7/10->7/22: -7.39%. Cumulative
7/10->7/23: -6.37%. News-close-to-scout-close 7/13->7/23: -1.93%. Showed that Bull's
Round 1 baseline (7/13 ~1228.63 vs 7/23 ~1223.45) was an intraday-stamp pairing that
happened to sit post-crash, silently discarding the entire -4.53% event-day
repricing — the single biggest factual error in the debate. Bear's milder -1.2%
figure was directionally right but also missed the event-day gap.

Priced Bull's best-case "capital discipline / buyback" thesis explicitly: the
mechanical ceiling on a re-rate from redeploying the full USD 960 million at zero
premium is the same ~1.0-1.4% materiality figure — 3.2x to 6.2x smaller than the
observed move (event-day and cumulative respectively). No plausible buyback-signal
magnitude closes that gap; the market is repricing the franchise multiple, not the
deal. Agreed Bear's qualitative "DOJ posture hardening" read and his own quantitative
franchise-repricing thesis are independently arrived-at and mutually corroborating —
flagged this convergence as the one piece of real corroboration in the debate, per
the prior institutional lesson distinguishing verified corroboration from false
consensus under a data blackout. Noted Bull's thesis requires a relief rally that the
tape (down, not up, over nine sessions) directly contradicts.

Explicitly tested a pre-earnings exit alternative: TDG fiscal Q3 typically reports in
the first week of August (~2026-08-04 to 08-06), so a clean pre-earnings exit window
is ~2026-07-31 to 2026-08-03 (a 5-7 trading-day hold from a 7/24 entry). Found this
makes the EV/cost ratio worse, not better: horizon sigma drops from ~4.8% (16-day
hold) to ~3.2% (7-day hold), but the gross edge shrinks roughly proportionally to
~±0.25%, giving SNR ~0.078 (versus 0.094 for the full-horizon plan) — worse in both
cases versus the 0.15 threshold. The ~16bps round-trip cost is fixed regardless of
horizon, so shortening the hold to dodge earnings makes that fixed cost consume a
larger fraction of a smaller edge. Also noted the +1.10% bounce on 7/23 is a single
draw well inside one daily standard deviation — not a signal. Revised confidence in
no-trade: 87/100 (up from 76). Confidence in any exploitable edge: under 8/100.
Final recommendation: NO TRADE, no position long or short, no entry scheduled.
Flagged that Bull's 35->15 shift is closer to a fourth no-trade vote than genuine
dissent, since it rested on mis-sampled data — the real evidentiary weight is that
the magnitude arithmetic and the tape point the same way independently across three
analytical approaches.

---

## Round 3 — Synthesis (opus)

**Hypothesis** — direction: no-trade, confidence: 88/100.

TransDigm's abandonment of the USD 960 million Stellant Systems bid under DOJ
pressure is not an exploitable event for TDG equity. The deal was only ~1.0-1.4% of
TDG's enterprise scale, yet the tape shows a -4.5% to -4.8% single-day move on
2026-07-13, a -7.39% peak-to-trough drawdown into 2026-07-22, and -6.37% cumulative
2026-07-10 to 2026-07-23 — a magnitude 3-6x larger than any deal-specific value
transfer can support. The parsimonious reading is a market-wide re-rating of TDG's
serial-M&A and regulatory-risk multiple, already absorbed, ten days stale at scout
time, and not mean-reverting on a three-week horizon absent a new catalyst.
Independently and dispositively, TDG fiscal Q3 earnings land in early August
(~2026-08-04 to 08-06), inside any exit at or near the stated 2026-08-15 window, so
any held position is an unhedged earnings bet rather than a test of the Stellant
thesis; the tested pre-earnings alternative (exit ~2026-07-31 to 08-03) makes the
EV/cost ratio worse, not better.

**Plan** — ticker: TDG, action: no-trade. No entry or exit scheduled. Gross EV
estimated at -0.45%, net -0.61% after ~16bps round-trip costs; SNR 0.087 vs. the
0.15 durability threshold. The stated 2026-08-15 impact date is a Saturday and its
natural remediation (Monday 2026-08-17) sits after TDG's fiscal Q3 print; the
earnings-clean alternative was explicitly tested and rejected on cost-to-edge
grounds. No holding period inside the window clears the bar in either direction.

**Dissent** — the strongest unresolved disagreement is the durability of the
franchise re-rating, not the trade decision. Bull's residual claim — that TDG
absorbed prior antitrust scrutiny (2019) with no lasting multiple compression once
the matter closed, implying the current de-rating is a transient scrutiny premium
that decays as the DOJ matter recedes — was conceded by no one and refuted by no
one. Quant's magnitude arithmetic proves the move was too large to be deal-specific,
but proves nothing about whether the resulting compression is permanent or reverts
over a multi-month horizon; both sides implicitly conceded a three-week window is
too short to test it. Post-mortem should record: if TDG re-rates upward on a
three-to-six month horizon post-DOJ-resolution, the no-trade was correct for this
window but the underlying bull mechanism was not wrong, only mis-scoped in time.

**Rationale.** All three personas converged on no-trade, and the convergence is
corroborated rather than merely agreed: the magnitude arithmetic, the tape (a fast,
complete, non-reverting event-day reaction), and Bear's qualitative DOJ-hardening
read arrive at the same franchise-repricing conclusion through independent routes —
stronger evidence than a false-consensus pattern seen in a prior debate under a data
blackout. The earnings-contamination finding is independently sufficient and decides
the case on its own: the stated impact window cannot be traded without taking an
unrelated 4-8% earnings risk, and the only earnings-clean shortening of the horizon
degrades expected value rather than improving it. Confidence is set at 88 rather than
higher only because the durability of the multiple compression — the live dissent —
remains untested and would matter on a longer horizon than this plan contemplates.
