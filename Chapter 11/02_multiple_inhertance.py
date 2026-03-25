class Employee: # This is called the base class/parent class
    company = "Amazon"
    name = "Aryan Singh"
    def Info(self):
        print(f"The name of the employee is {self.name} and working on the {self.company}")


class Coder: #This is also a parent class
    language = "Python"
    def Printlanguage(self):
        print(f"The language is {self.language}")

class Programmer(Employee,Coder): # This is called child class or Derived class
    company = "Google"
    def languageInfo(self):
        print(f"The employee is good with this {self.language} language")

a = Employee()
b = Programmer()


b.Printlanguage()
b.Info()
b.languageInfo()
