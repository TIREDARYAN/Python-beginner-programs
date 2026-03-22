# Write a program to make a copy of a text file “this. txt”

with open (r"D:\Python\Chapter 9-PS\this.txt","r") as f:
    content = f.read()

with open (r"D:\Python\Chapter 9-PS\this_copy.txt","w") as f:
    f.write(content)