def algo():
    max_digit_sum = 0
    for a in range(0, 100):
        for b in range(0, 100):
            total = a ** b
            s = sum([int(c) for c in str(total)])
            max_digit_sum = s if max_digit_sum < s else max_digit_sum

    return max_digit_sum
