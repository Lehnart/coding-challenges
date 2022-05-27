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
    max_consecutive = 0
    max_prime = 2

    for i in range(len(primes)):
        index = 1
        n = primes[i]
        while n < 1000000:
            if i + index >= len(primes):
                break
            n += primes[i + index]
            if is_prime(n) and index + 1 > max_consecutive:
                max_consecutive = index + 1
                max_prime = n
            index += 1

    return max_prime


if __name__ == "__main__":
    import cProfile

    cProfile.run("algo()")
