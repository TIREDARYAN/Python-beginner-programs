# Write a program which finds out whether a given name is present in a list or not

x = ["Aryan", "Ayush", "Preet", "Aditiya", "Mayank"]
name = input("Enter Your Name: ")
if( name in x ):
    print(f"Good Morning {name}")
else:
    print("You are not the part of this organization")