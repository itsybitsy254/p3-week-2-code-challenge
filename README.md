# p3-week-2-code-challenge


Coffee Shop Project
This project is a simple domain model of a coffee shop using Python. We have three main models: Customer, Coffee, and Order. The relationships between these models include:

A Customer can place many Orders.
A Coffee can have many Orders.
An Order belongs to both a Customer and a Coffee.
This results in a many-to-many relationship between Coffee and Customer.

Getting Started
Prerequisites
Python 3.x installed on your machine
pipenv for virtual environment and dependency management
Setup

Clone the Repository:

'''git clone https://github.com/itsybitsy254/p3-week-2-code-challenge.git'''
Navigate to the Project Directory:

open file directory:
'''cd p3-week-2-code-challenge.git'''
Install Dependencies:

Run the following command to install the required dependencies:

'''pipenv install'''
Activate the Virtual Environment:

To start working inside the virtual environment, run:

'''pipenv shell'''

To run project:
'''python main.py'''
Main.py acts as the debug.py
Inside main.py, you can create sample instances of Customer, Coffee, and Order and call their methods to test how they work.

Running the Tests:
You can run the test suite using pytest to verify the functionality of the methods:

'''pytest'''

Project Structure
Domain Models
Customer
Properties:
name: A customer's name, which must be a string between 1 and 15 characters.
Methods:
orders(): Returns a list of all the orders made by the customer.
coffees(): Returns a unique list of all coffees the customer has ordered.
create_order(coffee, price): Creates a new Order associated with this customer and the specified Coffee at the given price.
num_orders(): Returns the total number of orders placed by the customer.
average_price(): Returns the average price of all orders placed by the customer.
Properties:
name: The name of the coffee, which must be a string of at least 3 characters.
Methods:
orders(): Returns a list of all orders for that coffee.
customers(): Returns a unique list of all customers who have ordered this coffee.
num_orders(): Returns the total number of times this coffee has been ordered.
average_price(): Returns the average price paid for this coffee across all orders.
Order
Properties:
customer: The Customer who placed the order.
coffee: The Coffee that was ordered.
price: The price of the order, which must be a float between 1.0 and 10.0.
Key Features
Object Relationship Methods
Customer-Coffee Relationship: Since a customer can order multiple coffees and a coffee can be ordered by many customers, this creates a many-to-many relationship.
Order Tracking: Track which customer ordered which coffee and the total amount spent on each coffee by a customer.
Aggregate Methods: Aggregate data like the number of orders for each coffee, the total and average price of the orders, and which customer has spent the most on a particular coffee.
Error Handling
For any invalid inputs (e.g., invalid name length, price out of range), the system will raise an Exception. To enable this functionality, make sure you uncomment the necessary lines in the provided test files.
