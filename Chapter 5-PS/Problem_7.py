# If the names of 2 friends are same; what will happen to the program in problem 6?

x = {} #Empty Dictionary
Name = input("Enter Your Name: ") #Name is the Key
Language = input(f"Enter Your Favorite Language {Name}: ") #Language is the values
x.update({Name:Language}) # It create temp dict. inside {This},  Merge it after in the empty dict.


'''If i put Aryan here first time and his language Python here'''


Name = input("Enter Your Name: ") #Name is the Key
Language = input(f"Enter Your Favorite Language {Name}: ") #Language is the values
x.update({Name:Language}) # It create temp dict. inside {This},  Merge it after in the empty dict.

'''
If i put Aryan here is second time and his language English, So program gonna update First python as per the upper code
then update to English after that in this code
'''

Name = input("Enter Your Name: ") #Name is the Key
Language = input(f"Enter Your Favorite Language {Name}: ") #Language is the values
x.update({Name:Language}) # It create temp dict. inside {This},  Merge it after in the empty dict.
Name = input("Enter Your Name: ") #Name is the Key
Language = input(f"Enter Your Favorite Language {Name}: ") #Language is the values
x.update({Name:Language}) # It create temp dict. inside {This},  Merge it after in the empty dict.
print(x)