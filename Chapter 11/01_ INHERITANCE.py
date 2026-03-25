class Employee: # This is called the base class
    company = "Amazon"
    def Info(self):
        print(f"The name of the employee is {self.name} and working on this {self.company}" )

class Programmer(Employee): # This is called child class or Derived class
    company = "Google"
    def languageInfo(self):
        print(f"The employee is good with this {self.language} language")

a = Employee()
b = Programmer()

print(a.company,b.company)
