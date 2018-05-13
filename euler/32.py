from itertools import permutations

digits = '123456789'

products = set()
for permutation in permutations(digits):
    permutation = "".join(permutation)
    for equal_index in range(5, 7):
        for multiplication_index in range(1, equal_index):
            a = int(permutation[:multiplication_index])
            b = int(permutation[multiplication_index:equal_index])
            c = int(permutation[equal_index:])
            if a * b == c:
                products.add(c)

solution = sum(products)
print("Solution : " + str(solution))
