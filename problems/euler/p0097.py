def algo():
    n = 2 ** 30457
    n = int(str(n)[-10:])

    power = 2 ** 10000
    for i in range(0, 780):
        n *= power
        n = int(str(n)[-10:])

    s = (n * 28433) + 1
    return int(str(s)[-10:])


if __name__ == "__main__":
    print(algo())
