from sympy.ntheory import isprime


def algo():
    n = 5
    while True:

        i = 1
        is_verifying_Goldbach = False

        double_square = 2 * i ** 2
        while double_square < n:

            if isprime(n - double_square):
                is_verifying_Goldbach = True
                break

            i += 1
            double_square = 2 * i ** 2

        if not is_verifying_Goldbach:
            return n

        n += 2
        while isprime(n):
            n += 2
