# coinex-python
Python SDK (sync and async) for Coinex with Rest and WS capabilities.

You can check Coinex's docs here: [Docs](https://ccxt.com)


You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/coinex)

*This package derives from CCXT and allows you to call pretty much every endpoint by either using the unified CCXT API or calling the endpoints directly*

## Installation

```
pip install coinex-api
```

## Usage

### Async

```Python
from coinex_api import CoinexAsync

async def main():
    instance = CoinexAsync({})
    order = await instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Sync

```Python
from coinex_api import CoinexSync

def main():
    instance = CoinexSync({})
    order =  instance.create_order(__EXAMPLE_SYMBOL__, "limit", "buy", 1, 100000)
```

### Websockets

```Python
from coinex_api import CoinexWs

async def main():
    instance = CoinexWs({})
    while True:
        orders = await instance.watch_orders(__EXAMPLE_SYMBOL__)
```

