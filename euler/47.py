from sympy.ntheory import primefactors

n = 2
while True:

    n1, n2, n3, n4 = (n, n + 1, n + 2, n + 3)
    n_d = (set(primefactors(n1)), set(primefactors(n2)), set(primefactors(n3)), set(primefactors(n4)))
    if [len(el) for el in n_d] == [4] * 4:
        print("Solution : " + str(n))
    n += 1
