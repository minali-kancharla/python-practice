inventory = {
    "apples": {"quantity": 20, "price": 0.75},
    "bananas": {"quantity": 15, "price": 0.20},
    "milk": {"quantity": 10, "price": 4.30},
    "bread": {"quantity": 12, "price": 3.49},
}

print('''
1. View inventory
2. Add stock
3. Remove stock
4. Check quantity and price
5. Quit
''')

while True:
    
    x = int(input("Enter task #: "))

    if x == 1:
        for item, details in inventory.items():
            print(f"{item.title()} (${details['price']:.2f}): {details['quantity']}")
    elif x == 2:
        new_item = input("Add stock: ")
        new_quantity = int(input("Enter quantity: "))
        if new_item in inventory:
            inventory[new_item]["quantity"] += new_quantity
        else:
            new_price = float(input("Enter price: "))
            inventory[new_item] = {"quantity": new_quantity, "price": new_price}
    elif x == 3:
        remove_item = input("Remove stock: ")
        remove_quantity = int(input("Enter quantity of stock to remove: "))
        if remove_quantity > inventory[remove_item]["quantity"]:
            print("Not enough stock to remove that much.")
        else:
            inventory[remove_item]["quantity"] -= remove_quantity
    elif x == 4:
        check = input("Check quantity of...")
        if check in inventory:
            print(f"{check} (${inventory[check]['price']:.2f}) - {inventory[check]['quantity']}")
        else:
            print("Item not found.")
    elif x==5:
        break
    else:
        print("Invalid choice")