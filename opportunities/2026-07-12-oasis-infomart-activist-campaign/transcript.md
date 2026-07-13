# Research Debate Transcript — 2026-07-12-oasis-infomart-activist-campaign (2492.T)

Strategy: `debate-three-round-panel`. Personas: bull (sonnet), bear (sonnet),
quant (opus). Synthesizer: opus. PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL
ADVICE.

## Event

Oasis Management disclosed a 5.07% stake in Japan's Infomart (2492.T, Tokyo
Stock Exchange) and is pushing for asset disposals and business
discontinuation, with further activist proposals expected within 12 months.
Impact window: 2026-07-31. Dossier created 2026-07-12T22:16:05Z. Source:
[BigGo Finance](https://finance.biggo.com/news/fc73fcac-45ed-4110-b4ec-cdb8b42f0200).

## Institutional lessons injected (event.type=economic)

1. Anchor entry to a live pre-event quote, not the research-day price; if the
   live price has drifted >~0.5-1% from the plan anchor, re-derive
   targets/EV or void the trade rather than filling blind. (`2026-07-01-ism-mfg`)
2. When the thesis is "catalyst reprices X higher" and X has already rallied
   to a high before the event, treat the move as priced-in: fade or shrink,
   don't chase the entry. (`2026-07-01-ism-mfg`)
3. Skip trades whose only positive-EV path is a pre-market conditional entry
   the harness cannot fill. (`2026-07-02-june-jobs`)
4. Require a differentiated surprise vs. consensus before trading a data
   print. (`2026-07-02-june-jobs`)

## Price data note

`toa price 2492.T <ts> --provider twelvedata` returns `MarketDataUnavailable`
(HTTP 404) for every symbol format tried (`2492.T`, `TSE:2492`, `2492`) and
every date tried (2026-07-10, 2026-07-13). There is **no working live/historical
price feed for this ticker in this environment.** The only number available is
a second-hand, sourced print — Infomart popped +19.8% to ¥479 on the initial
disclosure per BigGo Finance's own citation of the July 2 filing reaction —
which is ~11 days stale by the time of this debate and was never treated as a
fillable anchor by the panel (see dissent below).

---

## Round 1 — Independent Opening Positions

### Bull (catalyst-hunter)

Did actual research (WebSearch/WebFetch) and found: Infomart popped +19.8% to
¥479 on the initial disclosure (BigGo Finance, citing the July 2 filing
reaction). Oasis's letter explicitly proposes asset disposal, business
discontinuation, **and** a 12-month roadmap including director
appointment/dismissal, delisting from TSE, and soliciting a third-party
majority-stake acquisition — described by BigGo as "unusually aggressive" for
a 5% holder. Oasis (Seth Fischer) is a repeat, resourced Japan activist
(Fujitec, PanaHome, Tokyo Dome, Nintendo engagement) currently running a
hot-handed parallel 2026 campaign at Kadokawa (stake escalating
8.86%→13.76%→15.25%, pushing to oust the CEO/restructure FromSoftware),
litigating against Kusuri no Aoki (¥7.2bn suit), and has stated 7 Japan
activist targets lined up for proxy season. Infomart has a real moat: #1 B2B
food-ordering platform in Japan, ~2.5 trillion yen GTV, ~4,100 buyer
companies/~46,000 seller companies. No confirmed ADR/options exist — long JPX
equity is the only clean instrument.

**Proposed action:** Long 2492.T, small-to-moderate toehold (~1-2% of book
pending a real quote), not chasing since ¥479 already reflects the pop; add on
formal proposal filings/buyout approach/further stake increases; partial
profits into any binary resolution event; full exit on an Oasis stake
reduction or successful company defenses. Flagged explicitly: no live price
feed, no confirmed P/B, no confirmed absence of takeover defenses, no
certainty July 31 is a real event date.

### Bear (skeptic)

The FIEA 5% threshold filing is mandatory/compliance-driven disclosure, not
discretionary PR timing — Japanese small/mid-caps routinely gap 5-15%+ on such
filings. Could not confirm current price (data gap); treated that as
disqualifying per the anchor-to-live-quote lesson — argued this alone should
void the trade. Oasis's track record (flagged as recalled/unverified): mixed —
many Oasis Japan campaigns drag multi-year, ending in partial concessions
(buybacks, governance tweaks) rather than the full "asset
disposal/business discontinuation" ask, historically the hardest ask to win in
Japan; cross-shareholdings/friendly banks blunt voting power even
post-TSE-reform. Concrete failure modes: management resistance as the modal
first response, possible cross-shareholder blocs (unverified for Infomart),
proxy-fight/AGM timing mismatch (if March FYE, next AGM ~June 2027, ~11 months
out, no confirmed EGM), thin liquidity risk on exit if the pop fades. No
scheduled structural event by July 31 — the "12 months" catalyst has no fixed
date in the stated window.

**Bottom line:** do not trade the 19-day window; if traded at all, size as a
multi-quarter position with confirmed live pricing first.

### Quant (pragmatist)

Base rate for a positive announcement-window reaction on a >5% JP activist
stake disclosure ~65-75%, typical pop +3-8% (occasionally +10-15%) — already
fired by entry time. Base rate for a campaign achieving its stated demands
within 12 months ~20-35%. Assumed residual incremental edge for a late entrant
~0% to +3%, roughly symmetric with give-back risk (pops fade 30-50% within a
week absent follow-through). Distinguished two trades: short-dated to July 31
(no scheduled catalyst, EV~0 before costs, negative after) vs. a 12-month hold
(the only horizon with a real catalyst, but illiquid/FX-exposed/low-probability
-on-any-date — a different trade than the harness supports). Flagged no known
US ADR and the 404'ing price feed — "no anchor price = void the trade" per
institutional lesson. FX risk (JPY stock, USD book) roughly the same magnitude
as the residual equity edge.

**Explicit EV:** P(up)=45%/mag+2.5%, P(down/flat)=55%/mag-3.0% → gross
EV=-0.525%; net of ~0.5% slippage + ~0.3% FX drag ≈ -1.3%. Even flipping to
55/45, gross EV only +0.15%, doesn't survive costs.

**Recommendation:** NO TRADE, size=0.

---

## Round 2 — Rebuttals

### Bull

Argued the ¥479 sourced print is a legitimate anchor (not a blackout) — a
dated, sourced number from the dossier's own primary source is what any desk
would use absent a live tick, so the right response is smaller size + a limit
collared around the known print, not zero. Argued Oasis's disclosed
multi-step roadmap plus demonstrated real-time follow-through at Kadokawa
raises the probability of *some* incremental disclosure/catalyst inside a
3-week window above quant's static generic model, while conceding no step has
a *confirmed* date in the July 31 window. Conceded bear's AGM-gap point is the
weakest bear leg, since Oasis creates interim catalysts that don't wait for
scheduled AGMs.

**Concessions:** cut proposed toehold from ~1-2% to ~0.5-1% of book; require a
limit order collared around the last known ¥479 print with a drift buffer
rather than a market order; conceded the pure July-31 fast-flip thesis is
weak — reframed explicitly as a **12-month campaign-length position, not a
July 31 trade**; conceded that a live quote showing the stock already
round-tripped/gone negative since ¥479 would materially weaken the case.

### Bear

Pushed back that the ¥479 print "relocates" the data gap rather than fixing
it — a second-hand citation of a citation, ~11 days stale, that doesn't tell
us today's cost of entry; called out bull's own words ("not chasing since
¥479 already reflects pop") as an implicit admission the current price is
unknown. Raised the "achieves full demands within 12mo" probability only
modestly, 20-35% → 25-40%, distinguishing it from "achieves *some*
concession," now put at 40-50% — escalation/effort (Kadokawa) is evidence of
seriousness of ask, not evidence of probability of winning the *hard* ask.
Cited Fujitec as Oasis's cleanest win — took 2+ years, ended in a
board-seat/governance settlement, not the harder ask being made here. Argued
quant's probabilities are now *less* defensible post-bull's-research, since
the confirmed +19.8% (vs. quant's generic 3-8%) means more of the move is
spent and the fade tail is larger. Named the worst case explicitly: buying
blind into either an unpriced second pop from an unseen follow-on filing, or a
stock that's already round-tripped back toward pre-filing levels after a
management defense.

**Bottom line unchanged:** size=0 for the July 31 window; multi-quarter
position only after (a) a live quote, (b) resolution of the 11-day
information gap, (c) at least one concrete near-term binding event.

### Quant

Stated explicitly that the confirmed +19.8% pop (vs. quant's own generic
3-8% prior) makes the late-long case *worse*, not better — a bigger pop means
more of the re-rating is already captured, and the give-back cushion above any
entry near ¥479 is larger; the stock must re-rate *further* from an
already-elevated, market-aware base. Conceded a real Bayesian update on
activist *follow-through* (Kadokawa) — raised P(Oasis actively escalates for
12mo) to 70-80% — but held that this is a different node from P(board
concedes the full ask), moved only modestly to 25-40%, since escalation ≠
winning and board entrenchment/cross-holdings are outcome-side constraints
roughly orthogonal to activist quality.

**Recomputed EV:** P(up)=40%/mag+2.5%, P(down/flat)=60%/mag-3.5% → gross
EV=-1.1%; net of ~0.5% slippage + ~0.3% FX drag ≈ -1.9% — worse than Round 1.
Framework point: "a strong narrative can never substitute for a fillable,
verifiable price" — the missing live quote is a categorical gate, not a
tiebreaker.

**Bottom line unchanged:** NO TRADE, size=0; new info strengthens the case
for zero.

---

## Round 3 — Synthesis (opus)

**Hypothesis:** Oasis's disclosed 5.07% stake and unusually aggressive
multi-step roadmap (asset disposal, business discontinuation, TSE delisting,
third-party buyer solicitation, board changes) at Infomart is a genuine,
high-quality catalyst on a **12-month campaign horizon**, backed by a
resourced, actively-escalating operator (Kadokawa precedent) against a
real-moat B2B platform asset. But the initial +19.8% disclosure pop to ¥479 is
already spent, there is no scheduled binding event inside the 2026-07-31
impact window, and the current entry price is unknown/unfillable — so the
near-term directional edge is negative-to-nil after costs. Direction:
**no_trade**. Confidence: **82**.

**Plan:** `no_trade`. Three independent gates fire simultaneously: (1)
operational — no working price feed for 2492.T in any format/date, so the
trade is non-executable/non-fillable in this environment, full stop; (2)
catalyst timing — the real catalyst lives on a 12-month horizon with no
confirmed dated event by 2026-07-31; (3) EV — quant's updated short-window EV
is negative (gross ≈ -1.1%, net ≈ -1.9%), made *worse*, not better, by the
confirmed large pop. Convergence: 2 of 3 personas (bear, quant) reached
size=0 even after seeing bull's genuinely strong research, and bull's own
final position is explicitly reframed as a 12-month position, not a July-31
trade — no persona actually advocates a trade in the stated window.

**Conditions to re-open:** (a) a live, fillable quote for 2492.T restored in
the harness (categorical gate); (b) confirmation of where the stock sits
relative to ¥479 — if it has faded toward ¥400-420 with a working feed, the
trade inverts into "buy the fade with a real anchor" on the 12-month thesis
(quant's stated flip condition); (c) at least one concrete near-term binding
catalyst with a date, or explicit re-scoping of this dossier to a multi-quarter
horizon. **Suggested re-review: 2026-08-11**, or sooner on any Oasis follow-on
filing/buyout approach/stake change headline.

**Dissent (post-mortem gold):** Whether the confirmed +19.8% pop and
Kadokawa-proven follow-through raise or lower the probability-weighted payoff
of entering now. Bull: demonstrated real-time escalation raises the odds of
*some* incremental catalyst inside even a short window, justifying a small
collared toehold. Quant/Bear: escalation is evidence of seriousness of ask,
not of probability of winning the hard ask, and a larger already-fired pop
mechanically means more edge is spent and the fade tail is larger. Two
distinct probability nodes were never reconciled: P(Oasis actively
escalates/sustains pressure for 12mo) ≈ 70-80% (all agree, updated up) vs.
P(board concedes the full hard ask within 12mo) ≈ 25-40% (moved only
modestly, orthogonal to activist quality). Post-mortem should test which node
actually drove Infomart's price path after 2026-07-12 — re-rate further on
*escalation activity* (bull's mechanism), or fade/stall pending an *outcome
that never arrived in-window* (quant/bear's mechanism).

---

*PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.*
