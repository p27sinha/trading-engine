import heapq
from collections import defaultdict

class OrderBook:
    def __init__(self):
        self.buys = []  # max-heap
        self.sells = []  # min-heap
        self.orders = {}

    def add_order(self, order):
        entry = (order.price if order.side == 'sell' else -order.price, order.timestamp, order)
        heapq.heappush(self.sells if order.side == 'sell' else self.buys, entry)
        self.orders[order.id] = order

    def match_orders(self):
        trades = []
        while self.buys and self.sells:
            best_buy = self.buys[0][2]
            best_sell = self.sells[0][2]
            if -self.buys[0][0] >= self.sells[0][0]:  # price match
                trade_qty = min(best_buy.quantity, best_sell.quantity)
                trades.append((best_buy.id, best_sell.id, best_sell.price, trade_qty))
                best_buy.quantity -= trade_qty
                best_sell.quantity -= trade_qty
                if best_buy.quantity == 0: heapq.heappop(self.buys)
                if best_sell.quantity == 0: heapq.heappop(self.sells)
            else:
                break
        return trades