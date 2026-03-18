string = "There are lots of elements in the periodic tables of elements"

file = open(r"D:\Python\Chapter 9\myfile.txt","w") 
# w stands for write mode. If the file does not exist, it will be created. If it already exists, it will be overwritten.

file.write(string)

file.close()