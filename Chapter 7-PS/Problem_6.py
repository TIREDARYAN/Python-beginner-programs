#Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter the number: ")) # Here we take input from the user
product = 1 # Product take 1 always because if we take 0 its going to give 0 to all
for i in range(1,num+1): # Start from 1 till n+1
    product *= i # Means store number in the product and product = product * i, where i is going to run till the input value.
print(f"The Factorial of the number {num} is {product}") # Printing our product using f string.
