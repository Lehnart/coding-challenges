cube_dict = {}
for n in range(0, 10000):
    cube = n ** 3
    cube_digits = [int(c) for c in str(cube)]
    cube_digits.sort()
    cube_digits_tuple = tuple(cube_digits)
    if cube_digits_tuple not in cube_dict:
        cube_dict[cube_digits_tuple] = []
    cube_dict[cube_digits_tuple].append(cube)

cube_solution = []
for key in cube_dict.keys():
    if len(cube_dict[key]) >= 5:
        cube_solution.extend(cube_dict[key])

print("Solution :" + str(min(cube_solution)))
