def print_table(number):
    for i in range(1, 11):
        product = number * i
        print(number, "x", i, "=", product)

n = int(input("What's n? "))
print_table(n)