class Employee: # Parent Class
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee): # Child class number 1
    def __init__(self):
        print("Constructor of Programmer")
    b = 2 

class Manager(Programmer): # Child class number 2
    def __init__(self):
        super().__init__() # "super()" is going to run the constructor of their parent class
        print("Constructor of Manager")
    c = 3 

# o = Employee()
# print(o.a) # Going to print a attribute in Employee class.

# o = Programmer()
# print (o.a,o.b)

o = Manager()
print(o.a,o.b,o.c)