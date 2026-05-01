
def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)

    except Exception as e: # If this block gonna run then try block not gonna run else.
        print(e)

    finally: # If try block successfully run then it will go to "else", 
        print("I'm Inside finally")

main()

# If finally gonna run on auto-mode every time with try so what the purpose of it we can simply just write it print statement.
# but it works with function where it needed to use to print.