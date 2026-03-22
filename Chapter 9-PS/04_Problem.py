"""
A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file. 
"""

with open (r"D:\Python\Chapter 9-PS\Donkey.txt","r") as f: 
    lines = f.readlines() # Read the file and store each line as an element in a list called 'lines'

new_lines = [] # create an empty list to store the modified lines

for line in lines: # Iterate through each line in the 'lines' list
    new_line = line.lower()                  # make everything lowercase
    new_line = new_line.replace("donkey", "#####") # Replace all occurrences of the word "donkey" with "#####"
    new_line = new_line.capitalize() # Capitalize the first letter of the modified line to maintain proper formatting
    new_lines.append(new_line) # Add the modified line to the 'new_lines' list

with open (r"D:\Python\Chapter 9-PS\Donkey.txt","w") as f: # write the modified lines back to the same file, overwriting the original content.
    f.writelines(new_lines) # The writelines() method is used to write the list of modified lines back to the file. 
    #Each element in the 'new_lines' list will be written as a separate line in the file.