# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3: # This is going to assign in True and the value of len is going to assign in n.
    print(f"List is too long ({n} elements, expected <= 3)")
# Output: List is too long (5 elements, expected <= 3)