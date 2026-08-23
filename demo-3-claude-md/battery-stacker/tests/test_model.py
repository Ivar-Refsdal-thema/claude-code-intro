import pandas as pd
import pytest

from battery_stacker.model import BatteryConfig, daily_dispatch, summarize_value


@pytest.fixture
def toy_prices():
    # One 4-hour day: cheap, cheap, expensive, expensive.
    index = pd.date_range("2026-01-01 00:00", periods=4, freq="h")
    return pd.Series([10.0, 20.0, 50.0, 40.0], index=index)


def test_dispatch_respects_power_and_energy_limits(toy_prices):
    config = BatteryConfig(power_mw=5, energy_mwh=5, round_trip_efficiency=1.0)
    dispatch = daily_dispatch(toy_prices, config)

    assert (dispatch["mw"] <= config.power_mw + 1e-9).all()
    assert set(dispatch["action"]) <= {"charge", "discharge", "idle"}
    # duration_hours = energy_mwh // power_mw = 1, so exactly one charge hour
    assert (dispatch["action"] == "charge").sum() == 1
    assert (dispatch["action"] == "discharge").sum() == 1


def test_dispatch_picks_cheapest_and_most_expensive_hours(toy_prices):
    config = BatteryConfig(power_mw=5, energy_mwh=5, round_trip_efficiency=1.0)
    dispatch = daily_dispatch(toy_prices, config)

    charge_hour = dispatch[dispatch["action"] == "charge"].index[0]
    discharge_hour = dispatch[dispatch["action"] == "discharge"].index[0]

    assert dispatch.loc[charge_hour, "price_eur_mwh"] == 10.0
    assert dispatch.loc[discharge_hour, "price_eur_mwh"] == 50.0


def test_net_value_matches_manual_calculation(toy_prices):
    config = BatteryConfig(
        power_mw=5,
        energy_mwh=5,
        round_trip_efficiency=1.0,
        charge_tariff_eur_mwh=1.0,
        discharge_tariff_eur_mwh=2.0,
    )
    dispatch = daily_dispatch(toy_prices, config)
    summary = summarize_value(dispatch, config)

    expected_cost = (10.0 + 1.0) * 5  # charge at cheapest hour + tariff
    expected_revenue = (50.0 - 2.0) * 5  # discharge at most expensive hour - tariff

    assert summary["total_cost_eur"] == pytest.approx(expected_cost)
    assert summary["total_revenue_eur"] == pytest.approx(expected_revenue)
    assert summary["net_value_eur"] == pytest.approx(expected_revenue - expected_cost)
    assert summary["cycles"] == pytest.approx(1.0)


def test_efficiency_loss_applied_on_discharge_only(toy_prices):
    config = BatteryConfig(power_mw=5, energy_mwh=5, round_trip_efficiency=0.8)
    dispatch = daily_dispatch(toy_prices, config)

    charge_row = dispatch[dispatch["action"] == "charge"].iloc[0]
    discharge_row = dispatch[dispatch["action"] == "discharge"].iloc[0]

    assert charge_row["mw"] == pytest.approx(config.power_mw)
    assert discharge_row["mw"] == pytest.approx(config.power_mw * 0.8)
