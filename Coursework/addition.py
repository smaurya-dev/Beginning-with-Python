def sum_upto(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

limit = 10
result = sum_upto(limit)
print("Sum from 1 to", limit, "is", result)