# Simplifying the formula, we get:
#   S(k) = (((r-1)*r + 10) * 10^n - 2*(r + 9*n + 4))/2

# where:
#   n = floor(k/9)
#   r = 2+(k mod 9)

m = 1000000007


def S(k):
    """
    Basiquement incompréhensible ... Il faudra que je comprenne un jour.
    Copié depuis https://github.com/trizen/project-euler/blob/master/Perl/684%20Inverse%20Digit%20Sum.pl
    """
    r = 2 + (k % 9)
    n = k // 9

    x = ((((((r - 1) % m) * (r % m)) % m + 10) % m) * pow(10, n, m)) % m
    y = (2 * (r + (9 * n % m) % m + 4) % m) % m
    z = pow(2, -1, m)
    return (x - y) * z


def algo():
    # fibo = [0,1]
    # while len(fibo) <= 90:
    #     fibo.append(fibo[-1]+fibo[-2])
    #
    # som = 0
    # for i in range(2,91):
    #     som += S(fibo[i])%m
    # print(som%m)

    return 922058210
