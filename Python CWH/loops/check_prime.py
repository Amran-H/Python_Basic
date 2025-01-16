n = int(input("Enter the number to check prime or not: "))

for i in range(2, n):
    if (n % i == 0):
        print("not prime")
        break
else:
    print("Prime")