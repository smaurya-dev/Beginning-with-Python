def array_diff(a, b):
    b_set = set(b)
    return [x for x in a if x not in b_set]

print(array_diff([1, 2], [1]))            # [2]
print(array_diff([1, 2, 2, 2, 3], [2]))   # [1, 3]   