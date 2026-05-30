numbers = []
while True:
    user_input = input("Enter a number or type done: ")
    while not user_input.isdigit() and user_input.lower() != "done":
        print("Invalid Input. Please enter a number or type done: ")
        user_input = input("Enter a number or type done: ")
    if user_input == "done" and len(numbers) > 0:
        break     
    elif user_input == "done" and len(numbers) == 0:
          print("Please Enter at least one number before typing done.")
    else:
        numbers.append(int(user_input))
print("Numbers entered:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Average:", sum(numbers) / len(numbers))