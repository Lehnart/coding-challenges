from fractions import Fraction

count = 0
for i in range(0, 1000):
    f = Fraction(1, 2)
    for j in range(0, i):
        f = Fraction(1, 2 + f)
    f += Fraction(1, 1)

    if len(str(f.numerator)) > len(str(f.denominator)):
        count += 1

print("Solution : " + str(count))
