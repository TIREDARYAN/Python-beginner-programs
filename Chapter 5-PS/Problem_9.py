# Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}

# You cannot include a list in a set, so you cannot change its values either.

# If you replace the list with a tuple (which is immutable), it will work:

s = {8, 7, 12, "Harry", (1, 2)}
print(s)