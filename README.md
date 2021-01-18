# tradingview-crypto-signals
A simple HTTP server to fetch cryptocurrency BUY/SELL signals from TradingView.

## Example

```bash
docker run -it -p 8002:6666 pcko1/tvcs:latest --pairs ETHBTC,LINKUSDT --interval 1h --exchange BINANCE
```

## Re-build the image
```bash
docker build -t tvcs:latest --no-cache .
```