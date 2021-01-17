import argparse
import re

from tvcs import TVCS


def main(args):
    oracle = TVCS()
    for pair in re.split(",", args.pairs):
        print(
            oracle.get_signal(
                symbol=pair, exchange=args.exchange, interval=args.interval
            )
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Poll TradingView for crypto signals.")
    parser.add_argument(
        "--pairs",
        type=str,
        default="BTCUSDT",
        help="Pair or comma-separated list of pairs.",
    )
    parser.add_argument(
        "--exchange",
        type=str,
        default="BINANCE",
        help="Exchange to get data from.",
    )
    parser.add_argument(
        "--interval",
        type=str,
        default="1d",
        help="Interval to calculate the signal for.",
    )

    args = parser.parse_args()
    main(args)
