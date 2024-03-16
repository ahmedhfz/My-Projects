menu = {"popcorn" : 5.99,
        "ice cream" : 3.50,
        "pizza" : 10.99,
        "fries" : 2.50}

cart = []
total = 0

print("----------MENU----------")
for urun , fiyat in menu.items() :
    print(f"{urun:10} : {fiyat:.2f}")
print("------------------------")

while True:
    order = str(input("What would you like to buy (q to quit): ")).lower()
    if order == "q":
        break
    elif order in menu.keys():
        cart.append(order)
        total += menu.get(order)

print("-------------YOUR ORDER------------")
for order in cart:
    print(order,end=" ")
print()

print(f"Your total is {total:.2f} $")

