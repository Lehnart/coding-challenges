import numpy as np


def max_product(sequence, solution):
    for index in range(len(sequence)):
        if index + 3 >= len(sequence):
            continue
        temp = sequence[index] * sequence[index + 1] * sequence[index + 2] * sequence[index + 3]
        if temp > solution:
            solution = temp
    return solution


def p0011(grid_file_name: str):
    solution = 0

    # transform grids tr in int numpy array
    grid_str = "".join(open(grid_file_name,"r").readlines())
    grid_list = [[int(n) for n in line.split(" ")] for line in grid_str.split('\n')]
    grid_array = np.array(grid_list)

    # find max 4 adjacent digit product in line
    for row_index in range(0, grid_array.shape[0]):
        row = grid_array[row_index, :]
        solution = max_product(row, solution)

    # find max 4 adjacent digit product in column
    for col_index in range(0, grid_array.shape[1]):
        col = grid_array[:, col_index]
        solution = max_product(col, solution)

    # find max 4 adjacent digit in diagonals
    for row_index in range(0, grid_array.shape[0]):
        up_right_diag = [grid_array[row_index - i, i] for i in range(0, row_index)]
        down_right_diag = [grid_array[row_index + i, i] for i in range(0, grid_array.shape[0] - row_index)]
        solution = max_product(up_right_diag, solution)
        solution = max_product(down_right_diag, solution)

    return solution
