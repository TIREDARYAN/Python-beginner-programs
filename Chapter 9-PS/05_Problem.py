# Repeat program 4 for a list of such words to be censored.

censored = ["donkey","idiot","stupid"]

with open (r"D:\Python\Chapter 9-PS\Censored.txt","r") as f:
    content = f.readlines()

new_lines = []

for line in content:
    line = line.lower()

    for word in censored:
        line = line.replace(word,"#"*len(word))
    new_lines.append(line)

with open (r"D:\Python\Chapter 9-PS\Censored.txt","w") as f:
    f.writelines(new_lines)
        

