# Name = "Aryan"
# print(Name[0:3]) # Here normal 0 to 3. (excluding 3)
# print(Name[-4:-1]) # Here neagtive Slicing where start from -4 to -1 (Excluding -1)
# print(Name[1:4]) # One more thing you can do is change into corresponding letter.

'''  Where in String "Aryan"  '''
#  1 -> -4 From start and 4 -> -1 Changing postive to just there neagtive for the string the output will be same.

# print(Name[:5]) # Here if the left side is blank it means there is 0
# It same as print(Name[0:5])

# print(Name[1:]) # If there is right side blank it maens -1. 
# it same as print(Name[1:5])


'''Slicing with a Skip'''

Count = "0123456789"
Skip = Count[1:9:2] 
'''
Here Skiping means 1 to 9 means (1 to 8) and 2 means:

0  1  2  3  4  5  6  7  8  
   |     |     |     |
This values going to print with a skip of 2 where i set on the programm. Gap of 2 after 1st.
'''
print(Skip)