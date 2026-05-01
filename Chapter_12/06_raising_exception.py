a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

if (b==0):
    raise ZeroDivisionError("Hey our program doesn't meant to be values divided by 0")
else:
    print(f"{a} divied by {b} is: ",a/b)