from bisect import bisect_left

from problems.euler.primes import primes_below

primes = primes_below(1000000)


def is_prime(n):
    if n in [2, 3, 5]:
        return True
    if n < 2 or (n % 2) == 0 or (n % 3) == 0 or (n % 5) == 0:
        return False

    i = bisect_left(primes, n)
    if i != len(primes) and primes[i] == n:
        return True
    else:
        return False


def algo():
    n = 9
    truncable_primes = []
    while len(truncable_primes) < 11:
        n += 2

        if not is_prime(n):
            continue

        is_truncable_prime = True
        len_n = len(str(n))
        for i in range(len_n - 1):
            if not is_prime(int(str(n)[i + 1:])) or not is_prime(int(str(n)[:len_n - i - 1])):
                is_truncable_prime = False
                break

        if is_truncable_prime:
            truncable_primes.append(n)

    return sum(truncable_primes)


if __name__ == "__main__":
    import cProfile

    cProfile.run("algo()")
