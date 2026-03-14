# If languages of two friends are same; what will happen to the program in problem 6?

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


# In Dict the identifyer is the Key, Value can be same.