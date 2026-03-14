# Write a program using functions to find greatest of three numbers.
def greates(a, b, c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>a and c>b):
        return c
a = 1
b = 9
c = 6 

print(greates(a, b, c))
