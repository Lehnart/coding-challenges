from sympy.ntheory import factorint

factors = factorint(600851475143, multiple=True)
print("Solution : " + str(max(factors)))
