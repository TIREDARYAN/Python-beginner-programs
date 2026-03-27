# Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.

class vector3D:
    
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other):
        return (self.x*other.x + self.y*other.y + self.z*other.z)
    
    def __str__(self):
        return f"{self.x},{self.y},{self.z}"
    
v1 = vector3D(1,2,3)
v2 = vector3D(5,6,7)

print("Addition",v1 + v2)
print("Dot Product:",v1*v2)
