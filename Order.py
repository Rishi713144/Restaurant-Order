menu = {
    'Pizza': 120,
    'Burger': 80,
    'Coffee': 70,
    'Pasta': 100,
    'Sandwich': 100,
    'Tea': 50,
    'Coke': 60,
    'Juice': 70,
    'Milkshake': 120,
    'Pepsi': 70,
    'Sprite': 70,
    'Fanta': 70,
    'Water': 50
}

print("Welcome To Our Restaurant")
print("--- Menu ---")
for item, price in menu.items():
    print(f"{item}: {price} Rs")
print("------------")

order_total = 0
order_list = []  # To track ordered items for summary

while True:
    item = input("Enter the item you want to order: ").capitalize()
    if item in menu:
        order_total += menu[item]
        order_list.append(item)
        print(f"Your item {item} has been added to your order")
    else:
        print("Sorry, we don't have that item on the menu")

    another_order = input("Do you want to add another item? (yes/no): ")
    if another_order.lower() != 'yes':
        break

# Calculate discount and taxtea

subtotal = order_total
discount = 0
if subtotal > 500:
    discount = subtotal * 0.1  # 10% discount for orders above 500 Rs
    order_total -= discount

tax_rate = 0.05  # 5% tax
tax_amount = subtotal * tax_rate
order_total += tax_amount

# Display order summary with discount and tax
if order_list:
    print("\n--- Bill Summary ---")
    from collections import Counter
    order_summary = Counter(order_list)
    for item, quantity in order_summary.items():
        print(f"{item} x{quantity}: {menu[item] * quantity} Rs")
    print(f"Subtotal: {subtotal} Rs")
    if discount > 0:
        print(f"Discount (10%): -{discount} Rs")
    print(f"Tax (5%): {tax_amount} Rs")
    print(f"Total Amount to Pay: {order_total} Rs")
    print("Thank you for your order!")
else:
    print("No items ordered. Goodbye!")
