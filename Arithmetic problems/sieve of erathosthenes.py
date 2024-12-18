# finding prime numbers
from math import sqrt

n = int(input("Enter the range to find prime numbers: "))

primes  = [True] * (n+1)
primes[0] = False
primes[1] = False
prime_numbers=[]
# print(primes)
for i in range(2, int(sqrt(n))+1):
    if primes[i] == True:
        for j in range  (i*i, n+1, i):
            primes[j] = False
            
for i in range(len(primes)):
    if primes[i] == True:
        prime_numbers.append(i)
print(prime_numbers)



# for single number checking
# flag=0
# for i in range(2, int(n**.5)+1):
#     if n%i==0:
#         flag=1
#         break
        
# if n>1 and flag==0:
#     print("Prime")
# else:
#     print("Not prime")
