import math

def calculate_factorial():
    try:
        num = int(input("Enter a non-negative integer for its factorial: "))
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            result = math.factorial(num)
            print(f"The factorial of {num} is {result}")
    except ValueError:
        print("Invalid input! Please enter a whole number.")

calculate_factorial()