#Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter your username: ")
if(len(username)<10):
    print("Your username doesn't contain 10 characters:",len(username)) #len is give the length of indexing by adding 1 in it so give the exact character values.
    # Relation ship= last index + 1 = (execat value)
else:
    print("All is well!")

