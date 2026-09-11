a = 1
b = 1

n = int(input("Enter the number of terms "))
for i in range(n):
    c = a+ b 
    print(c, end=",")
    a = b
    b = c