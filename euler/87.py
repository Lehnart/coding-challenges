from sympy import sieve

primes = [p for p in sieve.primerange(1,8002)]

ns = set()

for i1 in range(0,len(primes)):
    for i2 in range(0,len(primes)):
        for i3 in range(0,len(primes)):
            n = (primes[i1] ** 2) + (primes[i2] ** 3) + (primes[i3] ** 4)
            if n < 50000000 :
                ns.add(n)
            else :
                break

print("Solution :" + str(len(ns)))