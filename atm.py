balance=int(input("Enter your Account Balance="))
choice = ""
while choice != "4" and choice != "Exit":
    print("1.Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter choice: ").capitalize()
    if choice in ["1","Check balance"]:
        print(balance)
    elif choice in ["2","Deposit"]:
        deposit=int(input("Please Enter the Amount to be deposited="))
        balance+=deposit
        print("Currrent Balance=",balance)
    elif choice in ["3","Withdraw"]:
        withdraw=int(input("Please enter the amount you want to Withdraw="))
        if withdraw<=balance:
          balance-=withdraw
          print("Current Balance",balance)
        else:
          print("Insufficient Balance")
    elif choice in ["4","Exit"]:
        print("Thank you for using our Atm")
    else:
        print("Invalid Choice")