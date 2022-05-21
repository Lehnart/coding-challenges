from sympy.ntheory import factorint


def p0003():
    factors = factorint(600851475143, multiple=True)
    return max(factors)
