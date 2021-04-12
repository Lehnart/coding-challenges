from sympy.ntheory import factorint

def algo():
    # Determine all the required prime factors to have a multiple of all integers in range (1,20)
    n = 1
    expected_divisors = range(1, 21)
    factors_dict = {}
    for n in expected_divisors:
        n_factors_dict = factorint(n)
        for n_factor in n_factors_dict.keys():
            if n_factor not in factors_dict.keys() or factors_dict[n_factor] < n_factors_dict[n_factor]:
                factors_dict[n_factor] = n_factors_dict[n_factor]

    # Compute the solution
    solution = 1
    for factor in factors_dict.keys():
        for i in range(0, factors_dict[factor]):
            solution *= factor

    return solution
