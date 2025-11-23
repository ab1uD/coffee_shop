class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string.")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._name = value

    def orders(self):
        return self._orders

    def customers(self):
        return list({order.customer for order in self._orders})

   
    def num_orders(self):
        """Return the total number of orders for this coffee."""
        return len(self._orders)

    
    def average_price(self):
        """Return average price across all orders, or None if no orders exist."""
        if not self._orders:
            return None
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)




