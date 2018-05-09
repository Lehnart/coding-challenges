from math import sqrt

for a in range(1, 1000):
    for b in range(1, 1000 ):
        c = int(sqrt(a ** 2 + b ** 2))
        if c ** 2 == a ** 2 + b ** 2 and a + b + c == 1000:
            print("Solution : " + str(a * b * c))
            exit()
