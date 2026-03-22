#  Write a program to find out the line number where python is present from ques 6.

with open (r"D:\Python\Chapter 9-PS\log.txt","r") as f:
    line_number = 1

    for line in f:
        if "python" in line.lower():
            print ("Python found on line: ",line_number)
            break
        line_number += 1
    else:
        print("Python did not found")