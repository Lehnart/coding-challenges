from sympy.ntheory import isprime

max_n_primes = 0
max_a = 0
max_b = 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n_prime = 0
        n = 0
        while isprime(n ** 2 + a * n + b):
            n += 1
            n_prime += 1
        if n_prime > max_n_primes:
            max_n_primes = n_prime
            max_a = a
            max_b = b
print("Solution : " + str(max_a * max_b))
