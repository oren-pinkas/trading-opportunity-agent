---
id: 2026-07-23-mitie-ocs-takeover
title: Mitie shareholders back OCS Group GBP 3.1bn takeover
status: researched
created: '2026-07-23T18:53:42Z'
event:
  type: regulatory
  summary: Mitie AGM backed OCS Group's cash takeover at 221.6p/share; deal awaits
    UK CMA, EC and NSIA clearance, expected to close Q1 2027
  impact_window: '2027-03-31'
tickers:
- MTO
sources:
- title: 'Mitie Group AGM: Q1 revenue jumps 10% as board backs GBP 3.1B OCS takeover'
  url: https://www.msn.com/en-us/money/economy/mitie-group-agm-q1-revenue-jumps-10-as-board-backs-3-1b-ocs-takeover/ar-AA28nyQF
  accessed_at: '2026-07-23T18:53:42Z'
hypothesis:
  statement: >-
    MTO.L at an assumed ~211p versus the OCS Group 221.6p cash offer is a ~5.02%
    gross merger-arb spread that does not pay for its own risk. Decomposing
    deal-completion into four gates -- shareholder approval 0.98 (cleared at the
    2026-07-23 AGM, hence non-informative and already priced in), UK CMA 0.9125
    (0.75 Phase 1 unconditional clearance, plus 0.25 chance of Phase 2 referral
    times 0.65 survival), NSIA 0.97 (government/defense-adjacent "soft FM"
    contract book likely triggers mandatory notification but rarely a block),
    financing/8-month drift 0.97 -- yields P(complete) is approximately 84%,
    against a cost-adjusted break-even completion probability of 83.8%: the
    point estimate sits ON break-even, not above it. Net EV over the ~8-month
    hold to the guided Q1 2027 close is roughly +0.06% at an assumed 170p
    break price, or +0.67% (about 1.00% annualized) even granting a more
    generous 178p break price -- both below an assumed ~2.7% risk-free
    alternative over the same horizon, against a 16-19% left tail and an
    uninsurable overnight jump risk (an estimated -8% to -12% gap on a CMA
    Phase 2 referral) that this system's simulator cannot stop out of.
    Kelly-optimal sizing crosses zero at p of about 82.5%, inside the stated
    +/-5pp error band of a subjective four-gate decomposition, so correct size
    is zero on the thesis alone. Independently and sufficiently on its own,
    MTO.L returned five consecutive HTTP 429 (rate-limited, not 404) responses
    from the price provider across two research passes, including after a
    75-second-plus cooldown -- so no verified live entry mark, fill path, or
    size exists regardless of the thesis.
  direction: none
  confidence: 20
plan:
  ticker: MTO
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
    Entry timing, unresolved by consensus. The bull argues a merger-arb
    position must be established before the first regulatory milestone (CMA
    Phase 1) because spread compression is the return mechanism, and waiting
    risks the spread having largely collapsed by the time clearance prints.
    The quant argues the opposite: post-clearance entry is structurally
    superior, since completion probability would re-rate to roughly 94-95%
    and the remaining horizon shortens, making a residual spread of 3.5% or
    more (empirically common in UK schemes awaiting long-stop mechanics)
    worth roughly +2.75% (about 8.3% annualized) -- a real trade, versus the
    rejected pre-clearance entry's sub-1% annualized edge. This is an
    empirical claim about UK merger-arb spread behavior the panel had no
    data to adjudicate, not an arithmetic dispute. Post-mortem test: if CMA
    Phase 1 clears unconditionally, record the MTO.L spread on the clearance
    date -- spread >= 3.5% vindicates the quant (patient entry was available);
    spread < 3.5% vindicates the bull (waiting forfeited the compression, at
    the cost of having carried the pre-clearance 16-19% left tail). Secondary,
    immaterial-to-verdict dissent: the break-price floor was narrowed
    (170p to 178p, splitting the bull's 185-190p ask and the bear's argument
    that 170p already overstates the floor) but never settled; the no-trade
    conclusion held across the full contested range (p in 0.82-0.88, break in
    170-178p).
  last_updated: '2026-07-25T17:52:00Z'
---

## Scouted 2026-07-23T18:53:42Z

## Researched 2026-07-25T17:52:00Z — NO-TRADE

Three-round panel (bull/bear sonnet, quant opus; synthesizer opus), analyzed strictly
on this opportunity's own merits. Mitie (MTO.L) shareholders backed OCS Group's
GBP 3.1bn cash takeover at 221.6p/share at the 2026-07-23 AGM; deal awaits UK CMA, EC
and NSIA clearance, guided to close Q1 2027 (2027-03-31). The BULL opened with a
merger-arb spread-convergence thesis (confidence ~65%), riding sequential
CMA/EC/NSIA clearance as de-risking catalysts, citing Mitie's Q1 revenue +10% as
evidence against a distressed-sale/renegotiation risk. The BEAR countered that
shareholder approval was near-certain and non-informative (already priced in), and
that the real risk is the CMA horizontal-overlap (both UK facilities-management
operators) plus NSIA exposure from Mitie's government/defense-adjacent contract
book, plus financing/MAC risk over an 8-month window. The QUANT decomposed
completion into four gates (shareholder 0.98 x CMA 0.9125 x NSIA 0.97 x financing
0.97 is approximately 0.84), landing the point estimate ON the cost-adjusted
break-even completion probability (83.8%), with net EV of roughly +0.06% to +0.67%
over 8 months against a ~2.7% risk-free alternative and a 16-19% left tail --
negative excess return under every combination of the contested inputs (completion
probability 0.82-0.88, break price 170-178p). The BULL conceded the arithmetic in
Round 2 and revised confidence down to ~50%. Separately and sufficient on its own:
MTO.L returned five consecutive HTTP 429 (rate-limited, not a confirmed 404/
no-coverage venue gap) responses from `toa price`, including after a 75s+ cooldown,
across two independent personas -- no verified entry mark, fill path, or size
exists. Verdict: NO-TRADE (status: researched, not scheduled -- no schedulable
plan exists). Documented but explicitly NOT scheduled conditional watch: revisit
only if ALL of (a) CMA Phase 1 unconditional clearance (no Phase 2 referral, no
undertakings-in-lieu), (b) gross spread to 221.6p still >= 3.5%, (c) <= 4 months to
expected completion, and (d) MTO.L returns a real quote on two consecutive probes
>= 60s apart -- hold simultaneously; a Phase 2 referral is a hard kill, not a
re-look. Data blocker logged distinctly from structural venue gaps (.NS/.PA/.T):
this is a rate-limit/throttle failure on an LSE mainboard name, not a confirmed
no-coverage venue. Full debate with citations in `transcript.md`.
