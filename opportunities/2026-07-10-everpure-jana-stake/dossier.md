---
id: 2026-07-10-everpure-jana-stake
title: Jana Partners builds activist stake in Everpure
status: researched
created: '2026-07-10T07:38:15Z'
event:
  type: economic
  summary: Activist hedge fund Jana Partners disclosed a >1M share stake in Everpure
    (formerly Pure Storage), sending shares up ~9%, with a public strategy push likely
    in coming weeks.
  impact_window: '2026-07-31'
tickers:
- P
sources:
- title: Everpure (P) Gains 9.4% as Jana Partners Takes Stake
  url: https://www.gurufocus.com/news/8939319/everpure-p-gains-94-as-jana-partners-takes-stake
  accessed_at: '2026-07-10T07:38:15Z'
hypothesis:
  statement: >-
    A bare activist stake disclosure with no stated demands and no board slate has
    already re-rated Everpure ~9%, capturing the "someone is watching" premium. The
    only remaining edge — a concrete Jana ask — is un-triggered: no dated, specific
    campaign document exists yet, "likely in coming weeks" is not a scheduled event,
    and the toa price feed is independently unusable for absolute-level anchoring
    ($350.78 pre-announcement -> $482.62 announcement-day -> $212.38 now, incoherent
    with the dossier's own ~9% figure). Quant's EV table (continuation 0.30/+8%,
    drift 0.40/+0.5%, fade 0.25/-7%, tail 0.05/-15%) nets to roughly breakeven before
    costs and slightly negative after ~0.25% round-trip costs. Bull's rebuttal, taken
    at face value, only flips EV positive by inflating the continuation magnitude to
    a 6-24 month campaign payout (+8%) rather than the realistic 3-week catalyst-
    arrival re-rate (~+3.5%); horizon-corrected, it stays negative. The 2026-07-31
    window is mis-specified either way — too long for a scheduled-event trade, too
    short for a real campaign payout.
  direction: none
  confidence: 76
plan:
  ticker: P
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
    Whether "no trade" is itself an implicit directional bet. Bull's un-rebutted
    point: if Jana publishes a concrete, dated ask before 7/31, the stock may gap on
    confirmation rather than drift into it, so the wait-and-see stance could forfeit
    the re-rating a disciplined, stopped-out starter long would have captured.
    Bear and quant's EV framing assumes the tradable move is either absent pre-
    confirmation or fully capturable post-confirmation; neither closed this gap-risk
    objection. Testable post-mortem: did Jana publish a dated, specific proposal
    before 7/31, and if so, did P gap or drift on the news? Two explicit re-entry
    triggers, converged on by all three personas: (1) a confirmed concrete ask +
    timing lands in-window (continuation ~0.45-0.50 at realistic +6-8% magnitude,
    net EV ~+1.1%), or (2) a reconciled, trustable live feed shows price back near
    pre-disclosure levels (fade scenario stops being a loss, net EV turns positive
    even at base-case probabilities).
  last_updated: '2026-07-12T11:42:23Z'
---

## Scouted 2026-07-10T07:38:15Z

## Researched 2026-07-12T11:42:23Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Jana Partners
disclosed a >1M share stake in Everpure (P) on 2026-07-10, a bare 13D-style filing
with no stated demands, sending the stock up ~9.4% on the day (gurufocus). The
`toa price P` feed was independently flagged as unusable by all three personas —
$350.78 (2026-07-09 pre-announcement) -> $482.62 (2026-07-10 announcement, +37.6%)
-> $212.38 (2026-07-12 now, -56% from the announcement print) is internally
incoherent and inconsistent with the dossier's own ~9% figure, so no target prices
are recorded. BULL argued the initial pop only prices "an activist showed up," not
"what they want," and proposed a small stopped-out starter long into the 7/31
window; in rebuttal, bull conceded confidence down to ~50 and that the case leans
on stop-loss risk control more than organic continuation. BEAR argued the pop
already captures the "someone is watching" premium and that Jana's cited follow-
through pattern is uncited-as-evidence in this exercise; held NO TRADE at ~80.
QUANT's rebuttal was decisive: stress-testing bull's own continuation-probability
claim only flips EV positive if the +8% magnitude (a 6-24 month campaign payout) is
kept — horizon-corrected to a realistic 3-week catalyst-arrival re-rate (~+3.5%),
net EV goes more negative, not less. Verdict: NO-TRADE (not scheduled, not
simulated), confidence 76. Flips only on (1) a confirmed, dated, concrete Jana ask
landing before 7/31, or (2) a reconciled live feed showing price back near pre-
disclosure levels. Full debate with citations in `transcript.md`.
