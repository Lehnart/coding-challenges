from sympy.ntheory import factorint


def algo():
    factors = factorint(600851475143, multiple=True)
    return max(factors)
