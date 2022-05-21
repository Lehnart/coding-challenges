from sympy.ntheory import factorint


def p0005():
    # The idea is to construct a number composed of each prime factor and their multiplicity so it will
    # be divisible by each number from 1 to 20.
    prime_factor_multiplicity = {}
    for n in range(1, 20 + 1):
        n_prime_factor_multiplicity = factorint(n)
        for prime_factor in n_prime_factor_multiplicity.keys():
            if prime_factor not in prime_factor_multiplicity.keys():
                prime_factor_multiplicity[prime_factor] = n_prime_factor_multiplicity[prime_factor]
            else:
                prime_factor_multiplicity[prime_factor] = max(
                    prime_factor_multiplicity[prime_factor],
                    n_prime_factor_multiplicity[prime_factor]
                )

    # Build the number by multiplying each prime factor
    solution = 1
    for factor in prime_factor_multiplicity.keys():
        solution *= factor ** (prime_factor_multiplicity[factor])

    return solution
