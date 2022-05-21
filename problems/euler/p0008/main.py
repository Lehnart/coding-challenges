def p0008(number_str: str):
    solution = 0
    for index_str in range(len(number_str)):
        if index_str + 13 >= len(number_str):
            continue
        product = 1
        for digit in number_str[index_str:index_str + 13]:
            product *= int(digit)
        solution = (product if product > solution else solution)
    return solution
