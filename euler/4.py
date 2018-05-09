max_palindrom_int = 0
for n1 in range(100,1000) :
    for n2 in range(100,1000) :
        candidate_palindrom_str = str(n1*n2)
        if candidate_palindrom_str == candidate_palindrom_str[::-1] and n1*n2 > max_palindrom_int :
            max_palindrom_int = n1*n2
print( "Solution : " + str(max_palindrom_int) )