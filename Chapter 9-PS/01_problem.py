# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open(r"D:\Python\Chapter 9-PS\poems.txt") as f: 
    content = f.read()
# Above statement will read the content of the file and store it in the variable 'content'


if "twinkle" in content.lower():
    # The above condition checks if the word "twinkle" is present in the content of the file, ignoring case sensitivity
    print("twinkle twinkle present in the poems.txt")
else:
    print("twinkle twinkle is not present in the poems.txt")