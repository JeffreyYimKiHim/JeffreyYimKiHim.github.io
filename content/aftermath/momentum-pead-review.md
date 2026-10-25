---
title: "Momentum and PEAD — a strategy review"
date: 2026-08-02
tag: Momentum
summary: Time-series and cross-sectional momentum plus post-earnings-announcement drift — reviewed against the crash literature and the 2018–2020 quant winter. The premium persists; the crashes are the tuition.
status: published
---

Same six cuts as the standing autopsy format, applied at the strategy level: hypothesis, expression, sizing, what the market did, what was knowable at entry, and the kill criteria for next time.

## 1. Hypothesis

Assets that outperformed over the formation window keep outperforming over the holding window — cross-sectionally (long winners, short losers) and in time series (the sign of trailing returns predicts the sign of future returns across asset classes) — because underreaction, herding, and slow information diffusion are durable features of human markets. The earnings variant: *PEAD — stocks drift in the direction of an earnings surprise for days after the announcement* (Bernard & Thomas).

## 2. Expression

- **Time-series momentum across futures** is the cleanest expression — roll returns can be separated from the trend signal, and one factor runs across equity index, bond, FX, and commodity markets (Moskowitz–Yao–Pedersen).
- **Cross-sectional equity momentum**, monthly rebalance, is the classic version — and the one most exposed to crowding.
- **PEAD** trades the surprise, not the level: standardize the earnings shock, hold for the drift window. Note the window has been shrinking — from days toward intraday — as diffusion accelerated. A signal's shelf life is part of the expression.

## 3. Sizing

Momentum returns are negatively skewed: steady gains interrupted by crashes that cluster in post-bear-market rebounds. Volatility-scale the position, and cut the Kelly fraction further exactly when the recent track record looks best — the book's own red flag: cross-sectional stock momentum lost ~30% in 2008–09, commodities momentum ~33%, and the premium can stay dead for years after a crisis.

## 4. What the market actually did

Daniel & Moskowitz (JFE, 2016) formalized what practitioners already feared: momentum crashes are systematic, not anecdotal — 1932: −91.6%; Q2 2009: −40% — and they cluster when a bear market turns. November 2020's vaccine rotation replayed the pattern in miniature. Then came the quant winter of 2018–2020: only ~15% of quant funds beat their benchmarks in 2018–19 versus over 60% in 2017 (Nomura), and AQR's AUM fell from $226B to $140B — crowding thinned the factor premia the textbooks assumed. The factor didn't die; its carrying capacity shrank.

## 5. What was knowable at entry

Knowable, and therefore process if ignored: momentum dies after crises — the crash pattern was documented in the book's reference list before the worst of it repeated. Crowding is observable ex ante through factor correlations and fund-flow data; the 2018–19 underperformance did not arrive unannounced. PEAD's decaying horizon was visible in any honest out-of-sample log.

Not knowable: the day of the rotation. Crash timing is variance — answered by sizing and by the regime filter, not by conviction.

## 6. Kill criteria for next time

Written so future-me cannot negotiate:

- Post-crisis rebound regime (market off lows, vol elevated, leadership rotating) — momentum book halved immediately, no exceptions for "this time the trend is strong."
- Realized momentum-sleeve volatility above 1.5× its backtest value for a month — cut to core.
- Factor-crowding proxies (pairwise correlation of momentum funds, short interest in loser leg) at historical extremes — no new entries.
- Drawdown beyond 1.5× the backtest maximum — stop, assume regime shift, re-underwrite the strategy from the hypothesis up before re-entering.

*Verdict: momentum remains the most academically validated anomaly we have — and the one whose risk profile punishes textbook sizing hardest. Keep the factor; respect the crash calendar; never confuse a crowded premium with a safe one.*
