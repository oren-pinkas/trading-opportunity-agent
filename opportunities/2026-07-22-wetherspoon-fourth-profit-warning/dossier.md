---
id: 2026-07-22-wetherspoon-fourth-profit-warning
title: JD Wetherspoon issues fourth profit warning of the year
status: researched
created: '2026-07-22T17:49:00Z'
event:
  type: earnings
  summary: JD Wetherspoon (JDW.L) shares fell about 9% after its fourth profit warning
    this fiscal year, citing weaker sales and rising food, labour, repairs and energy
    costs; FY2026 (ending Jul 26) preliminary results are due Oct 2, 2026.
  impact_window: '2026-10-02'
tickers:
- JDW.L
sources:
- title: JD Wetherspoon shares sink after another profit warning - Invezz
  url: https://invezz.com/in/news/2026/07/22/jd-wetherspoon-shares-sink-after-another-profit-warning-why-are-uk-pubs-struggling/
  accessed_at: '2026-07-22T17:49:00Z'
hypothesis:
  statement: >-
    JD Wetherspoon's fourth FY2026 profit warning is not a tradable setup in
    either direction. The cited cost pressures (food, labour, repairs, energy)
    are sector-wide UK hospitality headwinds rather than JDW-idiosyncratic, and
    the fourth-warning-in-a-year cadence argues that both the derating and any
    reaction fatigue are already reflected in price. After a round-2 magnitude
    refinement (haircutting both tails per the bull's "sector-wide caps
    surprise" and the bear's "warning fatigue mutes reaction" arguments), BOTH
    legs carry negative expected value net of costs -- short roughly -0.44
    percent, long roughly -1.96 percent over the 10-week horizon to the Oct 2,
    2026 prelims -- so there is no edge against which to size a tail-risk bet.
    Independently and dispositively, JDW.L is unpriceable by our market-data
    provider (HTTP 404 on the LSE ticker via the twelvedata provider; no quote
    and no bars at either a prospective entry or the Oct 2 exit), which blocks
    entry, sizing, stop placement, and outcome verification regardless of
    thesis quality. This is recorded as a hard disqualifier, not a confidence
    discount. The bull opened a contrarian "kitchen sink into a lowered bar"
    long thesis at 50-55/100 confidence but conceded in round 2 that the
    missing price feed is disqualifying for a mean-reversion thesis
    specifically (no way to confirm proximity to the 52-week low), and revised
    to no-trade absent that data.
  direction: none
  confidence: 84
plan:
  ticker: JDW.L
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
    The bull's kitchen-sink/reset thesis was conceded on data grounds, never
    refuted on the merits. Bull argued a fourth warning is the point where
    management resets the bar low enough that Oct 2 prelims become a
    relief/beat catalyst; quant's rejection rests on an assumed combined
    upside probability of 0.30 (relief 0.20 plus squeeze 0.10) against the
    roughly 0.45 the bull's thesis requires, and that 0.30 was a prior, not an
    estimate from JDW-specific data. Nobody had the one dataset that would
    adjudicate it: the price reaction to warnings one, two, and three this
    fiscal year. If serial UK-hospitality warners historically show decaying
    negative reactions followed by a positive print reaction on the third or
    fourth cut, the bull was directionally right and the panel's convergence
    is a data-availability artifact, not an analytical conclusion. Separately,
    bear and bull never resolved what the muted ~9 percent reaction on warning
    four actually implies: bear reads it as efficient, already-discounted
    pricing; bull reads it as capitulation near a 52-week low; the 52-week
    range that would separate the two readings was never obtainable.
    Falsifiers to check after Oct 2, 2026: which of quant's five refined
    scenarios realized (roughly -11 percent, -3.5 percent, 0 percent, +7
    percent, or +16 percent); whether a fifth warning landed before the print
    (the p=0.28 branch); whether the Oct 2 prelims produced a relief rally on
    a weak print (the direct test of the bull's dissent); and, as a process
    check, how many opportunities the LSE/404 provider gap has now killed --
    if this is a repeat, the fix is provider coverage or a scout-stage venue
    filter, not spending a full three-round debate to reach a precondition
    failure.
  last_updated: '2026-07-24T23:54:18Z'
---

## Scouted 2026-07-22T17:49:00Z

## Researched 2026-07-24T23:54:18Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Bull opened
LONG JDW.L on a contrarian "fourth warning = kitchen sink into Oct 2 prelims"
thesis, confidence 50-55/100, explicitly discounted because no live price feed
means proximity to the 52-week low can't be confirmed. Bear opened skeptical:
the ~9 percent drop on a fourth warning may be a MUTED reaction (fatigue) --
most of the cost-inflation story (food, labour, repairs, energy -- sector-wide
UK hospitality pressures, not JDW-idiosyncratic) is likely already priced
either way, and the 10-week gap to Oct 2 is dominated by unrelated UK
macro/budget/rate noise. Quant flagged the missing JDW.L feed (404 from
twelvedata) as a hard, direction-agnostic blocker, then built a scenario tree
producing net EV short of +0.60 percent against an adverse-tail-to-edge ratio
of roughly 30:1 (versus a roughly 7-8x institutional threshold) -- a 4x
failure. In round 2, bull conceded the tree makes long EV negative and that
the missing feed specifically disqualifies a mean-reversion thesis; bear
showed the bull's kitchen-sink case bets the less-probable half of quant's own
tree; quant refined scenario magnitudes down per both opponents' framing and
found the round-1 short edge did not survive -- net EV flipped to
approximately -0.44 percent short and approximately -1.96 percent long, both
negative after costs. All three converged on NO-TRADE via two independent
routes (no positive EV on either leg; unpriceable instrument at both entry and
the Oct 2 exit). Verdict: NO-TRADE (not scheduled, not simulated). Revisit
after the Oct 2, 2026 FY2026 prelims only if the market-data provider gains
LSE coverage and fresh evidence (52-week range, peer multiples, warnings 1-3
reaction magnitudes, consensus revision history) becomes available. Full
debate with citations in `transcript.md`.
