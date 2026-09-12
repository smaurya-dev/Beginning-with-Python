def get_fibonacci_sequence(count: int) -> list[int]:
    sequence = []
    current_term, next_term = 0, 1

    for _ in range(count):
        sequence.append(current_term)
        current_term, next_term = next_term, current_term + next_term

    return sequence


def main():
    try:
        total_terms = int(input("Enter the number of terms: "))
        
        if total_terms <= 0:
            print("Please enter a positive integer greater than 0.")
            return
        fib_numbers = get_fibonacci_sequence(total_terms)
        
        formatted_output = ", ".join(map(str, fib_numbers))
        
        print("\nGenerated Fibonacci Sequence:")
        print(formatted_output)

    except ValueError:
        print("Error: Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
