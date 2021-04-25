from itertools import permutations


def algo():
    digits = "0123456789"
    divisors = [2, 3, 5, 7, 11, 13, 17]
    solution = 0
    for permutation in permutations(digits, len(digits) - 1):
        permutation_str = "".join(permutation)

        has_property = True
        for i in range(0, 7):
            digit1 = permutation_str[i]
            digit2 = permutation_str[i + 1]
            digit3 = permutation_str[i + 2]
            if int(digit1 + digit2 + digit3) % divisors[i - 1] != 0:
                has_property = False
                break

        if has_property:
            digit = [d for d in digits if d not in permutation_str][0]
            permutation_str = digit + permutation_str
            solution += int(permutation_str)

    return solution


if __name__ == "__main__":
    import cProfile

    cProfile.run("algo()")
