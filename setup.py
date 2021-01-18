from setuptools import setup

setup(
    name="tvcs",
    version="0.0.1",
    description="Fetch cryptocurrency signals from TradeView.",
    url="https://github.com/pcko1/tradeview-crypto-signals",
    author="Panagiotis-Christos Kotsias",
    author_email="kotsias.pan@gmail.com",
    license="MIT",
    packages=["tvcs", "tvcs.server"],
    install_requires=["tradingview_ta", "coverage"],
    include_package_data=True,
    zip_safe=False,
)