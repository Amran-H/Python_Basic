A, B = map(int, input("enter two integers separated by a space: ").split())

if -10**9 <= A <= 10**9 and -10**9 <= A <= 10**9:
    product =  A * B
    print(product)
else:
    print("Error")
