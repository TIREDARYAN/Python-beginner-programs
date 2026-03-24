class Employee:
    language = "Python" #This is a class attribute
    salary = 3000000

aryan = Employee()
aryan.language = "Javascript" #This is an instance attributes
print(aryan.language,aryan.salary)

# instance attributes take preference over the class attributes.
"""Going to check instance first then class"""
