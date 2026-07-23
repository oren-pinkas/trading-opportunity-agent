# Research Debate Transcript — 2026-07-22-olin-huntsman-merger-vote

Strategy: debate-three-round-panel. Personas: bull (sonnet), bear (sonnet), quant (opus). Synthesizer: opus.
PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

Event: Olin (OLN) and Huntsman (HUN) scheduled special shareholder meetings for August 25, 2026 to vote on their proposed all-stock merger. Source: "Olin, Huntsman set shareholder votes on merger for August 25" — Investing.com, https://ng.investing.com/news/stock-market-news/olin-huntsman-set-shareholder-votes-on-merger-for-august-25-93CH-2598539 (accessed 2026-07-22T12:26:30Z). Research run at 2026-07-23T21:35:56Z UTC.

Lessons injected (institutional memory):
1. (regulatory/CZR) Validate every entry/exit timestamp falls within an open trading session; roll non-trading exit dates forward.
2. (regulatory/CZR) Never map a corporate/legal calendar date directly onto an execution timestamp — treat it as a catalyst, derive fill time from the nearest valid trading session.
3. (regulatory/PLD) SNR below ~0.15 on a linear-EV fade is not durable; simulate-plans has no path-dependent stop-loss enforcement.
4. (regulatory/PLD) An actual entry fill printing outside the planned entry band is an early falsification signal.
5. (regulatory/NYAX) Test-query the real price provider for exact entry/exit timestamps during research before finalizing a plan.

---

## Round 1 — Independent Research

### Bull (Catalyst-hunter, sonnet)

Argued the vote date is the key near-term de-risking catalyst, structured as three phases: pre-vote drift, vote-day reaction, post-vote arb convergence into closing. Real prices via `toa price --provider twelvedata`: OLN ~22.14 (Jul 17) → ~24.05-24.23 (Jul 23), +8-9%; HUN ~12.34 (Jul 21) → ~13.11 (Jul 22-23), +6-7% — both grinding higher together, read as the market pricing in rising deal-completion odds. Proposed: long HUN (or a long-HUN/short-OLN relative-value spread), entry on a real open-session timestamp in the week of Aug 17-21 2026 (pre-vote drift window), exit on the first liquid session where the vote outcome is public — 2026-08-25 if the 8-K lands during market hours, rolling to 2026-08-26 otherwise. Falsification trigger: entry fill outside the ~13.0-13.5 HUN band. Acknowledged the exchange ratio was not yet sourced.

### Bear (Skeptic, sonnet)

Argued the vote-date-scheduling headline is stale/priced-in — a procedural formality, not new deal-probability information, since the merger itself was already public. Cited HUN $12.945 (Jul 22) → $13.00 (Jul 23), a near-flat +0.4% move, as evidence of no market reaction to the headline itself. Flagged: antitrust/regulatory risk given chemical-sector product overlap (specifically epoxy resins), all-stock structure meaning correlated fundamental risk rather than a clean arb (HUN leverage/cyclicality, OLN chlor-alkali cyclicality), unknown exchange ratio/collar terms as a critical gap, possible contested vote, and that OLN's Jul 23 price fetch failed (HTTP 429 rate limit). Recommended PASS on any single-leg directional trade absent deal-term and regulatory-status data.

### Quant (Pragmatist, opus)

Pulled real prints: OLN 24.05, HUN 13.00 (Jul 23 15:30Z); OLN 23.785, HUN 12.95 (Jul 22 15:00Z). Hit HTTP 400 errors pricing 2026-08-25 (33 days out) — no bars exist that far ahead, so any plan anchored to the vote date is currently unpriceable and would resolve as an uninformative neutral (lesson 5). Base rates: signed stock-for-stock deals reaching vote-scheduling stage complete ~90-95%; vote failure ~2-5%; arb spread convergence is gradual and happens at closing, not at the vote itself absent a surprise. Marginal information content of "vote date scheduled" is near-zero. EV for a headline-reaction trade ≈ 0/negative after ~20-30bps round-trip costs; EV for arb-capture-into-close ≈ thin +0.44% gross / +0.05-0.2% net (uncomputable precisely without the exchange ratio), against a fat left tail of -15-20% on deal break. Recommended PASS.

---

## Round 2 — Rebuttal

### Bull (rebuttal)

Conceded the Jul22→Jul23 near-flat HUN print undercuts the headline-reaction story — the week-over-week run is better explained as gradual arb-spread compression / sector sentiment than a headline-day pop. Conceded 2026-08-25 is unpriceable by the real provider, killing the vote-day-reaction exit leg as designed, and retracted it. Proposed fallback: a smaller, pure pre-vote-drift trade with entry AND exit both inside the currently-priceable window, abandoning the vote-outcome catalyst entirely. Argued the 90-95% completion base rate pushes toward "size down and reframe," not fold — a near-certain outcome is still an environment where steady drift-capture can have positive EV. Listed conditions that would flip to PASS: spread already fully converged, evidence of a live antitrust referral/second request, or provider fragility making even the shortened window unreliable.

### Bear (rebuttal)

Corrected own framing: acknowledged the wider week-over-week run is real, but separated "headline caused reaction" (still false per the flat Jul22→23 HUN print) from "deal-sentiment/sector beta drove the week" (plausible but undemonstrated — no chemicals-peer benchmark comparison was run). Argued Quant's base rates make the staleness thesis quantitative and stronger than originally framed. Argued the unpriceable vote date is an independent second reason to pass, not just an instrument-selection problem to route around, because the substantive gaps (exchange ratio/collar unknown, antitrust exposure, correlated non-hedged fundamental risk) persist regardless of which date is priceable. Flagged an unresolved data hole: never got a clean OLN print for the Jul22→23 window, so the staleness claim is one-ticker (HUN only), not two-ticker confirmed. Reaffirmed PASS.

### Quant (rebuttal / synthesis-prep)

Argued the OLN +8-9%/HUN +6-7% week-over-week co-movement is mechanically expected in a stock-for-stock deal (target moves with the acquirer via the ratio) and is NOT independent confirmation of rising completion odds — the informative metric would be the ratio-implied spread narrowing, uncomputable without the exchange ratio. Noted HUN rising less than OLN is, if anything, consistent with the spread widening rather than narrowing — the opposite of a de-risking signal. Noted the big weekly number collapses to flat (+0.4%) at the timestamp nearest any realistic entry. Could not distinguish "rising completion odds" from "sector beta/M&A-wide sentiment" without a chemicals-peer benchmark strip (XLB, DOW, LYB, CE, WLK); flagged the 8-9% one-week acquirer spike as atypical of pure arb de-risking. Found the HTTP 400 pricing gap applies to EVERY future timestamp, not just the vote date, so Bull's "exit before Aug25" fallback does not escape the pricing problem — the only fully priceable window is entry-and-exit-both-in-the-past, which is unexecutable. Even ignoring pricing, the narrower pre-vote-only structure has lower EV than the full arb-to-close. Converged with Bear on PASS, on partly different grounds: antitrust risk is mostly already priced into the 90-95% base rate (shave completion to ~85-88% for the epoxy-resin-specific increment, not a full independent haircut); leverage/cyclicality risk is real for a naked long but hedgeable via the long-HUN/short-OLN spread — except the hedge ratio itself requires the missing exchange ratio, so the same data gap blocks the fix.

---

## Round 3 — Synthesis (opus)

**Hypothesis:** The proposed OLN-HUN all-stock merger is highly likely to complete (roughly 85-88%), but the "vote date scheduled for Aug 25" headline carries near-zero marginal information because vote-scheduling is a procedural, already-public step and signed stock-for-stock deals reaching this stage historically complete about 90-95% of the time. The observed week-over-week OLN +8-9% and HUN +6-7% co-movement is mechanically expected in a stock-for-stock structure and is NOT independent confirmation of rising completion odds. The informative metric would be ratio-implied spread narrowing, which is uncomputable because the exchange ratio and collar terms remain unknown. No actionable, simulatable trade exists at this time.

- Direction: neutral / no-trade
- Confidence: 85 (deal-closes thesis); ~3-5/100 (any actionable simulatable trade)

**Plan:** No-trade. No ticker, no entry/exit, expected profit 0%. Rationale, on three overlapping legs:
1. Near-certain completion base rate means the headline adds essentially no tradable edge; EV for a headline-reaction trade ≈ 0/negative after ~20-30bps costs.
2. The price provider has no forward bars for ANY future timestamp, not just Aug 25 — every catalyst-dated or pre-vote-drift structure is currently unpriceable and would resolve as uninformative neutral. The "exit before the vote" fallback does not escape this, since only an entry-and-exit-both-in-the-past window is fully priceable, which is unexecutable.
3. Substantive gaps persist regardless of pricing: exchange ratio and collar unknown (blocks spread computation and the hedge ratio needed to neutralize correlated fundamental risk); epoxy-resin antitrust overlap is mostly already embedded in the base rate, with only a modest specific increment warranted.

**Dissent:** The strongest unresolved disagreement is whether the near-certain completion base rate is a reason to PASS or a reason to size down and trade the gradual arb convergence — Bull argued the latter (positive-EV drift-capture environment), Bear and Quant argued the former. A secondary carried dissent: the source of the weekly run-up was never resolved — no chemicals-peer benchmark strip (XLB, DOW, LYB, CE, WLK) was run to distinguish "rising deal-completion odds" from "sector or M&A-wide beta." Quant further flagged that HUN rising less than OLN is directionally consistent with the spread widening (the opposite of de-risking), and that an 8-9% one-week acquirer spike is atypical of pure arb de-risking. A data hole compounds this: no clean OLN print was obtained for the Jul22→Jul23 window (429 rate limit), so even the staleness claim is one-ticker (HUN-only), not two-ticker confirmed.

**Reopen criteria:** confirmed exchange ratio and collar; a priceable forward exit timestamp becomes available as time passes; HSR/second-request/antitrust status confirmed; a chemicals-peer benchmark run to separate deal-specific signal from sector beta; EV recomputed positive net of ~20-30bps costs.
