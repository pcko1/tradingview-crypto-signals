import argparse
import http.server
import json
import re

from tvcs import TVCSClient


class RequestHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, pairs, exchange, interval, client):
        self.pairs = pairs
        self.exchange = exchange
        self.interval = interval
        self.client = client

    def __call__(self, *args, **kwargs):
        """ Handle a request """
        super().__init__(*args, **kwargs)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

    def do_GET(self):
        self.do_HEAD()
        signals = []
        for i, pair in enumerate(re.split(",", self.pairs)):
            signals.append(
                self.client.get_signal(
                    symbol=pair, exchange=self.exchange, interval=self.interval
                )
            )
        self.wfile.write(json.dumps(signals, indent=4).encode("utf-8"))


def main(args):
    client = TVCSClient()
    handler = RequestHandler(args.pairs, args.exchange, args.interval, client)
    server = http.server.HTTPServer(("", args.port), handler)
    server.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Start a local webserver for TradingView signals."
    )
    parser.add_argument(
        "--port", type=int, default=6666, help="Port for the server to listen to."
    )
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
