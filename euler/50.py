from sympy import primerange, isprime

primes = [ prime for prime in primerange(1,10000000)]
max_consecutive = 0
max_prime = 2

for i in range(len(primes)):
    index = 1
    n = primes[i]
    while n < 1000000:
        n += primes[i+index]
        if isprime(n) and index+1> max_consecutive :
            max_consecutive = index+1
            max_prime = n
        index += 1

print("Solution : " + str(max_prime))