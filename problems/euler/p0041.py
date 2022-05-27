from itertools import permutations

from sympy.ntheory import isprime


def algo():
    solution = 2

    for n in range(2, 10):
        digits = "".join([str(i) for i in range(1, n + 1)])
        for permutation in permutations(digits, n):
            permutation_int = int("".join(permutation))
            if isprime(permutation_int) and permutation_int > solution:
                solution = permutation_int

    return solution
