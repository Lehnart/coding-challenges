from scipy.misc import comb

count = 0
for n in range(0, 101):
    for k in range(0, n):
        r = comb(n, k)
        if r > 1e6:
            count += 1
print("Solution : " + str(count))
