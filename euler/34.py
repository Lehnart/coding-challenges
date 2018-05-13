from math import factorial

solution = 0
for n in range(3, 9999999): # 9999999> 9! * 7
    fact_sum = 0
    for c in str(n):
        fact_sum += factorial(int(c))
    if fact_sum == n:
        solution += fact_sum

print("Solution : " + str(solution))
