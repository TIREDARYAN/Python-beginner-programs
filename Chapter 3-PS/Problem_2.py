# Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>", "Aryan").replace("<|Date|>", "18 February 2026"))

# Here we used first replace to replace the name from the string.
# and second replace on that whole name replace to take all the string after name replace and change the date.
# this thing called channing of the replace function.