solution = 0
for n1 in range(1, 10000):
    for product_count in range(1, 10):
        concatenated_product_str = ""
        concatenated_product_int = 1
        for n in range(1, product_count + 1):
            concatenated_product_str += str(n1 * n)

        concatenated_product_int = int(concatenated_product_str)
        concatenated_product_str = "".join(sorted(concatenated_product_str))
        if concatenated_product_str == "123456789" and concatenated_product_int > solution:
            solution = concatenated_product_int
print("Solution : " + str(solution))
