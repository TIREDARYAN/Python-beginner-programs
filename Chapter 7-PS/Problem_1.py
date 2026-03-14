#Write a program to print multiplication table of a given number using for loop.


'''MY CODE'''
#No error but it didn't show the multiplication table.
# i = int(input("Enter the Number: "))
# for i in range(0,(i*11),i):
#     if (i==0):
#         continue
#     print(i)



# Clear Code by chatgpt shows the table.
num = int(input("Enter the Number: "))
for i in range(1,11):
    # print(num, "x", i, "=", num*1)
    print(f"{num} x {i} = {num*i}") # Using f string. Direct use of variable in curly bracket.