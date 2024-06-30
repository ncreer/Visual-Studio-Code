program_running = True
print("Welcome to the Shopping Cart Program!")
cart = []

while program_running == True:
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = int(input("Please enter an action: "))
    if action == 1:
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? "))
        cart.append((item, price))
        print(f"'{item}' has been added to the cart.")
        print("")
    if action == 2:
        print("The contents of the shopping cart are:")
        for index, (item, price) in enumerate(cart):
            print(f"{index + 1}. {item} - ${price:.2f}")
        print("")
    if action == 3:
        remove = int(input("Which item would you like to remove? "))
        try:
            removed_item = cart.pop(remove - 1)
            print("Item removed.")
            print("")
        except IndexError:
            print("Sorry, that is not a valid item number.")
            print("")
    if action == 4:
        total = sum(price for item, price in cart)
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
        print("")
    if action == 5:
        program_running = False
print("Thank you. Goodbye.")