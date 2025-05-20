menu={
    'Pizza':120,
    'Burger':80,
    'Coffee':70,
    'Pasta':100,
    'Sandwich':100,
    'Tea':50,
    'Coke':60,
    'Juice':70,
    'Milkshake':120,
    'Pepsi':70,
    'Sprite':70,
    'Fanta':70,
    'Water':50,

}

print("Welome To Our Restaurant")
print("Pizza:120\nBurger:80\nCoffee:70\nPasta:100\nSandwich:100\nTea:50\nCoke:60\nJuice:70\nMilkshake:120\nPepsi:70\nSprite:70\nFanta:70\nWater:50")


order_total=0


while True:
    item = input("Enter the item you want to order: ")
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order")
    else:
        print("Sorry, we don't have that item on the menu")

    another_order = input("Do you want to add another item? (yes/no): ")
    if another_order.lower() != 'yes':
        break

print(f"The total amount to pay is {order_total} Rs")