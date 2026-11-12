# PythonBusTicket
Python Project for buying bus tickets, with customers and admin roles, CSV storage and input validation

# Bus Ticket Project  (Python)

A command-line bus ticketing system built in Python as university coursework. Customers can browse ticket categories, build a basket and check out, while an admin can view sales and update prices.

Features
Customer menu: browse ticket categories, add tickets to a basket, view the total and check out
Admin menu (password protected): view a sales report (tickets sold per type) and search for a ticket to change its price
Data from CSV: ticket products are loaded from mobile_products.csv, and completed orders are saved to orders.csv
Input validation: menu choices must be valid numbers in range, and text input cannot be empty
Error handling: the sales report handles a missing orders file

Concepts used
Object-oriented programming: topup (ticket), ticketCategory, User and Admin (inheritance) classes
File handling with Python's csv module (DictReader, writer)
Lists, dictionaries, loops and functions split across modules
try/except error handling

Project structure
BusTicket.py: main program and menus
Class.py: ticket, category and user classes
userInput.py: reusable input validation functions

How to run
python BusTicket.py

Requires Python 3 and mobile_products.csv in the same folder. Orders are written to orders.csv.

What I'd improve
Store the admin password securely instead of in the code
Save price changes back to the CSV so they persist
Add unit tests and format prices to two decimal places
