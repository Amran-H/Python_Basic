def is_prime(n):
    """Check if a number is prime."""
    flag=0
    if n<=1:
        return False
    for i in range(2, n):
        if n%i==0:
            flag=1
            break
    return flag==0

def prime_factors(n):
    """Return a list of unique prime factors of n."""
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            if is_prime(divisor):
                if divisor not in factors:
                    factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors

def main():
    number = int(input("Enter a positive integer greater than 3: "))
    if number <= 3:
        print("The number must be greater than 3.")
    else:
        factors = prime_factors(number)
        if factors:
            print(f"The prime factors are: {factors}")
        else:
            print("No prime factors found.")

if __name__ == "__main__":
    main()