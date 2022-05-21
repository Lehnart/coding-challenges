from sympy import sieve
from sympy.ntheory import isprime

prime_count = 1500
sieve.extend_to_no(prime_count)
primes = [p for p in sieve._list]
prime_concatenation_dict = {p: [] for p in primes}

for i in range(0, prime_count):
    for j in range(i + 1, prime_count):
        prime_i = primes[i]
        prime_j = primes[j]

        prime_i_str = str(prime_i)
        prime_j_str = str(prime_j)

        if isprime(int(prime_i_str + prime_j_str)) and isprime(int(prime_j_str + prime_i_str)):
            prime_concatenation_dict[prime_i].append(prime_j)
            prime_concatenation_dict[prime_j].append(prime_i)

next_prime_combinations = [[p] for p in primes]
for n_in_combination in range(1, 5):
    prime_combinations = next_prime_combinations
    next_prime_combinations = []
    for prime_combination in prime_combinations:

        concatenate_prime_sets = []
        for prime in prime_combination:
            concatenate_prime_set = set(prime_concatenation_dict[prime])
            concatenate_prime_sets.append(concatenate_prime_set)
        primes_to_be_added = set.intersection(*concatenate_prime_sets)

        for added_prime in primes_to_be_added:
            if added_prime in prime_combination or added_prime < prime_combination[-1]:
                continue

            current_prime_combination = []
            current_prime_combination.extend(prime_combination)
            current_prime_combination.append(added_prime)
            concatenate_prime_sets = []
            for prime in current_prime_combination:
                concatenate_prime_set = set(prime_concatenation_dict[prime])
                concatenate_prime_set.add(prime)
                concatenate_prime_sets.append(concatenate_prime_set)

            temp_set = set.intersection(*concatenate_prime_sets)

            if len(temp_set) >= n_in_combination + 1:
                next_prime_combinations.append(current_prime_combination)
print("Solution : " + str(sum(next_prime_combinations[0])))
