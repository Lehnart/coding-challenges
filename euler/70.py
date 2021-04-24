from sympy import sieve

min_n = 0
min_quotient = 9999999999999999999

totients = sieve.totientrange(1, 10000000)

n = 0
for totient in totients:
    n += 1

    if n < 10:
        continue

    n_digits = [int(c) for c in str(n)]
    n_digits.sort()
    n_digits = tuple(n_digits)
    totient_n_digits = [int(c) for c in str(totient)]
    totient_n_digits.sort()
    totient_n_digits = tuple(totient_n_digits)

    if n_digits == totient_n_digits:
        if n / totient < min_quotient:
            min_quotient = n / totient
            min_n = n

print("Solution :" + str(min_n))
