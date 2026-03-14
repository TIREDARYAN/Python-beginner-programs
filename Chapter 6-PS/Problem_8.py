# Write a program to find out whether a given post is talking about “Aryan” or not.
Post = input("Enter Your Post: ")

if("aryan" in Post.lower()): #This .lower() gonna make all the text in lower case also need to string in condition in smaller case also.
    print("This Post Talking About Aryan")
else:
    print("This Post Not Talking About Aryan")