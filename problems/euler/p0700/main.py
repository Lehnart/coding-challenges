def p0700(n_coins: int):
    """
    @param n_coins : how much euler coin to sum. If 0, sum all
    """

    found_coins = 0

    n = 1

    sum_coin = 0
    c =   1504170715041707
    mod = 4503599627370517
    min_coin = mod

    while found_coins < 1000:
        curr = (c * n) % mod
        if curr < min_coin:
            min_coin = curr
            sum_coin += curr
            found_coins += 1
            print("n ", found_coins, " min = ", min_coin, ", sum =", sum_coin)
        n += 1

    return sum_coin
