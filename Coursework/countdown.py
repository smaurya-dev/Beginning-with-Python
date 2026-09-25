def countdown(start):
    for i in range(start, 0, -1):
        print(i)
    print("Go!")

seconds = int(input("Enter the Starting time: "))
countdown(seconds)