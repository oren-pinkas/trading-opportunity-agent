---
id: 2026-07-24-blackstone-mortgage-earnings
title: Blackstone Mortgage Trust (BXMT) Q2 earnings July 28
status: researched
created: '2026-07-24T00:13:06Z'
event:
  type: earnings
  summary: Commercial mortgage REIT releases Q2 2026 results Jul 28 after close, a
    read on CRE credit quality amid elevated rates
  impact_window: '2026-07-29'
tickers:
- BXMT
sources:
- title: 'GuruFocus: Blackstone Mortgage Trust to Release Q2 Earnings'
  url: https://www.gurufocus.com/news/8958083/blackstone-mortgage-trust-to-release-q2-earnings-amid-market-challenges
  accessed_at: '2026-07-24T00:13:06Z'
hypothesis:
  statement: No executable event edge exists in BXMT through the Q2 2026 print.
    The stock's steady decline of about 16.9 percent from the 2026-04-15 high
    (USD 20.11) to the 2026-07-24 close (USD 16.715), at roughly 15 percent
    annualized realized volatility, reflects orderly credit and book-value
    repricing rather than a dislocation, so neither "bad news is priced in"
    nor "falling knife" alone is decisive. Under every probability and
    magnitude combination the panel tested, net expected value after
    round-trip costs rounds to zero on both sides (net EV long about minus
    0.61 percent, net EV short about plus 0.01 percent; under a bear-tilted
    case, minus 0.65 percent and plus 0.05 percent respectively). The adverse tail
    (an 8 percent chance of a dividend-cut announcement driving roughly a
    9 percent one-day drop, given the payout was already reset once to about
    USD 0.47 per share) sits at roughly a 30 to 1 tail-to-edge ratio against
    the available gross edge, about 4 times the institutional 7-8x no-trade
    threshold. A short would need P(dividend cut) near 22.5 percent, about 3
    times the panel's prior, to clear a plus 2 percent net EV bar; nothing in
    the price drift alone supports that. A defined-risk put priced against
    the panel's own distribution is the worst instrument on the table (EV
    roughly minus 58 to minus 66 percent of premium, breakeven near P(cut)
    about 42 percent), so it is not a safer substitute for a short.
  direction: none
  confidence: 20
plan:
  ticker: BXMT
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0.0
research:
  strategy: debate-three-round-panel
  personas:
  - bull
  - bear
  - quant
  models:
    bull: sonnet
    bear: sonnet
    quant: opus
    synthesizer: opus
  dissent: 'The strongest unresolved disagreement is the magnitude of the
    upside tail. The bull argued the beat or benign move is roughly 4-5
    percent, not the quant''s 3.0 percent, on relief-rally-off-a-compressed-base
    logic: after a roughly 17 percent drift lower, positioning is one-sided,
    so "not worse" mechanically squeezes harder than a normal-base beat
    would. The quant tested this by applying the same compressed-base logic
    symmetrically to the downside, which left net EV unchanged within noise
    - but the bull never conceded the symmetry is legitimate, arguing the
    asymmetry (more room to rally on relief than to fall on confirmation) is
    real, not assumed away. Neither side could settle it because the arbiter
    would be the options market (implied move and put or call skew), and the
    panel had no options pricing data at all - the same gap that forced the
    bear''s defined-risk put idea to remain a conditional override pending
    real premium data nobody had. Post-mortem should check whether the
    realized 2026-07-29 reaction to a benign print exceeded plus 3 percent,
    which would support the bull''s asymmetry and put the quant''s symmetric-
    adjustment default under scrutiny as a systematic EV-flattener. Also
    flagged: the dossier''s impact_window originally read 2026-07-28, but
    BXMT reports after that day''s close, so the tradeable reaction session
    is 2026-07-29, 13:30Z-19:59Z UTC; corrected here. This looks like a
    systematic scout-time defect (impact_window set to the release date
    rather than the next session) worth checking on other after-close-earnings
    dossiers.'
  last_updated: '2026-07-26T09:10:00Z'
---

## Scouted 2026-07-24T00:13:06Z

## Researched 2026-07-26T09:10:00Z

NO TRADE. Panel (bull sonnet / bear sonnet / quant opus) converged across all
three rounds. Quant's baseline: net EV long about minus 0.61 percent, net EV
short about plus 0.01 percent after roughly 0.30 percent round-trip costs;
adverse-tail-to-edge ratio about 30 to 1 versus a 7-8x institutional
no-trade threshold, roughly 4 times worse. Bull conceded to a contingent long
in round 2, then to NO-TRADE when EV still failed the 2 percent net-EV gate;
bear rejected a naked short from round 1 and converged to NO-TRADE by
default absent options premium data to justify a defined-risk put; quant
confirmed NO-TRADE final. Also corrected a mechanical dating error: the
dossier's impact_window read 2026-07-28 (the after-close release date) and
has been corrected to 2026-07-29 (the actual tradeable reaction session,
13:30Z-19:59Z UTC), since a plan dated entirely on 07-28 would price entry
and exit both before the catalyst. See `transcript.md` for the full
three-round debate.
