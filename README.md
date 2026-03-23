![Python](https://img.shields.io/badge/Python-3.10%2B-blue)![Dashboard](https://img.shields.io/badge/Streamlit-Dashboard-red)

**Early-warning risk engine for cashflow (inventory & logistics).** Deterministic signals **GREEN / YELLOW / RED** + decision-maker dashboard. v1.0 commercial MVP validated with synthetic scenarios.

**Run**
pip install -r requirements.txt
streamlit run app.py

ORACULUM – CASHFLOW SENTINEL (v2)

Softsensor core for early detection of logistics-driven cashflow risk.

OVERVIEW

Cashflow Sentinel v2 is the analytical softsensor core of the Oraculum
Cashflow Sentinel system.

This repository contains the second-generation internal engine designed
to quantify, explain, and score cashflow risk caused by operational and
logistics inefficiencies.

Unlike v1 (Commercial MVP), this version:

Has no UI or dashboard

Is not a finished product

Is designed as a reusable, extensible decision-intelligence core

WHAT THIS IS (AND IS NOT)

This repository IS:

A deterministic + scoring-based softsensor

A modular analytical core

A causal decision-support engine

A foundation for multiple downstream products

This repository IS NOT:

A dashboard application

A financial accounting tool

A black-box predictive model

A finished commercial product

PROBLEM DOMAIN

Many organizations suffer cashflow crises not due to lack of sales,
but due to logistics-driven capital lock-in, such as:

Excess inventory dwell time

Extended receivables cycles

Misaligned payables timing

Operational bottlenecks invisible to accounting systems

By the time financial statements reflect the issue,
the operational damage is already done.

Cashflow Sentinel v2 targets this pre-financial risk layer.

CORE CONCEPT: SOFTSENSOR

Cashflow Sentinel v2 operates as a softsensor:

Inputs: operational and logistics indicators

Processing: normalization, weighting, rule-based reasoning

Outputs: severity, confidence, and causal explanations

It does not predict bankruptcy.
It signals operational stress early enough to act.

ARCHITECTURE

Directory structure:

src/sentinel/

metrics/
Raw operational metrics and transformations
(e.g. cash gap calculation)

rules/
Risk evaluation and scoring logic

signals/
Structured definitions of cashflow risk signals

The architecture is designed to be extensible.
New metrics or rules can be added without refactoring existing logic.

Design principles:

Explicit causality

Interpretability over opacity

Modular extensibility

No hidden state

CURRENT CAPABILITIES

Cash gap calculation (inventory + receivables − payables)

Capital freeze ratio assessment

Normalized severity scoring (0.0 – 1.0)

Confidence estimation

Human-readable causal explanations

EXAMPLE USAGE (CONCEPTUAL)

Compute operational metrics (cash gap, frozen capital)

Pass metrics into the evaluation engine

Receive a structured cashflow risk signal containing:

Severity score

Confidence level

Explanatory reasons

Raw contributing values

VERSIONING NOTE

v1.x:
Commercial MVP with dashboard and fixed scope.
Frozen and released separately.

v2.x:
Analytical softsensor core (this repository).

v2 represents a conceptual and architectural evolution,
not a cosmetic update.

INTENDED EXTENSIONS

Multi-indicator aggregation

Scenario simulation (what-if stress testing)

Time-series trend accumulation

Industry-specific calibration profiles

Integration into dashboards, APIs, or decision engines

DESIGN PHILOSOPHY

This system prioritizes:

Operational truth over financial cosmetics

Explainability over prediction theater

Decision advantage over algorithmic novelty

The goal is not to look smart.
The goal is to give managers time.

AUTHOR

Leandro D. Coronel
Founder – Oraculum Systems

DISCLAIMER

This software is provided for research and decision-support purposes only.
It does not constitute financial, legal, or accounting advice.
