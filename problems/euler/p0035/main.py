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


def circular_permutations(number_string):
    l = len(number_string)
    for i in range(0, l):
        yield [number_string[(i + j) % l] for j in range(0, l)]


def p0035():
    circular_primes = {2, 3, 5, 7}
    pairs = ["0", "2", "4", "6", "8"]
    for n in range(11, 1000000, 2):
        is_circular_prime = True
        number_string = str(n)
        if any(p in number_string for p in pairs):
            continue

        for permutation in circular_permutations(number_string):
            if not is_prime(int("".join(permutation))):
                is_circular_prime = False
                break
        if is_circular_prime:
            for permutation in circular_permutations(number_string):
                circular_primes.add(int("".join(permutation)))

    return len(circular_primes)
