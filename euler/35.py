from sympy.ntheory import isprime


def circular_permutations(l):
    return [[l[(i + j) % len(l)] for j in range(0, len(l))] for i in range(0, len(l))]


circular_primes = set()
for n in range(2, 1000000):
    is_circular_prime = True
    for permutation in circular_permutations(str(n)):
        if not isprime(int("".join(permutation))):
            is_circular_prime = False
            break
    if is_circular_prime:
        for permutation in circular_permutations(str(n)):
            circular_primes.add(int("".join(permutation)))

print("Solution : " + str(len(circular_primes)))
