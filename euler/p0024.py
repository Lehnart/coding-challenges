from itertools import permutations


def algo():
    index = 0
    for permutation in permutations('0123456789'):
        index += 1
        if index == 1000000:
            return int("".join(permutation))
