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
    action = input("Please enter an action: ")
    if action == "1":
        item = input("What item would you like to add? ")
        cart.append(item)
    if action == "2":
        print("The contents of the shopping cart are:")
        for item in cart:
            print(item)
