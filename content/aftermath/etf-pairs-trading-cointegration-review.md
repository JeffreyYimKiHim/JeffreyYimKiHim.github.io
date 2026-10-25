---
title: "ETF pairs trading, ten years on — a strategy review"
date: 2026-10-25
tag: ETFs
summary: Cointegration pairs trading on country ETFs — the EWA–EWC family from Chan's Algorithmic Trading — reviewed against a decade of post-publication evidence. The concept survived; the economics got thinner.
status: published
---

Same six cuts as the standing autopsy format, applied at the strategy level: hypothesis, expression, sizing, what the market did, what was knowable at entry, and the kill criteria for next time.

## 1. Hypothesis

Two economically entangled ETFs — e.g., EWA (Australia) and EWC (Canada), both commodity economies — will see their price spread return to its mean within roughly one half-life, because the cointegrating relationship reflects real trade linkages, not correlation coincidence. Falsifiable version: *the EWA–EWC–IGE triplet mean-reverts with a half-life of about 23 days.*

## 2. Expression

Market-neutral spread, never a naked directional leg. The process is the edge:

- **Test before trade.** ADF on each series, CADF or Johansen on the pair/triplet. Chan's EWA–EWC CADF statistic was −3.64 — comfortably cointegrated. No test, no trade; correlation is not cointegration.
- **Kalman filter for the hedge ratio**, not static OLS — the book's EWA–EWC Kalman backtest printed APR 26.2%, Sharpe 2.4 (cost-free, 2013-era data).
- **Bollinger entry on the spread, exit at the mean**, with the half-life setting the patience budget. The triplet version showed APR 12.6%.

## 3. Sizing

Kelly on the spread's return distribution, f = m/s² — then take a quarter of it. Mean-reversion P&L is capped at the mean while the downside is unbounded when the relationship breaks; winning streaks breed the leverage that kills you at the regime change. Stop-loss beyond the maximum historical intraday drawdown, or CPPI — a "logical" stop inside the band contradicts the entry signal.

## 4. What the market actually did

- Do & Faff (2010/2012): the naïve distance method was largely unprofitable after 2002 once costs were included.
- Rad, Low & Faff (Quantitative Finance, 2016), 1962–2014: distance / cointegration / copula earned 91 / 85 / 43 bps per month gross — and 38 / 33 / **5** bps net. Opportunities shrank markedly from 2009. The cointegration variant was the best of the three in turbulent markets.
- Chen (2025) ETF replication: a z = 2 portfolio managed a Sharpe of only 0.28; profitability is now conditional on cointegration stability.
- Meanwhile, Jane Street built an empire on the institutional version of this same idea — ETF-versus-basket arbitrage — at a scale (and cost structure) no retail spread trader can match.

## 5. What was knowable at entry

Knowable, and therefore process if ignored: transaction costs consume most of the gross edge — the book's headline numbers were cost-free, which the text itself flagged. Cointegration is time-varying; a pair that tests well on one window can dissolve on the next (GLD–GDX's cointegration broke in July 2008 when oil ran to ~$145). Capacity is small; the crowding showed up in the data a decade ago.

Not knowable: the exact day the macro glue holding a pair together dissolves. That part is variance, and the correct response to variance is sizing, not regret.

## 6. Kill criteria for next time

Written so future-me cannot negotiate:

- Rolling CADF p-value above 0.10 for ten consecutive sessions — flat, no re-entry until it re-tests.
- Measured half-life running at more than 2× the backtest value — the patience budget is blown.
- Hurst exponent of the spread persistently above 0.5 — the pair has turned into a momentum trade; this book doesn't cover that risk.
- Net-of-cost Sharpe estimate below 0.5 on live fills — the edge exists, but not for me.

*Verdict: still a legitimate strategy family — but only in its cointegration/Kalman form, sized small, net of real costs. The textbook numbers are a museum piece; the framework is not.*
