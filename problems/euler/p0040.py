def algo():
    solution = ""
    n = 1
    while len(solution) < 1000000:
        solution += str(n)
        n += 1
    solution = int(solution[0]) * int(solution[9]) * int(solution[99]) * int(solution[999]) * int(solution[9999]) * int(
        solution[99999])
    return solution
