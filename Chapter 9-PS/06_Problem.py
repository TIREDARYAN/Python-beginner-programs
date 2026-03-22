# Write a program to mine a log file and find out whether it contains ‘python’.

with open (r"D:\Python\Chapter 9-PS\log.txt","r") as f:
    content = f.read()

if "python" in content.lower():
    print("Python is present")
else:
    print("Python is not present")