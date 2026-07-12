---
id: 2026-07-12-amazon-globalstar-acquisition
title: Amazon's $11.6B Globalstar acquisition under active FCC review
status: researched
created: '2026-07-12T13:03:15Z'
event:
  type: regulatory
  summary: Amazon's deal to buy Globalstar (GSAT) for $90/share (~$11.6B) is under
    FCC review after the July 6 public comment deadline, with close targeted for 2027.
  impact_window: '2027-01-01'
tickers:
- AMZN
- GSAT
sources:
- title: FCC Kicks Off Review of Amazon/Globalstar Deal (Via Satellite)
  url: https://www.satellitetoday.com/connectivity/2026/06/08/fcc-kicks-off-review-of-amazon-globalstar-deal/
  accessed_at: '2026-07-12T13:03:15Z'
hypothesis:
  statement: >-
    The GSAT/AMZN price feed is a deterministic stub (source is
    stub:deterministic, fetched_at null; GSAT printed $210.79 on 2026-07-12,
    ~2.3x the $90 all-cash deal price) and cannot support a sized entry.
    Independent of the data problem, a long GSAT merger-arb is not the
    correct trade under any interpretation — if the feed is corrupted, EV is
    uncomputable; if the "true" price sits near a plausible clean level
    (~$87), the arb spread (+3.45%) is EV-negative even before regulatory
    stress (-4.5% base case, -7.5% to -11.4% once deal-specific
    spectrum/national-security risk is applied), requiring a ~99.6%
    post-cost breakeven close probability that no FCC spectrum/national-security
    review clears as a base rate; and if the feed is somehow real (GSAT
    genuinely trading near $210), the only coherent trade would be short
    toward the $90 offer, not long. All three personas (bull, bear, quant)
    converged on standing aside.
  direction: no_trade
  confidence: 82
plan:
  ticker: GSAT
  action: no_trade
  entry: null
  exit: null
  expected_profit_pct: 0
  note: >-
    No long — the arb spread is EV-negative even under clean-price
    assumptions given the deal's spectrum/Kuiper-vertical-adjacency and
    national-security-adjacent FCC review profile (P(break) revised to
    0.20-0.25, break-downside -35% to -40%). No short — the price feed
    cannot be trusted to confirm GSAT is genuinely trading above $90, so a
    convergence-to-$90 short cannot be sized either. Revisit only if (1) the
    GSAT/AMZN price feed is independently reconciled against a real,
    non-stub market quote, (2) the FCC docket (comments filed by the
    2026-07-06 deadline, any shot-clock pause or conditions) becomes
    visible, and (3) either a clean sub-$90 price shows spread of 8-10% or
    more annualized with empirical (not narrative) P(close) above 0.92-0.95
    from comparable FCC spectrum-deal base rates, or a confirmed above-$90
    price supports a small, stopped short toward the offer price.
research:
  strategy: three-round-panel
  personas:
  - bull
  - bear
  - quant
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  dissent: >-
    Bull vs. Bear/Quant over the shape of the break-downside distribution —
    Bull proposed a blended -17% to -19% (price-cut / clean break /
    acrimonious break scenarios) that would narrow or close the EV gap on a
    future clean entry, while Bear and Quant argued the deal's
    spectrum/Kuiper-adjacency and national-security-review profile justifies
    a wider -35% to -40% downside and a higher 0.20-0.25 break probability.
    Unresolved because the price feed is unusable, so there is no clean
    spread or comparable-deal base rate to arbitrate whose distribution is
    right. Secondarily, the Quant's structural point that a genuinely
    above-$90 price implies a SHORT (not the Bull's original long) was never
    directly rebutted by the Bull — it was overtaken by the shared
    feed-is-broken conclusion rather than resolved.
  lessons_applied: []
  last_updated: '2026-07-12T17:03:00Z'
---

## Scouted 2026-07-12T13:03:15Z

## Researched 2026-07-12T17:03:00Z

Three-round panel debate (bull/sonnet, bear/sonnet, quant/opus) concluded
**no_trade** at 82/100 confidence. All three personas independently flagged
the `toa price` feed for GSAT/AMZN as a deterministic stub
(`source: stub:deterministic`, `fetched_at: null`) — GSAT printed $210.79,
$191.64, and $254.95 across three timestamps, all 2-2.8x ABOVE the $90/share
all-cash deal price, which is arithmetically incoherent for a pending cash
acquisition. Quant's key structural finding: under every interpretation of
the (probably broken) price data — corrupted feed, clean price near $87, or
feed somehow real near $210 — a LONG GSAT position is not the correct trade;
it is either uncomputable, EV-negative (a +3.45% spread cannot survive a
14-25% break probability with -30% to -40% downside, needing a ~99.6%
post-cost breakeven close probability no spectrum/national-security FCC
review clears as a base rate), or actually a short setup. Bull started at
58/100 favoring immediate entry, revised down to 42/100 (conditional,
sized-down entry pending price verification and docket visibility) after
conceding the price-feed point and the quant's EV math. Bear rose from 62/100
to 73/100 as the quant's mechanical EV framework corroborated the bear's
qualitative spectrum/national-security regulatory read from an independent
angle. Quant rose from 80/100 to 85/100. See `transcript.md` for the full
three-round debate with citations.
