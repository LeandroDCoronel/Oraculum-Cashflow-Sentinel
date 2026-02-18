from src.core.cashflow_metrics import calculate_cash_gap


def test_calculate_cash_gap_basic():
    """
    Cash Gap = Days Inventory + Days Receivable - Days Payable
    """
    result = calculate_cash_gap(
        days_inventory=30,
        days_receivable=45,
        days_payable=20
    )

    assert result == 55
