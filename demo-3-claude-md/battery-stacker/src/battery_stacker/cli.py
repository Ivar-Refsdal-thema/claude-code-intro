import argparse

from battery_stacker.model import BatteryConfig, daily_dispatch, load_prices, summarize_value


def main() -> None:
    parser = argparse.ArgumentParser(description="Battery value stacker")
    parser.add_argument("--prices", required=True, help="CSV with timestamp, price_eur_mwh")
    parser.add_argument("--power-mw", type=float, required=True)
    parser.add_argument("--energy-mwh", type=float, required=True)
    parser.add_argument("--efficiency", type=float, default=0.9)
    parser.add_argument("--charge-tariff", type=float, default=0.0)
    parser.add_argument("--discharge-tariff", type=float, default=0.0)
    parser.add_argument("--output", default="dispatch.csv")
    args = parser.parse_args()

    config = BatteryConfig(
        power_mw=args.power_mw,
        energy_mwh=args.energy_mwh,
        round_trip_efficiency=args.efficiency,
        charge_tariff_eur_mwh=args.charge_tariff,
        discharge_tariff_eur_mwh=args.discharge_tariff,
    )

    prices = load_prices(args.prices)
    dispatch = daily_dispatch(prices, config)
    dispatch.to_csv(args.output)

    summary = summarize_value(dispatch, config)
    print(f"Total revenue:  {summary['total_revenue_eur']:.2f} EUR")
    print(f"Total cost:     {summary['total_cost_eur']:.2f} EUR")
    print(f"Net value:      {summary['net_value_eur']:.2f} EUR")
    print(f"Cycles used:    {summary['cycles']:.2f}")
    print(f"Dispatch written to {args.output}")


if __name__ == "__main__":
    main()
