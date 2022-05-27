def algo():
    keylog_file = open("p0079_keylog.txt", 'r')
    code_template = ["X"] * 8
    next_possibilities = [code_template]

    for line in keylog_file:
        line = line.strip()
        digit_1, digit_2, digit_3 = line

        possibilites = next_possibilities
        next_possibilities = []

        while len(possibilites) > 0:
            n = possibilites.pop()

            digit_2_positions = [i for i in range(0, len(n)) if n[i] == "X" or n[i] == digit_2]
            for i in digit_2_positions:

                digit_1_positions = [i for i in range(0, len(n[:i])) if n[i] == "X" or n[i] == digit_1]
                digit_3_positions = [i for i in range(i + 1, len(n)) if n[i] == "X" or n[i] == digit_3]

                positions = [[d1, d2, d3]
                             for d1 in digit_1_positions
                             for d2 in [i]
                             for d3 in digit_3_positions
                             ]

                for position in positions:
                    next_template = n.copy()
                    next_template[position[0]] = digit_1
                    next_template[position[1]] = digit_2
                    next_template[position[2]] = digit_3
                    next_possibilities.append(next_template)

    keylog_file.close()
    return int("".join(next_possibilities[0]))
