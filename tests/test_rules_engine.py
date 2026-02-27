from sentinel.rules.strangulation import evaluate_cashflow_risk


def test_high_cashflow_risk():
    signal = evaluate_cashflow_risk(
        cash_gap_days=75,
        frozen_capital_ratio=0.42
    )

    assert signal.severity > 0.7
    assert signal.confidence > 0.8
    assert len(signal.explanations) >= 1