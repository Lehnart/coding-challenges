def p0006():
    n = 100
    square_of_sum = sum(i for i in range(1,n+1))**2
    sum_of_square = sum(i**2 for i in range(1, n + 1))
    return square_of_sum - sum_of_square
