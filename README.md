# coinex-python
Python SDK (sync and async) for Coinex cryptocurrency exchange with Rest and WS capabilities.

- You can check the SDK docs here: [SDK](https://docs.ccxt.com/#/exchanges/coinex)
- You can check Coinex's docs here: [Docs](https://www.google.com/search?q=google+coinex+cryptocurrency+exchange+api+docs)
- Github repo: https://github.com/ccxt/coinex-python
- Pypi package: https://pypi.org/project/coinex-api


## Installation

```
pip install coinex-api
```

## Usage

### Sync

```Python
from coinex import CoinexSync

def main():
    instance = CoinexSync({})
    ob =  instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = instance.fetch_balance()
    # order = instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

main()
```

### Async

```Python
import sys
import asyncio
from coinex import CoinexAsync

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = CoinexAsync({})
    ob =  await instance.fetch_order_book("BTC/USDC")
    print(ob)
    #
    # balance = await instance.fetch_balance()
    # order = await instance.create_order("BTC/USDC", "limit", "buy", 1, 100000)

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```



### Websockets

```Python
import sys
from coinex import CoinexWs

### on Windows, uncomment below:
# if sys.platform == 'win32':
# 	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    instance = CoinexWs({})
    while True:
        ob = await instance.watch_order_book("BTC/USDC")
        print(ob)
        # orders = await instance.watch_orders("BTC/USDC")

    # once you are done with the exchange
    await instance.close()

asyncio.run(main())
```





#### Raw call

You can also construct custom requests to available "implicit" endpoints

```Python
        request = {
            'type': 'candleSnapshot',
            'req': {
                'coin': coin,
                'interval': tf,
                'startTime': since,
                'endTime': until,
            },
        }
        response = await instance.public_post_info(request)
```


## Available methods

### REST Unified

- `create_deposit_address(self, code: str, params={})`
- `create_market_buy_order_with_cost(self, symbol: str, cost: float, params={})`
- `create_order_request(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_order(self, symbol: str, type: OrderType, side: OrderSide, amount: float, price: Num = None, params={})`
- `create_orders(self, orders: List[OrderRequest], params={})`
- `fetch_balance(self, params={})`
- `fetch_borrow_interest(self, code: Str = None, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_closed_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_contract_markets(self, params)`
- `fetch_currencies(self, params={})`
- `fetch_deposit_address(self, code: str, params={})`
- `fetch_deposit_withdraw_fee(self, code: str, params={})`
- `fetch_deposits(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_financial_balance(self, params={})`
- `fetch_funding_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_interval(self, symbol: str, params={})`
- `fetch_funding_rate_history(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_funding_rate(self, symbol: str, params={})`
- `fetch_funding_rates(self, symbols: Strings = None, params={})`
- `fetch_isolated_borrow_rate(self, symbol: str, params={})`
- `fetch_leverage_tiers(self, symbols: Strings = None, params={})`
- `fetch_leverage(self, symbol: str, params={})`
- `fetch_margin_adjustment_history(self, symbol: Str = None, type: Str = None, since: Num = None, limit: Num = None, params={})`
- `fetch_margin_balance(self, params={})`
- `fetch_markets(self, params={})`
- `fetch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_ohlcv(self, symbol: str, timeframe='1m', since: Int = None, limit: Int = None, params={})`
- `fetch_open_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_order_book(self, symbol: str, limit: Int = 20, params={})`
- `fetch_order(self, id: str, symbol: Str = None, params={})`
- `fetch_orders_by_status(self, status, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_position_history(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_position(self, symbol: str, params={})`
- `fetch_positions(self, symbols: Strings = None, params={})`
- `fetch_spot_balance(self, params={})`
- `fetch_spot_markets(self, params)`
- `fetch_swap_balance(self, params={})`
- `fetch_ticker(self, symbol: str, params={})`
- `fetch_tickers(self, symbols: Strings = None, params={})`
- `fetch_time(self, params={})`
- `fetch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `fetch_trading_fee(self, symbol: str, params={})`
- `fetch_trading_fees(self, params={})`
- `fetch_transfers(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `fetch_withdrawals(self, code: Str = None, since: Int = None, limit: Int = None, params={})`
- `add_margin(self, symbol: str, amount: float, params={})`
- `borrow_isolated_margin(self, symbol: str, code: str, amount: float, params={})`
- `cancel_all_orders(self, symbol: Str = None, params={})`
- `cancel_order(self, id: str, symbol: Str = None, params={})`
- `cancel_orders(self, ids, symbol: Str = None, params={})`
- `close_position(self, symbol: str, side: OrderSide = None, params={})`
- `describe(self)`
- `edit_order(self, id: str, symbol: str, type: OrderType, side: OrderSide, amount: Num = None, price: Num = None, params={})`
- `modify_margin_helper(self, symbol: str, amount, addOrReduce, params={})`
- `nonce(self)`
- `reduce_margin(self, symbol: str, amount: float, params={})`
- `repay_isolated_margin(self, symbol: str, code: str, amount, params={})`
- `set_leverage(self, leverage: Int, symbol: Str = None, params={})`
- `set_margin_mode(self, marginMode: str, symbol: Str = None, params={})`
- `transfer(self, code: str, amount: float, fromAccount: str, toAccount: str, params={})`
- `withdraw(self, code: str, amount: float, address: str, tag=None, params={})`

### REST Raw

- `v1_public_get_amm_market(request)`
- `v1_public_get_common_currency_rate(request)`
- `v1_public_get_common_asset_config(request)`
- `v1_public_get_common_maintain_info(request)`
- `v1_public_get_common_temp_maintain_info(request)`
- `v1_public_get_margin_market(request)`
- `v1_public_get_market_info(request)`
- `v1_public_get_market_list(request)`
- `v1_public_get_market_ticker(request)`
- `v1_public_get_market_ticker_all(request)`
- `v1_public_get_market_depth(request)`
- `v1_public_get_market_deals(request)`
- `v1_public_get_market_kline(request)`
- `v1_public_get_market_detail(request)`
- `v1_private_get_account_amm_balance(request)`
- `v1_private_get_account_investment_balance(request)`
- `v1_private_get_account_balance_history(request)`
- `v1_private_get_account_market_fee(request)`
- `v1_private_get_balance_coin_deposit(request)`
- `v1_private_get_balance_coin_withdraw(request)`
- `v1_private_get_balance_info(request)`
- `v1_private_get_balance_deposit_address_coin_type(request)`
- `v1_private_get_contract_transfer_history(request)`
- `v1_private_get_credit_info(request)`
- `v1_private_get_credit_balance(request)`
- `v1_private_get_investment_transfer_history(request)`
- `v1_private_get_margin_account(request)`
- `v1_private_get_margin_config(request)`
- `v1_private_get_margin_loan_history(request)`
- `v1_private_get_margin_transfer_history(request)`
- `v1_private_get_order_deals(request)`
- `v1_private_get_order_finished(request)`
- `v1_private_get_order_pending(request)`
- `v1_private_get_order_status(request)`
- `v1_private_get_order_status_batch(request)`
- `v1_private_get_order_user_deals(request)`
- `v1_private_get_order_stop_finished(request)`
- `v1_private_get_order_stop_pending(request)`
- `v1_private_get_order_user_trade_fee(request)`
- `v1_private_get_order_market_trade_info(request)`
- `v1_private_get_sub_account_balance(request)`
- `v1_private_get_sub_account_transfer_history(request)`
- `v1_private_get_sub_account_auth_api(request)`
- `v1_private_get_sub_account_auth_api_user_auth_id(request)`
- `v1_private_post_balance_coin_withdraw(request)`
- `v1_private_post_contract_balance_transfer(request)`
- `v1_private_post_margin_flat(request)`
- `v1_private_post_margin_loan(request)`
- `v1_private_post_margin_transfer(request)`
- `v1_private_post_order_limit_batch(request)`
- `v1_private_post_order_ioc(request)`
- `v1_private_post_order_limit(request)`
- `v1_private_post_order_market(request)`
- `v1_private_post_order_modify(request)`
- `v1_private_post_order_stop_limit(request)`
- `v1_private_post_order_stop_market(request)`
- `v1_private_post_order_stop_modify(request)`
- `v1_private_post_sub_account_transfer(request)`
- `v1_private_post_sub_account_register(request)`
- `v1_private_post_sub_account_unfrozen(request)`
- `v1_private_post_sub_account_frozen(request)`
- `v1_private_post_sub_account_auth_api(request)`
- `v1_private_put_balance_deposit_address_coin_type(request)`
- `v1_private_put_sub_account_unfrozen(request)`
- `v1_private_put_sub_account_frozen(request)`
- `v1_private_put_sub_account_auth_api_user_auth_id(request)`
- `v1_private_put_v1_account_settings(request)`
- `v1_private_delete_balance_coin_withdraw(request)`
- `v1_private_delete_order_pending_batch(request)`
- `v1_private_delete_order_pending(request)`
- `v1_private_delete_order_stop_pending(request)`
- `v1_private_delete_order_stop_pending_id(request)`
- `v1_private_delete_order_pending_by_client_id(request)`
- `v1_private_delete_order_stop_pending_by_client_id(request)`
- `v1_private_delete_sub_account_auth_api_user_auth_id(request)`
- `v1_private_delete_sub_account_authorize_id(request)`
- `v1_perpetualpublic_get_ping(request)`
- `v1_perpetualpublic_get_time(request)`
- `v1_perpetualpublic_get_market_list(request)`
- `v1_perpetualpublic_get_market_limit_config(request)`
- `v1_perpetualpublic_get_market_ticker(request)`
- `v1_perpetualpublic_get_market_ticker_all(request)`
- `v1_perpetualpublic_get_market_depth(request)`
- `v1_perpetualpublic_get_market_deals(request)`
- `v1_perpetualpublic_get_market_funding_history(request)`
- `v1_perpetualpublic_get_market_kline(request)`
- `v1_perpetualprivate_get_market_user_deals(request)`
- `v1_perpetualprivate_get_asset_query(request)`
- `v1_perpetualprivate_get_order_pending(request)`
- `v1_perpetualprivate_get_order_finished(request)`
- `v1_perpetualprivate_get_order_stop_finished(request)`
- `v1_perpetualprivate_get_order_stop_pending(request)`
- `v1_perpetualprivate_get_order_status(request)`
- `v1_perpetualprivate_get_order_stop_status(request)`
- `v1_perpetualprivate_get_position_finished(request)`
- `v1_perpetualprivate_get_position_pending(request)`
- `v1_perpetualprivate_get_position_funding(request)`
- `v1_perpetualprivate_get_position_adl_history(request)`
- `v1_perpetualprivate_get_market_preference(request)`
- `v1_perpetualprivate_get_position_margin_history(request)`
- `v1_perpetualprivate_get_position_settle_history(request)`
- `v1_perpetualprivate_post_market_adjust_leverage(request)`
- `v1_perpetualprivate_post_market_position_expect(request)`
- `v1_perpetualprivate_post_order_put_limit(request)`
- `v1_perpetualprivate_post_order_put_market(request)`
- `v1_perpetualprivate_post_order_put_stop_limit(request)`
- `v1_perpetualprivate_post_order_put_stop_market(request)`
- `v1_perpetualprivate_post_order_modify(request)`
- `v1_perpetualprivate_post_order_modify_stop(request)`
- `v1_perpetualprivate_post_order_cancel(request)`
- `v1_perpetualprivate_post_order_cancel_all(request)`
- `v1_perpetualprivate_post_order_cancel_batch(request)`
- `v1_perpetualprivate_post_order_cancel_stop(request)`
- `v1_perpetualprivate_post_order_cancel_stop_all(request)`
- `v1_perpetualprivate_post_order_close_limit(request)`
- `v1_perpetualprivate_post_order_close_market(request)`
- `v1_perpetualprivate_post_position_adjust_margin(request)`
- `v1_perpetualprivate_post_position_stop_loss(request)`
- `v1_perpetualprivate_post_position_take_profit(request)`
- `v1_perpetualprivate_post_position_market_close(request)`
- `v1_perpetualprivate_post_order_cancel_by_client_id(request)`
- `v1_perpetualprivate_post_order_cancel_stop_by_client_id(request)`
- `v1_perpetualprivate_post_market_preference(request)`
- `v2_public_get_maintain_info(request)`
- `v2_public_get_ping(request)`
- `v2_public_get_time(request)`
- `v2_public_get_spot_market(request)`
- `v2_public_get_spot_ticker(request)`
- `v2_public_get_spot_depth(request)`
- `v2_public_get_spot_deals(request)`
- `v2_public_get_spot_kline(request)`
- `v2_public_get_spot_index(request)`
- `v2_public_get_futures_market(request)`
- `v2_public_get_futures_ticker(request)`
- `v2_public_get_futures_depth(request)`
- `v2_public_get_futures_deals(request)`
- `v2_public_get_futures_kline(request)`
- `v2_public_get_futures_index(request)`
- `v2_public_get_futures_funding_rate(request)`
- `v2_public_get_futures_funding_rate_history(request)`
- `v2_public_get_futures_position_level(request)`
- `v2_public_get_futures_liquidation_history(request)`
- `v2_public_get_futures_basis_history(request)`
- `v2_public_get_assets_deposit_withdraw_config(request)`
- `v2_public_get_assets_all_deposit_withdraw_config(request)`
- `v2_private_get_account_subs(request)`
- `v2_private_get_account_subs_api_detail(request)`
- `v2_private_get_account_subs_info(request)`
- `v2_private_get_account_subs_api(request)`
- `v2_private_get_account_subs_transfer_history(request)`
- `v2_private_get_account_subs_spot_balance(request)`
- `v2_private_get_account_trade_fee_rate(request)`
- `v2_private_get_assets_spot_balance(request)`
- `v2_private_get_assets_futures_balance(request)`
- `v2_private_get_assets_margin_balance(request)`
- `v2_private_get_assets_financial_balance(request)`
- `v2_private_get_assets_amm_liquidity(request)`
- `v2_private_get_assets_credit_info(request)`
- `v2_private_get_assets_margin_borrow_history(request)`
- `v2_private_get_assets_margin_interest_limit(request)`
- `v2_private_get_assets_deposit_address(request)`
- `v2_private_get_assets_deposit_history(request)`
- `v2_private_get_assets_withdraw(request)`
- `v2_private_get_assets_transfer_history(request)`
- `v2_private_get_spot_order_status(request)`
- `v2_private_get_spot_batch_order_status(request)`
- `v2_private_get_spot_pending_order(request)`
- `v2_private_get_spot_finished_order(request)`
- `v2_private_get_spot_pending_stop_order(request)`
- `v2_private_get_spot_finished_stop_order(request)`
- `v2_private_get_spot_user_deals(request)`
- `v2_private_get_spot_order_deals(request)`
- `v2_private_get_futures_order_status(request)`
- `v2_private_get_futures_batch_order_status(request)`
- `v2_private_get_futures_pending_order(request)`
- `v2_private_get_futures_finished_order(request)`
- `v2_private_get_futures_pending_stop_order(request)`
- `v2_private_get_futures_finished_stop_order(request)`
- `v2_private_get_futures_user_deals(request)`
- `v2_private_get_futures_order_deals(request)`
- `v2_private_get_futures_pending_position(request)`
- `v2_private_get_futures_finished_position(request)`
- `v2_private_get_futures_position_margin_history(request)`
- `v2_private_get_futures_position_funding_history(request)`
- `v2_private_get_futures_position_adl_history(request)`
- `v2_private_get_futures_position_settle_history(request)`
- `v2_private_post_account_subs(request)`
- `v2_private_post_account_subs_frozen(request)`
- `v2_private_post_account_subs_unfrozen(request)`
- `v2_private_post_account_subs_api(request)`
- `v2_private_post_account_subs_edit_api(request)`
- `v2_private_post_account_subs_delete_api(request)`
- `v2_private_post_account_subs_transfer(request)`
- `v2_private_post_account_settings(request)`
- `v2_private_post_assets_margin_borrow(request)`
- `v2_private_post_assets_margin_repay(request)`
- `v2_private_post_assets_renewal_deposit_address(request)`
- `v2_private_post_assets_withdraw(request)`
- `v2_private_post_assets_cancel_withdraw(request)`
- `v2_private_post_assets_transfer(request)`
- `v2_private_post_assets_amm_add_liquidity(request)`
- `v2_private_post_assets_amm_remove_liquidity(request)`
- `v2_private_post_spot_order(request)`
- `v2_private_post_spot_stop_order(request)`
- `v2_private_post_spot_batch_order(request)`
- `v2_private_post_spot_batch_stop_order(request)`
- `v2_private_post_spot_modify_order(request)`
- `v2_private_post_spot_modify_stop_order(request)`
- `v2_private_post_spot_cancel_all_order(request)`
- `v2_private_post_spot_cancel_order(request)`
- `v2_private_post_spot_cancel_stop_order(request)`
- `v2_private_post_spot_cancel_batch_order(request)`
- `v2_private_post_spot_cancel_batch_stop_order(request)`
- `v2_private_post_spot_cancel_order_by_client_id(request)`
- `v2_private_post_spot_cancel_stop_order_by_client_id(request)`
- `v2_private_post_futures_order(request)`
- `v2_private_post_futures_stop_order(request)`
- `v2_private_post_futures_batch_order(request)`
- `v2_private_post_futures_batch_stop_order(request)`
- `v2_private_post_futures_modify_order(request)`
- `v2_private_post_futures_modify_stop_order(request)`
- `v2_private_post_futures_cancel_all_order(request)`
- `v2_private_post_futures_cancel_order(request)`
- `v2_private_post_futures_cancel_stop_order(request)`
- `v2_private_post_futures_cancel_batch_order(request)`
- `v2_private_post_futures_cancel_batch_stop_order(request)`
- `v2_private_post_futures_cancel_order_by_client_id(request)`
- `v2_private_post_futures_cancel_stop_order_by_client_id(request)`
- `v2_private_post_futures_close_position(request)`
- `v2_private_post_futures_adjust_position_margin(request)`
- `v2_private_post_futures_adjust_position_leverage(request)`
- `v2_private_post_futures_set_position_stop_loss(request)`
- `v2_private_post_futures_set_position_take_profit(request)`

### WS Unified

- `describe(self)`
- `watch_balance(self, params={})`
- `watch_my_trades(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_ticker(self, symbol: str, params={})`
- `watch_tickers(self, symbols: Strings = None, params={})`
- `watch_trades(self, symbol: str, since: Int = None, limit: Int = None, params={})`
- `watch_trades_for_symbols(self, symbols: List[str], since: Int = None, limit: Int = None, params={})`
- `watch_order_book_for_symbols(self, symbols: List[str], limit: Int = None, params={})`
- `watch_order_book(self, symbol: str, limit: Int = None, params={})`
- `watch_orders(self, symbol: Str = None, since: Int = None, limit: Int = None, params={})`
- `watch_bids_asks(self, symbols: Strings = None, params={})`
- `authenticate(self, type: str)`

## Contribution
- Give us a star :star:
- Fork and Clone! Awesome
- Select existing issues or create a new issue.