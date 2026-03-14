marks = {
    "Aryan" : 99,
    "Rohan" : 55,
    "Dabbu" : 60,
    0 : "Thunder"
}

# print(marks.items()) #Gives us all the key value pairs list in the tuple form.
# print(marks.keys()) # On the left side of the items are known as keys.
# print(marks.values()) # on the right side of the items are known as values.
# marks.update({"Dabbu":59,"Samiya":19}) # Using to update something in the dict. cause its mutable. Also adds somethings.
# print(marks)



'''Interview Question: Why they are different'''
print(marks.get("Aryan1")) # Its Print None. 
print(marks["Aryan1"]) # Its give error.

# You can find more dict methods using chatgpt.