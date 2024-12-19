# n = int(input("Enter the value to find sixy prime: "))

def generate_primes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**.5)+1):
        if primes[i]==True:
            for j in range (i*i, n+1, i):
                primes[j]=False
    return primes

L=6
R=59

my_primes = generate_primes(R)
for i in range(L, len(my_primes)-6):
    if my_primes[i] == True:
        x=i
        y=x+6
        if my_primes[y]==True:
            print(f"{(x),(y)}")
        


                

                
    