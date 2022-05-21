def p0002():
    u_n, u_n_minus_1 = (2, 1)
    even_sum = 2
    while u_n < 4000000:
        u_n_minus_1, u_n = (u_n, u_n + u_n_minus_1)
        if u_n % 2 == 0:
            even_sum += u_n
    return even_sum
