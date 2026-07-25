# Research Debate Transcript — 2026-07-23-boeing-smbc-737max-order

Strategy: three-round-panel (bull: sonnet, bear: sonnet, quant: opus, synthesizer: opus)
Run at: 2026-07-25T05:09:20Z
PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Event: SMBC Aviation Capital orders 100 Boeing 737 MAX jets (60 -10, 40 -8) at Farnborough Air Show, announced 2026-07-20. Ticker BA. Stated impact window 2026-08-31.
Source: SMBC Aviation Capital Orders 100 Boeing 737 MAX Jets — https://boeing.mediaroom.com/2026-07-20-SMBC-Aviation-Capital-Orders-100-Boeing-737-MAX-Jets (accessed 2026-07-23T22:07:07Z)

Institutional memory injected: lessons-relevant --type product --tickers BA returned one lesson tagged to ticker SPCX (fresh-IPO data-coverage risk) — noted as likely inapplicable to BA (mature, highly liquid ticker) but panel was asked to flag any analogous data-coverage issue.

---

## Round 1 — Independent research

### BULL (sonnet)

Long BA, narrative/momentum thesis: SMBC's first-ever MAX-10 order is a competitive-win signal vs. Airbus in the lessor channel, at a moment the market is watching Boeing's production-ramp/cash-flow recovery narrative closely. Cited: Boeing press release 2026-07-20; order composition 60 MAX-10 + 40 MAX-8; Farnborough as a high-visibility catalyst window; lessor orders as a leading indicator of airline-side sentiment.

Catalyst timing: acknowledged the event is 5 days old by 2026-07-25 and any same-day pop has likely already happened; framed the edge as a slower "Farnborough was a good show for Boeing" narrative accumulation into the 2026-08-31 window rather than a hard binary catalyst.

Proposed action: long BA common equity, entry near spot, exit/target around 2026-08-31, rough target +3-6%.

Confidence: 55-60% (moderate).

Data-coverage flag: hit repeated `KeyError: no 1min bar` calling `toa price BA <ts> --provider twelvedata` for 2026-07-20/23/24 — flagged as a live provider/cache gap, not the SPCX-style fresh-IPO pattern, but recommended verifying fillable bars at planned entry/exit before scheduling.

### BEAR (sonnet)

Routine, pre-telegraphed air-show order news — not a tradeable catalyst. Argued Farnborough order announcements are routinely negotiated over months and previewed by trade press ahead of the official release; a 100-unit order from an existing MAX operator is a mix-shift/variant story (first MAX-10 buy), not a volume surprise.

Materiality: Boeing's 737 MAX backlog runs 4,000-5,500+ units; 100 units ≈ 2% of backlog, immaterial to the multi-year revenue outlook. Lessor orders (vs. airline orders) are a weaker signal — speculative, frequently split/deferred/renegotiated. Noted 60 of 100 are MAX-10s, the least-mature variant, pushing delivery/revenue realization further out.

Timing: order dated 2026-07-20, scouted T+3, today T+5; no mechanism ties the stated 2026-08-31 window to any scheduled event tied to this specific order. Priced `toa price BA 2026-07-20T13:30:00Z --provider twelvedata` → $216.18 as a reference point.

What would change mind: evidence of a discontinuous, statistically unusual price/volume reaction specifically timestamped to the release; a credible mechanism for the 8/31 date; evidence of sell-side EPS/delivery estimate revisions off this order.

Confidence: 80% (high) — NO TRADE.

### QUANT (opus)

Pulled real BA 1-min bars via `toa price BA <ts> --provider twelvedata`:

| Date | ~13:35Z | ~19:55Z |
|---|---|---|
| 7/17 (pre-event) | 212.37 | 214.32 |
| 7/20 (event day) | 215.65 | 209.34 |
| 7/21 | 207.98 | 204.92 |
| 7/22 | 206.92 | 208.55 |
| 7/23 (scouted) | 209.45 | 208.19 |
| 7/24 (latest) | 208.79 | 209.37 |

Event day: gapped up ~+0.6% intraday then closed down; further -2.1% next day. Trough 204.92 on 7/21 = -4.4% from the 7/20 open, i.e. the tape moved *against* the bull thesis, not with it.

Base rate: single-customer BA order announcements (ex-large flag orders/defense) carry median |abnormal return| ≈ 0.2-0.4%, sign statistically indistinguishable from zero. No PEAD/drift channel exists because a discounted lessor order generates no EPS revision.

EV calculation: realized σ_daily ≈ 1.6% (later corrected to ≈1.9%, see Round 2) → σ over ~26 trading days to 8/31 ≈ 8-10%. Round-trip cost stack ≈ 11 bps (spread + slippage + fees). Generous-to-bull case (p(up)=0.52, magnitude ±4%): EV_gross +0.16%, EV_net +0.05% — indistinguishable from zero, Sharpe ≈ 0.006. Honest-prior case (p=0.50): EV_net −0.11%, negative. Breakeven requires p(up) ≥ 0.564, a 6.4-point edge nothing in the dossier supports.

Confounder: BA Q2 earnings almost certainly fall inside the 2026-08-31 window — flagged as unverified but structurally important; any hold to 8/31 is effectively an earnings bet, not an order-news bet.

Recommendation: 0% position, NO TRADE (would cap any override at ≤0.25% of book as a pure paper stub).

Confidence: ~75-85% across sub-claims; overall NO-TRADE verdict ~85%.

Data-coverage flag: confirmed the `20:00:00Z` minute has no 1-min bar even for BA (mature/liquid) — an operational gap, not a data-availability gap; `19:55Z`/`13:35Z` resolve cleanly. Recommended any scheduled plan use in-session minute timestamps only.

---

## Round 2 — Rebuttal

### BULL (sonnet)

Conceded directly: the stock fell, not rose, after the event — "I won't rationalize this away... this is disconfirming evidence against the 'order news → immediate positive drift' version of my thesis. I concede that version is dead." Noted the partial 7/22-7/24 recovery but acknowledged it's equally consistent with plain mean reversion as with any bull narrative, and can't be disentangled with available data.

Narrowed surviving claim to: the order is at most "a small positive data point on the delivery/production credibility axis," conceding the bear's "immaterial by unit count" framing is largely fair.

Accepted the earnings-contamination point as decision-relevant, not just a confidence-quibble — holding to 8/31 becomes an earnings bet in an order-news costume, which the Round 1 plan didn't account for.

Updated confidence: 35-40% (down from 55-60%). Updated action: no new directional position, or at most a token residual long explicitly framed as non-conviction/earnings-exposed rather than order-news-driven.

### BEAR (sonnet)

Declined to flip to a short thesis on the drawdown: argued that attributing the fall specifically to the SMBC order, absent headline-level causal evidence, would be the same category error as the bull's original mistake, just sign-flipped — the drawdown is "a fact about the tape that week, not a fact about this dossier's causal mechanism."

Treated the earnings-contamination point as reinforcing, independent grounds for avoiding the trade: any position (long or short) held to 8/31 misattributes P&L to the wrong catalyst, which would corrupt future post-mortem lessons regardless of outcome — a research-integrity argument, not just a risk one.

Minor numeric nit: flagged that quant's Round 1 -2.3%/-2.1% figures may have mixed close-to-close vs. open-to-close conventions (resolved in quant's Round 2 correction below).

Final: NO TRADE, no short case constructed. Confidence: 85% (up from 80%).

### QUANT (opus)

Noted the convergence explicitly but discounted it: bear's fundamental case and quant's statistical case are independent corroboration; bull's Round 1 stance is "an abstention, not a vote" since it was reached without verifiable price data (root-caused to the missing `--provider twelvedata` flag and querying the nonexistent `20:00:00Z` bar rather than `19:59Z`).

Self-correction: re-pulled bars and corrected the Round 1 drawdown estimate from ~4.4% to the verified **-5.29%** open-to-trough (7/20 open 216.18 → 7/21 close 204.74) — flagged explicitly as an error that had favored quant's own conclusion, corrected anyway rather than left standing. Updated daily-return series gives σ_daily ≈ 1.9% (~30% annualized); ~27 sessions to 8/31 implies σ_period ≈ ±10%, before any earnings gap.

Confirmed the last three sessions (7/22-7/24) traded within a 0.32% band — measured zero residual drift, i.e. the move (whatever its sign) had already fully completed.

Considered and explicitly rejected a residual sell-the-news short thesis: acknowledged it is better evidenced than the long (real gap-up-then-fade pattern), but rejected it on (1) timing — the fade had already completed by 7/21-22, entry now would chase a completed move; (2) n=1 sample, no base rate to condition on; (3) identical earnings-contamination problem as the long. Explicitly logged this as "declined on execution-timing grounds, not on absence-of-signal grounds" for the post-mortem record.

Verified the earnings-contamination structural point against the repo's own `2026-07-29-boeing-q2-fy26` dossier (TipRanks-sourced, B-tier): BA Q2 FY26 earnings fall 2026-07-29, inside the 2026-08-31 window — corroborated but not independently confirmed against Boeing IR; flagged as a hard gate if anyone later tries to schedule a plan that dodges earnings by exiting early.

Final: NO TRADE, 0% position. Confidence: 85% (up from ~75-80%), driven by the new zero-drift data point, not by the panel's apparent agreement.

---

## Round 3 — Convergence (synthesizer, opus)

**Hypothesis**
- Statement: The SMBC order is not a tradeable catalyst for BA into 2026-08-31. Three independent objections stack: (1) Materiality — 100 units ≈ 1.8% of Boeing's ~5,500-unit backlog, routine pre-telegraphed air-show news, no EPS-revision channel, base-rate abnormal return 0.2-0.4%, below ~11bps round-trip cost. (2) The realized tape disconfirms the long thesis outright: BA gapped up +0.85% at the 7/20 open, closed lower, fell to a 204.74 trough on 7/21 (-5.29% open-to-trough), recovered to ~209 by 7/24, and traded in a 0.32% band over the last three sessions — i.e., measured zero residual drift; the signal (whatever its sign) was fully paid out by 7/22. (3) Catalyst contamination — BA Q2 FY26 earnings fall 2026-07-29 (TipRanks-sourced, B-tier, corroborated but not independently IR-confirmed), inside the 2026-08-31 window; any position held to 8/31 is an earnings bet mislabeled as an order-news bet, which would corrupt post-mortem attribution regardless of outcome.
- Direction: none
- Confidence: 85

**Plan**
- Ticker: BA
- Action: no_trade (deliberate, unanimous panel convergence — not an omission)
- Entry: n/a — no position
- Exit: n/a — no position
- Expected profit: 0.0% by construction (rejected long's EV was ~0.2-0.4% gross / breakeven-to-negative net of ~11bps costs; rejected short's signal had already decayed to a measured 0.32% band by 7/24)

**Dissent (preserved for post-mortem)**

Whether the -5.29% open-to-trough move on 7/20-7/21 contained a real, correctly-signed sell-the-news short signal declined for the wrong reason. Quant explicitly rejected the short on *execution-timing* grounds (move already paid out by 7/22; n=1 sample; earnings collision) — NOT on absence-of-signal grounds. Bear rejected the short one level deeper, arguing no headline-level evidence links the drawdown to the order at all (could be broad-market/unrelated Boeing news), which would make even quant's "real signal, unplayable" framing an attribution error. These were never reconciled. Post-mortem test: (a) check primary sources for a non-SMBC driver of the 7/20-7/21 decline — if found, bear was right and any sell-the-news rule built from this episode is overfit to n=1; (b) independently confirm the 2026-07-29 Q2 earnings date against Boeing IR, since the contamination argument was load-bearing and rests on a B-tier source; (c) if BA drifts lower into 8/31, that does not vindicate a short declined on timing/contamination grounds — grade the reasoning, not the outcome.

**Operational notes carried forward**
- `toa price <ticker> <ts>` silently returns stub data unless `--provider twelvedata` is passed.
- There is no `20:00:00Z` 1-min bar for BA (or likely any US-listed ticker) — the last bar of the session is `19:59Z`. This caused the bull's Round 1 price-verification failure, not a data outage.
