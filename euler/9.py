import math
limit = 1500000
triangles = {}
result = 0
mlimit = int(math.sqrt(limit / 2))

for m in range(2,mlimit) :
    for n in range(1,m) :
        if (n + m) % 2 == 1 and math.gcd(n, m) == 1 :
            a = m * m + n * n
            b = m * m - n * n
            c = 2 * m * n
            p = a + b + c
            while p <= limit :
                if p not in triangles :
                    triangles[p] = 0
                triangles[p]+=1
                p += a + b + c
result = 0
for p in triangles.keys() :
    if triangles[p] ==  1 :
        result +=1

print("Solution "+ str(result))