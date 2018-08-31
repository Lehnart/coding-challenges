from sympy import totient

max_n = 0
max_quotient = 0
for n in range(1,1000000):
    if n/totient(n) > max_quotient :
        max_quotient = n/totient(n)
        max_n = n

print("Solution :" + str(max_n))