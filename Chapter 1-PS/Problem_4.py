#Write a python program to print the contents of a directory using the os module. Search online for the function which does that
# Use CHATGPT

import os

# Specify the directory path you want to list
directory_path = "/"  # replace this with your actual path

try:
    # Get the list of items in the directory
    contents = os.listdir(directory_path)

    # Print each item
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You don't have permission to access this directory.")
