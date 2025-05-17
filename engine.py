from order import Order
from order_book import OrderBook

class TradingEngine:
    def __init__(self):
        self.book = OrderBook()

    def place_order(self, side, price, quantity):
        order = Order(side, price, quantity)
        self.book.add_order(order)
        trades = self.book.match_orders()
        return order.id, trades