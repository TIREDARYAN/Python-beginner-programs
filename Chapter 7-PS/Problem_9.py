"""
Write a program to print the following star pattern.
* * *
*   * for n = 3
* * * 
"""

n = int(input("Enter the value: "))

for i in range (1,n+1):
    if (i==1 or i==n): # First condition that if the value of i or user's input print star till (user input)
        print("*"*n,end="")
    else: 
        print("*",end="") # Else print star
        print(" "*(n-2),end="") # Then give space (n-2) means user says 5 so it means 3 spaces only border stars gonna print
        print("*",end="") # This star complete the border.
    print()
    