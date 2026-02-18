import pandas as pd

from src.core.cashflow_metrics import calculate_cash_gap
from src.core.rules_engine import detect_cashflow_strangulation


df = pd.read_csv("data/samples/demo_company.csv")

row = df.iloc[0]

cash_gap = calculate_cash_gap(
    row.days_inventory,
    row.days_receivable,
    row.days_payable
)

frozen_ratio = row.inventory_value / row.total_assets

signal = detect_cashflow_strangulation(
    cash_gap_days=cash_gap,
    frozen_capital_ratio=frozen_ratio
)

print("=== ORACULUM CASHFLOW SENTINEL ===")
print(f"Company: {row.company}")
print(f"Cash Gap (days): {cash_gap}")
print(f"Frozen Capital Ratio: {frozen_ratio:.2%}")
print(f"Risk Level: {signal.level}")
print(f"Insight: {signal.message}")
