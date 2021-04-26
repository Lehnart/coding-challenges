def hasproperty(d1, d2, d3, divisor):
    return int(d1 + d2 + d3) % divisor == 0


def algo():
    digits = "0123456789"
    divisors = [2, 3, 5, 7, 11, 13, 17]
    solution = 0
    permutation_str = ["?"] * 10
    for d0 in digits:
        permutation_str[0] = d0
        for d1 in digits:
            if d1 in permutation_str[:1]: continue
            permutation_str[1] = d1
            for d2 in digits:
                if d2 in permutation_str[:2]: continue
                permutation_str[2] = d2
                for d3 in digits:
                    if d3 in permutation_str[:3]: continue
                    permutation_str[3] = d3
                    if not hasproperty(d1, d2, d3, divisors[0]): continue
                    for d4 in digits:
                        if d4 in permutation_str[:4]: continue
                        permutation_str[4] = d4
                        if not hasproperty(d2, d3, d4, divisors[1]): continue
                        for d5 in digits:
                            if d5 in permutation_str[:5]: continue
                            permutation_str[5] = d5
                            if not hasproperty(d3, d4, d5, divisors[2]): continue
                            for d6 in digits:
                                if d6 in permutation_str[:6]: continue
                                permutation_str[6] = d6
                                if not hasproperty(d4, d5, d6, divisors[3]): continue
                                for d7 in digits:
                                    if d7 in permutation_str[:7]: continue
                                    permutation_str[7] = d7
                                    if not hasproperty(d5, d6, d7, divisors[4]): continue
                                    for d8 in digits:
                                        if d8 in permutation_str[:8]: continue
                                        permutation_str[8] = d8
                                        if not hasproperty(d6, d7, d8, divisors[5]): continue
                                        for d9 in digits:
                                            if d9 in permutation_str[:9]: continue
                                            permutation_str[9] = d9
                                            if not hasproperty(d7, d8, d9, divisors[6]): continue
                                            n = int(d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9)
                                            solution += n
    return solution


if __name__ == "__main__":
    import cProfile

    cProfile.run("algo()")
