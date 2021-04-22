from bisect import bisect_left

from euler.primes import primes_below

primes = primes_below(20000)


def is_prime(n):
    if n in [2, 3, 5]:
        return True
    if n < 2 or (n % 2) == 0 or (n % 3) == 0 or (n % 5) == 0:
        return False

    i = bisect_left(primes, n)
    if i != len(primes) and primes[i] == n:
        return True
    else:
        return False


def algo():
    max_n_primes = 0
    max_a = 0
    max_b = 0
    for a in range(-999, 1001, 2):
        for b in range(-999, 1001, 2):
            n_prime = 0
            n = 0
            while is_prime(n ** 2 + a * n + b):
                n += 1
                n_prime += 1
            if n_prime > max_n_primes:
                max_n_primes = n_prime
                max_a = a
                max_b = b
    return max_a * max_b
