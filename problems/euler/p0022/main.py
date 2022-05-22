def p0022(name_file_path):
    names_file = open(name_file_path, 'r')
    names_list = names_file.readline().replace('\"', "").split(',')
    names_list.sort()
    names_file.close()

    solution = 0
    index = 1
    for name in names_list:
        score = sum(ord(c) - ord('A') + 1 for c in name)
        solution += index * score
        index += 1

    return solution
