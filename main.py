from coffee import Coffee
from customer import Customer
from order import Order

# Example use
def main():
    # Create instances of Coffee
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")

    # Create instances of Customer
    jack = Customer("Jack Wells")
    jay = Customer("Jay Cole")

    # Create orders for existing customers
    jack_order_1 = jack.create_order(coffee1, 3.5)
    jack_order_2 = jack.create_order(coffee2, 4.0)
    jay_order_1 = jay.create_order(coffee2, 4.5)

    # Adding a new customer (user)
    will = Customer("Willy Smith")  # New customer

    # Create orders for the new customer
    will_order_1 = will.create_order(coffee1, 4.0)   
    will_order_2 = will.create_order(coffee2, 5.0)    

    # Print details
    print(f"{jack.name} has ordered {jack.num_orders()} coffee's.")
    print(f"Average price of Jack's orders: ${jack.average_price():.2f}")
    print(f"Jack's ordered coffee's: {jack.coffee_order_names()}")

    print(f"{jay.name} has ordered {jay.num_orders()} coffee.")
    print(f"Average price of Jay's orders: ${jay.average_price():.2f}")
    print(f"Jay's ordered coffee: {jay.coffee_order_names()}")

    print(f"{will.name} has ordered {will.num_orders()} coffee's.")
    print(f"Average price of Will's orders: ${will.average_price():.2f}")
    print(f"Will's ordered coffee's: {will.coffee_order_names()}")

    print(f"{coffee1.name} has been ordered {coffee1.num_orders()} times.")
    print(f"Customers who ordered {coffee1.name}: {[customer.name for customer in coffee1.customers()]}")
    print(f"Average price of {coffee1.name}: ${coffee1.average_price():.2f}")

    print(f"{coffee2.name} has been ordered {coffee2.num_orders()} times.")
    print(f"Customers who ordered {coffee2.name}: {[customer.name for customer in coffee2.customers()]}")
    print(f"Average price of {coffee2.name}: ${coffee2.average_price():.2f}")

if __name__ == "__main__":
    main()
