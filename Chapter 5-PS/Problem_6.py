# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

x = {} #Empty Dictionary
Name = input("Enter Your Name: ") #Name is the Key
Language = input(f"Enter Your Favorite Language {Name}: ") #Language is the values
x.update({Name:Language}) # It create temp dict. inside {This},  Merge it after in the empty dict.
Name = input("Enter Your Name: ") #Name is the Key
Language = input(f"Enter Your Favorite Language {Name}: ") #Language is the values
x.update({Name:Language}) # It create temp dict. inside {This},  Merge it after in the empty dict.
Name = input("Enter Your Name: ") #Name is the Key
Language = input(f"Enter Your Favorite Language {Name}: ") #Language is the values
x.update({Name:Language}) # It create temp dict. inside {This},  Merge it after in the empty dict.
Name = input("Enter Your Name: ") #Name is the Key
Language = input(f"Enter Your Favorite Language {Name}: ") #Language is the values
x.update({Name:Language}) # It create temp dict. inside {This},  Merge it after in the empty dict.
print(x)