import random
import csv
from engine import TradingEngine

NUM_ORDERS = 500  # you can scale this up
PRICE_RANGE = (90, 110)
QTY_RANGE = (1, 20)

engine = TradingEngine()

# Prepare CSV logging
with open('trades.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Buy_ID', 'Sell_ID', 'Price', 'Quantity'])  # header

    for _ in range(NUM_ORDERS):
        side = random.choice(['buy', 'sell'])
        price = random.randint(*PRICE_RANGE)
        quantity = random.randint(*QTY_RANGE)

        order_id, trades = engine.place_order(side, price, quantity)

        # Print order details
        print(f"Placed {side.upper()} {quantity}@{price} | ID: {order_id}")

        # Log each trade
        for trade in trades:
            writer.writerow(trade)  # (buy_id, sell_id, price, qty)
