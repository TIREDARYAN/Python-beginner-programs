dict1 = {"a":1,"b":2}
dict2 = {"b":3,"c":4}

merged = dict1 | dict2

print(merged)

# Output {'a': 1, 'b': 3, 'c': 4}


# changes in b because:
# "b" already exists.
# So it replaces the old value (2) with new value (3).