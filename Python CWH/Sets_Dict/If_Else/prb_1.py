mark1 = int(input("Enter mark 1 = "))
mark2 = int(input("Enter mark 2 = "))
mark3 = int(input("Enter mark 3 = "))

total_percentage = ((mark1+mark2+mark3)*100)/300

if ( total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print(f"you passed with {total_percentage} %")
    
else:
    print(f"you failed with {total_percentage} %")