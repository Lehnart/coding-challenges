def triangle(n):
    return int(n * (n + 1) / 2)


def square(n):
    return int(n * n)


def pentagonal(n):
    return int(n * (3 * n - 1) / 2)


def hexagonal(n):
    return int(n * (2 * n - 1))


def heptagonal(n):
    return int(n * (5 * n - 3) / 2)


def octogonal(n):
    return int(n * (3 * n - 2))


def fill_list(fun):
    list = []
    n = 1
    while True:
        number = fun(n)

        if number >= 10000:
            break

        if number >= 1000:
            list.append(number)

        n += 1
    return list


def dict_from_two_first_letters(list_n):
    list_str = [str(n) for n in list_n]
    dict = {}
    for n_str in list_str:
        if n_str[:2] not in dict:
            dict[n_str[:2]] = []
        dict[n_str[:2]].append(int(n_str))
    return dict


triangles = fill_list(triangle)
squares = fill_list(square)
pentagonals = fill_list(pentagonal)
hexagonals = fill_list(hexagonal)
heptagonals = fill_list(heptagonal)
octogonals = fill_list(octogonal)

print(triangles)
print(squares)
print(pentagonals)
print(hexagonals)
print(heptagonals)
print(octogonals)

triangles_begin_str = dict_from_two_first_letters(triangles)
squares_begin_str = dict_from_two_first_letters(squares)
pentagonals_begin_str = dict_from_two_first_letters(pentagonals)
hexagonals_begin_str = dict_from_two_first_letters(hexagonals)
heptagonals_begin_str = dict_from_two_first_letters(heptagonals)
octogonals_begin_str = dict_from_two_first_letters(octogonals)

good_numbers = {}
for triangle in triangles:
    triangle_str = str(triangle)
    triangle_end_str = triangle_str[2:]
    if triangle_end_str in squares_begin_str:
        if triangle not in good_numbers:
            good_numbers[triangle] = []
        good_numbers[triangle].extend(squares_begin_str[triangle_end_str])

next_good_numbers = {}
for triangle in good_numbers.keys():
    for square in good_numbers[triangle]:
        square_str = str(square)
        square_end_str = square_str[2:]
        if square_end_str in pentagonals_begin_str:
            if (triangle, square) not in next_good_numbers:
                next_good_numbers[(triangle, square)] = []
            next_good_numbers[(triangle, square)].extend(pentagonals_begin_str[square_end_str])

good_numbers = next_good_numbers
next_good_numbers = {}
for (triangle, square) in good_numbers.keys():
    for pentagonal in good_numbers[(triangle, square)]:
        pentagonal_str = str(pentagonal)
        pentagonal_end_str = pentagonal_str[2:]
        if pentagonal_end_str ==str(triangle)[:2]:
            print([triangle,square,pentagonal])


good_numbers = next_good_numbers
next_good_numbers = {}
for (triangle, square) in good_numbers.keys():
    for pentagonal in good_numbers[(triangle, square)]:
        pentagonal_str = str(pentagonal)
        pentagonal_end_str = pentagonal_str[2:]
        if pentagonal_end_str in hexagonals_begin_str:
            if (triangle, square, pentagonal) not in next_good_numbers:
                next_good_numbers[(triangle, square, pentagonal)] = []
            next_good_numbers[(triangle, square, pentagonal)].extend(hexagonals_begin_str[pentagonal_end_str])

good_numbers = next_good_numbers
next_good_numbers = {}
for (triangle, square, pentagonal) in good_numbers.keys():
    for hexagonal in good_numbers[(triangle, square, pentagonal)]:
        hexagonal_str = str(hexagonal)
        hexagonal_end_str = hexagonal_str[2:]
        if hexagonal_end_str in heptagonals_begin_str:
            if (triangle, square, pentagonal, hexagonal) not in next_good_numbers:
                next_good_numbers[(triangle, square, pentagonal, hexagonal)] = []
            next_good_numbers[(triangle, square, pentagonal, hexagonal)].extend(
                heptagonals_begin_str[hexagonal_end_str])

good_numbers = next_good_numbers
next_good_numbers = {}
for (triangle, square, pentagonal, hexagonal) in good_numbers.keys():
    for heptagonal in good_numbers[(triangle, square, pentagonal, hexagonal)]:
        heptagonal_str = str(heptagonal)
        heptagonal_end_str = heptagonal_str[2:]
        if heptagonal_end_str in octogonals_begin_str:
            if (triangle, square, pentagonal, hexagonal, heptagonal) not in next_good_numbers:
                next_good_numbers[(triangle, square, pentagonal, hexagonal, heptagonal)] = []
            next_good_numbers[(triangle, square, pentagonal, hexagonal, heptagonal)].extend(octogonals_begin_str[
                                                                                                heptagonal_end_str])

for numbers in next_good_numbers.keys():
    all_numbers = []
    all_numbers.extend(numbers)
    all_numbers.extend(next_good_numbers[numbers])
    print(all_numbers)
    print("Solution :" + str(sum(all_numbers)))
