a = float(input("Enter a side: "))
b = float(input("Enter b side: "))
c = float(input("Enter c side: "))

if a + b > c and b + c > a and a + c > b:
    print("The triangle can be drew")

else:
    print("The triangle cannot be drew")