from sympy.ntheory import divisor_count

n = 1
while True:
    triangle_number = int(n * (n + 1) / 2)
    if divisor_count(triangle_number) > 500:
        break
    n += 1

print("Solution : " + str(triangle_number))
