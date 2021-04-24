from math import sqrt

a, b = (0, 1)
count = 0
while True:
    print(a)
    a += 1
    b = a
    while True:
        b += 1
        if a ** 2 + b ** 2 == int(a ** 2 + b ** 2):
            count += 1
        if sqrt(a ** 2 + b ** 2 + (a + b) ** 2) > 1500000:
            break
