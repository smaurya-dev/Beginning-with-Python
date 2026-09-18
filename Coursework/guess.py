import random

def guessing_game():
    secret_number = random.randint(1, 20)
    attempts = 0
    print("I'm thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

guessing_game()