'''
Write a program to print the following star pattern.
  *
 ***
***** for n = 3 # Where n is the number of rows in the pattern.
'''

# Chat GPT One.

# n = int(input("Enter the number: ")) # Taking input from the user
# for i in range(n): 
#     print(" " * (n - i - 1) + "*" * (2 * i + 1)) 

    
"""
Space Logic: in printing statement "<space>" multiplying (n - i - 1) times means if we run 3 times the space gonna deduct slowly 
# 3 - 0 - 1 = 2 
# 3 - 1 - 1 = 1
# 3 - 2 - 1 = 0
"""

"""
Logic of star multiplication: Star multiplying from (2*i times then add 1) means:  
* multiply by ( 2 multiply 0 + 1 ) = Star 1 time print
* multiply by ( 2 multiply 1 + 1 ) = Star 3 time print
* multiply by ( 2 multiply 2 + 1 ) = Star 5 time print
"""

# Code with Harry One:

n = int(input("Enter the number of rows: "))
for i in range (1, n+1):
    print(" " * (n-i), end="") # This end="" # Used for don't give new line by default. Also here (n-i) where i run from 1 to the input value so the it means space should be according to the how many stars we want.
    print("*" * (2*i-1), end="") # (2*i-1) series of odd numbers. if "i" gonna start from 0 so we gonna write +1 not -1.
    print() # This print() always gives new lines 