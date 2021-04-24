import os

from math import sqrt


def is_pentagonal(n):
    sqrt_delta = sqrt(1 + 24 * n)
    if sqrt_delta != int(sqrt_delta):
        return False
    i = (1 + sqrt_delta) / 6
    if i != int(i):
        return False
    return True


pentagonals = []
pentagonal_count = 10000
for i in range(1, pentagonal_count + 1):
    pentagonals.append(int(i * (3 * i - 1) / 2))

for i in range(pentagonal_count):
    n_i = pentagonals[i]
    for j in range(i + 1, pentagonal_count):
        n_j = pentagonals[j]
        if is_pentagonal(n_j - n_i) and is_pentagonal(n_j + n_i) in pentagonals:
            print("Solution : " + str(n_j - n_i))
            os._exit(1)
