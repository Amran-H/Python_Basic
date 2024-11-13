def check_prime(value): 
    if value > 1:
        for i in range(2, value):
            if value % i == 0:
                return False
        else:
            return True
    else:
        return False
    

for i in range(1, 400):
    prime_numbers = check_prime(i)
    if prime_numbers == True:
        print(i)
                 