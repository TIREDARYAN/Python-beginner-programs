def greet(name, ending):
    print("Good day, "+name) # Here we are combinig two strings
    print(ending)
    return "Done" # Return means function take a value with you and give it to the variable when he ask you to give else gonna prine none if we don't use this.
a = greet("Aryan", "Thanks")
print(a) # in this case the return value gonna get to a.


"""
Function def where we used name, ending 
Function call where we user "Aryan", "Thanks"
so name and ending become variable "Aryan" goes in the name and "Thanks" goes in the ending
"""