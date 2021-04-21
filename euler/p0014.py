chain_length_dict = {1: 1}


def chain(n):
    """
    Coompute next Collatz number
    :param n: current number i collatz sequence
    :return: next number in collatz sequence
    """
    if n in chain_length_dict:
        return chain_length_dict[n]

    if n % 2 == 0:
        l = 1 + chain(n // 2)
        chain_length_dict[n] = l
        return l

    l = 1 + chain((3 * n) + 1)
    chain_length_dict[n] = l
    return l


def algo():
    max_len = 0
    max_key = 0

    for n in range(500000, 1000000):
        l = chain(n)
        if l > max_len:
            max_len = l
            max_key = n

    return max_key


if __name__ == "__main__":
    import cProfile

    cProfile.run("algo()")
