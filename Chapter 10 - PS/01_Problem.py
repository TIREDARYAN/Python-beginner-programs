# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self,name,profile,salary):
        self.name = name
        self.profile = profile
        self.salary = salary

a = Programmer("Aryan Singh","Data Analyst",5000000)
print(a.name,a.profile,a.salary,a.company)
r = Programmer("Ranveer Singh","Mafia",5000000)
print(r.name,r.profile,r.salary,r.company)