import sys
import coinex.ccxt as ccxt_module
sys.modules['ccxt'] = ccxt_module

from coinex.ccxt import coinex as CoinexSync
from coinex.ccxt.async_support.coinex import coinex as CoinexAsync
from coinex.ccxt.pro.coinex import coinex as CoinexWs
