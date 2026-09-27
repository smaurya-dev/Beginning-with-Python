l = []
n = int(input("Enter the no. of elements "))
for i in range(n):
    num = int(input("Enter the value "))
    l.append(num)
print(l)
print("Maximum= ", max(l))
print("Minimum= ", min(l))