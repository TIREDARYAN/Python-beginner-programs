# Write a program to print multiplication table of a given number using while loop.

num = int(input("Enter the Number: "))
i = 1
while(i<=10):
    print(f"{num} x {i} = {num*i}") # My mistake here i'm using this print at last outside the while loop.
    i += 1


'''
Simple Rule for While Loops

Start value 
Condition 
Update value
'''