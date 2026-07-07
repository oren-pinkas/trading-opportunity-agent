# Post-mortem — 2026-07-02-june-jobs

Analyzed 2026-07-06T23:30:00Z. PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

**Outcome:** neutral, -0.0058% (matched_hypothesis: no). **Root cause:** priced-in.

## Reconstruction
SHORT TLT into the June NFP release (Jul 2, 13:30Z), betting an in-line-or-hot print
(~130k) would push yields 15-20bp higher and TLT ~2.65% lower over the 13:35Z→17:00Z
hold. Entry (short) filled 85.475, cover 85.48 — a half-cent, 3.5-hour flat, realized
-0.0058%, NEUTRAL. The expected yield spike / selloff never materialized. TLT was also
~1.5% below the stale 86.80 plan reference by the open, the fingerprint of a catalyst
already discounted.

## Root cause: priced-in
The flat non-event was foreseen from three angles in the transcript. The bear argued
hawkishness was "already priced post-June-17" and the pre-market release meant the move
was "70-80% exhausted by the cash open." The quant quantified it: the executable
cash-open entry carried EV of only ~+0.13% ("thin"), with the attractive ~+1.8% EV
living exclusively in a conditional, direction-confirmed pre-market entry. The synthesis
note is the smoking gun — the synthesizer wanted an 08:45 ET conditional entry, but "the
orchestrator normalized entry to the cash open (13:35 UTC) because free intraday data
covers the regular session only — so the recorded plan captures the residual post-open
trend, not the pre-market gap." The dissent then predicted the in-line print was already
in TLT's ~$87 level and any dip would be "faded by duration buyers near $86." The price
path confirmed every word. A correctly-diagnosed, wrongly-taken trade: the harness
executed a leg whose only positive-EV path it structurally could not fill. The ~1.5%
stale entry reference is a secondary data-hygiene issue but did not cause the outcome —
even a correctly-priced blind short would have gone nowhere.

## Lessons
1. Skip trades whose only positive-EV path is a pre-market conditional entry the harness
   cannot fill. If the executable cash-open leg's EV is ~0 (here ~+0.13%), don't record
   the trade — the edge lives in a leg that will never execute.
2. After a known regime shift (e.g. a Fed dot-flip), require a *differentiated* surprise
   vs consensus before shorting duration into a data print — an in-line result is already
   in the curve and gets faded by duration buyers.
