import random

n = random.randint(1, 100)
a = -1
guess = 0
while (a != n):
    a = int(input("Enter the number: "))
    guess += 1
    if (a>n):
        print("Lower number please")
    elif (a<n):
        print("Higher number please")
    else:
        print(f"You won the game in {guess} Guesses and the number is {n}")

