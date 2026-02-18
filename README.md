ORACULUM – CASHFLOW SENTINEL
===========================

Early warning system for logistics-driven cashflow strangulation.

------------------------------------------------------------------

OVERVIEW
--------
Oraculum Cashflow Sentinel is an early warning system designed to detect
cashflow strangulation caused by logistics and operational inefficiencies.

The system focuses on identifying hidden financial stress signals that
traditional accounting systems detect too late, especially in
logistics-heavy SMEs and export-oriented operations.

This project is part of the Oraculum Systems initiative, aimed at building
decision intelligence tools for real-world operational risk.

------------------------------------------------------------------

PROBLEM STATEMENT
-----------------
Many companies experience cashflow crises not because of lack of sales,
but due to:

- Inventory accumulation
- Delayed logistics cycles
- Poor turnover ratios
- Operational bottlenecks invisible to standard financial reports

By the time accounting reflects the problem, the company is already
financially constrained.

Cashflow Sentinel addresses this gap by monitoring operational indicators
that precede financial collapse.

------------------------------------------------------------------

CORE FEATURES
-------------
- Early detection of logistics-driven cashflow stress
- KPI-based risk signaling (green / yellow / red zones)
- Time-series analysis of operational metrics
- Interactive dashboard for decision-makers
- Designed for non-technical users

------------------------------------------------------------------

KEY INDICATORS (CURRENT VERSION)
--------------------------------
- Inventory Turnover Velocity
- Logistics Cycle Time
- Cash Conversion Cycle (CCC)
- Working Capital Stress Index (composite metric)
- Trend-based anomaly detection

------------------------------------------------------------------

TECH STACK
----------
- Python
- Pandas / NumPy
- Streamlit (interactive dashboard)
- Matplotlib / Plotly
- Modular analytical pipeline

------------------------------------------------------------------

ARCHITECTURE OVERVIEW
---------------------
1. Data ingestion (synthetic or real operational data)
2. KPI normalization and scaling
3. Signal extraction and trend analysis
4. Risk classification engine
5. Visualization layer (dashboard)

The system is designed to be extensible:
new indicators and models can be added without refactoring the core.

------------------------------------------------------------------

CURRENT STATUS
--------------
Version: v0.3 – Core pipeline stable

✔ Core KPIs implemented
✔ Analytical pipeline operational
✔ Dashboard functional
✔ Synthetic data validated

------------------------------------------------------------------

ROADMAP
-------
v0.4
- Improved anomaly detection logic
- KPI weighting calibration

v0.6
- Scenario simulation (what-if analysis)
- Export-ready reporting

v1.0
- Production-ready release
- SME-oriented configuration
- Market-viable MVP

------------------------------------------------------------------

HOW TO RUN
----------
1. Clone the repository
2. Create a virtual environment
3. Install dependencies:

   pip install -r requirements.txt

4. Run the application:

   streamlit run app.py

------------------------------------------------------------------

DESIGN PHILOSOPHY
-----------------
This project prioritizes:
- Interpretability over black-box models
- Operational causality over pure financial metrics
- Decision support over prediction theater

The goal is not to predict bankruptcy,
but to give managers time to act before it happens.

------------------------------------------------------------------

AUTHOR
------
Leandro D. Coronel
Founder – Oraculum Systems

------------------------------------------------------------------

DISCLAIMER
----------
This project is provided for research and decision-support purposes.
It is not a substitute for professional financial advice.
