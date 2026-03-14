# A function which call itself.
"""
factorial (0) = 1
factorial (1) = 1
factorial (2) = 2 x 1
factorial (3) = 3 x 2 x 1
factorial (4) = 4 x 3 x 2 x 1
factorial (5) = 5 x 4 x 3 x 2 x 1

factorial (n) = n * (n-1) ... 3 x 2 x 1
factorial (n) = n * factorial(n-1) # We take all the values after n = factorial(n-1)

# Where factorial(n-1) gonna call itself till it goes till 1.

"""

def factorial(n):
    if (n == 1 or n == 0): # Factorial 0 is by default 1 by mathematics rules.
        return 1 # Here it gonna give the value 1 when user write 1 or the factorial value reach till 1.
    return n * factorial(n-1) # Menas multiply the value of n till 1. Factorial gonna call itself till 1. Gonna subtact 1 every time till 1 and multiply in n.
n = int(input("Enter the number: "))
print(f"Factorial of this number is {factorial(n)}")
