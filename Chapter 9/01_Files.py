"""
Let's say i have a program to extract emails from it.

a = "a very long string with emails"

emails = []

program going to run for 3 second in ram and then exit.

in some cases to store that process data we use file.
"""

f = open(r"D:\Python\Chapter 9\file.txt") 
# Here i opened the python folder so that's why i need to use full path
# as well r-string cause the backslashes going to give error.
# also i can use double back slashes here.

data = f.read() # read() method will read the whole file and return it as a string.
print(data)
f.close() # always close the file after using it. otherwise it will cause memory leak.