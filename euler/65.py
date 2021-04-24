from fractions import Fraction

es = []
for i in range(0, 100 + 1):
    if (i - 1) % 3 == 0:
        es.append(int(((i - 1) / 3) + 1) * 2)
    else:
        es.append(1)

for i in range(0, len(es)):
    frac = Fraction(es[i], 1)
    for j in range(i - 1, 0 - 1, -1):
        frac = Fraction(es[j], 1) + Fraction(frac.denominator, frac.numerator)
    frac = Fraction(2, 1) + Fraction(frac.denominator, frac.numerator)
    if i == 100 - 2:
        print("Solution : " + str(sum([int(c) for c in str(frac.numerator)])))
