lst = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
unique_sorted = sorted(set(lst))

if len(unique_sorted) >= 2:
    print("Second largest element:", unique_sorted[-2])
else:
    print("List must contain at least two distinct elements.")