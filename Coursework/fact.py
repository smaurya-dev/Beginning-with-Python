import math
num = int(input("Enter a number: "))
if num < 0:
    print("Error: num must be bigger than 0")
else:
    result = math.factorial(num)
    print(f"The factorial of {num} is {result}")