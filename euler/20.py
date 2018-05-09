from math import factorial

n_str = str(factorial(100))
solution = 0
for c in n_str:
    solution += int(c)
print("Solution : " + str(solution))
