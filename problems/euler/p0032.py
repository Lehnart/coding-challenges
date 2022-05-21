import ctypes
import datetime
from itertools import permutations

digits = '123456789'


def algo():
    libc = ctypes.cdll.LoadLibrary("./p0032.so")

    products = set()
    for permutation in permutations(digits):
        permutation = "".join(permutation).encode("utf-8")
        r = libc.compute(ctypes.c_char_p(permutation))
        if r != 0:
            products.add(r)

    solution = sum(products)
    return solution


if __name__ == "__main__":
    import cProfile

    cProfile.run("algo()")

