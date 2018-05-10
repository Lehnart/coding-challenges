numbers = []
for n in range(10,1000000):
    n_str = str(n)
    n_digit_power_sum = sum([ int(c)**5 for c in n_str])
    if n_digit_power_sum == n :
        numbers.append(n)

print("Solution : " + str(sum(numbers)))