#Can you change the self-parameter inside a class to something else (say“harry”). Try changing self to “slf” or “harry” and see the effects.

class Programmer:
    company = "Microsoft"
    def __init__(slf,name,profile,salary):
        slf.name = name
        slf.profile = profile
        slf.salary = salary

a = Programmer("Aryan Singh","Data Analyst",5000000)
print(a.name,a.profile,a.salary,a.company)
r = Programmer("Ranveer Singh","Mafia",5000000)
print(r.name,r.profile,r.salary,r.company)

#Nothing will change but its's going to mix up the names if you use any name before. Readablity issue.