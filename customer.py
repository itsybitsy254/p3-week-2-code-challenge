from coffee import Coffee
from order import Order

class Customer:
    def __init__(self, name):
        self.name = name  # This will use the setter to validate and set the name
        self._orders = []

    @property
    def name(self):
        return getattr(self, '_name', None) 

    @name.setter
    def name(self, value):
        if not hasattr(self, '_name') and isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        elif hasattr(self, '_name'):
            raise Exception("Name already exists and cannot be changed.")
        else:
            raise Exception("Name must be a string between 1 and 15 characters")

    def add_order(self, new_order):
        if isinstance(new_order, Order) and new_order not in self._orders:
            self._orders.append(new_order)

    def orders(self):
        # Return a list of all orders for this customer
        return [order for order in self._orders if isinstance(order, Order)]

    def coffees(self):
        # Return a unique list of all coffees this customer has ordered
        coffees = {order.coffee for order in self._orders if isinstance(order.coffee, Coffee)}
        return list(coffees)
    
    def coffee_order_names(self):
        """Return a list of coffee names ordered by the customer."""
        return [order.coffee.name for order in self._orders if isinstance(order.coffee, Coffee)]

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise Exception("The coffee must be an instance of Coffee.")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise Exception("Price must be a number between 1.0 and 10.0 inclusive.")
        
        # Create a new Order instance
        new_order = Order(customer=self, coffee=coffee, price=price)
        
        # Add the new order to the customer's orders and coffee orders
        self.add_order(new_order)
        coffee.add_order(new_order)
        coffee.add_customer(self)
        
        return new_order

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0  
        
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)
