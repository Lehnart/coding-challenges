def algo():
    count = 0
    for n in range(0, 10001):

        current_n = n
        is_lychrel = True

        current_n_str = str(current_n)
        current_n_str_reversed = current_n_str[::-1]
        current_n = int(current_n_str) + int(current_n_str_reversed)

        for i in range(0, 50):
            current_n_str = str(current_n)
            current_n_str_reversed = current_n_str[::-1]

            if current_n_str == current_n_str_reversed:
                is_lychrel = False
                break
            else:
                current_n = int(current_n_str) + int(current_n_str_reversed)

        if is_lychrel:
            count += 1
            # print(str(n) + " is a lychrel number")

    return count
