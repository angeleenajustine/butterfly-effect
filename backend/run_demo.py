from backend.engine.simulator import Company, Assumptions, simulate

company = Company("Northstar Apparel", 2025, 2_400_000, 1_600_000, 450_000, 200_000)
assumptions = Assumptions(revenue_growth=0.08, expense_growth=0.05, horizon_years=5)

print(f"{'Year':<6}{'Revenue':>14}{'Expenses':>14}{'Profit':>14}{'Cash':>14}")
for r in simulate(company, assumptions):
    print(f"{r.year:<6}{r.revenue:>14,.0f}{r.expenses:>14,.0f}{r.profit:>14,.0f}{r.cash:>14,.0f}")