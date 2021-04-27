from fractions import Fraction


def algo():
    count = 0
    f = Fraction(1 / 2)
    for i in range(0, 1000):
        f = Fraction(1, 2 + f)
        t = f + Fraction(1, 1)

        if len(str(t.numerator)) > len(str(t.denominator)):
            count += 1

    return count
