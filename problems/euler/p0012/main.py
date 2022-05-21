from sympy.ntheory import divisor_count


def p0012():
    n = 1
    while True:
        triangle_number = int(n * (n + 1) / 2)
        if divisor_count(triangle_number) > 500:
            break
        n += 1

    return triangle_number
