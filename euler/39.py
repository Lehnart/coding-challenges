from math import sqrt

solution = 0
max_solution_count = 0

couples = []
for a in range(1, 1000):
    for b in range(a, 1000):
        c = sqrt(a ** 2 + b ** 2)
        if c == int(c):
            couples.append((a, b))

for p in range(1, 1000):
    solution_count = 0
    for a, b in couples:
        if a + b + int(sqrt(a ** 2 + b ** 2)) == p:
            solution_count += 1
    if solution_count > max_solution_count:
        solution = p
        max_solution_count = solution_count

print("Solution : " + str(solution))
