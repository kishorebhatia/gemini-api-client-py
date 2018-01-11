# Crypto transact using Gemini Exchange API's (WS and REST)
:moneybag: Python bindings for trading Bitcoin, Ethereum, & USD on the Gemini.com Exchange API.

---

## Quickstart

1. **Download & install**
- Python3.6
- Git clone and install Dependencies
```bash
git clone
cd gemini-api-client-py
pip3 install -r requirements.txt
```

2. **Open https://exchange.gemini.com/settings/api and get an API key & secret**
```bash
cp secrets_default.py secrets.py
nano secrets.py  # add key & secret here
```

3. **Start hacking! First with Sandbox API's (Test everything here first!!!)**
```bash
python3.6 ./buyETHSandbox.py
```

4. **Then with Real Exchange API**
```bash
nano settings.py                   # Confirm your API URL's
python3.6 ./buyEth.py        # Buy ETH
```

## Configuration

 - **API Key Secrets:** `secrets.py`
 - **API URL:** `settings.py`

## API Documentation

```python
import gemini_api as api
from symbols import Order, USD, BTC, ETH
```

### Data Types

**Currencies:**

 - `symbols.USD`: US Dollar `USD(1.25)`
 - `symbols.BTC`: Bitcoin   `BTC(0.000001)`
 - `symbols.ETH`: Ethereum  `ETH(0.0001)`

All currency symbols are based on the base type `symbols.Currency`.

**Order:**
All API functions that deal with order data like `new_order` or `order_status` return a raw json dict from Gemini with the schema below.  It can be converted to a type-checked python object by using `Order(order_json)`.
```python
order_json = {
    "order_id": "44375901",
    "id": "44375901",
    "symbol": "btcusd",
    "exchange": "gemini",
    "avg_execution_price": "400.00",
    "side": "buy",
    "type": "exchange limit",
    "timestamp": "1494870642",
    "timestampms": 1494870642156,
    "is_live": False,
    "is_cancelled": False,
    "is_hidden": False,
    "was_forced": False,
    "executed_amount": "3",
    "remaining_amount": "0",
    "options": [],
    "price": "400.00",
    "original_amount": "3",
}
buy_order = Order(order_json)
order_id = buy_order.id       # values can be accessed as properties
```

### REST API Functions
The Gemini REST API functions documentation can be found here:  
https://docs.gemini.com/rest-api/#requests

**`api.ticker(symbol: str) -> dict`:**  
Get the ticker price info for a given symbol, e.g.:
```python
ticker_info = api.ticker('ethusd')
# {'bid': '914.00', 'ask': '914.44', 'volume': {'ETH': '94530.56656129', 'USD': '83955829.9730076926', 'timestamp': 1515014100000}, 'last': '915.39'}
last_price = USD(ticker_info['last'])
```

**`api.new_order(side: str, symbol: str, amt: Currency, price: Currency) -> dict`:**  
Submit a new order to Gemini, e.g:
```python
buy_order = Order(api.new_order('buy', 'ethusd', ETH(0.01), USD(965)))
sell_order = Order(api.new_order('sell', 'ethusd', ETH(0.01), USD(965)))
```

**`api.order_status(order_id: str) -> dict`:**  
Get the updated order info json from Gemini for a given order_id, e.g.:
```python
buy_order = Order(api.order_status('44375901'))
print(buy_order.filled_amt)
```

### WebSocket API Functions
The Gemini WebSocket API functions documentation can be found here:  
https://docs.gemini.com/websocket-api/#websocket-request

**`api.order_events(order_id: str) -> Generator[dict]`:**  
Get a live-updating stream of order events via WebSocket e.g.:
```python
for event in api.order_events('44375901'):
    print(event)
```

## Roadmap

* Add GDAX/Coinbase Exchange API bindings

## Developer Info

This repo uses gemini-api PY lib courtesy crypto-trader https://github.com/pirate/crypto-trader and is built on Python 3.6 and uses MyPy for type checking.

## Disclaimer

I'm not responsible for any money you lose from this code.  The code is MIT Licensed.
