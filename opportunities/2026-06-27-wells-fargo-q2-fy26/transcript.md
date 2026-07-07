# Debate transcript — Wells Fargo (WFC) Q2 FY2026 earnings

PAPER-TRADING SIMULATION ONLY. NOT FINANCIAL ADVICE.

- **Event:** WFC reports Q2 FY2026 BMO Tuesday 2026-07-14 (leads bank season with JPM/GS the same morning). Mon 7/13 and Tue 7/14 are both normal NYSE sessions.
- **Strategy:** three-round-panel. **Personas/models:** bull (sonnet), bear (sonnet), quant (opus), synthesizer (opus).
- **Spot anchor at research time:** WFC ~$84 (≈ -12% YTD; ~14% below a Jan-2026 ATH ~$97.76; ~9.7% rally over the prior 30 days). Local `toa price` returned the offline stub; persona targets used web-researched levels.
- **Verdict:** NO-TRADE. direction=none, confidence=33.

---

## Round 1 — Independent research

### Bull (LONG, +3-5%)
- Consensus EPS $1.74 (+13% YoY); Q1 loan growth +11% YoY (ahead of guide). [Yahoo preview](https://finance.yahoo.com/markets/stocks/articles/wells-fargo-quarterly-earnings-preview-104347036.html); [Hudson Labs](https://www.hudson-labs.com/research/wfc-q2-2026-earnings)
- Stress-test pass + 11% dividend hike to $0.50 (June 24); $5.4B returned in Q1. [GuruFocus](https://www.gurufocus.com/news/8930506/wells-fargo-wfc-completes-stress-test-and-plans-dividend-increase)
- 17 Buys / 0 Sells, median PT $95 vs ~$84; 12.65x trailing P/E; Q2 = first fully clean post-asset-cap comp. [Benzinga](https://www.benzinga.com/quote/WFC/analyst-ratings); [TipRanks](https://www.tipranks.com/stocks/wfc/stock-analysis)
- **Action:** buy WFC, entry 2026-07-13T20:00Z, exit 2026-07-14T14:30Z, target +3-5%, size ~1%.
- **Key unknown:** NII is the swing factor (Q1 NII miss drove -5.7%).

### Bear (SKIP / short, -4 to -6%)
- ~9.7% 30-day run-up inflates the bar; "sell the news" reflex — Q4 2025 -3.4% (on an NII beat), Q1 2026 -5.7% (NII miss, three same-day PT cuts). [StockAnalysis](https://stockanalysis.com/stocks/wfc/); [FinancialContent Q1](https://markets.financialcontent.com/stocks/article/marketminute-2026-4-14-wells-fargo-stumbles-on-net-interest-income-miss-a-divergent-path-in-the-2026-banking-landscape); [WRAL Q4](https://markets.financialcontent.com/wral/article/finterra-2026-1-14-the-new-era-of-wells-fargo-decoding-the-q4-2025-earnings-paradox)
- CFO pre-guided 3-4bps further NIM compression for Q2 (NIM 2.60% → 2.47% in Q1); commercial charge-offs +71% YoY to $360M; provision +22% YoY to $1.135B. [Hudson Labs](https://www.hudson-labs.com/research/wfc-q2-2026-earnings); [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/04/14/wells-fargo-wfc-q1-2026-earnings-call-transcript/)
- **Action:** short, entry 2026-07-14T13:30Z, exit 2026-07-14T19:00Z, target -4 to -6%, 0.5-1%.

### Quant (SKIP, size 0)
- Last 5 reports 4 of 5 DOWN (-5.7, -3.4, -2.9, -1.0); lone up-move +6.4-7.6% was the one-time asset-cap removal. [CNBC Q3'25](https://www.cnbc.com/2025/10/14/wells-fargo-earnings-q3-2025.html); [CNBC Q1'25](https://www.cnbc.com/2025/04/11/wells-fargo-wfc-earnings-q1-2025.html); [MarketChameleon](https://marketchameleon.com/Overview/WFC/Earnings/Earnings-Dates/)
- Implied ~3.2% vs realized avg ~4.0%. **EV:** P(down)=0.55; short EV after slippage ≈ +0.07-0.17% (≈ zero). **Edge does not survive.**

---

## Round 2 — Rebuttal

### Bull
- The 4-of-5-down pattern was *always one line* — NII — and the NII bar has been reset 3 quarters running; a contrarian long has asymmetry. The lone +7% was the market repricing the structural story (loans +11% YoY), which is *still compounding*. [Hudson Labs](https://www.hudson-labs.com/research/wfc-q2-2026-earnings)
- Bear's run-up argument is internally inconsistent: stock still -12% YTD, only +2.6% off the Q1 drop, 12.65x. NIM compression (3-4bps) is "already in the model." [Simply Wall St](https://simplywall.st/stocks/us/banks/nyse-wfc/wells-fargo/news/wells-fargo-wfc-stock-valuation-check-after-recent-performan)
- **Folds the long if:** full-year ~$50B NII guide is CUT, credit deteriorates materially, or implied move <3% (would trim, not zero).

### Bear
- The de-risking events (dividend hike, stress-test pass) ARE the run-up — upside catalysts are spent while downside (NIM compression, charge-offs) reports fresh July 14. The down-driver isn't de-risked, it's **scheduled** (CFO pre-guided NIM compression). [Hudson Labs](https://www.hudson-labs.com/research/wfc-q2-2026-earnings)
- "Cheap / loved / 17 Buys" is the exact crowded-long posture that preceded the Q1 -5.7%. Concedes the EV is thin → lands on **SKIP** as the trade, small-short only if forced.

### Quant
- Accepts the bear's run-up + scheduled-NIM points → moves P(down) 0.55 → ~0.62. Re-runs short EV: 0.62×3.2 − 0.38×3.2 = +0.77% gross − 0.20% slippage = **+0.57% net** ("clears costs").
- Rejects the bull's +3-5% long: the only up-move was the non-repeating asset-cap catalyst; four straight "good fundamentals" prints fell. Fundamentals are a multi-week thesis, not a one-day gap.
- **Default SKIP** on unconfirmed implied move; a **small short** (≤0.25 budget) becomes EV-positive only if the live straddle ≤2.5%; if ≥4.0%, stay SKIP.

---

## Round 3 — Synthesis (NO-TRADE, confidence 33)

**Open-gap decomposition (the decisive JPM-precedent test):** Fresh research shows WFC's drops ARE open-gap-capturable — Q1 2026 gapped down ~4.92% PRE-MARKET to ~$83.30 on the revenue miss (then partially recovered intraday); Q4 2025 -3.4% landed in early trading. [Investing.com Q1](https://ca.investing.com/news/company-news/wells-fargo-q1-2026-slides-earnings-beat-offset-by-revenue-miss-93CH-4564385); [Tickeron](https://tickeron.com/blogs/wells-fargo-wfc-q1-2026-earnings-eps-beat-but-revenue-miss-weighs-on-shares-12553/); [WRAL Q4](https://markets.financialcontent.com/wral/article/finterra-2026-1-14-the-new-era-of-wells-fargo-decoding-the-q4-2025-earnings-paradox) So the structure is valid here, *unlike* JPM.

This is the only name in the batch where a panelist found a conditional positive-EV edge (quant's small short, +0.57% net). But it holds ONLY if the live straddle ≤2.5% AND the move is gap-form; with ~4% realized and a ~9.7% run-up, the live implied move is more likely 3-4%+, where the quant's own rule says SKIP.

**Plan:** WFC, no-trade. (If traded, gap-hold: entry 2026-07-13T19:50:00Z, exit 2026-07-14T13:45:00Z; a short would set exit target below entry.) expected_profit_pct = 0.

**Dissent:** The bull's "spent-driver asymmetry" vs the quant/bear "scheduled-downside" framing. Unresolved because we cannot know today whether the full-year ~$50B NII guide is REAFFIRMED (bull's long) or the pre-guided NIM compression headlines fresh (bear/quant short) — that single guidance line, not the EPS print, determines direction and whether the move clears the 2.5% implied-move gate. [TIKR $50B NII](https://www.tikr.com/blog/wells-fargo-cfo-just-confirmed-50b-in-nii-heres-why-the-stock-still-looks-cheap)
