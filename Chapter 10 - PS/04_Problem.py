# Add a static method in problem 2, to greet the user with hello.
import math

class Calculator:

    @staticmethod
    def greet():
        return "Hello"
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

print(f"""{c.greet()}
Square = {c.square()}
Cube = {c.cube()}
Square Root = {c.square_root()}

""")
