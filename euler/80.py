import decimal
import math

som = 0
for n in range(1, 101):

    sqrt_n = math.sqrt(n)
    if sqrt_n != int(sqrt_n):
        decimal.getcontext().prec = 1000
        sqrt = decimal.Decimal(n).sqrt()
        digits_str = str(sqrt).replace(".","")[:100]
        som += sum([int(d) for d in digits_str])

print("Solution : " + str(som))
