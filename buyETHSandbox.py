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
if current_price > USD(40.00):
    buy_order = Order(api.new_order('buy', 'ethusd', ETH(0.008), current_price))
