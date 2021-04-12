def algo():
    square_of_sum, sum_of_square = 0, 0
    for i in range(1, 100 + 1):
        square_of_sum += i
        sum_of_square += i * i
    square_of_sum **= 2

    return square_of_sum - sum_of_square
