import os
import sys

from random import randint
from datetime import datetime
from time import sleep
from decimal import Decimal

import gemini_api as api
from symbols import Order, ETH, USD

current_price = USD(api.ticker('ethusd')['last'])
print(current_price)
if current_price > USD(1000.00):
    buy_order = Order(api.new_order('buy', 'ethusd', ETH(0.008), current_price))
"""order_events only works for Private API with realtime order events - not applicable to sandbox WS api """
    for event in api.order_events(buy_order.id):
        print(event)
