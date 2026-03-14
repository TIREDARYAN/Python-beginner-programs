'''
Write a program to greet all the person names stored in a list 'l' and which starts
with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]

'''
# With for loop.
l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l: #Here name become a variable and store each value from the list inside it.
#     if(name.startswith("S")):
#         print(f"Hello {name}")




# With while loop.

i = 0 # Here i is a variable which store the index of the list and we will use it to access the elements of the list.
while(i<len(l)): # Here we are checking the condition that i should be less than the length of the list because if i becomes equal to the length of the list then it will give an error because there is no element at that index.
    if (l[i].startswith("S")): # Here l[i] is used to access the element of the list at index i and then we are checking if it starts with "S" or not.  
        print(f"Hello {l[i]}") # Here we are printing the greeting message with the name of the person.
    i += 1
# why does the l[i] work? Because i is the index of the list and we can access the element of the list by using the index. For example, if i is 0 then l[i] will give us the first element of the list which is "Harry". If i is 1 then l[i] will give us the second element of the list which is "Soham" and so on.
"""
Real Life Example

Imagine stairs.

# While Loop (Manual Control)

You say:

Start at step 1
Check step <= 5
Climb one step
Repeat

You control every step.

# For Loop (Automatic Control) 

You say:

Climb steps from 1 to 5

Python handles the stepping.
"""