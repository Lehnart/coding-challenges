import math

pythagoreans = {}

max_m = 4000
for m in range(1, max_m):

    for n in range(1, m):
        for k in range(1, max_m):
            a, b, c = (k * (m ** 2 - n ** 2), k * (2 * m * n), k * (m ** 2 + n ** 2))
            if a > max_m or b > max_m or c > max_m:
                break

            l = [a, b, c]
            l.sort()
            a, b, c = l

            if a not in pythagoreans: pythagoreans[a] = set()
            pythagoreans[a].add(b)

            if b not in pythagoreans: pythagoreans[b] = set()
            pythagoreans[b].add(a)

m = 1
count = 0

while True:
    m += 1
    c = m
    if c in pythagoreans:
        for a_plus_b in pythagoreans[c]:
            if a_plus_b < c:
                for b in range(1, int(a_plus_b / 2) + 1):
                    a = a_plus_b - b
                    l1 = math.sqrt(a ** 2 + (b + c) ** 2)
                    l2 = math.sqrt(b ** 2 + (a + c) ** 2)
                    l3 = math.sqrt(c ** 2 + (a + b) ** 2)

                    l = min(l1, l2, l3)
                    if l == l3:
                        count += 1


            else:
                for b in range(1, int(a_plus_b / 2) + 1):
                    a = a_plus_b - b

                    if a > c or b > c:
                        continue

                    l1 = math.sqrt(a ** 2 + (b + c) ** 2)
                    l2 = math.sqrt(b ** 2 + (a + c) ** 2)
                    l3 = math.sqrt(c ** 2 + (a + b) ** 2)

                    l = min(l1, l2, l3)
                    if l == l3:
                        count += 1

    if count > 1000000: break

print("Solution :" + str(m))
