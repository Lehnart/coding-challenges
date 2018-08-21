from math import sqrt

count = 0
for n in range (2,10001) :

    if sqrt(n) == int(sqrt(n)) :
        continue

    a0 = int(sqrt(n))
    ass = [a0]
    bs = [1]
    cs = [a0]
    b_c_seen = []

    period = 0
    while True:

        prev_b = bs[- 1]
        prev_c = cs[- 1]

        num = (sqrt(n) + prev_c)
        den = (n - prev_c ** 2) / prev_b

        a = num // den
        ass.append(a)

        b = den
        bs.append(b)
        c = (a * den) - prev_c
        cs.append(c)

        if (b,c) in b_c_seen :
            break
        b_c_seen.append((b,c))

    if len(b_c_seen) % 2 == 1 :
        count += 1

print("Solution :" + str(count))