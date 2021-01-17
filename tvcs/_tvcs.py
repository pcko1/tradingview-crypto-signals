import tradingview_ta as tv

from tvcs.enums import ExchangesEnum as exchanges


class TVCS:
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
        return self._handler.get_analysis().summary

    def get_signal(
        self,
        symbol: str,
        exchange: str = exchanges.BINANCE,
        interval: str = tv.Interval.INTERVAL_1_DAY,
    ) -> dict:
        print(symbol, exchange, interval)
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
