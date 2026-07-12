---
id: 2026-07-02-levi-q2-fy26
title: Levi Strauss Q2 FY2026 earnings (press release July 8 AMC)
status: analyzed
created: '2026-07-02T11:00:05Z'
event:
  type: earnings
  summary: 'DATE CORRECTED — Levi Strauss (LEVI) Q2 FY2026 press release is released
    2026-07-08 AFTER close (concurrent with the 5pm ET call), per the company''s own
    webcast notice; the scout''s "July 2" was a stale third-party calendar artifact.
    Reaction trades at the 2026-07-09 open. Catalysts: denim demand, tariff/margin
    commentary, DTC mix (>50%). NOTE: July 2 = early close 1pm ET, July 3 = market
    fully closed (Independence Day observed) — neither is the event date.'
  impact_window: '2026-07-08'
tickers:
- LEVI
sources:
- title: Levi Strauss & Co to Webcast Second Quarter 2026 Earnings (StockTitan)
  url: https://www.stocktitan.net/news/LEVI/levi-strauss-co-to-webcast-second-quarter-2026-earnings-conference-jk1jrhujlwdf.html
  accessed_at: '2026-06-25T11:00:05Z'
- title: Levi Strauss IR — Q1 FY2026 results (beat-and-raise precedent)
  url: https://investors.levistrauss.com/news/financial-news/news-details/2026/Levi-Strauss--Co--Reports-First-Quarter-Results/default.aspx
  accessed_at: '2026-06-25T12:00:00Z'
- title: BusinessWire — CFO Harmit Singh to retire after a planned transition
  url: https://www.businesswire.com/news/home/20260407430551/en/Levi-Strauss-Co.-Announces-That-After-a-Planned-Transition-Chief-Financial--Growth-Officer-Harmit-Singh-Will-Retire
  accessed_at: '2026-06-25T12:00:00Z'
hypothesis:
  statement: 'PANEL IS GENUINELY SPLIT WITH NO DIRECTIONAL CONSENSUS — the quant (tiebreaker)
    finds no directional edge. Recorded as a minimal LONG expression reflecting the
    slight probability tilt (~52/48) from a beat-and-raise momentum name (beats 5
    of 6 quarters, DTC >50% mix). Entry before the 7/8 AMC print, exit after the 7/9
    open gap. The compressed implied move (~5%) is a volatility signal, not a direction
    signal. Direction: long, very low conviction.'
  direction: long
  confidence: 35
plan:
  ticker: LEVI
  action: buy
  entry:
    time: '2026-07-08T19:50:00Z'
    target_price: 23.5
  exit:
    time: '2026-07-09T13:45:00Z'
    target_price: 23.65
  expected_profit_pct: 0.6
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
  dissent: 'No directional consensus. Quant (opus, tiebreaker): directional net EV
    ~0 to -0.4% after costs — compressed implied move (~5%, consistent with 4.89%
    recent realized) argues for a long-gamma/straddle structure (out of scope), NOT
    a directional bet; would pass. Bear (conf 38): SHORT — priced for perfection within
    ~5% of the 52-wk high ($24.82), elevated bar on every metric, CFO Harmit Singh
    retiring (transition by Nov 2026), unquantified Bangladesh tariff (~29%) risk
    to H2 margins; down-gaps from a high base tend to be larger. Bull (conf 48): LONG
    — beat-and-raise momentum, DTC mix-shift, tariffs pre-guided. The down- magnitude
    skew the bear cites partly offsets the long probability tilt.'
  last_updated: '2026-06-25T12:10:00Z'
simulation:
  ran_at: '2026-07-10T22:46:36Z'
  fills:
  - leg: entry
    planned_price: 23.5
    actual_price: 24.41
    source: https://api.twelvedata.com/time_series?symbol=LEVI&interval=1min&date=2026-07-08&timezone=UTC
    fetched_at: 2026-07-08T19:50Z
  - leg: exit
    planned_price: 23.65
    actual_price: 23.955
    source: https://api.twelvedata.com/time_series?symbol=LEVI&interval=1min&date=2026-07-09&timezone=UTC
    fetched_at: 2026-07-09T13:45Z
  realized_profit_pct: -1.864
  outcome: loss
  matched_hypothesis: 'no'
postmortem:
  ran_at: '2026-07-12T23:30:05Z'
  root_cause: wrong-assumption
  lessons:
  - When the highest-confidence panelist (the quant) says directional EV is ~0 and
    the only positive-EV structure is out of mandate (e.g. a straddle), log NO TRADE
    — do not manufacture a minimal directional position 'for the learning loop'; a
    no-edge coin-flip still books real losses.
  - Anchor entry prices to a live quote fetched at the actual entry timestamp, not
    a stale pre-move reference — validate the planned entry is still within a small
    tolerance of the current price before filling, and re-price or abort if the stock
    has already run away from the modeled entry.
---

## Scouted 2026-07-02T11:00:05Z

## Researched 2026-06-25T12:10:00Z

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus). **Date corrected**
via the company's own webcast notice: the Q2 FY2026 press release drops 2026-07-08 AMC
(concurrent with the 5pm ET call), so the reaction is the 2026-07-09 open — the scout's
"July 2" was a stale calendar artifact (and would have collided with the July 3 market
closure). Real price ~$23.4-23.6 (NOT the stub's $488). The panel split with no
directional consensus; the quant found no directional edge (compressed IV is a vol, not
direction, signal). Recorded as a minimal LONG at confidence 35 for the learning loop.
Full debate with citations in `transcript.md`.

---
### Revision 2026-07-10T22:46:36Z
Simulated LEVI buy: -1.864% (loss, matched=no)

---
### Revision 2026-07-12T23:30:05Z
Post-mortem: wrong-assumption
