from sympy.ntheory import divisors


def is_amicable(n):
    b = sum(divisors(n)[:-1])
    if n == sum(divisors(b)[:-1]) and n != b:
        return True
    return False


def algo():
    solution = 0
    for n in range(10000):
        if is_amicable(n):
            solution += n
    return solution