class Employee:
    language = "Python" #This is a class attribute
    salary = 3000000

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")
    
    @staticmethod
    def greet(): # Here we define greet as an staticmethod that doesn't require object. Also known as decorater
        print("Good Morning")

aryan = Employee()
# aryan.language = "Javascript" #This is an instance attributes

# Employee.getInfo(aryan)
aryan.greet()
aryan.getInfo()