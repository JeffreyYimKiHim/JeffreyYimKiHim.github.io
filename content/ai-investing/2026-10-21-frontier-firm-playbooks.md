---
layout: post
title: "What XTX, Jane Street, and DeepSeek Actually Teach a Traditional Fund"
date: 2026-10-21
categories: [ai-augmented-investing]
tags: [xtx, jane-street, deepseek, research-culture, asset-management, strategy]
---

*The most useful thing about frontier trading firms isn't their models — it's their meta-rules. A look at what public evidence says they actually invest in, and five lessons a traditional asset manager can implement without a GPU cluster. Not investment advice.*

## The evidence base (and its limits)

Top trading firms never publish P&L attribution. What we can observe is hiring language, public statements, open-sourced infrastructure, and sustained capital allocation — which, over years, is a reliable signal of what's *validated* rather than fashionable.

**XTX Markets** is the cleanest specimen: a pure algorithmic market maker (~300 people, ~$250B daily volume, ML forecasts across 53,000+ instruments) whose revenue is entirely spread and model performance. Every technology dollar is P&L-audited by definition. Its stated model lineage — econometric methods → trees → neural networks → modern deep learning, "and we expect this evolution to continue" — plus a 25,000+ GPU estate, an exabyte-scale open-sourced filesystem (TernFS), a €1B Finnish data-center buildout, and a dedicated ML research arm (XTY Labs) whose mission is integrating models into live trading on a **weeks-not-months** cadence.

**Jane Street** publicly calls deep learning "the future of quantitative trading" while running interviews that test statistical reasoning under noise, non-stationarity, and latency constraints *first* — and pays FPGA engineers the same as ML engineers.

**Citadel Securities** writes job specs asking ML researchers to ship models that "move P&L in options markets"; its equities quant research arm defines alpha as "rigorous, repeatable and profitable in live trading — the true out-of-sample."

**DeepSeek** is the domestic-Chinese data point that should make every asset manager sit up: a quant fund (High-Flyer) whose AI research arm produced frontier architecture work — MLA, and the January 2026 manifold-constrained hyper-connections paper (mHC) — competitive with anything from dedicated labs. Ubiquant's research arm open-sourcing a code model that beats GPT-5.1 on SWE-bench is the second data point.

## The meta-rule hiding in plain sight

Three firms, one sentence each, same rule:

- XTX: "Backtests are flattering. Models that look good in backtests can be worthless in the market."
- Jane Street: deep learning is part of the toolkit, "not the starting point."
- Citadel: profitable in *live* trading, the *true* out-of-sample.

**The moat is not any model. It is evaluation discipline × infrastructure × iteration speed.** This is excellent news for traditional funds: two of those three multipliers are organizational, not capital-intensive.

## The AttnRes lesson: research culture as strategy

Moonshot AI's Attention Residuals paper (arXiv:2603.15031) attacked the most unquestioned component in modern AI — the residual connection, fixed since 2015 — replacing uniform additive accumulation with learned, content-aware attention over depth. The payoff: baseline-matching loss at 1.25x less compute, with the largest gains on multi-step reasoning (+7.5 GPQA-Diamond) and code (+3.1 HumanEval). A follow-up (MSAR) already reports 1.58x.

The transferable move isn't the architecture — it's the **question template**: *find a default that nobody has examined for a decade, and ask why it must be fixed.* AttnRes (Kimi), mHC (DeepSeek), and Hyper-Connections (ByteDance) all attacked the same default within twelve months, which tells you where the low-hanging fruit was hiding: in plain sight, inside the "solved" pile.

Every investment organization has its own residual connections:

- Why must factor combination use fixed IC weights? (That's an equal-weighted portfolio of signals — would you run your book that way?)
- Why must backtesting mean replaying history? (Generative market simulation attacks this default.)
- Why is on-balance-sheet leverage the default starting point for credit risk? (The hyperscaler analysts who decomposed five categories of off-balance-sheet obligations were running the AttnRes play on credit analysis.)

## Five implementable lessons for a traditional fund

1. **Measure research-to-decision latency as a KPI.** XTX's weeks-not-months loop is a compounding advantage: iteration speed is the denominator of alpha decay. Most traditional funds take quarters to move an idea from memo to portfolio. Instrument that pipeline; halve it.
2. **Buy evaluation taste before buying compute.** Jane Street's interview logic — statistics under non-stationarity first, deep learning second — is a hiring template any fund can copy for free.
3. **Adopt the "true out-of-sample" definition of done.** No research result counts until it survives live-paper trading with costs, latency, and capacity charged. This single rule kills more bad AI projects than any technical review.
4. **Match your compute to research, not latency.** A traditional fund doesn't need 25,000 GPUs; ~20 for simulation, backtesting, and fine-tuning captures most of the research-side value. Latency engineering is for market makers.
5. **Institutionalize one "default audit" per year.** Pick one load-bearing assumption in your process (benchmark construction, factor weights, data-vendor definitions) and assign a team to attack it. Budget it like research, because it is.

## The strategic bottom line

The firms converting AI into durable profit share a pattern: they treat research as an engineering discipline with unforgiving evaluation, and they fund the questioning of their own defaults. Both are choices about culture and capital allocation — not about having the fanciest model. That's precisely why they're available to any asset manager willing to make them.

---

*Based solely on public statements, job postings, open-source releases, and published papers. An informal strategy note, not investment advice.*
