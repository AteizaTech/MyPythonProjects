items = input("Which items would you like to buy?: ")
price = float(input("How much would you like to buy per item?: "))
quantity = int(input("How many items would you like?: "))

total_price = price * quantity

print("--------------------------------")
print(f"you bought {quantity} pieces of {items}.")
print(f"you total amount is: ${round(total_price, 2)} ")