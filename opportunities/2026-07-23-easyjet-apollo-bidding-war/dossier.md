---
id: 2026-07-23-easyjet-apollo-bidding-war
title: easyJet Apollo takeover bid deadline
status: researched
created: '2026-07-23T09:13:03Z'
event:
  type: regulatory
  summary: Apollo Global topped Castlelake with a GBP 5.7bn cash bid for easyJet;
    board switched support, firm offer due early August
  impact_window: '2026-08-05'
tickers:
- EZJ.L
- APO
sources:
- title: Apollo hijacks easyJet takeover with GBP 5.7bn bid, trumping Castlelake
  url: https://www.euronews.com/business/2026/07/10/apollo-hijacks-easyjet-takeover-with-57bn-bid-trumping-castlelake
  accessed_at: '2026-07-23T09:13:03Z'
hypothesis:
  statement: Apollo's GBP 5.7bn all-cash topping bid for easyJet, board-recommended
    with a firm offer due near 2026-08-05, is a high-probability completion event
    that is already substantially priced into EZJ.L and immaterially reflected in
    APO. The tradeable edge is target-side merger-arb spread capture, and that leg
    cannot be priced in this venue -- EZJ.L is unresolvable across three symbol
    formats. The only priceable leg, APO, carries EV_net of roughly +0.13 percent
    against approximately 2 percent daily sigma (signal-to-noise about 0.12), below
    the 0.15 floor. No expressible position has positive risk-adjusted expectancy.
  direction: none
  confidence: 82
plan:
  ticker: EZJ.L
  action: no-trade
  entry:
    time: '2026-07-23T09:13:03Z'
    target_price: 23.31
  exit:
    time: '2026-08-05T16:30:00Z'
    target_price: 23.31
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
  dissent: 'Bull and bear converged on no-trade for incompatible reasons the debate
    could not resolve: bull argued the target-side edge was real and only blocked
    by a tooling gap (EZJ.L symbol resolution) -- fixing the quote could have produced
    a legitimate long into 2026-08-05, and bear''s "close to fully priced" claim was
    asserted, never measured, since no one ever obtained the actual spread-to-offer.
    Bear countered that even with a perfect quote this is a thin, three-week-stale,
    ~90-percent-base-rate arb whose residual spread compensates for slip/financing
    risk rather than representing alpha, worsened by simulate-plans having no path-dependent
    stop-loss to manage a deal-break gap. This is unresolvable without the missing
    quote -- the debate could not falsify either side because the measurement was
    unavailable, which is itself the lesson worth keeping. Secondary, smaller dissent:
    quant would have accepted a token 0.25 percent notional APO long in round 1;
    bear rejected any non-zero exposure below the 0.15 signal-to-noise floor, and
    the stricter reading won on the grounds that sub-floor sizing converts a risk
    rule into a suggestion. Data-layer lesson: EZJ.L, EZJ.LON, and EASYJET.L all
    returned HTTP 404 via twelvedata; the bare root symbol "EZJ" silently returned
    a different, wrong-scale instrument (approximately 62.99) rather than failing
    loudly -- same failure class as the toa-price-stub-default note. Non-US-listed
    tickers should be resolved and sanity-checked for scale/currency during scouting,
    before a full debate is spent on a thesis the venue cannot price. Internal toa
    price tool returns EZJ.L at 23.31 (source stub:deterministic, this system''s
    internal simulated-fill price) -- not a real market quote, used only as an entry/exit
    placeholder given the unanimous no-trade verdict.'
  last_updated: '2026-07-25T10:30:04Z'
---

## Scouted 2026-07-23T09:13:03Z

## Researched 2026-07-25T10:30:04Z — NO-TRADE

Panel verdict: NO TRADE (unanimous). Apollo Global's GBP 5.7bn all-cash bid tops Castlelake's prior offer for easyJet; the board switched its recommendation to Apollo, with a firm offer expected near the 2026-08-05 impact window (Euronews, 2026-07-10). Bull's thesis -- that bidding-war reflexivity would carry EZJ.L toward the offer price into the deadline -- could not be tested: three independent symbol resolutions (EZJ.L, EZJ.LON, EASYJET.L) all returned HTTP 404 via twelvedata, and the bare root symbol "EZJ" silently resolved to a different, wrong-scale instrument (approximately 62.99) rather than failing loudly. A leg with no verifiable fill price has EV of exactly zero, so bull conceded the target-side long rather than force a fabricated print. Quant priced the only tradeable leg, APO (the acquirer): real twelvedata prints of 119-120.7 across 2026-07-22 through 2026-07-24 show pure chop with no visible deal repricing. The deal is roughly 11 percent of APO's market cap, giving conditional acquirer-side moves of +0.30 percent (firm offer posted, P=0.75), 0.00 percent (slip, P=0.20), and +0.20 percent (collapse relief, P=0.05); EV_gross is about +0.235 percent, net of ~0.10 percent costs about +0.13 percent, against ~2 percent daily sigma -- signal-to-noise of about 0.12, below the 0.15 floor flagged by a prior lesson. Bear's fade thesis fails symmetrically: it needs the same unobtainable EZJ.L quote, and modal risk here is PUSU slippage (P=0.20), not deal break (P=0.05), worth only ~0-1 percent of spread widening -- too thin to fade after costs. The board-recommended ~90 percent base-rate completion probability is exactly why the residual spread three weeks after the 2026-07-10 news carries no edge in either direction. Keep 2026-08-05 on watch; re-open only if a valid EZJ.L or ISIN-level quote becomes obtainable before then. See transcript.md for the full three-round debate with citations.
