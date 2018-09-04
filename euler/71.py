d_max = 1000000

good_fraction = 0
min = 99999.
for d in range(1, d_max + 1):
    for n in range(int(3 * d / 7) + 1, 0, -1):

        if d % n == 0:
            continue

        elif 3 / 7 <= n / d:
            continue

        elif (3 / 7) - (n / d) < min:
            min = (3 / 7) - (n / d)
            good_fraction = (n, d)

        else:
            break

print("Solution :" + str(good_fraction[0]))
