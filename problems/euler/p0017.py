from num2words import num2words


def algo():
    solution = 0
    for n in range(1, 1000 + 1):
        n_litteral = num2words(n)
        solution += sum(c.isalpha() for c in n_litteral)

    return solution
