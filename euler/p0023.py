import ctypes

from sympy.ntheory import divisors


def is_abundant(n):
    if sum(divisors(n)[:-1]) > n:
        return True
    return False


def algo():
    # Find all abundants number below 28123
    n_max = 28123
    abundants = []
    for n in range(28123):
        if is_abundant(n):
            abundants.append(n)

    libc = ctypes.cdll.LoadLibrary("./p0023.so")
    abundant_array_type = ctypes.c_long * len(abundants)
    abundant_array = abundant_array_type(*abundants)
    abundant_size = ctypes.c_int(len(abundants))

    sum_size = ctypes.c_int(n_max)
    sum_array_type = ctypes.c_int * n_max
    sum_array = sum_array_type()
    s = libc.compute(abundant_array, abundant_size, sum_array, sum_size)

    return s


if __name__ == "__main__":
    import cProfile

    cProfile.run("algo()")
