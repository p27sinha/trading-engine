import uuid
from datetime import datetime

class Order:
    def __init__(self, side, price, quantity):
        self.id = str(uuid.uuid4())
        self.side = side  # 'buy' or 'sell'
        self.price = price
        self.quantity = quantity
        self.timestamp = datetime.now()

    def __repr__(self):
        return f"{self.side.upper()} {self.quantity}@{self.price} [{self.timestamp}]"