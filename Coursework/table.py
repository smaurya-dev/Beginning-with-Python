def print_table(number):
    for i in range(1, 11):
        product = number * i
        print(number, "x", i, "=", product)

n = 7
print_table(n)