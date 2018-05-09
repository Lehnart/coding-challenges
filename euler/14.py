def next_number(n):
    """
    Coompute next Collatz number
    :param n: current number i collatz sequence
    :return: next number in collatz sequence
    """
    if n % 2 == 0:
        return int(n / 2)
    return (3 * n) + 1


chain_length_dict = {}
for n in range(1, 1000000):

    current_term = n
    chain_length = 1

    # Build the chain
    while current_term != 1:

        # if chain length already knew from this number, use it
        if current_term in chain_length_dict.keys():
            chain_length += chain_length_dict[current_term] - 1
            current_term = 1

        # Else, compute next number
        else:
            current_term = next_number(current_term)
            chain_length += 1

    chain_length_dict[n] = chain_length

# find number iwth max chain length
max_key = -1
max_value = 0
for key in chain_length_dict.keys():
    if chain_length_dict[key] > max_value:
        max_value = chain_length_dict[key]
        max_key = key
print("Solution : " + str(max_key))
