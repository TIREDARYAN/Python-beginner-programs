a = int(input("Enter Your Age: "))


# if statement no. 1
if(a%2==0): # if can be independent.
    print("a is even")
# End of if statement no.1


# if statement no. 2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")
elif(a<0): # elif can't be independent.
    print("You are entering an invalid age")
elif(a==0): # You can use as much elif you want to use.
    print("You are entering an which is not applicable")     
else: # else can't be independent. Else gonna execute when all the above condition inside the if doesn't fullfill.
    print("You are under the age of consent")    
# End of if statement no.2    

'''Here both of the if gonna work because they are independent in there way'''