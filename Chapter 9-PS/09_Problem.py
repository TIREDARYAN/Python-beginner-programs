# Write a program to find out whether a file is identical & matches the content of another file.

with open (r"D:\Python\Chapter 9-PS\this.txt","r") as f1, open (r"D:\Python\Chapter 9-PS\this_copy.txt","r") as f2:
    content_1 = f1.read()
    content_2 = f2.read()

    if (content_1 == content_2):
        print("The files are identical & matches the content of another file")
    else:
        print("Files are not identical")