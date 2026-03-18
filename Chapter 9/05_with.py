# f = open(r"D:\Python\Chapter 9\file.txt") 
# print(f.read())
# f.close()

# We can do the same thing without closing the file using with statement.

with open(r"D:\Python\Chapter 9\file.txt") as f:
    print(f.read())

# This will do the same work without using "f.close()".