from sympy.ntheory import isprime


def is_perm(a, b):
    chars_a = [c for c in str(a)]
    chars_a.sort()
    perm_a = "".join(chars_a)

    chars_b = [c for c in str(b)]
    chars_b.sort()
    perm_b = "".join(chars_b)

    if perm_a == perm_b:
        return True

    return False

def algo():
    n, f = 1487, 1  # start search with prime from description
    while True:
        n += 3 - f  # generates prime candidates faster than checking odd numbers
        f = -f
        b, c = n + 3330, n + 6660
        if isprime(n) and isprime(b) and isprime(c) \
                and is_perm(n, b) and is_perm(b, c): break

    return int(str(n) + str(b) + str(c))
