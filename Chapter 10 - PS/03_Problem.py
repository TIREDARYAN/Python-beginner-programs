# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’.
# Does this change the class attribute?

class Demo:
    a = 5

o = Demo()
print(o.a) # Printing Class Attribute

o.a = 0 # Instance Attribute Set
print(o.a)

print(Demo.a) # Printing Class Attribute

# The answer is no. class attribute doesn't change.