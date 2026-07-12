---
id: 2026-07-09-freenome-pcsc-vote
title: Freenome/PCSC SPAC merger vote
status: researched
created: '2026-07-08T15:28:00Z'
event:
  type: economic
  summary: Perceptive Capital Solutions Corp (PCSC) shareholders vote Jul 9 on the
    business combination with early-cancer-detection company Freenome, which would
    close and rename the company Freenome Inc.
  impact_window: '2026-07-09'
tickers:
- PCSC
sources:
- title: 'PCSC (Nasdaq: PCSC) sets July 9, 2026 vote on Freenome SPAC merger after
    S-4 effectiveness'
  url: https://www.stocktitan.net/sec-filings/PCSC/8-k-perceptive-capital-solutions-corp-reports-material-event-de27c07068ed.html
  accessed_at: '2026-07-08T15:28:00Z'
hypothesis:
  statement: All three personas independently converged on no_trade, and the
    decisive evidence is data integrity, not directional edge. The price feed
    (tagged "stub:deterministic") is economically impossible for a pre-vote
    SPAC common - it prints $247.31 on 2026-07-08 versus the ~$10-11 trust
    NAV a real SPAC trades near, then $486.49 on vote day and $184.02 on
    2026-07-11 - so every node in the series is rejected as fabricated,
    leaving no valid anchor for entry, stop, or EV. The vote outcome itself
    is a resolved-but-unverifiable binary (no web access, single stale
    StockTitan 8-K, no confirmation the deal closed or that PCSC is still
    the live ticker), so even the base-rate structural view (~95% approval
    given a scheduled vote, ~80% high-redemption, negative median de-SPAC
    drift of -30% to -50%, naive-long EV ~-15.5% gross / -17% to -18% net)
    is unfillable. No long (dead/stale catalyst, no anchor) and no short
    (unconfirmed close, no borrow/float data, unusable feed).
  direction: no_trade
  confidence: 96
plan:
  ticker: PCSC
  action: no_trade
  entry: null
  exit: null
  expected_profit_pct: 0
  note: No long - the only bull angle (post-close re-rate) is killed by
    negative median de-SPAC drift and there is no valid price anchor, since
    a $247.31 pre-vote SPAC print is ~24x trust NAV and flags the entire
    feed as synthetic. No short - despite base rates directionally favoring
    a fade on the "deal closes" branch, the trade is unfillable - outcome
    unverifiable, live ticker/options chain unconfirmed, no borrow/float/
    redemption data, and the feed is fictional at every node. Nothing to
    trade until real data exists.
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
  dissent: The apparent 3-way convergence is partly a shared blind spot, not
    three independent confirmations - all three personas abstain on the same
    single unverified fact (did the vote pass?). Separately, Bull's thin-float
    squeeze-watch and Quant's short-the-confirmed-close point at opposite
    tails of the same event (population median-drift vs. thin-float squeeze
    risk for this specific SoftBank/Roche-backed name); undecidable without
    real post-close data (confirmed outcome, redemption %, borrow/float).
  lessons_applied: []
  last_updated: '2026-07-12T07:34:00Z'
---

## Scouted 2026-07-08T15:28:00Z

## Researched 2026-07-12T07:34:00Z

Three-round panel debate (bull/bear/quant) concluded **no_trade** at 96/100
confidence. All three personas converged not just on direction but on
mechanism: the price feed is economically impossible for a pre-vote SPAC
(Bull's catch - $247.31 vs. ~$10-11 trust NAV), and the vote outcome is a
resolved-but-unverifiable binary in this environment. Bear flagged that the
convergence is partly a shared blind spot rather than independent
corroboration. A fade-vs-squeeze tension on the post-close name is logged
as a future, gated hypothesis, not a position. Full transcript: `transcript.md`.
