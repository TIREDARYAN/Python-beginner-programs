string = "There are lots of elements in the periodic tables of elements"

file = open(r"D:\Python\Chapter 9\myfile.txt","a") 
# a stands for append mode. If the file does not exist, it will be created. 
# If it already exists, the new content will be added to the end of the file without overwriting the existing content.

file.write(string)

file.close()