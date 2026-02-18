def calculate_cash_gap(
    days_inventory: int,
    days_receivable: int,
    days_payable: int
) -> int:
    return days_inventory + days_receivable - days_payable
