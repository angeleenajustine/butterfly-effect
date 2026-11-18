from dataclasses import dataclass, field
from typing import Callable


@dataclass(frozen=True)
class Decision:
    type: str
    year: int
    params: dict = field(default_factory=dict)


@dataclass(frozen=True)
class Effect:
    """What a decision changes in one year. Added on top of the baseline forecast."""
    revenue: float = 0.0    # extra revenue this year
    expenses: float = 0.0   # extra expenses this year
    cash: float = 0.0       # one-off cash in or out (investment, loan proceeds)
    debt: float = 0.0       # change in debt this year


DECISION_REGISTRY: dict[str, Callable[[Decision, int], Effect]] = {}


def register(decision_type: str):
    """Decorator: file a function in the registry under a decision type name."""
    def wrapper(func):
        DECISION_REGISTRY[decision_type] = func
        return func
    return wrapper


def get_effect(decision: Decision, year: int) -> Effect:
    if decision.type not in DECISION_REGISTRY:
        raise ValueError(f"Unknown decision type: {decision.type}")
    return DECISION_REGISTRY[decision.type](decision, year)