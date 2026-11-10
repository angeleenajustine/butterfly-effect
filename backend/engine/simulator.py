from dataclasses import dataclass

@dataclass(frozen=True)
class Company:
    name: str
    start_year: int
    revenue: float
    expenses: float
    cash: float
    debt: float

@dataclass(frozen=True)
class Assumptions:
    revenue_growth: float = 0.08
    expense_growth: float = 0.05
    horizon_years: int = 5

@dataclass(frozen=True)
class YearResult:
    year: int
    revenue: float
    expenses: float
    profit: float
    cash: float
    debt: float

def simulate(company: Company, assumptions: Assumptions) -> list[YearResult]:
    revenue, expenses = company.revenue, company.expenses
    cash, debt = company.cash, company.debt
    results = []
    for i in range(1, assumptions.horizon_years + 1):
        revenue *= 1 + assumptions.revenue_growth
        expenses *= 1 + assumptions.expense_growth
        profit = revenue - expenses
        cash += profit
        results.append(YearResult(company.start_year + i, revenue, expenses, profit, cash, debt))
    return results