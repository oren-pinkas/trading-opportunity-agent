---
id: 2026-07-23-moderna-flu-vaccine-pdufa
title: Moderna mRNA-1010 flu vaccine PDUFA due August 5
status: researched
created: '2026-07-23T22:07:07Z'
event:
  type: regulatory
  summary: Moderna's mRNA-1010 seasonal flu vaccine has an FDA PDUFA target action
    date of August 5, 2026, after an FDA advisory committee unanimously backed its
    benefit-risk profile in June.
  impact_window: '2026-08-05'
tickers:
- MRNA
sources:
- title: 'Regulatory round-up: 20 July 2026 - The Pharmaletter'
  url: https://www.thepharmaletter.com/regulation/regulatory-roundup-20-july-2026
  accessed_at: '2026-07-23T22:07:07Z'
hypothesis:
  statement: >-
    MRNA's mRNA-1010 flu PDUFA (2026-08-05) is a de-risked, largely priced-in
    regulatory event, not a tradable catalyst: a unanimous June 2026 adcomm
    vote puts approval odds at approximately 88-92%, the approval branch
    historically moves a company of MRNA's size only about +1% to +4% (often
    negative on sell-the-news), and the residual 8-12% delay/CRL tail is the
    only real information content left. Net expected edge (about +0.2% on
    approximately 4% sigma, EV/sigma about 0.05) sits inside estimate noise,
    and no verified spot, realized-vol, or implied-vol data exists -- the
    real price provider (twelvedata) returned HTTP 429 (rate-limited, not
    404) on two consecutive attempts -- so both a directional long and a
    "fade the pop" short fail on economics after slippage, fees, and
    cost-of-capital over the 11-day hold to the PDUFA date.
  direction: none
  confidence: 80
plan:
  ticker: MRNA
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
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
    Whether the approximately 5% early-approval/positive-surprise branch,
    combined with MRNA's depressed multiple and unmeasured short interest,
    is fat enough to make a small premium-only long call convex rather than
    pure theta burn. The bull conceded to near-no-trade but never withdrew
    this branch, and it was rejected only on unverifiable grounds -- with
    two consecutive HTTP 429s there was no IV, skew, or short-interest data,
    so the option was priced off priors, not measurements. A future
    post-mortem should recheck (a) MRNA's actual 2026-08-03 to 2026-08-06
    realized move and whether any pop faded within 1-3 days, (b) what
    pre-event implied vol actually was, and (c) whether the no-trade call
    was correct on the merits or merely correct-by-default because the data
    pipeline was throttled -- the latter would be a process failure likely
    to recur on the next catalyst.
  last_updated: '2026-07-25T17:52:47Z'
---

## Scouted 2026-07-23T22:07:07Z

## Researched 2026-07-25T17:52:47Z

Three-round panel (bull/bear/quant, sonnet/sonnet/opus, synthesized on opus) converged
on NO-TRADE. Full transcript: `transcript.md`. Real price provider (twelvedata)
returned HTTP 429 on two consecutive attempts during quant's research -- no verified
spot/vol/IV data was available at research time.
