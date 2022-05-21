def algo():
    n = 123456
    while True:
        n += 1
        n_strs = []
        for i in range(1, 6 + 1):
            n_str_list = list(set(str(n * i)))
            n_str_list.sort()
            n_strs.append(tuple(n_str_list))
        if len(set(n_strs)) <= 1:
            return n