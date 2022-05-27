from math import sqrt


def is_pentagonal(n):
    sqrt_delta = sqrt(1 + 24 * n)
    if sqrt_delta != int(sqrt_delta):
        return False
    i = (1 + sqrt_delta) / 6
    if i != int(i):
        return False
    return True


def is_triangle(n):
    sqrt_delta = sqrt(1 + 8 * n)
    if sqrt_delta != int(sqrt_delta):
        return False
    i = (-1 + sqrt_delta) / 2
    if i != int(i):
        return False
    return True


def is_hexagonal(n):
    sqrt_delta = sqrt(1 + 8 * n)
    if sqrt_delta != int(sqrt_delta):
        return False
    i = (1 + sqrt_delta) / 4
    if i != int(i):
        return False
    return True


def hexagonal(n):
    return n * (2 * n - 1)


def algo():
    for i in range(144, 1000000):
        n = hexagonal(i)
        if is_pentagonal(n) and is_hexagonal(n) and is_triangle(n):
            return n
