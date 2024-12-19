def compute_xor_power_mod(t, test_cases):
    MOD = 100000009
    results = []
    
    for a, b, n in test_cases:
        # Ensure that the input constraints are met
        if not (1 <= t <= 1000):
            raise ValueError("Number of test cases t must be between 1 and 1000")
        if not (0 <= a <= 100000 and 0 <= b <= 100000 and 0 <= n <= 100000):
            raise ValueError("Each of a, b, and n must be between 0 and 100000")

        # Compute the XOR of a and b
        xor_value = a ^ b
        # Compute (xor_value ** n) % MOD efficiently
        result = pow(xor_value, n, MOD)
        results.append(result)
    
    return results

t = int(input())
if not (1 <= t <= 1000):
    raise ValueError("Number of test cases t must be between 1 and 1000")
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

results = compute_xor_power_mod(t, test_cases)

for res in results:
    print(res)