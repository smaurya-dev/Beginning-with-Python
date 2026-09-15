def average(marks):
    total = 0
    count = 0
    for m in marks:
        total = total + m
        count = count + 1
    return total / count

marks = list(input("What's the marks in five subjects? "))
print("Average marks =", average(marks))