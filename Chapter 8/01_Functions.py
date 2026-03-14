# Example: We need to find average of 3 numbers 5 times, We don't wanna repeat our program 5 times so there functions comes.

def avg(): # First we write def then variable = here we take "avg" then () bracket and this ":" after write our statement.
    # This thing know as function defination.
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    average = (a+b+c)/3
    print(average)
avg() # This means run our function 1 times ,  without this we can't run our function 
print("Thank you") # After 1st function print thank you
avg() # This means run our function 2 times,  just need to put variable name and then () bracket to run the function.
print("Thank you") # After 2nd function print thank you.
avg() # This means run our function 3 times ,  Also this is called function call.
