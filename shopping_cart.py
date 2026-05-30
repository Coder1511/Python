cart=[]
while True:
    choice=input("Enter 'add' or '1' to add, 'remove' or '2' to remove, 'view' or '3' to view , 'delete' or '4' to delete or 'done' or '5' to finish: ").strip().lower()
    if choice == "done" or choice == "5":
        print("Final cart contents:", cart)
        break
    elif choice == "add" or choice == "1":
        item = input("Enter the item to add: ").strip()
        cart.append(item)
        print(f"Added '{item}' to the cart.")
    elif choice == "remove" or choice == "2":
        item = input("Enter the item to remove: ").strip()
        if item in cart:
            cart.remove(item)
            print(f"Removed '{item}' from the cart.")
        else:
            print(f"'{item}' is not in the cart.")
            print("Please enter an item that is in the cart.")
    elif choice == "view" or choice == "3":
        print("Items in the cart: ", cart)
    elif choice == "delete" or choice == "4":
        cart.clear()
        print("Cart has been cleared.")