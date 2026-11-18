import dataclasses
import pytest
from backend.engine.decisions import Decision, Effect, DECISION_REGISTRY, get_effect


def test_effect_defaults_to_zero():
    e = Effect()
    assert e.revenue == 0
    assert e.expenses == 0
    assert e.cash == 0
    assert e.debt == 0


def test_decision_is_immutable():
    d = Decision("expand", 2026, {"initial_investment": 100})
    with pytest.raises(dataclasses.FrozenInstanceError):
        d.year = 2027


def test_unknown_decision_type_raises():
    with pytest.raises(ValueError):
        get_effect(Decision("does_not_exist", 2026), 2026)


def test_registered_type_is_used(monkeypatch):
    # monkeypatch adds the test type temporarily and removes it after the test
    monkeypatch.setitem(DECISION_REGISTRY, "test_type", lambda d, year: Effect(cash=-5))
    assert get_effect(Decision("test_type", 2026), 2026) == Effect(cash=-5)