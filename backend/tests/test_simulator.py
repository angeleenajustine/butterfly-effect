from backend.engine.simulator import Company, Assumptions, simulate

def test_zero_growth_cash_accumulates_flat_profit():
    c = Company("Test", 2025, revenue=1000, expenses=600, cash=450, debt=0)
    a = Assumptions(revenue_growth=0, expense_growth=0, horizon_years=3)
    results = simulate(c, a)
    assert results[-1].cash == 450 + 3 * 400