import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    
    def setUp(self):
        self.coffee = Coffee("CoffeeType")
        self.customer = Customer("Customer1")
    
    def test_order_creation(self):
        order = Order(self.customer, self.coffee, 3.5)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 3.5)
    
    def test_invalid_price(self):
        with self.assertRaises(Exception):
            Order(self.customer, self.coffee, 0.5)  # Invalid price
        
        with self.assertRaises(Exception):
            Order(self.customer, self.coffee, 15.0)  # Invalid price

if __name__ == "__main__":
    unittest.main()
