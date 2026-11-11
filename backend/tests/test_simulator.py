import pytest

from backend.engine.simulator import Company, Assumptions, simulate

def test_zero_growth_cash_accumulates_flat_profit():
    c = Company("Test", 2025, revenue=1000, expenses=600, cash=450, debt=0)
    a = Assumptions(revenue_growth=0, expense_growth=0, horizon_years=3)
    results = simulate(c, a)
    assert results[-1].cash == 450 + 3 * 400
    
def test_positive_growth_matches_hand_calculation():
    c = Company("Test", 2025, revenue=1000, expenses=600, cash=450, debt=0)
    a = Assumptions(revenue_growth=0.10, expense_growth=0.05, horizon_years=2)
    results = simulate(c, a)

    #year 1
    assert results[0].revenue == pytest.approx(1100)
    assert results[0].expenses == pytest.approx(630)
    assert results[0].profit == pytest.approx(470)
    assert results[0].cash == pytest.approx(920)

    #year 2
    assert results[1].revenue == pytest.approx(1210)
    assert results[1].expenses == pytest.approx(661.5)
    assert results[1].profit == pytest.approx(548.5)
    assert results[1].cash == pytest.approx(1468.5)