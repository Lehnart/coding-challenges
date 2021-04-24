import os
from bisect import bisect_left

from sympy import sieve

primes = [p for p in sieve.primerange(1, 100)]

for p in primes:
    target = p
    ways = [0] * (target + 1)
    ways[0] = 1
    for prime in primes[:bisect_left(primes, target)]:
        for j in range(prime, target + 1):
            ways[j] += ways[j - prime]

    if ways[-1] >= 5000:
        print("Solution :" + str(target))
        os._exit(0)
