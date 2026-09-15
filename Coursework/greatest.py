def find_max(numbers):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest

scores = list(input("What's the list? "))
print("Largest score is", find_max(scores))