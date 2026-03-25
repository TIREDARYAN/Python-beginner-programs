class Employee: # Parent Class (of all)
    a = 1

class Programmer(Employee): # Child class number 1 (and parent of manager)
    b = 2 

class Manager(Programmer): # Child class number 2 (child of programmer) 
    c = 3 

o = Employee()
print(o.a) # Going to print a attribute in Employee class.
# print(o.b) # Going to give error because there is no attribute b in programmer class

o = Programmer()
print (o.a,o.b)

o = Manager()
print(o.a,o.b,o.c)