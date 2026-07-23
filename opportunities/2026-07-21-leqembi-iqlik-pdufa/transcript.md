# Research debate transcript — 2026-07-21-leqembi-iqlik-pdufa

Strategy: three-round-panel (bull/bear/quant, sonnet/sonnet/opus; synthesizer opus).
PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Event: FDA PDUFA date for Leqembi IQLIK (subcutaneous formulation of lecanemab)
extended to 2026-08-24 after the agency requested additional information in May 2026.
Ticker: BIIB (Biogen; Leqembi co-marketed with Eisai). Source: BiopharmaWatch PDUFA
Calendar 2026, https://www.biopharmawatch.com/PDUFA-calendar, accessed 2026-07-21T10:40:07Z.

Institutional lessons applied (from `toa lessons-relevant --type regulatory --tickers BIIB`):
1. Validate every entry/exit timestamp falls within an open trading session; roll non-trading exit dates forward.
2. Never map a corporate/legal calendar date directly onto an execution timestamp — derive fill time from the nearest valid trading session.
3. S/N ratio below ~0.15 on a linear-EV fade is not a durable edge; simulate-plans has no path-dependent stop enforcement.
4. An entry fill outside the planned band is an early falsification signal.
5. Test-query the real price provider (`toa price <ticker> <timestamp> --provider twelvedata`) before finalizing timestamps, or the plan resolves as an uninformative neutral.

## Round 1 — Independent opening positions

### Bull (sonnet)
Long BIIB. Argues an "additional information" extension on an already-approved-mechanism
drug historically resolves as approval more often than not (general background knowledge,
not a dossier-sourced fact). IQLIK (subcutaneous, at-home dosing) is framed as the
commercially critical unlock for Leqembi's addressable market this year, with potential
to re-rate BIIB's forward multiple. Proposed: long BIIB common equity, entry ~2026-08-19/20,
exit ~2026-08-25/26, target 3-6% move on approval, small-to-moderate size. Confidence:
55/100. Self-caveated: no hard base-rate data, unverified price quotability, and IQLIK is
a formulation improvement (smaller expected magnitude than a first-time approval).

### Bear (sonnet)
Skeptical of tradeability. IQLIK is a lifecycle/convenience filing on an already-approved,
already-revenue-generating drug in a diversified large-cap — low information content,
likely already reflected in sell-side BIIB models. Flags the May "additional information"
request as an underweighted risk (could be device/human-factors data for the autoinjector,
carrying real CRL tail risk on combination products) and worries about a "sell the news"
outcome on a non-binary catalyst. Also flags execution mechanics: FDA decisions can land
outside market hours, so a naive exit fill may not reflect the true reaction (lessons
1/2/5 apply). Proposes NO TRADE, or at most a tiny fade sized only if S/N clears 0.15.
Confidence in a tradeable edge: 20/100.

### Quant (opus)
P(approve) ≈ 0.82 (heuristic for resubmission-type extensions on an already-approved
active ingredient, flagged as a rough base rate, not a hard citation), P(delay/CRL) = 0.18.
Assumes asymmetric magnitude: +1.5% on approval (largely expected), -4.0% on
delay/CRL (downside surprise). EV_gross = 0.82(1.5%) + 0.18(-4.0%) = +0.51%. Net of
event-day slippage/spread (0.30-0.50%), net EV ≈ +0.01% to +0.21%. Outcome SD ≈ 2.3%,
gross S/N ≈ 0.22, collapsing below the 0.15 durability floor after costs.
Recommends NO-TRADE; caps at 0.25R "lottery" sizing if forced to express a view.
Confirms 2026-08-24 is a Monday and a valid NYSE session, but stresses it is a calendar
catalyst, not an execution timestamp (lesson 2) — proposed placeholder entry
2026-08-21T14:00Z / exit 2026-08-25T14:00Z, contingent on `toa price BIIB ... --provider
twelvedata` verification (lesson 5). Confidence in tradeable edge: 15/100.

## Round 2 — Rebuttals

### Bull rebuttal
Concedes the "already priced in" point and quant's EV math are substantive, and concedes
underweighting the May info-request CRL tail risk. Still argues the mechanism-unlock
narrative carries an unquantified fat right tail (broad label, fast payer uptake
commentary) that a binary EV framing compresses away. Revises confidence 55 → 40/100.
Would flip further bearish if the info-request is confirmed device/human-factors related;
more bullish if confirmed clinical/CMC-only — flags that neither side has verified which,
and that this is the single fact the debate is missing.

### Bear rebuttal
Notes that quant's independent EV math converges with bear's qualitative read — two
different methods landing on the same no-edge conclusion is stronger than either alone.
Disputes bull's 3-6% magnitude as the tail case, not the median — that scale is priced
for a first approval of a novel mechanism, not a delivery-route change on an
already-marketed drug; anchors on quant's asymmetric ±1.5%/-4.0% as more defensible.
Revises to 88% confidence there is NO tradeable edge (from 80%). Concedes one real gap:
neither bear nor quant models interim information flow — a leaked/disclosed clean
human-factors readout before 2026-08-24 could cause pre-decision drift that a static,
single-event probability model doesn't capture. Flags this as a reason to watch for a
different setup, not to trade this one as structured. Position unchanged: NO TRADE.

### Quant rebuttal
Rejects bull's 3-6% as undefensible for a convenience-reformulation of an
already-marketed biologic — historical analogues for this event class cluster 1-3%,
skewed lower for diversified large-caps; this event structurally can't deliver a
surprise-driven re-rate. Clarifies that bear's "priced-in" argument attacks the
*magnitude* lever, not P(approve); only bear's device/human-factors point touches
P(approve), and only modestly. Revises: P(approve) 0.82 → 0.80, approve-magnitude
1.5% → 1.2% (priced-in trim), holds CRL magnitude at -4.0%. New EV_gross =
0.80(1.2%) + 0.20(-4.0%) = +0.16%. Net of slippage (0.30-0.50%) ≈ -0.34% to -0.14% —
now NEGATIVE. Gross S/N ≈ 0.07, well below the 0.15 floor and worse than Round 1.
Confidence in tradeable edge revised 15 → 11/100. Recommends NO-TRADE; if overridden,
hard cap 0.25R at the same placeholder entry/exit timestamps, still contingent on
twelvedata verification.

## Round 3 — Synthesis (opus)

All three seats converged toward NO-TRADE: bull down to 40/100 in favor of trading,
bear up to 88% confident there is no edge, quant's net EV crossed to negative
(-0.34% to -0.14%, S/N ≈ 0.07, below the 0.15 floor).

**hypothesis**: A directional trade on BIIB around the Leqembi IQLIK PDUFA
(2026-08-24) does not carry positive expected value net of costs. This is a
low-information-content convenience-reformulation event on an already-approved
mechanism, in a diversified large-cap; approval is the base case (~0.80) but the
approve-side magnitude is small and largely priced (~1.2%), and the CRL tail
(~-4.0%) is real but not large enough to make either direction cheap.
Direction: none. Confidence (that a directional trade has positive net EV): 12/100.

**plan**: no-trade. No schedule set. Quant's placeholder timestamps
(2026-08-21T14:00Z entry / 2026-08-25T14:00Z exit) are explicitly UNVERIFIED against
a real price provider and must not be executed as-is; per lesson 5, `toa price BIIB
<timestamp> --provider twelvedata` must be run first if this is ever revisited, or the
plan defaults to no-trade/no-schedule.

Calendar/execution check: 2026-08-24 (Monday) is a valid NYSE trading session — no US
market holiday falls on that date — but it is a calendar catalyst, not an intraday
execution timestamp (lesson 2).

**dissent** (for post-mortem):
1. Primary — no seat verified what the May 2026 "additional information" request
   actually concerns. If device/human-factors (combination-product) data, P(approve)
   and the CRL tail both worsen materially; if clinical/CMC-only, bull's upside case
   strengthens. The no-trade call rests on this unverified assumption.
2. Secondary — the interim-information-flow gap bear and quant both flagged but did
   not model: a leaked or disclosed clean human-factors readout before 2026-08-24
   could drive pre-decision drift, a potentially different tradeable setup this
   debate's binary-event framing does not capture. Post-mortem should check whether
   such a signal appeared and whether any edge existed pre-decision rather than at
   the PDUFA print itself.
