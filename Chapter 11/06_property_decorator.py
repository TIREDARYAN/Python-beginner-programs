class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The value of class attribute is {cls.a}")

    @property # Get the value from value @name.setter
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter # Set the value
    def name(self,value):
        self.fname = value.split(" ")[0] # Split the string from space and give index 0 to self.fname
        self.lname = value.split(" ")[1] # Split the string from space and give index 1 to self.lname

e = Employee()
e.a = 45 # If we don't use class method going to show 45 because class going to take the instance attributes.

e.name = "Aryan Singh"
print(e.fname,e.lname)

e.show()