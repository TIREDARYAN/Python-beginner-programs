'''
A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams
'''

comment = input("Enter the comment:")

if("make a lot of money" in comment.lower() or  # "in" check inside the weather the value is present in the string tuple or list.
   "buy now" in comment.lower() or   # comment.lower() used for make every comment lower case so it can check the word.
   "subscribe this" in comment.lower() or 
   "click this" in comment.lower()):
    print("This comment is a spam")
else:
    print("This comment is not spam")