n = int(input("Enter the number: "))

for i in range(2, n):
    if n%i == 0:
        print("Number is not prime ")
        break

    if i + 1 == n:
        print("number is prime")