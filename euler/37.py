from sympy.ntheory import isprime

primes = []
n = 9
while len(primes) < 11:
    n += 1

    if not isprime(n):
        continue

    is_truncable_prime = True
    len_n = len(str(n))
    for i in range(len_n - 1):
        if not isprime(int(str(n)[i + 1:])) or not isprime(int(str(n)[:len_n - i - 1])):
            is_truncable_prime = False
            break

    if is_truncable_prime:
        primes.append(n)

print("Solution : " + str(sum(primes)))
