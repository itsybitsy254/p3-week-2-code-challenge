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
code editor

Clone the Repository:

'''git clone https://github.com/itsybitsy254/p3-week-2-code-challenge.git'''
Navigate to the Project Directory:

open file directory:
'''cd p3-week-2-code-challenge/'''
Install Dependencies:

Run the following command to install the required dependencies:

'''pipenv install'''
Activate the Virtual Environment:

To start working inside the virtual environment, run:

'''pipenv shell'''

To run project:
**python main.py**
Main.py acts as the debug.py
Inside main.py, you can create sample instances of Customer, Coffee, and Order and call their methods to test how they work.

Running the Tests:
You can run the test suite using pytest to verify the functionality of the methods:

'''pytest'''

Structure
The project is structured as follows:
Customer. py:
Defines the Customer class.
Contains methods to create customers, retrieve orders, retrieve coffees, and create new orders.
Ensures that customer names are validated and are within the required length.

Coffee. py:
Defines the Coffee class.
Contains methods to manage coffee orders and retrieve a list of customers who have ordered a particular coffee.
Also includes aggregate methods like num_orders (total number of orders for the coffee) and average_price (average price for a coffee).

Order. py:
Defines the Order class.
Manages the creation of an order that links a customer, a coffee, and the price for the order.
Ensures that prices are validated and within the allowed range.