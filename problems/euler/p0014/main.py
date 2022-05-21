chain_length_dict = {1: 1}


def chain(n0):
    """
    Coompute next Collatz number
    :param n0: current number i collatz sequence
    :return: next number in collatz sequence
    """
    if n0 in chain_length_dict:
        return chain_length_dict[n0]

    if n0 % 2 == 0:
        n = 1 + chain(n0 // 2)
        chain_length_dict[n0] = n
        return n

    n = 2 + chain(((3 * n0) + 1)//2)
    chain_length_dict[n0] = n
    return n


def p0014():
    max_len = 0
    max_key = 0

    for n in range(500000, 1000000):
        length = chain(n)
        if length > max_len:
            max_len = length
            max_key = n

    return max_key
