import math

from common.tools import split


def is_ok(n, objective):
    if n == objective:
        return True

    if n == 0:
        return n == objective

    for i in range(int(math.log10(n)), 0, -1):
        current_n = int(n // (10 ** i))
        if current_n > objective:
            return False

        if current_n <= objective:
            next_n = n % (10 ** i)
            if next_n < objective - current_n:
                continue

            if is_ok(next_n, objective - current_n):
                return True

    return False


def is_S_number(n):
    if is_ok(n, int(math.sqrt(n))):
        return n
    return 0


def sum_s_numbers(squares):
    return sum(is_S_number(n) for n in squares)


def p0719(n_max: int):
    squares = [n ** 2 for n in range(4, int(math.sqrt(n_max)) + 1)]
    import multiprocessing as mp
    pool = mp.Pool(mp.cpu_count())
    results = pool.map(sum_s_numbers, split(squares, mp.cpu_count()))
    pool.close()
    return sum(results)
