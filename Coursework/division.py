def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result:.2f}")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")

divide_numbers()