solution = ""
n = 1
while len(solution) < 1000000:
    solution += str(n)
    n += 1

print("Solution : " + str(
    int(solution[0]) *
    int(solution[9]) *
    int(solution[99]) *
    int(solution[999]) *
    int(solution[9999]) *
    int(solution[99999])))
