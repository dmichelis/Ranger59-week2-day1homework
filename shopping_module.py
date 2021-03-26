def shopping_cart():
    print("Hello this is your shopping cart")
    
    cart = {}
    
    while True:
        #add_another = True
        current_choice = (input("What would you like to do next?(Show/Add/Edit/Remove or Quit): ")).lower()
        if current_choice == 'quit':
            print("You are closing your cart, this is what you had:")
            break
        elif current_choice in cart:
            print(f"You already have {current_choice} in your cart, would you like to 'Edit'?")
        elif current_choice == 'show':
            if cart == {}:
                print("Your cart is now empty")
            else:
                print(f"Here is your current cart:")
                print("____________")
                for key, value in cart.items():
                    print(f"|{key.title()} -- Qty: {value}")
                print("____________")
        elif current_choice == 'add':
            item = input("Enter Item to Add: ")
            if item in cart:
                while add_another == True:
                    repeat_add = input("Add another?(Y/N): ")
                    if repeat_add.lower() == 'y' or repeat_add.lower() == 'yes':
                        item = input("Enter Item to Add: ")
                        if item in cart:
                            print(f"You already have {current_choice} in your cart, maybe try 'Edit' option?")
                            add_another = False
                        else:
                            quantity = input("Enter Quantity: ")
                            cart[item] = quantity
                    else:
                        add_another = False
        elif current_choice == 'edit':
            print(f"Here is your current cart:")
            print("____________")
            for key, value in cart.items():
                print(f"|{key.title()}-- Qty: {value}")
            print("____________")
            item_to_change = (input("What item would you like to change the quantity of?: ")).lower()
            if item_to_change in cart:
                quantity_change = input("New Quantity (enter 0 to delete): ")
                if int(quantity_change) > 0:
                    cart[item_to_change] = quantity_change
                elif int(quantity_change) == 0:
                    del cart[item_to_change]
            else:
                print("Sorry, we did not find that item in your cart.")
        elif current_choice == 'remove':
            print(f"Here is your current cart:")
            print("____________")
            for key, value in cart.items():
                print(f"|{key.title()}-- Qty: {value}")
            print("____________")
            remove_item = input("What item would you like to remove?: ")
            del cart[remove_item]
        else:
            print("Sorry, please enter a valid input: Show/Add/Edit/Remove or Quit")
    print("____________")
    for key, value in cart.items():
        print(f"|{key.title()}-- Qty: {value}")
    print("____________")