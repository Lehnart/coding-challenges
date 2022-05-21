from itertools import permutations, combinations

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n_circles = 5
solutions = []

for som in [13, 14, 15, 16, 17, 18, 19, 20]:
    for combination in combinations(digits, n_circles):
        other_digits = [d for d in digits if d not in combination]
        for circle_permutation in permutations(combination, n_circles):
            for other_permutation in permutations(other_digits, n_circles):
                is_good = True
                sets = []
                other_permutation = list(other_permutation)
                if other_permutation[0] != min(other_permutation):
                    break

                for i in range(len(other_permutation)):
                    current_digits = [other_permutation[i]]
                    current_digits += [circle_permutation[i], circle_permutation[(i + 1) % n_circles]]
                    sets.append(current_digits)
                    if sum(current_digits) != som:
                        is_good = False
                        break

                if is_good:
                    solutions.append(tuple(sets))

max = 0
for solution in solutions:
    #    print(solution)
    string = ""
    for group in solution:
        string += "".join([str(d) for d in group])

    if len(string) == 16 and int(string) > max:
        max = int(string)

print("Solution :" + str(max))
