'''
Write a program to calculate the grade of a student from his marks from the
following scheme:
90 - 100 => Ex
80 - 90 => A
70 - 80 => B
60 - 70 =>C
50 - 60 => D
<50 => F
'''
Maths = int(input("Enter the Maths Marks: "))
SST = int(input("Enter the SST Marks: "))
Science = int(input("Enter the Science Marks: "))
English = int(input("Enter the English Marks: "))
Hindi = int(input("Enter the Hindi Marks: "))

Percentage = (Maths+SST+Science+English+Hindi)/5

if(Percentage>90 and Percentage<=100):
    print("Excellent", Percentage)
elif(Percentage>80 and Percentage<=90):
    print("A", Percentage)
elif(Percentage>70 and Percentage<=80):
    print("B", Percentage)
elif(Percentage>60 and Percentage<=70):
    print("C", Percentage)
elif(Percentage>50 and Percentage<=60):
    print("D", Percentage)
else:
    print("F")