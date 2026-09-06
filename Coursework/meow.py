#This program prints "meow" n times, where n is postive integer input by the user
def main():
    number = get_number()
    meow(number)
#This function prompts the user for a positive integer and returns it 

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
def meow(n):

    for _ in range(n): 
        print("meow")