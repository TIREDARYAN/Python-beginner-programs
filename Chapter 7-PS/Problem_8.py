"""
Write a program to print the following star pattern:
*
**
*** for n = 3
"""

n = int(input("Enter the rows: "))
for i in range (1, n+1):
    print("*"*(i)) # i gonne run from 1 to input rows as how many stars we want in a rows ==  input by user so use i here 

