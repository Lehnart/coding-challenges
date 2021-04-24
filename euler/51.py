from itertools import combinations, product

from sympy.ntheory import isprime

n_digits = 1
while True:
    n_digits += 1
    for n_replace_digit in range(1, n_digits):
        indices = set(range(0, n_digits))
        replaced_index_list = combinations(range(0, n_digits), n_replace_digit)

        for replaced_indices in replaced_index_list:
            not_replaced_indices = indices.difference(replaced_indices)
            not_replaced_digit_list = product(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                                              repeat=len(not_replaced_indices))

            for not_replaced_digits in not_replaced_digit_list:
                index_list = list(indices)
                index_list.sort()

                number_str = ""
                index_not_replaced = 0
                for index in index_list:
                    if index in replaced_indices:
                        number_str += "X"
                    else:
                        number_str += not_replaced_digits[index_not_replaced]
                        index_not_replaced += 1

                if number_str[-1] == 'X':
                    continue
                if number_str[-1] != 'X' and int(number_str[-1]) % 2 == 0:
                    continue

                not_prime_count = 0
                primes = []
                for digit in "0123456789":

                    if digit == '0' and number_str[0] == 'X':
                        continue

                    number = int(number_str.replace("X", digit))
                    if isprime(number):
                        primes.append(number)
                    else:
                        not_prime_count += 1
                if len(primes) == 8:
                    print("Solution : " + str(primes[0]))
                    # print(number_str)
                    # print(primes)
