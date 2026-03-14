# Write a program to detect double space in a string.

text =  "One Piece is the greatest  manga of  all time"
print(text.find("  ")) # This is going to find the sub-string from the parent string.

# If the output is -1 so it means there is no space.
# It the output is something else than -1 so it means there is space in the string.