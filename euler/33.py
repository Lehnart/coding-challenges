from fractions import Fraction
from itertools import product

solution = Fraction(1, 1)

# loop on fractions
for den in range(11, 100):
    for num in range(11, den):
        frac = Fraction(num, den)

        # try to simplify the fraction in an incorrect way
        num_str, den_str = (str(num), str(den))
        for el in product([0, 1], repeat=2):
            new_num, new_den = int(num_str[(el[0] + 1) % 2]), int(den_str[(el[1] + 1) % 2])
            if num_str[el[0]] == den_str[el[1]] and den_str[el[1]] != "0" and new_den != 0 and Fraction(new_num, new_den) == frac:
                solution *= frac

print("Solution : " + str(solution.denominator))
