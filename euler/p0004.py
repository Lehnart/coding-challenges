def algo():
    max_palindrome_int = 0
    for n1 in range(100, 1000):

        # If n1 are multiple of 10, product will end by 0 and it won't be a palindrom
        if n1 % 10 == 0:
            continue

        for n2 in range(n1, 1000):

            # If n2 are multiple of 10, product will end by 0 and it won't be a palindrom
            if n2 % 10 == 0:
                continue

            candidate_palindrome_str = str(n1 * n2)
            if candidate_palindrome_str == candidate_palindrome_str[::-1] and n1 * n2 > max_palindrome_int:
                max_palindrome_int = n1 * n2
    return max_palindrome_int
