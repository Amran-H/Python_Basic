def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True 

def prime_factor(n):
    factors=[]
    divisor=2
    while n>1:
        if n % divisor == 0:
            if is_prime(divisor):
                if divisor not in factors:
                    factors.append(divisor)
            n = n // divisor
        else:
            divisor +=1
    return factors

while True:
    number = int(input("Enter a positive integer greater than 3: "))
    if number>3:
        break
    else:
        print("Please enter a number greater than 3")

factors = prime_factor(number)
if factors:
    print (f"The prime factors are: {factors}")
else:
    print("The number has no prime factors")