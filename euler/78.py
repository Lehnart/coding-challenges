p = []
p.append(1)
n=1

while True :
    i= 0
    penta = 1
    p.append(0)

    while penta <= n :
        sign = -1 if (i % 4 > 1) else 1
        p[n] += sign * p[n - penta]
        p[n] %= 1000000
        i +=1

        j = int(i / 2 + 1) if (i % 2 == 0) else int(-(i / 2 + 1))
        penta = int(j * (3 * j - 1) / 2)

    if p[n] == 0 : break
    n +=1

print("Soution :"+str(n))