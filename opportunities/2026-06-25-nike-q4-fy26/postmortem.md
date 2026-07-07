# Post-mortem — 2026-06-25-nike-q4-fy26

Analyzed 2026-07-06T23:30:00Z. PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

**Outcome:** loss, -0.5576% (matched_hypothesis: no). **Root cause:** priced-in.

## Reconstruction
SHORT NKE held across the 6/30 after-close Q4 FY26 print into the 7/1 open. Entry
(short) filled at 41.25 (favorable vs the 41.85 plan), cover filled at 41.48 — NKE
ticked *up* ~+0.6% against the short instead of the median -6.9% the base rate implied.
The thesis rested on the post-print selloff base rate (down ~65% of prints, last two
-20%/-15.5%) plus likely FY27 guidance withholding; confidence was capped at 42 by an
explicitly flagged tariff-refund EPS beat / short-cover squeeze tail off the 52-week low.
That exact tail is what played out, at benign magnitude (+0.6% vs the feared +10-15%).

## Root cause: priced-in
NKE entered the print already at a 52-week low ($41.31), ~48% off its $80.17 high. The
bull (Round 1) argued the ~$42 price "discounts near-worst-case" and that the confirmed
one-time ~$1B IEEPA tariff refund was "pure upside to consensus"; the quant independently
noted "real price ~$41.72 near 52-wk lows." When a washed-out name has already absorbed
the bad-news narrative (China reset, withheld guidance, tariff GM headwind), the
asymmetric downside the short needed no longer exists, and a benign/one-time-beat print
flips the reaction positive. This was knowable at research time — it *is* the logged
dissent and the reason confidence sat at a near-coin-flip 42.

Note the honest caveat: at -0.56%, the loss is within intraday noise on a bet that was a
coin-flip by construction. The process critique the panel itself surfaced is the real
lesson, not the tiny realized number.

## Lessons
1. Confidence ≤~45 with an un-hedgeable positive tail and net EV <~2% against a ~7-8x
   adverse-tail-to-edge ratio (the quant's own figures, which rated "no-trade" equally
   defensible) is a no-trade filter, not a size-down. Express such earnings gap-shorts
   via defined-risk options (put spread), never a naked short.
2. Discount post-earnings negative base rates when the name is already at/near its
   52-week low — most of the drawdown is priced in, and a benign or one-time-beat print
   flips the reaction positive. Require a fresh, un-discounted catalyst before shorting a
   washed-out stock into a print.
