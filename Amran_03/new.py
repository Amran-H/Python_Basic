n = int(input("Enter your numner: "))
def fibo(n):
  if (n<=0):
    print("Invalid input")
  elif (n==1):
    return 1
  elif (n==2):
    return 1
  else:
    return fibo(n-1)+fibo(n-2)
print(fibo(n))