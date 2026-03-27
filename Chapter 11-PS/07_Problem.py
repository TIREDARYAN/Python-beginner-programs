#  Override the __len__() method on vector of problem 5 to display the dimension of the vector.

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
    
    def __len__(self):
        return 3
    
v = vector3D(1,2,3)

print(len(v))