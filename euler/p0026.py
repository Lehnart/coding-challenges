def algo():
    sequence_length = 0
    for i in range(2, 1000):
        found_remainders = [0] * i
        value = 1
        position = 0
        while found_remainders[value] == 0 and value != 0:
            found_remainders[value] = position
            value *= 10
            value %= i
            position += 1

        if position - found_remainders[value] > sequence_length:
            sequence_length = position - found_remainders[value]
            solution = i

    return solution
