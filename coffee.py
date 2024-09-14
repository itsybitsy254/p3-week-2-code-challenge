class Coffee:
    def __init__(self, name):
        self.name = name 
        self._orders = [] 
        self._customers = [] 

    @property
    def name(self):
        return getattr(self, '_name', None) 

    @name.setter
    def name(self, value):
        if not hasattr(self, '_name') and isinstance(value, str) and len(value) >= 3:
            self._name = value
        elif hasattr(self, '_name'):
            raise Exception("Name already set and cannot be changed.")
        else:
            raise ValueError("Name must be a string with at least 3 characters")

    def add_order(self, new_order):
        # Check if the order already exists to prevent adding it twice
        if new_order not in self._orders:
            self._orders.append(new_order)
    
    def add_customer(self, new_customer):
        # Add customer only if not already present
        if new_customer not in self._customers:
            self._customers.append(new_customer)
    
    def orders(self):
        # Return a list of all orders for this coffee
        return self._orders
    
    def customers(self):
        # Return a unique list of all customers who have ordered this coffee
        return list(set(order.customer for order in self._orders))
    
    def num_orders(self):
        # Return the total number of times this coffee has been ordered
        return len(self._orders)
    
    def average_price(self):
        # Calculate the average price of the orders
        if self._orders:
            total_price = sum(order.price for order in self._orders)
            return total_price / len(self._orders)
        return 0

    def __str__(self):
        return f"Coffee(name={self.name})"
