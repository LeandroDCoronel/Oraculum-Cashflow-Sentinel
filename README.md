Oraculum CashFlow Sentinel
=========================

Autonomous early-warning system for cash flow strangulation caused by logistics.

Oraculum CashFlow Sentinel is a SaaS-oriented engine that detects when cash becomes trapped
between supplier payments, logistics delays, inventory stagnation, and customer collections.

Designed explicitly for CEOs and CFOs — not for operational dashboards.


---------------------------------------------------------------------

WHAT PROBLEM DOES IT SOLVE?
--------------------------

Many importers and distributors:
- Sell well
- Have demand
- Show healthy margins
- Yet consistently suffer from cash tension

The root cause is rarely margin or sales volume.

The root cause is time.

Paying suppliers today, selling weeks later, and collecting months after
silently strangles working capital.

This system detects that dynamic before it becomes critical.


---------------------------------------------------------------------

CORE PRINCIPLE
--------------

This system treats cash flow as a dynamic system under time constraints,
not as a static accounting outcome.

Cash is modeled as capital in motion, exposed to temporal friction.


---------------------------------------------------------------------

WHAT DOES THE SYSTEM DO?
-----------------------

Autonomously and continuously, the system:

- Computes real Cash Conversion Cycles per shipment, not period averages
- Detects cash frozen in inventory, transit, or delayed collections
- Quantifies the daily liquidity cost of operational delays
- Translates financial risk into executive-readable alerts

No dashboards are required to create value.
Signal clarity is prioritized over data exhaust.


---------------------------------------------------------------------

WHAT KIND OF ALERTS DOES IT GENERATE?
------------------------------------

Examples of real alerts:

- CRITICAL: $327,000 trapped for 41 days due to inventory stagnation
- WARNING: Logistics delay consuming $9,400 per day
- CRITICAL: Customer payment delay putting $96,500 at risk
- POSITIVE: $213,000 cash released compared to historical baseline

Alerts are expressed in money and time, not technical metrics.


---------------------------------------------------------------------

WHAT THIS SYSTEM IS NOT
----------------------

- Not a BI or analytics dashboard
- Not an accounting or ERP replacement
- Not a real-time treasury or trading system

It complements ERPs by observing what they do not:
the temporal friction of cash.


---------------------------------------------------------------------

QUICK DEMO
----------

Run a fully functional demo with realistic (synthetic) data:

python -m scripts.run_demo

Expected output:

=== ORACULUM CASHFLOW SENTINEL ===
Company: Importadora Andina
Cash Gap (days): 68
Frozen Capital Ratio: 40.00%
Risk Level: HIGH
Insight: Severe cashflow strangulation detected

This demo illustrates how the system detects cash flow risk
before it becomes visible in financial statements.


---------------------------------------------------------------------

HIGH-LEVEL SYSTEM ARCHITECTURE
------------------------------

CSV / ERP Data
    ↓
Ingestion & Validation
    ↓
Cash Flow Metrics Engine
    ↓
Risk & Alert Rules Engine
    ↓
Email / WhatsApp Executive Alerts

The architecture is intentionally minimal:
- Cron-based execution
- Autonomous operation
- Scales across companies, countries, and currencies


---------------------------------------------------------------------

PROJECT STRUCTURE
-----------------

oraculum-cashflow-sentinel/
├── config/        Global settings and alert thresholds
├── data/          Raw and processed data (local and demo)
├── src/
│   ├── core/      Core financial logic (intellectual property)
│   ├── ingestion/ Data loading and validation
│   ├── alerts/    Alert generation and delivery
│   ├── models/    Domain entities
│   ├── jobs/      Autonomous scheduled jobs
│   └── utils/     Shared helpers
├── tests/         Core logic tests
├── docs/          Product and business documentation
└── scripts/       Bootstrap and demo scripts


---------------------------------------------------------------------

CORE FINANCIAL METRICS
---------------------

The system computes real, operational metrics:

- DPO_real: Days from supplier payment to inventory arrival
- DIO_real: Days inventory remains unsold
- DSO_real: Days from sale to cash collection

CCC_real = DPO_real + DIO_real + DSO_real

Unlike textbook CCC, CCC_real is computed per shipment
and weighted by capital exposure rather than period averages.

From these metrics, the system derives:
- Cash frozen amount
- Daily cash cost of delays
- Cash-at-risk by shipment, supplier, customer, or period


---------------------------------------------------------------------

CONFIGURATION
-------------

All thresholds are configurable per company and environment.

Example (config/thresholds.yaml):

delay_days_threshold: 5
cash_frozen_threshold: 50000
daily_cash_cost_threshold: 1000
ccc_deviation_ratio: 1.2


---------------------------------------------------------------------

DESIGN PHILOSOPHY
-----------------

Oraculum CashFlow Sentinel is designed to be:

- Autonomous rather than interactive
- Financially expressive rather than metric-heavy
- Executive-facing rather than operationally noisy

The system exists to answer one question daily:

"Is time silently destroying cash anywhere in the operation?"
