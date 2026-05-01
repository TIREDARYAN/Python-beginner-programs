a = 89 # Global variable

def fun():
    global a #Change the global variable to local variable
    a = 4 #local variable of the function
    print(a)

fun()
print(a)