# Write a program to find whether a given number is prime or not.

# num = int(input("Enter the Number: "))

# if (num <= 1): #We don't need 1 because its not a prime number.
#     print("Not a prime number")
# else:
#     for i in range(2, num): # We are starting from 2 and take the ends_with = input itself.
#         if (num % i == 0): # Modulus Operator:% Give remainder. because the program gonna run from 2 to number itself. so it means i enter 5 so its starts wit 2 and ends with 5, if any number in between cut him so it will not be a prime number.
#         # Why 2 is not giving if upper condition say 2%2 == 0. Because loop run 0 times.
#             print("Not a prime number")
#             break
#     else:
#         print("Prime Number")




# On my own.

# num = int(input("Enter the number:"))

# if (num <= 1):
#     print("Not a prime number")
# else:
#     for i in range(2,num):
#         if (num%i==0):
#             print("Not a prime number")
#             break # kill the loop. if we don't use it else gonna run.
#     else: # Else run only when loop is run normally without using any break or continue.
#         print("Prime Number")


#Same code in while loop:

num = int(input("Enter the number: "))

i=2
if (num<=0):
    print("Not a prime number")
else:
    while (i<num):
        if num % i == 0: # % gives remainder...
            print("Not a prime number")
            break
        i += 1
    else:
        print("Its a prime number")
