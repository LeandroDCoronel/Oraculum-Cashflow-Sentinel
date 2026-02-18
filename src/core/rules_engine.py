from dataclasses import dataclass


@dataclass
class CashflowSignal:
    level: str  # LOW | MEDIUM | HIGH
    message: str
    cash_gap_days: int
    frozen_capital_ratio: float


def detect_cashflow_strangulation(
    cash_gap_days: int,
    frozen_capital_ratio: float
) -> CashflowSignal:

    if cash_gap_days > 60 and frozen_capital_ratio > 0.35:
        return CashflowSignal(
            level="HIGH",
            message="Severe cashflow strangulation detected",
            cash_gap_days=cash_gap_days,
            frozen_capital_ratio=frozen_capital_ratio
        )

    if cash_gap_days > 45:
        return CashflowSignal(
            level="MEDIUM",
            message="Potential cashflow stress",
            cash_gap_days=cash_gap_days,
            frozen_capital_ratio=frozen_capital_ratio
        )

    return CashflowSignal(
        level="LOW",
        message="Cashflow operating normally",
        cash_gap_days=cash_gap_days,
        frozen_capital_ratio=frozen_capital_ratio
    )
