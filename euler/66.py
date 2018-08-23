from fractions import Fraction
from math import sqrt

max_x = 0
max_d = 0
for d in range(2, 1001):

    if sqrt(d) == int(sqrt(d)):
        continue

    a0 = int(sqrt(d))
    ass = [a0]
    bs = [1]
    cs = [a0]
    b_c_seen = []

    period = 0
    while True:

        prev_b = bs[- 1]
        prev_c = cs[- 1]

        num = (sqrt(d) + prev_c)
        den = (d - prev_c ** 2) / prev_b

        a = num // den

        b = den
        bs.append(b)
        c = (a * den) - prev_c
        cs.append(c)

        if (b, c) in b_c_seen:
            break
        ass.append(int(a))

        b_c_seen.append((b, c))

    frac = 1
    if len(ass) > 2:

        for j in range(len(ass) - 2, 0, -1):
            if j == len(ass) - 2:
                frac = Fraction(ass[j], 1)
            else:
                frac = Fraction(ass[j], 1) + Fraction(frac.denominator, frac.numerator)
    else:
        frac = Fraction(ass[-1], 1)

    frac = Fraction(ass[0], 1) + Fraction(frac.denominator, frac.numerator)

    x0 = frac.numerator
    y0 = frac.denominator

    x = x0
    y = y0
    while True :
        if x**2 - d*y**2 == 1 :
            break
        x1 = (x0*x) + (d*y0*y)
        y1 = (x0*y) + (y0*x)
        x = x1
        y = y1

    if max_x < x:
        max_x = x
        max_d = d

print("Solution :" + str(max_d))
