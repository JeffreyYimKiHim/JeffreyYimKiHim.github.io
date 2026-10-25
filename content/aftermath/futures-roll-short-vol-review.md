---
title: "Futures roll returns and the short-vol trade — a strategy review"
date: 2026-10-25
tag: Strategy review
summary: Calendar spreads, the VX–ES basis, and harvesting volatility carry — reviewed after Volmageddon. The roll yield was real; the left tail was realer.
status: published
---

Same six cuts as the standing autopsy format, applied at the strategy level: hypothesis, expression, sizing, what the market did, what was knowable at entry, and the kill criteria for next time.

## 1. Hypothesis

In a persistently contangoed volatility curve, shorting the front of the VX term structure harvests the negative roll yield within weeks, because hedging demand keeps the curve upward-sloping most of the time. Sister bet in energy: *the CL calendar spread earns the roll without flat-price risk* — the book's backtest printed APR 8.3%, Sharpe 1.3.

## 2. Expression

- **Calendar spreads, not outright futures.** Long the far month, short the near (or the reverse in backwardation) — you are trading the curve's shape, not the commodity. Spot return is noise; roll return is the signal.
- **The VX–ES hedge** from the book's regression: ES×50 ≈ −0.3906×VX×1000 + 77,150 — a tradeable linkage between the volatility future and the equity index, valid only while the regression regime holds.
- **Instrument choice is the expression.** Selling vol via futures spreads is one thing; via daily-reset inverse ETPs is another — the reset mechanics create their own feedback loop, which is precisely what detonated in February 2018.

## 3. Sizing

Short-vol P&L is many small gains against rare catastrophic losses — a distribution that Gaussian Kelly will mis-size into ruin. Quarter-Kelly at most, with a hard leverage cap, and position size set so that twice the worst historical day stays inside the risk budget. Max drawdown scales non-linearly with leverage; the book's own example needed f÷7, not f÷2, to halve the drawdown.

## 4. What the market actually did

2018-02-05: VIX rose 115% in a single session (17.31 → 37.32, the largest one-day move on record). XIV lost ~96% and was terminated within days; SVXY fell ~90% and later cut its leverage; the leveraged/inverse-vol complex had grown to roughly $4B. The roll-return premium the strategy harvested was genuine — and the product structure monetizing it was a loaded spring. The post-2016 literature now treats short-vol carry as a textbook case of picking up pennies with a steamroller in the room.

## 5. What was knowable at entry

Knowable, and therefore process if ignored: contango persists *most* of the time, not all of it — backwardation arrives with crises and does not send a calendar invitation. The daily-reset decay and procyclical rebalancing of inverse ETPs were documented before 2018 (the Cheng–Madhavan leveraged-ETF mechanics were in the book's own reference list). The vol complex's growth made the unwind reflexive — crowded exits were visible in open interest.

Not knowable: which specific day the curve would snap. Variance — answered with sizing, not with a tighter stop that gaps can't respect.

## 6. Kill criteria for next time

Written so future-me cannot negotiate:

- VX curve flips to backwardation — flat same day, no averaging.
- Realized vol doubles its trailing 60-day median — halve the position before doing any analysis.
- Term-structure slope below its backtest entry threshold for three consecutive sessions — the harvest condition is gone.
- The product's daily-reset mechanics or leverage terms change — re-underwrite from zero; do not assume continuity.

*Verdict: roll-return harvesting remains a real premium with a permanent address in the left tail. Trade the curve, not the ETP; size for the day the contango ends, because it always ends.*
