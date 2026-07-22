---
id: 2026-07-16-capricor-deramiocel-pdufa
title: FDA PDUFA decision due for Capricor's Deramiocel in Duchenne cardiomyopathy
status: scheduled
created: '2026-07-16T11:35:00Z'
event:
  type: regulatory
  summary: FDA target action date Aug 22, 2026 for Capricor Therapeutics BLA for Deramiocel
    cell therapy in Duchenne muscular dystrophy.
  impact_window: '2026-08-22'
tickers:
- CAPR
sources:
- title: Capricor Therapeutics, Inc. - Form 8-K (SEC)
  url: https://www.sec.gov/Archives/edgar/data/0001133869/000110465926078327/capr-20260626x8k.htm
  accessed_at: '2026-07-16T11:35:00Z'
hypothesis:
  statement: >-
    The roughly 35 percent drawdown from USD 30.01 (2026-06-25) to about USD
    19.46 to 20.13 (2026-07-21) has repriced CAPR from "priced for approval"
    to something closer to a coin flip, while the underlying HOPE-3 dataset
    (pre-specified primary endpoint PUL 2.0 p equals 0.03, key secondary LVEF
    p equals 0.04) remains a genuine positive data point that neither bear
    nor quant disputed on the science. The FDA's newly scheduled, company-
    unrequested CTGTAC advisory committee meeting on Jul 29, 2026 sits inside
    the trade window, 3.5 weeks before the Aug 22, 2026 PDUFA date, and is
    the real near-term catalyst. The quant's bear-adjusted expected-value
    framework still clears its own break-even with a thin cushion
    (unconditional approval probability of about 0.50 to 0.525 versus a 43.3
    percent break-even; net expected value of roughly plus 6 to plus 13
    percent), but the edge rests on contested probability inputs, so this is
    a small, defined-risk, staged long, not a conviction trade. The central
    unresolved disagreement is whether the unrequested adcom reflects a
    post-Sarepta Elevidys institutional reflex to route all Duchenne cell and
    gene therapies through public review regardless of file strength (a
    reading that keeps expected value positive), or undisclosed internal FDA
    reviewer disagreement following the original efficacy-based Complete
    Response Letter of Jul 2025 (a reading that would flip expected value
    negative).
  direction: long
  confidence: 54
plan:
  ticker: CAPR
  action: buy
  entry:
    time: '2026-07-22T14:00:00Z'
    target_price: 19.60
  exit:
    time: '2026-08-24T14:00:00Z'
    target_price: 22.30
  expected_profit_pct: 13
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
    The strongest unresolved disagreement is the value of two probability
    inputs feeding the unconditional approval probability: P(positive
    adcom) and P(approval given positive adcom), and underneath them,
    whether the efficacy-based CRL history, the unrequested adcom, and the
    Sarepta Elevidys regulatory chill are three independent negatives or
    largely one correlated negative counted three times. The bear stacked
    all three and landed at an approval probability of about 0.30 to 0.38,
    below the quant's own 43.3 percent break-even, which flips the
    framework's conclusion to negative expected value and argues for flat
    or a small defined-risk short. The quant revised to P(positive adcom)
    equals 0.50 and P(approval given positive adcom) equals 0.80, yielding
    an approval probability of about 0.525, and explicitly rejected the
    bear's combined math as double counting the same adverse signal across
    multiple nodes, reasoning that a CTGTAC panel votes precisely on the
    efficacy question the original CRL turned on, so a positive vote is
    unusually dispositive of exactly the bear's strongest fact. Neither side
    had the one piece of differential evidence that would break the tie -
    the FDA briefing document for the Jul 29 adcom, which had not published
    as of this research. If this trade loses, the most likely reason is
    that the bear's reading was correct and P(positive adcom) was really
    0.40 or below - the market's "surprise adcom equals bad omen" instinct
    would have been signal, not noise, and the quant's rejection of the
    bear's stacking would itself have been the error.
  last_updated: '2026-07-22T12:00:00Z'
---

## Scouted 2026-07-16T11:35:00Z

## Researched 2026-07-22T12:00:00Z — LONG, staged, defined-risk

Three-round panel (bull/bear on sonnet, quant on opus; synthesizer on
opus). Bull opened long on a sentiment/fundamentals divergence: CAPR fell
about 35 percent from USD 30.01 (2026-06-25) to USD 19.46 (2026-07-21) on
the Jul 29 FDA adcom announcement despite positive HOPE-3 Phase 3 data
(PUL 2.0 p equals 0.03, LVEF p equals 0.04, about 54 percent slowing of
skeletal disease progression) and analyst price-target raises (Oppenheimer
USD 15 to USD 43; consensus range roughly USD 41 to 63). Bear countered
that the original Jul 2025 Complete Response Letter was efficacy-based (a
harder bar than manufacturing-only), that the Jul 29 adcom was
unrequested and unexplained by the company's own CEO, that HOPE-3's
p-values are marginal on a modest n equals 106, and that Sarepta's
Elevidys safety fallout has raised the regulatory bar sector-wide - and
argued the market has not fully priced this in. Quant framed the trade as
two discrete catalysts (the Jul 29 adcom and the Aug 22 PDUFA, which falls
on a Saturday) and ran an explicit four-state expected-value calculation;
after the bear's rebuttal, the quant revised its approval-probability
assumption down from about 0.63 to about 0.525, cutting the cushion over
its own 43.3 percent break-even from about 20 points to about 9 points,
but the sign stayed positive even under a punitive stress test (about plus
6 percent net expected value). Verdict: small staged long, defined-risk
structure (call spread or collar) only, never naked common - roughly half
the intended size (about 0.75 percent of book) now, with the remainder
contingent on a clearly positive Jul 29 adcom vote, capped at about 1.5
percent of book total. Hard rule: a negative or split Jul 29 adcom vote
means exit the initial leg before Aug 22 and do not deploy the second leg
or average down into the PDUFA. Exit is pinned to 2026-08-24 (Monday),
not the Aug 22 Saturday PDUFA date itself, per the institutional lesson on
never mapping a regulatory calendar date directly onto an execution
timestamp. Confidence 54. Full debate with citations in
`transcript.md`.
