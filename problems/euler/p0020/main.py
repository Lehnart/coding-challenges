from math import factorial


def p0020():
    n_str = str(factorial(100))
    solution = 0
    for c in n_str:
        solution += int(c)
    return solution
