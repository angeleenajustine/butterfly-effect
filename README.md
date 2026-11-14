# Butterfly Effect

A financial alternate-reality simulator: how might a company's financial future change if it made a different decision?

**Status:** v0.1.0: deterministic 5-year forecast engine. Decisions, branching timelines and a web interface are planned.

> Illustrative simulations on fictional companies. Not predictions.

## What it does today

Given a company's starting revenue, expenses, cash and debt, plus growth assumptions, the engine forecasts revenue, expenses, profit and cash for each year.

## Run it

Requires Python 3.13.

```bash
git clone https://github.com/angeleenajustine/butterfly-effect.git
cd butterfly-effect
py -3.13 -m venv .venv
.venv\Scripts\activate
python -m pip install pytest
python -m pytest
python -m backend.run_demo
```

## How the model works

- Revenue(t+1) = Revenue(t) × (1 + revenue growth)
- Expenses(t+1) = Expenses(t) × (1 + expense growth)
- Profit = Revenue − Expenses
- Cash(t+1) = Cash(t) + Profit

Starting facts (`Company`) are kept separate from assumptions about the future (`Assumptions`).

## Current limitations

- Cash is allowed to go negative. There is no insolvency or borrowing logic.
- No taxes, investments, debt repayment or working capital yet.

## Roadmap

- [ ] v0.2: decisions (expand, marketing, loan)
- [ ] v0.3: branching timelines and comparison
- [ ] v0.4: FastAPI backend and SQLite storage
- [ ] v0.5: React frontend
- [ ] v1.0: validation, documentation, release
- [ ] Later: Monte Carlo, sensitivity analysis, financial statements