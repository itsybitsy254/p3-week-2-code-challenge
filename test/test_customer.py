import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.coffee1 = Coffee("Coffee1")
        self.coffee2 = Coffee("Coffee2")
        self.customer = Customer("Customer1")

    def test_create_order(self):
        order = self.customer.create_order(self.coffee1, 3.5)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee1)
        self.assertEqual(order.price, 3.5)
        self.assertIn(order, self.customer.orders())

    def test_num_orders(self):
        self.customer.create_order(self.coffee1, 3.5)
        self.customer.create_order(self.coffee2, 4.0)
        self.assertEqual(self.customer.num_orders(), 2)

    def test_average_price(self):
        self.customer.create_order(self.coffee1, 3.5)
        self.customer.create_order(self.coffee2, 4.5)
        self.assertAlmostEqual(self.customer.average_price(), 4.0)

    def test_customer_coffees(self):
        self.customer.create_order(self.coffee1, 3.5)
        self.customer.create_order(self.coffee2, 4.0)
        coffees = self.customer.coffees()
        self.assertIn(self.coffee1, coffees)
        self.assertIn(self.coffee2, coffees)

if __name__ == "__main__":
    unittest.main()
