import math


def algo():
    n = 1010101030
    step = 60
    while True:
        step = 40 if step == 60 else 60
        n += step
        n_str = str(n * n)
        if n_str[2] != "2":
            if n_str[2] == "3" :
                n += int((math.sqrt( (4*n*n) + (4*9*10**16)) -2*n)/2)//100*100
            continue
        if n_str[4] != "3":
            continue
        if n_str[6] != "4":
            continue
        if n_str[8] != "5":
            continue
        if n_str[10] != "6":
            continue
        if n_str[12] != "7":
            continue
        if n_str[14] != "8":
            continue
        if n_str[16] != "9":
            continue
        if n_str[18] != "0":
            continue

        return n


if __name__ == "__main__":
    print(algo())
