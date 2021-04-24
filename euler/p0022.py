def algo():
    names_file = open("p0022_names.txt", 'r')
    names_list = names_file.readline().replace('\"', "").split(',')
    names_list.sort()

    solution = 0
    index = 1
    for name in names_list:
        score = 0
        for c in name:
            score += ord(c) - ord('A') + 1
        solution += index * score
        index += 1

    names_file.close()
    return solution
