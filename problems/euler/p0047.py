from bisect import bisect_left

from sympy.ntheory import primefactors

from problems.euler.primes import primes_below

PRIMES = primes_below(150000)


def is_prime(n):
    i = bisect_left(PRIMES, n)
    if i != len(PRIMES) and PRIMES[i] == n:
        return True
    else:
        return False


def algo():
    n = 2

    n1, n2, n3, n4 = (n, n + 1, n + 2, n + 3)
    n_d = (set(primefactors(n1)), set(primefactors(n2)), set(primefactors(n3)), set(primefactors(n4)))
    while True:
        n1, n2, n3, n4 = (n, n + 1, n + 2, n + 3)
        if is_prime(n4):
            n += 4
            n1, n2, n3, n4 = (n, n + 1, n + 2, n + 3)
            n_d = (0, set(primefactors(n1)), set(primefactors(n2)), set(primefactors(n3)), 0)
            continue

        n_d = (n_d[1], n_d[2], n_d[3], set(primefactors(n4)))
        if [len(el) for el in n_d] == [4] * 4:
            return n
        n += 1


if __name__ == "__main__":
    import cProfile

    cProfile.run("algo()")
