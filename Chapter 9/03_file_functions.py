f = open(r"D:\Python\Chapter 9\file.txt")

# lines = f.readlines()

# print(lines, type(lines)) #type will show that this readline function gonna give list output after using print.



# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))


line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()


f.close()
