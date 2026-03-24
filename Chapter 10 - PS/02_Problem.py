# Write a class “Calculator” capable of finding square, cube and square root of a number.
import math

class Calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        return self.n * self.n
    def cube(self):
        return self.n * self.n * self.n
    def square_root(self):
        return math.sqrt(self.n)

n = int(input("Enter the number: "))

c = Calculator(n)

print(f"""
Square = {c.square()}
Cube = {c.cube()}
Square Root = {c.square_root()}

""")
