# Write a program to wipe out the content of a file using python.


with open (r"D:\Python\Chapter 9-PS\this.txt","r") as f1, open (r"D:\Python\Chapter 9-PS\this_copy.txt","r") as f2:
    content_1 = f1.read()
    content_2 = f2.read()

    if (content_1 == content_2):
        with open (r"D:\Python\Chapter 9-PS\this_copy.txt","w") as f2:
            f2.write("") # Deleting the content of the file if they were find identical 
            print("Files were find identical (So i'm deleting the content)")
    else:
        print("Files were not identical so content stay the same")