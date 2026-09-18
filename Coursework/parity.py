def check_even_odd():
    try:
        user_input = input("Enter an integer: ")
        number = int(user_input)
        if number % 2 == 0:
            print(f"{number} is Even.")
        else:
            print(f"{number} is Odd.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

check_even_odd()