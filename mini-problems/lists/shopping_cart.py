products = {
    "apples": 3.99,
    "milk": 4.50,
    "bread": 2.99,
    "eggs": 5.49
}

print("--------- RECEIPT ---------")

for product, price in products.items():
    print(f"{product} ----- ${price:.2f}")

subtotal = sum(products.values())

tax = subtotal * 0.085

total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")