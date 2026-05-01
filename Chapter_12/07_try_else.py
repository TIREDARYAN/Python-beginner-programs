try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e: # If this block gonna run then try block not gonna run else.
    print(e)

else: # If try block successfully run then it will go to "else", 
    print("I'm Inside Else")