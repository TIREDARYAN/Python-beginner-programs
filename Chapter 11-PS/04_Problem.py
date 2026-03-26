# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self,real,imag):
        self.real = real # Real Part
        self.imag = imag # Imag Part

    # Print complex number nicely
    def __str__(self):
        return f"{self.real} + {self.imag}i"

    #Overloading + Operator
    def __add__(self, other): 
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return Complex(real_part,imag_part)
    
    #Overloading * Operator
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + other.real * self.imag
        return Complex(real_part,imag_part)
    
# Creating Objects
c1 = Complex(1,2)
c2 = Complex(3,4)

# Addition
print("Addition: ", c1 + c2)

#Multiplication
print("Multiplication: ",c1 * c2)
