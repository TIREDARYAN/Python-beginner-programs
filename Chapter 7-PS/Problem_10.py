# Write a program to print multiplication table of n using for loops in reversed order.
n = int(input("Enter the number: "))
for i in range (1, 11):
    print(f"{n} x {11-i} = {n*(11-i)}")


'''
In this whole counting every line there sum is 11, so 11-1=10 so it makes the value in desending order just multiple the value from i.
our program is ready.
1   10 
2   9  
3   8
4   7
5   6
6   5 
7   4 
8   3
9   2
10  1
'''