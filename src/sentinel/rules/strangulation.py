from sentinel.signals.cashflow_signal import CashflowSignal


def normalize(value: float, min_value: float, max_value: float) -> float:
    if value <= min_value:
        return 0.0
    if value >= max_value:
        return 1.0
    return (value - min_value) / (max_value - min_value)


def evaluate_cashflow_risk(
    cash_gap_days: int,
    frozen_capital_ratio: float
) -> CashflowSignal:

    explanations = []

    cash_gap_score = normalize(
        cash_gap_days,
        min_value=30,
        max_value=90
    )

    frozen_capital_score = normalize(
        frozen_capital_ratio,
        min_value=0.15,
        max_value=0.50
    )

    if cash_gap_days > 60:
        explanations.append("Extended cash gap indicates delayed capital recovery")

    if frozen_capital_ratio > 0.35:
        explanations.append("High proportion of capital frozen in operations")

    severity = round(
        0.6 * cash_gap_score +
        0.4 * frozen_capital_score,
        2
    )

    confidence = min(1.0, 0.5 + severity / 2)

    return CashflowSignal(
        severity=severity,
        confidence=confidence,
        cash_gap_days=cash_gap_days,
        frozen_capital_ratio=frozen_capital_ratio,
        explanations=explanations
    )