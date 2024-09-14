import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    
    def setUp(self):
        self.coffee = Coffee("CoffeeType")
        self.customer = Customer("Customer1")
    
    def test_add_order(self):
        order = Order(self.customer, self.coffee, 3.5)
        self.coffee.add_order(order)
        self.assertIn(order, self.coffee.orders())

    def test_num_orders(self):
        order = Order(self.customer, self.coffee, 3.5)
        self.coffee.add_order(order)
        self.assertEqual(self.coffee.num_orders(), 1)

    def test_average_price(self):
        order1 = Order(self.customer, self.coffee, 3.5)
        order2 = Order(self.customer, self.coffee, 4.5)
        self.coffee.add_order(order1)
        self.coffee.add_order(order2)
        self.assertAlmostEqual(self.coffee.average_price(), 4.0)

if __name__ == "__main__":
    unittest.main()
