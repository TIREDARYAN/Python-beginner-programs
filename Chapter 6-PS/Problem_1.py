# Write a program to find the greatest of four numbers entered by the user.
a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
c = int(input("Enter the Third Number: "))
d = int(input("Enter the Fourth Number: "))

if(a>b and a>c and a>d):
    print("First Number is the Greatest of them all", a)
elif(b>a and b>c and b>d):
    print("Second Number is the Greatest of them all",b)
elif(c>a and c>b and c>d):
    print("Third Number is the Greatest of them all",c)
elif(d>a and d>b and d>c): #You can run a programm without using else.
    print("Fourth Number is the Greatest of them all",d)        