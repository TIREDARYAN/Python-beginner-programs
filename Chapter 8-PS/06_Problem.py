# Write a python function which converts inches to cms.
def converter(i):
    c = i * 2.54
    return c
i = int(input("Enter the inches: "))
print(f"This many inches {i} is {converter(i)} cm")