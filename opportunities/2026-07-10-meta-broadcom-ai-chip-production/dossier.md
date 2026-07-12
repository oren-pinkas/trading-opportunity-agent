---
id: 2026-07-10-meta-broadcom-ai-chip-production
title: Meta to start production of Broadcom co-developed Iris AI chip in September
status: researched
created: '2026-07-10T15:17:34Z'
event:
  type: product
  summary: Meta will begin manufacturing its in-house Iris (MTIA) AI chip, co-developed
    with Broadcom and fabbed by TSMC, in September 2026, targeting 14GW of compute
    by 2027.
  impact_window: '2026-09-01'
tickers:
- AVGO
sources:
- title: Meta to put AI chip into production in September as it looks to double computing
    capacity, Reuters reports
  url: https://www.cnbc.com/2026/07/09/meta-to-put-ai-chip-into-production-in-september-report.html
  accessed_at: '2026-07-10T15:17:34Z'
hypothesis:
  statement: The Meta MTIA/Iris production-start report is a low-information confirmation
    of a publicly known (since ~2023) Broadcom co-design relationship, not a quantified
    disclosure of Broadcom-booked revenue. Bull upside (ramp momentum, networking
    attach) and bear downside (sell-the-news, multi-generation in-house substitution,
    customer concentration) approximately cancel over this headline-to-impact window,
    leaving expected value statistically indistinguishable from zero net of costs.
    The real tradable catalyst is Broadcom's own September 2026 earnings call, not
    this news.
  direction: no_trade
  confidence: 68
plan:
  ticker: AVGO
  action: no-trade
  entry:
    time: null
    target_price: null
  exit:
    time: null
    target_price: null
  expected_profit_pct: 0
  note: 'No entry on this headline. Internal AVGO price feed is confirmed broken/incoherent
    in this environment ($64.01/$341.77/$174.64 across 3 nearby timestamps) and no
    WebSearch/WebFetch was available to any persona, so no price levels can be stated.
    Conditional plans (require a working price feed first): (A) if live data shows
    minimal pre-reaction, open a small fractional-size conditional long biased toward
    Broadcom''s Sept 2026 earnings call, not the headline, killed if that call shows
    no AI-segment guidance step-up tied to the Meta program; (B) if AVGO already gapped
    +4% or more on the headline, consider a small defined-risk short-the-pop (not
    an outright short). Primary revisit trigger: Broadcom''s September 2026 earnings
    call.'
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
  dissent: 'Bull vs. bear disagree on whether the September earnings catalyst is clean
    or contaminated. Bull holds that Meta''s in-house-substitution risk applies to
    future chip generations, not this production ramp, so Sept earnings should cleanly
    show the NRE-to-unit-revenue conversion. Bear holds substitution risk is only
    retimed (pushed 3-5 years out per the Google TPU / Amazon Trainium precedent),
    so even Sept earnings is contaminated by the same long-run revenue-share-erosion
    overhang. Bull never engaged with bear''s multi-generation revenue-share-erosion
    question -- this crux is unresolved and should be re-examined at the Sept earnings
    call with actual segment guidance and margin data. Secondary latent dissent: quant
    rejected the +8-15% quantified-disclosure base rate bull implicitly leaned on,
    since no $/unit/margin figures exist in the report -- unresolved until such figures
    are disclosed.'
  last_updated: '2026-07-12T12:53:00Z'
---

## Scouted 2026-07-10T15:17:34Z

## Researched 2026-07-12T12:53:00Z — NO-TRADE

Three-round panel debate (bull/sonnet, bear/sonnet, quant/opus) converged on NO TRADE for this specific headline. Round 1: bull proposed a long (conf 62) on backlog-conversion/networking-attach thesis; bear argued no new long, sell-the-news risk, in-house substitution risk (conf 62); quant found EV indistinguishable from zero (gross +0.15%, net +0.07%; conf 35/100 on estimates, 72/100 on no-trade direction) given the news is 2-3 days stale, second-hand, non-quantified, and the relationship has been public since ~2023. Round 2: bull revised down to conf 56, conceding sell-the-news risk and retiming (not retiring) the substitution risk, refining to scale-in-on-weakness-only with Sept earnings as the primary confirm/kill checkpoint; bear revised up to conf 66, converging with quant and sharpening that even Sept earnings is contaminated by the substitution overhang; quant reweighted both tails (P(positive) 35%->38%, P(negative) 25%->30%) landing at net EV +0.13% -- still statistically indistinguishable from zero, variance up but mean flat. Round 3 (Opus synthesizer): no_trade hypothesis, confidence 68/100. Blocking data gap: the internal AVGO price feed returned incoherent values ($64.01 / $341.77 / $174.64 across three nearby timestamps) and no WebSearch/WebFetch was available to any persona -- no real price levels could be verified, so no entry/exit targets are stated. Revisit at Broadcom's September 2026 earnings call using the falsifiers/confirm-signals listed in the plan note.
