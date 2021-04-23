import numpy
from sympy.ntheory import divisors
import numpy as np

def is_abundant(n):
    if sum(divisors(n)[:-1]) > n:
        return True
    return False


def algo():
    is_abundant_sum = [False] * 28123
    # Find all abundants number below 28123
    abundants = []
    for n in range(28123):
        if is_abundant(n):
            abundants.append(n)

    # Find all pair of abundant numbers
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            s = abundants[i] + abundants[j]
            if s >= 28123:
                break
            is_abundant_sum[s] = True

    # Find integer that can t be written as the sum of 2 abundant numbers
    solution = 0
    for n in range(28123):
        if not is_abundant_sum[n]:
            solution += n
    return solution


if __name__ == "__main__":
    import cProfile

    cProfile.run("algo()")
