# Simple example of class:

class Employee:
    age = 22 #This is a class attribute
    salary = 3000000

aryan = Employee()
aryan.name = "Aryan" #This is an instance attributes
print(aryan.name,aryan.age)

rohan = Employee()
rohan.name = "Rohan"
print(rohan.name,rohan.salary)



'''
Here, names are object/instance attributes and salary and age are class attributes beacuse they are directly belong to the class.


• Noun → Class → Employee
• Adjective → Attributes → name, age, salary
• Verbs → Methods → getSalary(), increment()
'''

