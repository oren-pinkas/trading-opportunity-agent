# Debate Transcript — ZION Q2 FY26 Earnings

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Strategy: three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus).
Synthesizer: opus. Debate run: 2026-07-22, ~19:34-19:44Z. Event: ZION reported Q2 FY26
earnings after the close on 2026-07-20; debate occurred two trading sessions later.

Institutional lessons injected (via `toa lessons-relevant --type earnings --tickers ZION`):
see dossier research notes; key ones applied: (1) a catalyst that already drove the move is
priced in, do not re-bet it as a fresh trigger (DAL); (2) when the strongest unrebutted
dissent aligns with the quant's own EV math, synthesize to NO-TRADE rather than a
quarter-size position (DAL); (3) when directional EV is ~0, log NO TRADE rather than
manufacture a coin-flip position "for the learning loop" (LEVI); (4) confidence <=~45 with
an un-hedgeable tail and low net EV is a no-trade filter, express only via defined-risk
options if at all (NKE).

Note on data access: each persona subagent ran in a sandbox with no live web access
(outbound HTTP/curl denied, no WebSearch tool). Each independently used `toa price ZION
<timestamp> --provider twelvedata` for price anchoring, and each disclosed the gap
transparently rather than fabricating fundamentals. The orchestrator (this session) fetched
real Q2 fundamentals and analyst reaction via WebSearch between Round 1 and Round 2 and fed
them to all three personas for Round 2.

---

## Round 1 — Independent Research (parallel, personas blind to each other)

### Bull (sonnet)

Disclosed no live web access; anchored on two `toa price` pulls: 2026-07-22T13:35Z =
$68.45, 2026-07-22T19:00Z = $70.05 (source: twelvedata via `toa price`), reading continued
intraday strength two sessions post-print as consistent with post-earnings-announcement
drift (PEAD) off a "clean beat" inferred from price action alone (explicitly flagged as
unverified). Proposed: long common stock at ~$70.05, 4-6 week PEAD-style hold, targeting
analyst estimate revisions/price-target hikes, stop below the (unretrieved) pre-earnings
base. Risks acknowledged: could not verify actual reported numbers; CRE concentration is a
real structural risk; regional-bank macro beta; only two price data points.

### Bear (sonnet)

Disclosed no live web access. Price series: 2026-07-20T13:30Z = $72.40 (pre-reaction),
2026-07-21T13:30Z = $68.02 (first reaction session, -6.0%), 2026-07-22T19:00Z = $70.05
(partial +3.0% bounce, still -3.2% net). Read: "market didn't like something in the print
or the call" — not the shape of a clean beat-and-rip. Named CRE credit deterioration and
NIM/deposit-cost stickiness as the specific disqualifying risks, plus the possibility of a
forward guidance cut and regional-bank sector correlation risk. Concluded: no clean edge on
either side without the real fundamental driver; the ~3% bounce is as consistent with
short-covering noise as with overreaction-correcting. Disconfirming scenario named: a
confirmed beat with stable/improving NIM and flat/declining CRE charge-offs, with the drop
attributable to something transient — which would flip the bounce into legitimate mean
reversion.

### Quant (opus)

Disclosed no live web access. Price series: 2026-07-17T19:45Z = $72.07 (pre-earnings),
2026-07-20T19:45Z = $71.655 (still pre-reaction, reports after close), 2026-07-21T19:45Z =
$69.035 (-3.66% reaction day), 2026-07-22T19:30Z = $69.92 (+1.28% bounce). Read: a modestly
negative print, mostly digested, with roughly a third of the gap already retraced —
base-rate view that the easy PEAD money is in the first 1-2 sessions, which have passed, and
that chasing a short on day+2 into a live bounce is negative selection. Explicit EV: both
long and short theses net to ~0 to slightly negative (long +0.20% gross / ~0.00% net; short
-0.20% gross / ~-0.40% net) after ~0.20% round-trip costs, at ~50-55% directional
confidence either way — no informational edge, since the surprise is already in the tape and
the underlying numbers were unverifiable. Recommendation: NO TRADE, applying the LEVI/DAL
lessons against manufacturing a coin-flip position; if expressed at all, defined-risk options
only, never naked directional.

---

## Orchestrator fundamentals check (between Round 1 and Round 2)

Real data fetched via WebSearch (all accessed 2026-07-22):

- Adjusted EPS $1.74 — beats one cited consensus of $1.56; misses a different cited
  consensus of $1.8453 (sources disagree on which consensus figure is authoritative, a
  known messiness in bank EPS comparisons around one-time items). ([Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-zions-beats-q2-2026-eps-forecast-as-shares-fall-after-hours-93CH-4801779))
- GAAP EPS $3.05, net earnings $452M, includes a $215M gain on Visa Class B-1 share
  liquidation plus a $37M unrealized SBIC gain — over half of headline net earnings from
  non-recurring items. ([StockTitan](https://www.stocktitan.net/news/ZION/zions-bancorporation-national-association-reports-second-quarter-zm7r851eujuw.html), [BigGo Finance](https://finance.biggo.com/news/0365628a-f624-4e1c-89cd-b125e7b67e80))
- Revenue ~$878-879M, roughly in line to slightly below ~$919.5M some estimates had — a
  "revenue miss" narrative in some outlets. ([ChartMill](https://www.chartmill.com/news/ZION/Chartmill-51219-Zions-Bancorp-NASDAQZION-Misses-Q2-2026-Estimates-Stock-Falls-on-Earnings-and-Revenue-Shortfall))
- NIM 3.27%, up from 3.17% a year earlier; NII $677M +4% YoY; loan growth +4.7%
  annualized. ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/zions-bancorporation-n-q2-earnings-230325654.html))
- Credit quality: net charge-offs 0.06% annualized, NPAs $298M / 0.48% of loans, CET1 up to
  11.8%. ([Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/zions-bancorporation-n-q2-earnings-230325654.html))
- Stock fell ~2.63% in after-hours trading on the print.
- RBC raised PT $74→$76, TD Cowen raised to $73 (kept Hold), Baird raised to $75 (kept
  Neutral) — all three maintained Hold/Neutral ratings despite the target hikes.
  ([DailyPolitical](https://www.dailypolitical.com/2026/07/21/zions-bancorporation-n-a-nasdaqzion-given-new-76-00-price-target-at-royal-bank-of-canada.html), [MarketsDaily](https://www.themarketsdaily.com/2026/07/21/wells-fargo-company-forecasts-strong-price-appreciation-for-zions-bancorporation-n-a-nasdaqzion-stock.html))
- MarketBeat consensus: Hold rating, consensus price target $70.53.

---

## Round 2 — Rebuttal (parallel, each shown the other two Round 1 positions plus real data)

### Bull rebuttal

Conceded the Round 1 PEAD/momentum framing was weak (built on price-continuation proxy
alone) but reframed: the dossier's own stated thesis (deposit costs, CRE credit quality)
resolved clearly favorably — NIM expansion, near-zero charge-offs, low NPAs, higher CET1 are
exactly what the event was supposed to read on, and they beat. Attributed the negative
after-hours/next-day reaction to optics: a contested revenue-consensus comparison and a GAAP
EPS number flattered by one-time Visa/SBIC gains, not real deterioration — a classic
overreaction-to-headline setup, corroborated by three sell-side target hikes in the same news
cycle. Conceded the bear's "don't size blind to the cause" point directly, and conceded the
quant's price-only EV-neutral read was defensible given only price data. Revised action:
downgraded from full-conviction momentum long to a smaller, defined-risk long — preferred a
$70/$75 call spread (30-45 DTE) over common stock, citing the fresh post-print target
average (~$74.7, i.e. RBC $76 + TD Cowen $73 + Baird $75, avg) as the more relevant
Street-implied upside (+6.6% from ~$70.05) versus the stale $70.53 blended consensus. If using
common stock instead: smaller size, entry ~$70, target zone $73-76, stop below $68.02.
Disconfirming evidence named: a confirmed forward guidance cut, CRE sub-segment
deterioration not visible in headline NPA/NCO figures, an outright rating downgrade from any
of the three shops that raised targets, price breaking and holding below $68.02 on volume, or
peer regional banks showing CRE/NIM deterioration this cycle.

### Bear rebuttal

Explicitly withdrew the CRE-credit-deterioration and NIM/deposit-cost-compression claims as
directly falsified by the real data (NIM up 10bp, charge-offs near zero, NPAs low, CET1
improved — "I named the wrong mechanism"). Identified the real mechanism behind the
after-hours drop as earnings quality: >55% of headline net earnings from non-recurring Visa/
SBIC gains, plus a contested/light core revenue figure — "beat by accounting, missed by
economics." Assessed this as a real but low-conviction risk (sentiment/multiple risk, not
solvency/credit risk) — Q3 will lap a harder comp once the one-time gains roll off, which
argues against chasing the bull's momentum/drift framing but does not rise to a standalone
short thesis given how clean credit and capital actually are. Noted all three target hikes
kept Hold/Neutral ratings (target moved, conviction did not) as evidence the market is
pricing exactly this ambivalence, not mispricing it. Converged explicitly to NO TRADE,
agreeing with the quant over the bull.

### Quant rebuttal

Reconciled the three independently-pulled price series (absolute-level noise across
providers/timestamps, but consistent shape: ~-3% net move with a live bounce by Jul 22).
Re-ran EV with real fundamentals: identified that a one-time-gain-driven "beat" produces no
forward core-EPS revision engine — direct evidence being that all three sell-side target
hikes came with maintained Hold/Neutral ratings (targets nudged, conviction didn't), which
specifically undermines the bull's PEAD/drift thesis (PEAD requires genuine estimate
revisions to work). Re-run: long ≈ -0.39% net EV (P(up)=0.51, E[up]=+3.0%, P(down)=0.49,
E[down]=-3.5%), short ≈ -0.38% net EV (P(down)=0.47, P(up)=0.53, both E=3.0%) — both fail
after ~0.20% round-trip costs. Flagged price ($69.92) sitting within +0.76-0.9% of the
consensus target ($70.53) as the single cleanest quantitative NO-TRADE argument: an
efficient-market fixed point already synthesizing the good-core/weak-optics/Hold-rated
picture. Final: NO TRADE, direction none, confidence-in-no-trade 74/100, directional
confidence ~50-51/100 (genuine coin flip). Would fund no options structure either — unlike
the NKE lesson's carve-out for a compensated tail, no positive-EV structure exists here.

---

## Round 3 — Convergence (synthesizer, opus)

**hypothesis:**
- statement: ZION's Q2 FY26 print is a two-sided non-event by debate time (Jul 22, two
  sessions post-print). Core fundamentals genuinely beat (NIM 3.27% up YoY, net charge-offs
  0.06%, NPAs 0.48%, CET1 11.8%), but the headline EPS beat is >55% driven by non-recurring
  items ($215M Visa + $37M SBIC gains), producing no forward core-EPS revision engine —
  confirmed by three sell-side shops raising targets while maintaining Hold/Neutral ratings.
  Price (~$69.92-70.05) sits within ~0.8% of the ~$70.53 consensus target: an
  efficient-market fixed point. Cost-adjusted EV is negative in both directions (long
  ~-0.39%, short ~-0.38% net of ~0.20% costs), and no positive-EV options structure exists.
- direction: none
- confidence: 76 (confidence in the NO-TRADE conclusion; directional confidence ~50/100)

**plan:**
- ticker: ZION, action: no_trade, entry/exit: null, expected_profit_pct: 0
- Reopen only if ALL of: (1) a genuine core-EPS (ex one-time gains) consensus revision
  higher, evidenced by an actual rating upgrade, not just a target bump; (2) price dislocates
  >3-4% from the ~$70.5 consensus target; (3) a fundable options structure with positive
  expected value exists at current IV/pricing.

**dissent:** The strongest unresolved disagreement is a mechanism dispute over whether
post-print price-target increases with unchanged ratings constitute a real forward catalyst.
Bull: yes — analysts marked the whole distribution higher (avg ~$74.7), that's a real signal
to fade the optics-driven selloff toward. Quant/bear: no — a target hike without a
rating/conviction upgrade is not a tradeable revision; PEAD/drift requires genuine estimate
revisions, which a one-time-gain-inflated beat does not generate. This is genuinely
unfalsifiable from current data (bull cannot point to a core-EPS revision higher; quant
cannot rule out the target cluster leading price over 4-6 weeks). Synthesizer sided with
quant/bear per the institutional lesson that when the strongest unrebutted dissent aligns
with the quant's own EV math, synthesize to NO-TRADE. Post-mortem check: did ZION drift
toward the $74-76 target cluster over the following 4-6 weeks, or stay pinned near $70? That
answer directly adjudicates the bull vs. quant crux.
