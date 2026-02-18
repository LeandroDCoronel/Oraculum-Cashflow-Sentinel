from src.core.rules_engine import detect_cashflow_strangulation


def test_high_risk_cashflow_strangulation():
    signal = detect_cashflow_strangulation(
        cash_gap_days=72,
        frozen_capital_ratio=0.42
    )

    assert signal.level == "HIGH"
