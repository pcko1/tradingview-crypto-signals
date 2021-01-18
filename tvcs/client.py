import argparse
import re
from datetime import datetime, timezone

import tradingview_ta as tv

from tvcs.enums import ExchangesEnum as exchanges


class TVCSClient:
    def __init__(self):
        self._handler = tv.TA_Handler()
        self._handler.set_screener_as_crypto()

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._handler.set_symbol_as(value)
        self._symbol = value

    @property
    def exchange(self):
        return self._exchange

    @exchange.setter
    def exchange(self, value):
        self._handler.set_exchange_as_crypto_or_stock(value)
        self._exchange = value

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        self._handler.set_interval_as(value)
        self._interval = value

    def _format_results(self, res: dict) -> dict:
        dt = datetime.now()
        utc_time = dt.replace(tzinfo=timezone.utc)
        utc_timestamp = int(utc_time.timestamp())
        res = {
            "pair": self.symbol,
            "exchange": self.exchange,
            "interval": self.interval,
            "recommendation": res["RECOMMENDATION"],
            "votes": {
                "buy": res["BUY"],
                "sell": res["SELL"],
                "neutral": res["NEUTRAL"],
            },
            "timestamp": utc_timestamp,
        }
        return res

    def specify_signal(self, symbol: str, exchange: str, interval: str):
        """Specify symbol, exchange and interval for a signal.

        Args:
            symbol (str): The pair symbol, e.g. "BTCUSDT"
            exchange (str): The crypto exchange, e.g. "BINANCE"
            interval (str): The time interval, e.g. "1d"
        """
        self.symbol = symbol
        self.exchange = exchange
        self.interval = interval

    def get_specific_signal(self) -> dict:
        """Get the signal for prespecified query params.

        Returns:
            dict: The dict with the signal and all subsignal counts
        """
        return self._format_results(self._handler.get_analysis().summary)

    def get_signal(
        self,
        symbol: str,
        exchange: str = exchanges.BINANCE,
        interval: str = tv.Interval.INTERVAL_1_DAY,
    ) -> dict:
        """Specify query params and get a trade signal.

        Args:
            symbol (str): The pair symbol, e.g. "BTCUSDT"
            exchange (str, optional): The crypto exchange. Defaults to "BINANCE".
            interval (str, optional): The time interval. Defaults to "1d".

        Returns:
            dict: The dict with the signal and all subsignal counts
        """
        self.specify_signal(symbol, exchange, interval)
        return self.get_specific_signal()


def main(args):
    client = TVCSClient()
    for pair in re.split(",", args.pairs):
        print(
            client.get_signal(
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
