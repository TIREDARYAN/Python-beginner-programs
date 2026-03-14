# What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(len(s))

#Answer: Length of s is = 2

# Because if the two values are same python thinks its one value. ex 1 == 1.0 used in repl.