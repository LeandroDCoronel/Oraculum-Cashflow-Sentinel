from dataclasses import dataclass
from typing import List


@dataclass
class CashflowSignal:
    severity: float          # 0.0 – 1.0
    confidence: float        # 0.0 – 1.0
    cash_gap_days: int
    frozen_capital_ratio: float
    explanations: List[str]