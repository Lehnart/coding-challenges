def get_smallest_digit(n):
    number_of_9 = n // 9
    first_digit = n % 9
    s = '9' * number_of_9
    if first_digit != 0:
        s = str(first_digit) + s
    return int(s)


def algo():
    fibo = [0, 1]
    while len(fibo) <= 90:
        fibo.append(fibo[-1] + fibo[-2])

    som = 0
    for i in range(1, 21):
        som += get_smallest_digit(i)

    som = 0
    for i in range(1, 21):
        if i <= 18 :
            som += get_smallest_digit(i)
        else :
            som += (20 - 18)*99
            break
    print(som)

    som = 0
    for i in range(2, 12):
        for j in range(1, fibo[i] + 1):
            if j <=90:
                som += get_smallest_digit(j)
            else:
                som += 999999999 * (fibo[i] - 81)
                break
    result = som % 1000000001
    return result


if __name__ == "__main__":
    print(algo())
