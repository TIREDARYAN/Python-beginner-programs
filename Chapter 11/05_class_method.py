class Employee:
    a = 1
    @classmethod
    def value(cls):
        print(f"The value of class attribute is {cls.a}")

e = Employee()
e.a = 45 # If we don't use class method going to show 45 because class going to take the instance attributes.
e.value()