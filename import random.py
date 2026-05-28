import random
x= random.randint(1,100)
attempt=0
while True:
 guess=int(input("Please enter the guess=" ))
 attempt+=1
 if guess>x:
    print("Guess is too High")
 elif guess<x:
    print("Guess is too Low")
 else:
    print("Your guess is Correct")
    break
print("No of attempts=",attempt)

