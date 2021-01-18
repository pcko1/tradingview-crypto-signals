# tradingview-crypto-signals
A local HTTP server to fetch cryptocurrency BUY/SELL signals from TradingView, built on top of the `tradingview_ta` [package](https://github.com/deathlyface/python-tradingview-ta). The returned data are in JSON format and can be easily parsed using any language.

## Example

### Docker

It takes **one line** to get the server up and running using `docker`, without even cloning the repo.

```bash
docker run -it -p 8002:6666 pcko1/tvcs:latest --pairs BTCUSDT,ETHBTC,LINKUSDT --interval 1h --exchange BINANCE
```

After the server starts, you can access the results at http://localhost/8002. 

The results are in JSON format and the timestamp is UTC:

```json
[ { "pair": "BTCUSDT", "exchange": "BINANCE", "interval": "1h", "recommendation": "BUY", "votes": { "buy": 16, "sell": 3, "neutral": 9 }, "timestamp": 1611006994 }, { "pair": "ETHBTC", "exchange": "BINANCE", "interval": "1h", "recommendation": "BUY", "votes": { "buy": 13, "sell": 6, "neutral": 9 }, "timestamp": 1611006994 }, { "pair": "LINKUSDT", "exchange": "BINANCE", "interval": "1h", "recommendation": "SELL", "votes": { "buy": 10, "sell": 9, "neutral": 9 }, "timestamp": 1611006995 } ]
```


## Arguments

- `exchange`: All exchanges supported by `tradingview_ta`, e.g. `BINANCE` (default) or `BITTREX`
- `pairs`: All crypto pairs found on the chosen `exchange`, e.g. `BTCUSDT`(default)
- `interval`: All time intervals supported by `tradingview_ta`, i.e. `1m`, `5m`, `15m`, `1h`, `4h`, `1d` (default), `1w`, `1M`.

## Target Machines
You may find pre-built containers for different OS and H/W architectures:

- `pcko1/tvcs:linux/amd64`
- `pcko1/tvcs:linux/arm64` 
- `pcko1/tvcs:linux/arm/v/7`
- `pcko1/tvcs:linux/arm/v/6`