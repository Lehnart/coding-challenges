def p0048():
    solution = 0
    for i in range(1, 1001):
        solution += i ** i

    return int(str(solution)[-10:])
