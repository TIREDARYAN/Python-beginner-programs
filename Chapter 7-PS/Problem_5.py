#Write a program to find the sum of first n natural numbers using while loop

'''It means like n = 4, So, 1 + 2 + 3 + 4 = 10'''

n = int(input("Enter the number: ")) # Take input from user
i = 0 # i is the loop encounter variable. 
sum = 0 # Sum is a variable with store the loop encounter values.
while (i<=n): # Here input and i value should be equal.
    sum += i # Here we are adding i value in the sum, First loop 0 + 0 then 0+1, then 1 + 2
    i += 1 # Here the i value counter till the n number which we take input from the user.
print(sum)