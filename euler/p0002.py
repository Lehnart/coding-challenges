def algo():
    n, prev, solution = (2, 1, 2)
    while n < 4000000:
        prev, n = (n, n + prev)
        if n % 2 == 0:
            solution += n
    return solution
