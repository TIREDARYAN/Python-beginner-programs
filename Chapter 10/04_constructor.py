class Employee:
    language = "Python" #This is a class attribute
    salary = 3000000

    def __init__(self,name,salary,language): # Dunder method which they are called automatically.
        self.name = name 
        self.salary = salary
        self.language = language
        print(" (__init__) Dunder method going to call automatically for each created object")

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")
    
    @staticmethod
    def greet(): # Here we define greet as an staticmethod that doesn't require object. Also known as decorater
        print("Good Morning")

aryan = Employee("Aryan",500000,"C++") #This values going to pass in (__init__) method
# aryan.language = "Javascript" #This is an instance attributes
print(aryan.name,aryan.language,aryan.salary)

# rohan = Employee() #redo the comment (__init__) dunder method gonna call itself again.

