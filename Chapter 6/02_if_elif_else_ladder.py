a = int(input("Enter Your Age: "))

#if elif else ladder

#only one thing gonna execute from the ladder from all the condition which we set.

if(a>=18):
    print("You are above the age of consent")
    print("Good for you")
elif(a<0):
    print("You are entering an invalid age")
elif(a==0):
    print("You are entering an which is not applicable")     
else:
    print("You are under the age of consent")    


'''
These all are connected to itself "if" condition doesn't true then elif and if its no true then elif at last else if its condition doesn't meet.
'''      