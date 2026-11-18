#!/usr/bin/env python3
"""watch_service_ledger - price a mechanical watch by its service ledger.

Sticker price is the down payment on a mechanical watch; the service visits
are the real bill. This runner takes the purchase price, the per-service
cost, the service interval, and an optional daily wear figure, then prints
the full ownership ledger over a horizon: visit count, total cost, cost per
ownership year, and cost per 1,000 wrist hours.

Stdlib only. Run: python3 watch_service_ledger.py --label "Seiko 5 Sports" \
    --price 200 --service 150 --interval 5 --horizon 20 --hours-per-day 12
"""
import argparse
import sys


def visit_count(interval: float, horizon: float) -> int:
    """Service visits inside a horizon.

    >>> visit_count(5, 20)
    4
    >>> visit_count(4.5, 20)
    4
    >>> visit_count(25, 20)
    0
    """
    if interval <= 0:
        return 0
    return int(horizon // interval)


def ledger_total(price: float, service: float, visits: int) -> float:
    """Purchase price plus every service visit.

    >>> ledger_total(200.0, 150.0, 4)
    800.0
    >>> ledger_total(3000.0, 900.0, 5)
    7500.0
    """
    return round(price + service * visits, 2)


def per_thousand_hours(total: float, horizon: float, hours_per_day: float) -> float:
    """Ledger spread over wrist hours, reported per 1,000 hours.

    >>> round(per_thousand_hours(800.0, 20, 12), 2)
    9.13
    >>> per_thousand_hours(800.0, 20, 0)
    inf
    """
    if hours_per_day <= 0:
        return float("inf")
    hours = horizon * 365 * hours_per_day
    return total / (hours / 1000)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        description="Price a watch by its service ledger, not its sticker.")
    p.add_argument("--label", default="watch", help="what is on the dial")
    p.add_argument("--price", type=float, required=True,
                   help="purchase price today")
    p.add_argument("--service", type=float, required=True,
                   help="cost of one full service")
    p.add_argument("--interval", type=float, required=True,
                   help="years between services")
    p.add_argument("--horizon", type=float, default=20.0,
                   help="ownership years to price (default 20)")
    p.add_argument("--hours-per-day", type=float, default=0.0,
                   help="daily wear hours; 0 skips the wrist-hour row")
    args = p.parse_args(argv)

    if args.price < 0 or args.service < 0 or args.interval < 0:
        print("prices, service cost, and interval must be non-negative")
        return 2

    visits = visit_count(args.interval, args.horizon)
    total = ledger_total(args.price, args.service, visits)
    per_year = round(total / args.horizon, 2) if args.horizon > 0 else float("inf")

    print(f"Watch: {args.label}")
    print(f"Ledger: ${args.price:,.0f} purchase + {visits} services x "
          f"${args.service:,.0f} = ${total:,.2f} over {args.horizon:.0f} years")
    print(f"Per ownership year: ${per_year:,.2f}")
    if args.hours_per_day > 0:
        per_kh = per_thousand_hours(total, args.horizon, args.hours_per_day)
        print(f"Per 1,000 wrist hours ({args.hours_per_day:g} h/day): "
              f"${per_kh:,.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
