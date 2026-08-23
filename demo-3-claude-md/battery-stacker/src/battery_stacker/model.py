from dataclasses import dataclass

import pandas as pd


@dataclass
class BatteryConfig:
    power_mw: float
    energy_mwh: float
    round_trip_efficiency: float = 0.9
    charge_tariff_eur_mwh: float = 0.0
    discharge_tariff_eur_mwh: float = 0.0

    @property
    def duration_hours(self) -> int:
        return max(1, int(self.energy_mwh // self.power_mw))


def load_prices(csv_path: str) -> pd.Series:
    df = pd.read_csv(csv_path, parse_dates=["timestamp"])
    df = df.sort_values("timestamp")
    return df.set_index("timestamp")["price_eur_mwh"]


def daily_dispatch(prices: pd.Series, config: BatteryConfig) -> pd.DataFrame:
    rows = []
    for _, day_prices in prices.groupby(prices.index.date):
        duration_hours = min(len(day_prices), config.duration_hours)

        charge_hours = day_prices.sort_values(ascending=True).head(duration_hours).index
        remaining = day_prices.drop(charge_hours)
        discharge_hours = remaining.sort_values(ascending=False).head(duration_hours).index

        for timestamp, price in day_prices.items():
            if timestamp in charge_hours:
                action = "charge"
                mw = config.power_mw
                cash_flow = -(price + config.charge_tariff_eur_mwh) * mw
            elif timestamp in discharge_hours:
                action = "discharge"
                # Round-trip efficiency losses are applied on discharge, not
                # on charge: the energy actually delivered to the grid is
                # less than the rated power once losses are accounted for.
                mw = config.power_mw * config.round_trip_efficiency
                cash_flow = (price - config.discharge_tariff_eur_mwh) * mw
            else:
                action = "idle"
                mw = 0.0
                cash_flow = 0.0

            rows.append(
                {
                    "timestamp": timestamp,
                    "price_eur_mwh": price,
                    "action": action,
                    "mw": mw,
                    "cash_flow_eur": cash_flow,
                }
            )

    return pd.DataFrame(rows).set_index("timestamp")


def summarize_value(dispatch: pd.DataFrame, config: BatteryConfig) -> dict:
    total_revenue = dispatch.loc[dispatch["cash_flow_eur"] > 0, "cash_flow_eur"].sum()
    total_cost = -dispatch.loc[dispatch["cash_flow_eur"] < 0, "cash_flow_eur"].sum()
    discharged_mwh = dispatch.loc[dispatch["action"] == "discharge", "mw"].sum()

    return {
        "total_revenue_eur": total_revenue,
        "total_cost_eur": total_cost,
        "net_value_eur": total_revenue - total_cost,
        "cycles": discharged_mwh / config.energy_mwh if config.energy_mwh else 0.0,
    }
