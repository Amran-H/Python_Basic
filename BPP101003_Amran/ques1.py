# def check_prime(value): 
#     if value > 1:
#         for i in range(2, value):
#             if value % i == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False

# value = int(input("Please enter the range to find prime numbers: "))
# prime_numbers=[]
# for i in range(1, value):
#     primes = check_prime(i)
#     if primes == True:
#         prime_numbers.append(i)
        
# print(prime_numbers)




def check_prime(value):
    if value < 2:
        return False

    for i in range(2, int(value**.5)+1):
        if value%i==0:
            return False
    return True

while True:
    value = int(input("Enter the range to check the prime numbers: "))
    if value < 2:
        print("Please enter and integer greater than 2")
        continue
    prime_numbers = [i for i in range(2, value) if check_prime(i)]
    print(prime_numbers)
# for i in range(1, value):
#     if check_prime(i):
#         print(i)
                 