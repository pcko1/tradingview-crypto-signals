from dataclasses import dataclass


@dataclass(frozen=True)
class ExchangesEnum:
    BINANCE: str = "BINANCE"
    BITTREX: str = "BITTREX"