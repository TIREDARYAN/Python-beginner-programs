# Write a python program using function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(c): # Here we take c as an parameter so it will recieve the value to pass the program.
    # Parameters are the variables inside the function that recieve the values.
    f = (9/5)*c+32
    return f
c = int(input("Enter the Celsius: "))
print(f"Fahernheit: {round(celsius_to_fahrenheit(c),2)}") 
#                    round                          2
#means round all the decimal points and show only   2  decimal points at the end.