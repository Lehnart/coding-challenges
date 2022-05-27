def algo():
    solution = 0
    for n in range(1, 1000000, 2):
        bin_n_str = str(bin(n))[2:]
        if str(n) == str(n)[::-1] and bin_n_str == bin_n_str[::-1]:
            solution += n

    return solution
