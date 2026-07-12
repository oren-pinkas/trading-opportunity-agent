---
id: 2026-07-12-june-ppi-report
title: June PPI report due July 15
status: researched
created: '2026-07-12T07:48:30Z'
event:
  type: economic
  summary: BLS releases the June 2026 Producer Price Index on July 15 at 8:30am ET,
    a wholesale-inflation read that feeds into Fed rate-path expectations ahead of
    the July 29 FOMC decision.
  impact_window: '2026-07-15'
tickers:
- SPY
- TLT
sources:
- title: Schedule of Releases for the Producer Price Index
  url: https://www.bls.gov/schedule/news_release/ppi.htm
  accessed_at: '2026-07-12T07:48:30Z'
hypothesis:
  statement: 'June PPI is a second-tier catalyst with no locatable surprise vector:
    no June consensus estimate exists to gauge surprise magnitude, only a hot May
    level to trend-extrapolate from. The one positive-EV expression (a pre-print reaction
    leg) is unfillable by the harness; the fillable expressions (cash-open-after-print
    or day-before-close entry) are symmetric coin-flips that go net-negative after
    costs and (for the overnight variant) financing.'
  direction: no-trade
  confidence: 80
plan:
  action: no-trade
  rationale: 'All three personas converged on skip. Quant''s EV math: long SPY open-to-close
    net ≈ -0.055%, long TLT net ≈ -0.10%, short-TLT overnight (bull''s fix for the
    fill-timing problem) net ≈ -0.01% — essentially zero with added overnight gap
    risk for no premium. Bull''s own day-before entry solves the lesson-#3 fill-mechanics
    objection but, by bull''s own concession, deletes the information edge, leaving
    pure variance (bull confidence fell 55→42/100). Bear''s CPI-sequencing point (same-month
    CPI likely already printed and priced before July 15, making PPI confirmatory
    not fresh) went unrefuted and was rated by quant as the strongest point in the
    debate. No consensus/whisper divergence, no cheap implied move, and no options
    leg exists to monetize the one real-but-unlocatable edge (hot-regime payoff convexity).'
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
  dissent: 'Strongest unresolved thread: the CPI-sequencing question. If same-month
    June CPI already printed cool/in-line before July 15, PPI becomes the freshest
    hawkish data point ahead of a live-hike FOMC (CME FedWatch ~25-30% hike / ~0%
    cut priced as of 2026-07-08) — inverting it from ''confirmatory/fade-prone'' to
    a genuine catalyst. Nobody in the panel had the June CPI date or result in hand;
    this is a shared blind spot, not resolved in either direction. Secondary: quant
    granted a real payoff-convexity skew (in a live-hike regime, a hot TLT surprise
    plausibly moves price more than a symmetric cool surprise reverts) but no cash-only
    vehicle exists to harvest it — an options leg would change the calculus. Evidence
    that would flip the verdict to TAKE: (a) a published June PPI consensus/whisper
    number showing meaningful surprise probability, (b) confirmation June CPI already
    printed cool/in-line, (c) an options leg or cheap implied move to monetize the
    convexity, (d) a fill mechanism within ~30 minutes of the 12:30Z print.'
  last_updated: '2026-07-12T23:17:45Z'
---

## Scouted 2026-07-12T07:48:30Z

## Researched 2026-07-12T23:17:45Z — NO-TRADE

Three-round debate (bull/bear sonnet, quant/synthesizer opus) converged to a **skip** verdict.

**Round 1 (independent):** Bull (55/100) proposed a momentum-continuation short TLT into the hot May PPI base (+1.1% MoM/+6.5% YoY) and a live hawkish Fed (CME FedWatch ~25-30% hike / ~0% cut priced, accessed 2026-07-12), entering the close before the print (2026-07-14T20:00Z) to dodge the harness's pre-market-fill constraint, exiting same-day close (2026-07-15T20:00Z). Bear (74/100 in the bear case) called PPI a second-tier, confirmatory release given same-month CPI typically prints first, with in-line-print fade risk and mid-July earnings-season confounds. Quant (82/100, verdict SKIP) modeled a roughly symmetric 25/50/25 hot/in-line/cool scenario distribution (SPY ±0.2-0.5%, TLT ±0.3-0.8%) and found both a long-SPY and long-TLT cash trade net negative after costs, with the only positive-EV path (front-running the 12:30Z print) unfillable by the harness.

**Round 2 (rebuttal):** Bull conceded the day-before entry fixes execution but not edge — it converts the trade into a pure overnight coin-flip with no informational edge, dropping to 42/100. Bear held that the day-before entry is the *weakest* part of bull's case (deletes edge, adds gap risk) and pointed to the unrefuted CPI-sequencing issue, rising to 78/100. Quant re-ran the EV on bull's fixed entry (short TLT overnight) and got ≈ -0.01% net — flat, with added gap variance for nothing — while granting a real but unmonetizable payoff-convexity skew; held SKIP at 78/100.

**Round 3 (synthesis):** No-trade, confidence 80/100. See dissent field for the CPI-sequencing gap that could flip this.
