## Restaurant Billing System

## Overview

This Python script implements a simple restaurant billing system. It allows customers to view a menu, place orders, and receive a bill summary with applicable discounts and taxes. The system tracks ordered items, calculates the subtotal, applies a discount for orders above 500 Rs, adds a 5% tax, and displays a detailed bill summary.

## Features





Menu Display: Shows a list of available food and drink items with their prices.



Order Placement: Users can input items to order, and the system validates if the item exists in the menu.



Order Tracking: Keeps track of all ordered items for a summary at the end.



Discount Calculation: Applies a 10% discount for orders with a subtotal exceeding 500 Rs.



Tax Calculation: Adds a 5% tax to the subtotal.



Bill Summary: Displays a detailed summary of ordered items, quantities, subtotal, discount (if applicable), tax, and total amount.

## Requirements





Python 3.x



Standard library module: collections (used for Counter to summarize orders)

No external dependencies are required.

## How to Run





Save the script as restaurant_billing.py.



Ensure Python 3.x is installed on your system.



Run the script using the command:

python restaurant_billing.py



## Follow the prompts to:





View the menu.



Enter the name of the item you want to order (case-insensitive, automatically capitalized).



Choose whether to add another item (yes to continue, no to finalize).



After finalizing the order, the system will display a bill summary with the subtotal, discount (if applicable), tax, and total amount.

## Code Structure





Menu: A dictionary containing items and their prices in Rs.



Order Loop: A while loop to collect user orders, validate items, and track the order list.



## Calculations:





Subtotal: Sum of prices for all ordered items.



Discount: 10% of the subtotal if it exceeds 500 Rs.



Tax: 5% of the subtotal.



Total: Subtotal minus discount plus tax.



Bill Summary: Uses Counter from the collections module to group items by quantity and display the final bill.
