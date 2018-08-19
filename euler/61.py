import os


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


def next_good_numbers(good_numbers, next_number_dict):
    next_good_numbers = []

    for good_number in good_numbers:
        n = good_number[0]
        n_history = good_number[1]
        n_end_str = str(n)[2:]
        if n_end_str in next_number_dict:
            for next_n in next_number_dict[n_end_str]:
                try:
                    next_good_numbers.append((next_n, (*n_history, next_n)))
                except:
                    next_good_numbers.append((next_n, (n_history, next_n)))

    return next_good_numbers


triangles = fill_list(triangle)
squares = fill_list(square)
pentagonals = fill_list(pentagonal)
hexagonals = fill_list(hexagonal)
heptagonals = fill_list(heptagonal)
octogonals = fill_list(octogonal)

triangles_begin_str = dict_from_two_first_letters(triangles)
squares_begin_str = dict_from_two_first_letters(squares)
pentagonals_begin_str = dict_from_two_first_letters(pentagonals)
hexagonals_begin_str = dict_from_two_first_letters(hexagonals)
heptagonals_begin_str = dict_from_two_first_letters(heptagonals)
octogonals_begin_str = dict_from_two_first_letters(octogonals)

lists = [
    (triangles, triangles_begin_str),
    (squares, squares_begin_str),
    (pentagonals, pentagonals_begin_str),
    (hexagonals, hexagonals_begin_str),
    (heptagonals, heptagonals_begin_str),
    (octogonals, octogonals_begin_str)
]

from itertools import permutations

for permutation in permutations(lists, 6):
    good_numbers = [(n, (n)) for n in permutation[0][0]]
    permutation = (permutation[1:])
    for l in permutation:
        good_numbers = next_good_numbers(good_numbers, l[1])

    new_good_numbers = []
    for good_number in good_numbers :
        if str(good_number[0])[2:] == str(good_number[1][0])[:2]:
            new_good_numbers.append(good_number)
    good_numbers = new_good_numbers

    if len(good_numbers) > 0 :
        all_numbers = [ n for n in good_numbers[0][1]]
        print(all_numbers)
        print("Solution :" + str(sum(all_numbers)))
        os._exit(0)
