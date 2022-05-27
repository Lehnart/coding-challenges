matrix_file = open("matrix.txt", "r")

matrix = []
for line in matrix_file:
    matrix.append([int(c) for c in line.split(",")])

min_sum_path_matrix = []
for row in matrix:
    min_sum_path_matrix.append([])
    for col in matrix[0]:
        min_sum_path_matrix[-1].append(1e6)

col_max = len(matrix[-1]) - 1
row_max = len(matrix) - 1
for i in range(len(matrix) - 1, -1, -1):
    for j in range(len(matrix[i]) - 1, -1, -1):

        candidate = matrix[i][j]

        if i == row_max and j == col_max:
            min_sum_path_matrix[i][j] = candidate

        elif i == row_max:
            candidate += min_sum_path_matrix[i][j + 1]

        elif j == col_max:
            candidate += min_sum_path_matrix[i + 1][j]

        else:
            candidate += min(min_sum_path_matrix[i][j + 1], min_sum_path_matrix[i + 1][j])

        if min_sum_path_matrix[i][j] == 1e6:
            min_sum_path_matrix[i][j] = candidate

        else:
            min_sum_path_matrix[i][j] = min_sum_path_matrix[i][j] if candidate > min_sum_path_matrix[i][
                j] else candidate

print("Solution :" + str(min_sum_path_matrix[0][0]))
