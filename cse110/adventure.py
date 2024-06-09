def initial_prompt():
    first = input("You wake up to find yourself lost in a forest, its turning night and you spot an abandoned cabin, do you seek SHELTER, or LOOK around for supplies to make your own?  ")
    if first == "shelter":
            shelter = input("test")
    elif first == "look":
                look = input("test2")
    else:
                print("Try again.")
                initial_prompt()
initial_prompt()