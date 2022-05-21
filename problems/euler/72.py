from sympy import sieve

d_max = 1000000
count = 0
results = sieve.totientrange(2, d_max)

print("Solution :" + str(sum(results)))
