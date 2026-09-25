import random

def roll_dice():
    while True:
        user_choice = input("Press 'Enter' to roll the dice or type 'quit' to exit: ").strip().lower()
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        
        roll = random.randint(1, 6)
        print(f"You rolled a {roll}!\n")
        
roll_dice()
