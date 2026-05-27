import random

x = random.randint(1, 100)

attempt = 0

while True:

    guess = int(input("Please enter the guess: "))

    attempt += 1

    if guess > x:
        print("Guess is too high")

    elif guess < x:
        print("Guess is too low")

    else:
        print("Your guess is correct")
        break

print("Number of attempts =", attempt)