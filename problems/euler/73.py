from sympy import igcd

d_max = 12000

count = 0
for d in range(1, d_max + 1):
    for n in range(int(1 * d / 2) + 1, 0, -1):

        if d % n == 0:
            continue

        if d % 2 == 0 and n % 2 == 0:
            continue

        if d % 3 == 0 and n % 3 == 0:
            continue

        if igcd(n, d) != 1:
            continue

        elif 1 / 2 <= n / d:
            continue

        elif n / d <= 1 / 3:
            break

        else:
            count += 1

print("Solution :" + str(count))
