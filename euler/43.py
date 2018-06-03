from itertools import permutations

digits = "0123456789"
divisors = [2,3,5,7,11,13,17]
solution = 0
for permutation in permutations(digits,len(digits)):
        permutation_str = "".join(permutation)

        has_property = True
        for i in range(1,8):
            digit1 = permutation_str[i]
            digit2 = permutation_str[i+1]
            digit3 = permutation_str[i+2]
            if int(digit1 + digit2 + digit3) % divisors[i-1] != 0 :
                has_property = False
                break

        if has_property :
            solution +=  int(permutation_str)

print("Solution : " + str(solution))