'''
Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.
'''

Maths = int(input("Enter your maths marks: "))
English = int(input("Enter your English marks: "))
Science = int(input("Enter your Science marks: "))

Total = Maths + English + Science
Percentage = Total/3

if(Maths >=33  and English >= 33 and Science >=33) and (Percentage >= 40):
    print("You are passed", Percentage)
else:
    print("You failed the exam", Percentage)