value  = float(input("Enter value to convert: "))
operation  = str(input("Unit you are converting form (km, mile): "))

if operation == "km":
    miles = value * 0.621
    print(miles, "miles")
elif operation == "mile":
    km = value / 0.621
    print(km, "km")