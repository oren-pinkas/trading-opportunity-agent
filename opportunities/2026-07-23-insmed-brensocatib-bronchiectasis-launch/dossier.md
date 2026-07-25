---
id: 2026-07-23-insmed-brensocatib-bronchiectasis-launch
title: Insmed's brensocatib approval ramp for non-CF bronchiectasis
status: researched
created: '2026-07-23T11:19:21Z'
event:
  type: regulatory
  summary: Insmed's DPP1 inhibitor brensocatib (Brinsupri), FDA-approved for non-CF
    bronchiectasis after positive Phase 3 ASPEN data, enters its first full launch
    quarter with print scripts and payer coverage as the swing factor for peak-sales
    estimates.
  impact_window: '2026-08-15'
tickers:
- INSM
sources:
- title: These 7 Small Caps Are On Fire In July
  url: https://www.benzinga.com/markets/small-cap/26/07/60593569/russell-2000-small-cap-stocks-july-biggest-gainers-2026
  accessed_at: '2026-07-23T11:19:21Z'
hypothesis:
  statement: >-
    INSM's post-approval move already happened and round-tripped before any entry
    was possible: the true July high was 118.30 on 2026-07-09, and the stock is
    back to 106.30 on 2026-07-24 -- a -10.14% round-trip, -0.55% on the month, and
    -20.2% since 133.21 on 2026-05-01, in a clean lower-highs sequence (133 to 118
    to 109). The dossier's catalyst is narrative-driven with no confirmed dated
    disclosure inside the window, and the stated impact_window of 2026-08-15 is a
    Saturday with no trading session, so the thesis cannot even be resolved on its
    own date. Reweighted for the negative-drift regime, EV_gross is -0.60 percent
    and EV_net -0.75 percent after roughly 15bps costs, with signal-to-noise -0.080
    against a +0.15 threshold and 14-day sigma of about 7.5-8.4 percent -- the edge
    is on the wrong side of zero and an order of magnitude inside the noise. All
    three personas converged on no-trade, and the quant's numbers moved further
    negative on data correction rather than less.
  direction: none
  confidence: 88
plan:
  ticker: INSM
  action: no-trade
  entry:
    time: '2026-07-27T15:30:00Z'
    target_price: null
  exit:
    time: '2026-08-14T19:55:00Z'
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
    The panel agreed on no-trade now but never reconciled what would count as a
    valid re-entry trigger. Bull and Bear converged on a soft watchlist standard --
    park the name pending a real catalyst (e.g. confirmed Q3 earnings), plus
    qualitative leading indicators (IQVIA NBRx, payer formulary wins with effective
    dates), and Bear even allowed that a materially cheaper entry price alone could
    flip the read. Quant set a strictly harder two-part gate -- a confirmed Q2
    earnings date inside the window AND two consecutive higher closes reclaiming
    109.15 to break the lower-high sequence. Under Bear's price-alone condition a
    further drawdown to, say, 95 would itself become a buy signal; under Quant's,
    that same drawdown extends the lower-high regime and makes the setup worse.
    Secondary and related -- Bear steelmanned that the -10 percent fade has already
    bled off some priced-for-perfection risk, making this two-sided with downside
    skew rather than a clean short, while Quant's Kelly output implied a large short
    signal it dismissed as noise-driven and non-actionable; both agreed the short
    isn't tradeable but for different reasons that were never tested against each
    other.
  last_updated: '2026-07-25T14:30:06Z'
---

## Scouted 2026-07-23T11:19:21Z

## Researched 2026-07-25T14:30:06Z -- NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). Round 1: Bull and
Bear both had their own `toa price` lookups fail (HTTP 400) and argued from priors --
Bull citing the dossier's own Benzinga "on fire in July" source as live momentum, Bear
calling that same source a lagging/retail signal. Quant pinned `--provider twelvedata`
and got real fills, initially reading a -7.5% pullback off a 114.92 high. Round 2: Quant
corrected its own sampling -- the true July peak was 118.30 on 2026-07-09, making the
round-trip -10.14%, with the stock down 20.2% since 2026-05-01 in a clean lower-highs
sequence. That correction demolished the Bull's momentum leg entirely (Bull conceded)
and sharpened the Bear's already-priced-in case, while also flagging that 2026-08-15
(the dossier's impact_window) is a Saturday with no trading session and no confirmed
earnings date sits inside the window. Reweighted EV_net came out at -0.75% against
~7.5-8.4% sigma (signal-to-noise -0.080, threshold +0.15) -- worse than Round 1, not
better. Verdict: NO-TRADE, confidence 88 in the skip. Flips only on a confirmed Q2
earnings date inside a window AND a technical reclaim of 109.15 (Quant's bar) or a
softer real-catalyst/leading-indicator standard (Bull/Bear's bar) -- this gap is the
recorded dissent. Full debate in `transcript.md`.
