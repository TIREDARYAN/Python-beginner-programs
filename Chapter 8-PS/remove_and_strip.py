# Write a python function to remove a given word from a list ad strip it at the same time.

def remove_and_strip(l, word):
    n = [] # This list store final cleaned values.
    for item in l: # Checking item one by one.
        if not (item == word):
            n.append(item.strip(word))
    return n


l = ["Aryan", "Rohan", "Subham", "an"]
print(remove_and_strip(l, "an"))